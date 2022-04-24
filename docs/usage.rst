
.. meta::
    :description: ECS Compose-X MSK Cluster
    :keywords: AWS, ECS, docker, compose, MSK, kafka

====================
Use the extension
====================

To use the extension, after installing the package, simply create a YAML file (or your existing compose file) and simply
add ``x-msk_cluster``, to define new MSK clusters to create/lookup.


.. literalinclude:: ../use-cases/create_only/services.yaml
    :language: yaml


Then we simply run the following command


.. code-block:: bash


    ecs-compose-x render -n project-with-msk -f <file_name>

