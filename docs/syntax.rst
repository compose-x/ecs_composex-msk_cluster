
.. meta::
    :description: ECS Compose-X MSK Cluster
    :keywords: AWS, ECS, MSK, compose

====================
Syntax Reference
====================

.. code-block:: yaml

    x-msk_cluster:
      Properties: {}
      MacroParameters: {}
      Lookup: {}
      Services: {}


Properties
============

All properties are supported!

See `Properties for MSK Cluster`_ in AWS Cloudformation documentation.

.. hint::

    With new MSK clusters, your ECS Service automatically is granted access via a clients dedicated security group
    which automatically is granted the appropriate access via Security Group ingress rules.

    You can later re-use this Security Groups with other services to get ingress access automatically.


Services
=========

The Services for the MSK module are more advanced than other ECS Compose-X modules this far. It contains the default
`Access` section, allowing only to describe the cluster with the `RO` permissions.


However to grant meaningful access to your services to MSK cluster, you can define `KafkaAccess`_ which will set rules
based on the authentication method chosen to MSK.

.. include:: kafka_access.rst

Lookup
=========

The Lookup for MSK allows to use an existing MSK Cluster and setup all the appropriate IAM permissions to access said
cluster.

Lookup.Cluster
---------------

Tags associated with the MSK cluster. The tags must point to a single cluster. If multiple clusters match with the given
tags, the lookup will result in error.


Lookup.ClientsSecurityGroup
---------------------------

You can set ``ClientsSecurityGroup`` which will allow you to automatically add an existing Security Group
which would have access to the MSK cluster in order to provide yourself with access to said cluster, on the network.

For example, the below Lookup will search for a cluster with tag **Name** and value **msk-lookup**. It will also
look for a security group to use for the services in addition to their new default one.

.. code-block:: yaml

    x-msk_cluster:
      new-cluster:
        Lookup:
          Cluster:
            Tags:
              - Name: msk-lookup
          ClientsSecurityGroup:
            Tags:
              - aws:cloudformation:logical-id: newclusterClientsSecurityGroup

.. _Properties for MSK Cluster: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
