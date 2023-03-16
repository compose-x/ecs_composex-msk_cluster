
.. meta::
    :description: ECS Compose-X MSK Cluster
    :keywords: AWS, ECS, MSK, compose

.. _kafka_access:

KafkaAccess
-----------------

``KafkaAccess`` allows you to define whether your service is going to access the cluster via IAM, SCRAM, or TLS. For SCRAM
and TLS, that's up to you to administer and manage Kafka ACLs to grant further access to your services.

.. tip::

    Checkout `CFN Kafka Admin`_, an open source CloudFormation resource to manage Kafka ACLs, Topics & Schemas.

.. attention::

    You cannot set both `Iam` and `SaslScram` both at the same time.

Iam
^^^^

This section allows you to define 4 different types of resources access

* `topic`_
* `group`_
* `transactional-id`_
* `cluster`_

For each of these resource types, you can use one or more of the predefined profiles, and for each of them, grant access
to resources using a syntax compatible with ``PREFIX`` pattern with Kafka ACLs.

For example, ``my-app-topics*`` grants access to all topics starting with ``my-app-topics``.

.. note::

    By default, the clients are all given **kafka-cluster:Connect** to the cluster which is required for all operations.

cluster
********

As described above, **kafka-cluster:Connect** is granted to the service by Task role by default.
This section allows you to define further cluster-level ACL access.

Currently the only option is **IdempotentWrite**, boolean, which allows to idempotent writes on the MSK Cluster.

topic
*****

There are 4 profiles to manage topics:

* Admin: allows all actions on topics, including create and delete
* Producer: allows to write data to the topic(s)
* Consumer: allows to read data from the topic(s)
* ProducerConsumer: allows both read and write access to the topic(s)

+-------------------------+-----------------------------+-----------------------------+-----------------------------+
|           Admin         |           Producer          |           Consumer          |       ProducerConsumer      |
+=========================+=============================+=============================+=============================+
| kafka-cluster:*Topic*   | kafka-cluster:DescribeTopic | kafka-cluster:DescribeTopic | kafka-cluster:DescribeTopic |
|                         |                             |                             |                             |
|                         |                             |                             |                             |
| kafka-cluster:ReadData  | kafka-cluster:WriteData     | kafka-cluster:ReadData      | kafka-cluster:WriteData     |
|                         |                             |                             |                             |
|                         |                             |                             |                             |
| kafka-cluster:WriteData |                             |                             | kafka-cluster:ReadData      |
+-------------------------+-----------------------------+-----------------------------+-----------------------------+


group
******

There are 2 profiles to manage consumer groups

* Admin: grants all Kafka ACLs on the security group, including delete
* Consumer: grants normal use of the consumer group(s) for the application.

+-----------------------------+-----------------------------+
|            Admin            |          Consumer           |
+=============================+=============================+
| kafka-cluster:DescribeGroup | kafka-cluster:DescribeGroup |
|                             |                             |
| kafka-cluster:AlterGroup    | kafka-cluster:AlterGroup    |
|                             |                             |
| kafka-cluster:DeleteGroup   |                             |
+-----------------------------+-----------------------------+

transactional-id
*****************

There is 1 profile for Kafka transactional IDs.

* Producer: allows all Kafka ACLs related to Transactional IDs

+---------------------------------------+
|               Producer                |
+=======================================+
| kafka-cluster:AlterTransactionalId    |
|                                       |
|                                       |
| kafka-cluster:DescribeTransactionalId |
+---------------------------------------+

Schema Definition
==================

The below schema is used to perform input validation from users. It allows to validate the input early and flag any
errors in your YAML compose files.

.. literalinclude:: ../ecs_composex_msk_cluster/x-msk_cluster.spec.json

.. _Properties for MSK Cluster: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
.. _CFN Kafka Admin: https://github.com/compose-x/cfn-kafka-admin
