# SPDX-License-Identifier: MPL-2.0
# Copyright 2020-2022 John Mille <john@compose-x.io>

"""Main module."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecs_composex.mods_manager import XResourceModule
    from ecs_composex.common.settings import ComposeXSettings
    from .msk_cluster import MskCluster

from compose_x_common.aws.msk import MSK_CLUSTER_ARN_RE
from compose_x_common.compose_x_common import keyisset
from ecs_composex.common.stacks import ComposeXStack
from ecs_composex.common.troposphere_tools import build_template
from ecs_composex.vpc.vpc_params import (
    APP_SUBNETS,
    PUBLIC_SUBNETS,
    STORAGE_SUBNETS,
    VPC_ID,
)
from troposphere.msk import Cluster as CfnMskCluster

from .msk_cluster_params import MSK_CLUSTER_ADDRESSING_TYPE
from .msk_cluster_template import build_msk_clusters


def describe_kafka_cluster(
    cluster: MskCluster, account_id: str, resource_id: str
) -> dict:
    client = cluster.lookup_session.client("kafka")
    cluster_r = client.describe_cluster_v2(ClusterArn=resource_id)
    return cluster_r["ClusterInfo"]


def define_msk_clusters_mappings(module: XResourceModule, settings: ComposeXSettings):
    for cluster in module.lookup_resources:
        cluster.init_outputs()
        cluster.lookup_resource(
            MSK_CLUSTER_ARN_RE,
            describe_kafka_cluster,
            CfnMskCluster.resource_type,
            "kafka:cluster",
            use_arn_for_cloud_id=True,
        )
        settings.mappings[module.mapping_key].update(
            {cluster.logical_name: cluster.mappings}
        )


class XStack(ComposeXStack):
    """
    Class to handle MSK resources
    """

    def __init__(
        self, title: str, settings: ComposeXSettings, module: XResourceModule, **kwargs
    ):
        if module.lookup_resources:
            if not keyisset(module.mapping_key, settings.mappings):
                settings.mappings[module.mapping_key] = {}
            define_msk_clusters_mappings(module, settings)
        if module.new_resources:
            stack_template = build_template(
                f"{module.res_key} - Root Stack",
                [
                    VPC_ID,
                    STORAGE_SUBNETS,
                    APP_SUBNETS,
                    PUBLIC_SUBNETS,
                ],
            )
            super().__init__(title, stack_template, **kwargs)
            build_msk_clusters(module, self)
            self.parent_stack = settings.root_stack
        else:
            self.is_void = True
        for resource in module.lookup_resources:
            resource.stack = self
