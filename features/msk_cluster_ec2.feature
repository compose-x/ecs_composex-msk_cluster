# msk_cluster
Feature: ecs_composex_msk_cluster - EC2 Only

    Background: I run in Fargate only
        Given With docker-compose.yaml
        And With compute_modes/ec2.yaml

    @create
    Scenario Outline: Render docker-compose with new msk_cluster resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |

    @lookup
    Scenario Outline: Render docker-compose with new msk_cluster resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |

    @create_lookup
    Scenario Outline: Render docker-compose with new msk_cluster resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |
