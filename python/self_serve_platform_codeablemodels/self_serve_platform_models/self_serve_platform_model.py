from api_ddd_models.domain_model import domain_model, identified_interface_elements, domain_model_and_api, \
    domain_model_element_link
from codeable_models import CClass, add_links, CBundle
from map_models.map_domain_model import api, message, operation, api_contract
from metamodels.guidance_metamodel import do_nothing_design_solution, decision, practice, add_decision_option_link, \
    add_stereotyped_link_with_how_tagged_value, force, negative, uses, positive, can_be_realized_with, extension, \
    consider_if_not_decided_yet, decide_for_some_instances_of, pattern, decide_for_all_instances_of, \
    very_negative, neutral, very_positive, can_use, enables, variant, is_a, includes, leads_to, realizes


def add_force_relations(force_relations_definition):
    for practice in force_relations_definition.keys():
        for force in force_relations_definition[practice]:
            stereotype = (force_relations_definition[practice])[force]
            add_links({practice: force}, role_name="forces", stereotype_instances=stereotype)


# patterns
api_catalog = CClass(pattern, "API Catalog")
data_catalog = CClass(pattern, "Data Catalog") #+ searchability, +discoverability, +centrally govern
single_data_landing_zone = CClass(pattern, "Single Data Landing Zone")
multiple_data_landing_zones = CClass(pattern, "Source system- and consumer-aligned data landing zones")
cdc = CClass(pattern, "Change Data Capture")
hub_generic_special_data_landing_zones = CClass(pattern, "Hub-, generic-, and special data landing zones")
large_scale_enterprise = CClass(pattern, "Large scale enterprise requiring different data management zones")
functional_and_regionally_aligned_data_landing_zones = CClass(pattern, "Functional and regionally aligned data landing zones")
register_derived_data_as_data_product = CClass(practice, "Registering the derived batch data set as a platform's own data product")
distributed_file_storage = CClass(pattern, " Distributed file storage")
elastic_performance_engine = CClass(pattern, 'Elastic Performance Engine')
query_engine = CClass(pattern, "Query Engine")
sql_endpoint = CClass(pattern, 'SQL Endpoint')
research_groups = CClass(pattern, "Research Groups")
unified_batch_stream_processing_service = CClass(pattern, 'Unified Batch Stream Processing Service')
research_groups = CClass(pattern, "Research Groups")
integration_service = CClass(pattern, 'Integration Service')
workflow_automation_engine = CClass(pattern, 'Workflow Automation Engine')
polygot_storage_option = CClass(pattern, 'Polygot Storage Option')
schema_registry = CClass(pattern, 'Schema Registry')

# practices
data_lineage = CClass(practice, "Data Lineage")
ci_cd_process = CClass(practice, 'CI/CD process')
runtime_observability = CClass(practice, 'Runtime Observability')
application_bootstraps = CClass(practice, 'Application Bootstraps')
self_serve_ui = CClass(practice, 'Self-Serve UI')
quality_management = CClass(practice, 'Quality Management')
log_management = CClass(practice, 'Log management')
mdm = CClass(practice, "Master Data Management")
ml_services = CClass(practice, "ML services")
data_lake_services = CClass(practice, "Data Lake Service")
VNetPeering = CClass(practice, "VNetPeering")
private_endpoints = CClass(practice, "Private Endpoints")
event_streaming_backbone = CClass(pattern, "Event Streaming Backbone")
lambda_architecture = CClass(pattern, "Lambda Architecture")
kappa_architecture = CClass(pattern, "Kappa Architecture")
data_source_ingestion = CClass(practice, "Data Source Ingestion")
access_control_management = CClass(practice, "Access control management")
manage_read_write_permissions = CClass(practice, "Manage read write functions")
policy_automation = CClass(practice, "Policy Automation")
managed_compute_infrastructure = CClass(practice, "Managed Compute Infrastructure") #+ abstract away, + elastic, + adapt to change
no_code_transformation = CClass(practice, "No-code transformation")
dependable_pipeline_management = CClass(practice, "Dependable pipeline management")
automated_issue_detection = CClass(practice, "Automated issue detection")
alerting = CClass(practice, "Alerting")
resolution = CClass(practice, "Resolution")
configure_depency = CClass(practice, "Configure pipelines for dependency management")
configure_thresholds = CClass(practice, "Configure pipelines for error tolerance thresholds")
configure_scheduling = CClass(practice, "Configure pipelines for scheduling")
data_transformation_orchestration = CClass(practice, "Data Transformation Orchestration")
manage_security_policies_of_dps = CClass(practice, "Manage security policies of DPs")
manage_emergent_graphs_of_dps = CClass(practice, "Manage emergent graphs of DPs")
discovery_and_explore_dps = CClass(practice, "Discovery and explore DPs")
declaratively_create_dp = CClass(practice, "Declaratively create DP")
read_dp = CClass(practice, "Read DP")
version_dp = CClass(practice, "Version DP")
secure_dp = CClass(practice, "Secure DP")
build_deploy_monitor_dp = CClass(practice, "Build, deploy, monitor DP")
separating_storage_and_compute = CClass(practice, 'Separating storage and compute') # + scalability, + autonomous
separating_compute_from_compute = CClass(practice, 'Separating compute from compute') # + scalability, + autonomous
restore_data_without_backups = CClass(practice, 'Ability to restore data and set back without having to take care of backups')
in_place_consumption = CClass(practice, 'Ability to restore data and set back without having to take care of backups') #- data movement, + global governance, + discrepancies, - costs, + up-to-date, + access control
scale_across_platforms_and_regions = CClass(practice, 'Ability to scale globally across platforms and regions')
metadata_management = CClass(practice, 'Metadata Management')
runtime_metadata = CClass(practice, 'Automatically make runtime data available')
compatible_metadata = CClass(practice, 'Automatically publish compatible metadata')
document_dp = CClass(practice, 'Document DP')
knowledge_graph = CClass(practice, 'Knowledge Graph')
central_search_function = CClass(practice, 'Central Search Function')
set_privacy_dp = CClass(practice, 'Set privacy DP')
elastic_performance_engine = CClass(pattern, 'Elastic Performance Engine')
infrastructure_as_code = CClass(practice, 'Infrastructure as Code')
visualization_function = CClass(practice, "Visualization Function")
software_as_a_service = CClass(practice, 'Software as a Service')
uptime_checks = CClass(practice, 'Uptime checks')
cost_management = CClass(practice, 'Cost Managment')
semantic_data_layer = CClass(practice, "Semantic Data Layer")
VMs = CClass(pattern, 'VMs')

# forces
complexity = CClass(force, "Complexity")
distinguish = CClass(force, "Distinguish")
domain_agnostic = CClass(force, "Domain-agnostic")
regional_legal = CClass(force, "Flexibility in regional or legal boundaries")
control_over_data = CClass(force, "Control over data")
time_travel = CClass(force, "Time travel")
redeliveries = CClass(force, "Redeliveries")
scalability = CClass(force, 'Scalability')
storage_function = CClass(practice, "Storage Function")
searchability = CClass(force, "Searchability")
discoverability = CClass(force, "Discoverability")
centrally_govern = CClass(practice, "Centrally govern data")
abstact_away_details = CClass(force, "Abstract away computational details")
elastic = CClass(force, "Elastic")
adapt_to_changing_volumes = CClass(force, "Adapt to changing volumes")
autonomous = CClass(force, 'Autonomous')
data_movement = CClass(force, 'Data movement')
global_governance = CClass(force, 'Global governance')
discrepancies = CClass(force, 'Discrepancies')
up_to_date = CClass(force, 'Up-to-date')
access_control = CClass(force, 'Access controls')
costs = CClass(force, 'Cost')
federated_analytics = CClass(force, 'Federated analytics')
delegated_ownership = CClass(force, 'Delegated ownership')
flexibility = CClass(force, 'Flexibility')
ad_hoc_exploration = CClass(force, 'Ad hoc exploration')
bi_reporting = CClass(force, 'BI reporting')
feature_engineering = CClass(force, 'Feature Engineering')
interactive_applications = CClass(force, 'Interactive Applications')
understandability = CClass(force, 'Understandability')
accessibility = CClass(force, 'Accessibility')
automation = CClass(force, 'Automation')
usability = CClass(force, 'Usability')
resource_deployment_process = CClass(force, 'Resource deployment process')
inconsistencies_between_deployed_resources_and_declared_code_in_source_control = CClass(force, 'Inconsistencies between deployed resources and declrared code in source control')
accurate_health_representation = CClass(force, 'Accurate health representation')
reduce_work_data_product_team = CClass(force, 'Reduce work done by data product team')
easily_replicable = CClass(force, 'Easily Replicable')
accuracy = CClass(force, 'Accuracy')
speed = CClass(force, 'Speed')
avoids_information_island = CClass(force, 'Avoids Information Island')
container_registry = CClass(force, 'Container Registry')

# decisions, options, and contexts

# ** deployment_decision **

deployment_decision = CClass(decision, "What type of data product can be developed?")
add_decision_option_link(deployment_decision, single_data_landing_zone,
                         "Use a single data landing zone")
add_decision_option_link(deployment_decision, multiple_data_landing_zones,
                         "Use source system- and consumer-aligned data landing zones")
add_decision_option_link(deployment_decision, hub_generic_special_data_landing_zones,
                         "Use hub-, generic-, special data landing zones")
add_decision_option_link(deployment_decision, functional_and_regionally_aligned_data_landing_zones,
                         "Use functional and regionally aligned data landing zones")
add_decision_option_link(deployment_decision, large_scale_enterprise,
                         "Use a large scale enterprise data landing zone")
add_force_relations({multiple_data_landing_zones: {complexity: negative},
                     hub_generic_special_data_landing_zones: {domain_agnostic: positive,
                                                              flexibility: positive,
                                                              control_over_data: positive,
                                                              time_travel: positive,
                                                              redeliveries: positive},
                     functional_and_regionally_aligned_data_landing_zones: {scalability: positive},
                     large_scale_enterprise: {scalability: positive}
                     })






