
.. meta::
    :description: ECS Compose-X MSK Cluster
    :keywords: AWS, ECS, MSK, Kafka, compose

====================
Use the extension
====================

To use the extension, after installing the package, simply create a YAML file (or your existing compose file) and simply
add ``x-msk_cluster``, to define new MSK clusters to create/lookup.

For example, deploy MSK Cluster & Conduktor to manage the resources within.

.. literalinclude:: ../use-cases/conduktor.yaml
    :language: yaml


Then we simply run the following command


.. code-block:: console

    ecs-compose-x render -d templates -n conduktor-msk-iam -f use-cases/conduktor.yaml
