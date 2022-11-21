
.. meta::
    :description: ECS Compose-X MSK Cluster
    :keywords: AWS, ECS, MSK, compose

.. image:: https://img.shields.io/pypi/v/ecs_composex_msk_cluster.svg
        :target: https://pypi.python.org/pypi/ecs_composex_msk_cluster


This package is an extension to `ECS Compose-X`_ to create or use AWS Managed Kafka Clusters (MSK).

Installation
=============

.. code-block::

    python3 -m venv venv
    source venv/bin/activate
    # With poetry

    pip install pip poetry -U
    poetry install

    # Via pip
    pip install pip -U
    pip install ecs-composex-msk-cluster


Usage
=======

To use this module, after installing it, set `x-msk_cluster` in your docker-compose file, and link your services to it.
For example, with the Conduktor Platform

.. code-block:: console

    ecs-compose-x render -d templates -f use-cases/conduktor.yaml -p conduktor-msk-iam

.. _ECS Compose-X: https://docs.compose-x.io


.. toctree::
   :maxdepth: 2
   :caption: Content

   installation
   usage
   syntax
   modules
   contributing
   authors
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
