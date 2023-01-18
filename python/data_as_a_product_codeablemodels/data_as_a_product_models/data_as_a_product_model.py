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

search_engine = CClass(pattern, "Search Engine")
service_locator = CClass(pattern, "Service Locator")
data_catalogue = CClass(pattern, "Data Catalogue")
query_catalogue = CClass(pattern, "Query Catalogue")
observation_port = CClass(pattern, "Observation Port")
schema_manager = CClass(pattern, "Schema Registry")
change_data_capture = CClass(pattern, "Change Data Capture")
data_onboarding = CClass(pattern, "Data Onboarding")
immutable_change_audit_log = CClass(pattern, "Immutable Change Audit Log")
cqrs = CClass(pattern, "CQRS")
feature_layer = CClass(pattern, "Feature Store")
central_data_product_catalogue = CClass(pattern, "Central Data Product Catalogue")
discovery_port = CClass(pattern, "Discovery Port")
event_bus = CClass(pattern, "Event Bus")
templated_data_pipeline = CClass(pattern, "Templated Data Pipeline")
pub_sub = CClass(pattern, "Pub/Sub")
api_gateway = CClass(pattern, "API Gateway")
strangler_fig_pattern = CClass(pattern, "Strangler-Fig")
control_port = CClass(pattern, "Control Port")
zero_trust_architecture = CClass(pattern, "Zero Trust Architecture")
mdm = CClass(pattern, "Master Data Management")
observation_plane = CClass(pattern, "Observation Plane")
control_plane = CClass(pattern, "Control Plane")
storage_read_api = CClass(pattern, "Storage Read API")
cloud_storage_api = CClass(pattern, "Cloud Storage API")
event_streaming = CClass(pattern, "Event Streaming Backbone")
api_invocation = CClass(pattern, "API Invocation")

# practices
raw_data_as_data_product = CClass(practice, "Expose Data Product as Raw Data")
derived_data_as_data_product = CClass(practice, "Expose Data Product as Derived Data")
decision_support_model_as_data_product = CClass(practice, "Expose Data Product as an Optimisation-based Decision Support System")
automated_decision_making_model_as_data_product = CClass(practice, "Expose Data Product as an AI/ML Model")
hybrid_products = CClass(practice, "Expose Data Product as a Hybrid Product")
composite_products = CClass(practice, "Expose Data Product as a Composite Product")
register_datasets = CClass(practice, "Register datasets")
request_access_engine = CClass(practice, "Request access to datasets in search engine")
request_access = CClass(practice, "Fine-grained Access Control")
quality_monitoring = CClass(practice, "Provide a single integrated experience for monitoring")
algorithms_as_data_product = CClass(practice, "Expose Data Product as an algorithm")
domain_datasets = CClass(practice, "The domain datasets belong to a specific domain")
core_datasets = CClass(practice, "Core datasets are those that are useful for more than one domain")
virtualisation = CClass(practice, "Virtualisation")
incremental_sync = CClass(practice, "Incremental Sync")
role_based_access_control = CClass(practice, "Role-based Access Control")
encryption = CClass(practice, "Encryption")
time_bounded_backwards_compatibility = CClass(practice, "Time-bounded Backwards Compatibility")
ci_cd_process = CClass(practice, " CI/CD process")
versioning = CClass(practice, "Versioning")
k8s = CClass(practice, "Kubernetes")
infrastructure_as_code = CClass(practice, "Infrastructure as Code")
containerisation = CClass(pattern, "Single-container design")
unified_batch_stream = CClass(practice, "Create a component for unified batch and stream data processing")
open_access = CClass(practice, "Open Access")
maintaining_source_of_truth = CClass(practice, "Maintaining a single source of truth")
run_tests = CClass(practice, "Run automated testing on your data product")
centrally_manage_monitor_govern_data = CClass(practice, "Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts")
snapshots_ETL = CClass(practice, "Send snapshots via nightly ETL")
snapshots_via_ReqResAPI = CClass(practice, "Send snapshots via Req/Res API")
dataset_versioning = CClass(practice, "Dataset Versioning")
view_versioning = CClass(practice, "View Versioning")
docker = CClass(practice, "Docker")
security_controls = CClass(practice, "Security Controls")
triggering = CClass(practice, "Alterting")
sql_layer = CClass(practice, "Attach a SQL access point to each Data Product")
rest_apis = CClass(practice, "Attach REST APIs to each data product")
cache = CClass(practice, "Implement a highly available in-memory cache")
internal_storages = CClass(practice, "Internal storages where the data product is deployed, not exposed to consumers")
end_to_end = CClass(practice, "end-to-end connection")
no_sql_system = CClass(practice, "NoSQL system")
orchestration = CClass(practice, "Orchestrator")
data_marketplace = CClass(practice, "Data Marketplace")
attribute_based_access_control = CClass(practice, "Attribute-based Access Control")
multi_tenancy_model = CClass(practice, " A single Subscription with a single workspace")
single_subscription_single_workspace_dedicated_artifacts_per_domain = CClass(practice, "A single Subscription with a single workspace with dedicated artifacts for each domain")
single_subscription_multiple_workspaces = CClass(practice, " A Subscription with multiple workspaces")
single_subscription_dedicated_workpasce_per_domain = CClass(practice, "A single Azure Subscription with separate workspaces for each domain")
separate_subscriptions_separate_workspace_per_domain = CClass(practice, "Separate subscriptions with separate workspaces for each domain")
start_from_scratch = CClass(practice, "Greenfield Development")
migration = CClass(practice, "Migration")
data_marts = CClass(practice, "Incrementally build business process-centric data marts")
non_functional = CClass(practice, "Non-Functional Components")
function_as_a_service = CClass(practice, "Functiona-as-a-Service")
run_time_environment_access_control = CClass(practice, "Run-time Environment Access Control")
row_based_access_control = CClass(practice, "Row-based Access Control")
api_access_control = CClass(practice, "API Access Control")
stream_access_control = CClass(practice, "Stream Access Control")
shared_storage = CClass(practice, "Shared Storage")
remote_procedure_invocation = CClass(practice, "gRPC")
graphQL = CClass(practice, "GraphQL")

# forces
security = CClass(force, "Security")
discoverability = CClass(force, "Discoverability")
accelerate_decision_making = CClass(force, "Accelerate Decision Making")
more_granular_data = CClass(force, "More granular data")
understandability = CClass(force, "Understandability")
standardised_transformation = CClass(force, "Standardised Transformation")
duplication = CClass(force, "Duplication")
obscurity = CClass(force, "Obscurity")
trustworthiness = CClass(force, "Trustworthiness")
interoperability = CClass(force, "Interoperability")
completeness = CClass(force, "Completeness")
integrity = CClass(force, "Integrity")
multiple_independent_read_only_views = CClass(force, "Multiple independent read-only views")
time_to_market = CClass(force, "Time-to-Market")
periodic_execution = CClass(force, "Execution at periodic intervals")
consistency = CClass(force, "Consistently Applied Security")
stability = CClass(force, "Stability")
swamp = CClass(force, "Turning the data lake into a swamp")
agility = CClass(force, "Agility")
manual_toil = CClass(force, "Manual Toil")
quality = CClass(force, "Data Quality")
fast_data_propagation = CClass(force, "Fast data propagation")
handle_large_data_volumes = CClass(force, "Handle large data volumes")
limit_recipients = CClass(force, "Limit receptions")
addressability_subscriptions = CClass(force, "Addressability")
control_over_data_schema = CClass(force, "Control over data schema")
real_time_data_access = CClass(force, "Real-time Data Access")
multiple_environments = CClass(force, "Can be deployed in multiple environments")
production_grade_integrations = CClass(force, "Production Grade Integrations")
reproducibility = CClass(force, "Reproducibility")
traceability = CClass(force, "Traceability")
verifiability = CClass(force, "Verifiability")
unified = CClass(force, "Unified")
up_to_date = CClass(force, "Up-to-date")
accessible = CClass(force, "Accessibility")
addressible = CClass(force, "Addressable")
immutability = CClass(force, "Immutability")
transparency = CClass(force, "Transparency")
scalable = CClass(force, "Scalable")
entry_barrier = CClass(force, "Entry Barrier")
data_search = CClass(force, "Data Search")
data_enrichment = CClass(force, "Data Enrichment")
autonomous = CClass(force, "Autonomous")
observability = CClass(force, "Observability")
grouping = CClass(force, "Grouping")
filtering = CClass(force, "Filtering")
centralization = CClass(force, "Centralization")
data_lineage = CClass(force, "Data Lineage")
governance = CClass(force, "Governance")
decomposition = CClass(force, "Decomposition")

# decisions, options, and contexts

# ** data_product_type_decision **

data_product_type_decision = CClass(decision, "What type of data product can be developed?")
add_decision_option_link(data_product_type_decision, raw_data_as_data_product,
                         "Use raw data from the data product")
add_decision_option_link(data_product_type_decision, derived_data_as_data_product,
                         "Use derived data from the data product")
add_decision_option_link(data_product_type_decision, algorithms_as_data_product,
                         "Use algorithms to return information or insights")
add_force_relations({raw_data_as_data_product: {understandability: negative},
                     derived_data_as_data_product: {understandability: positive},
                     algorithms_as_data_product: {understandability: neutral}
                     })

algorithms_data_product_first_variation = \
    decision_support_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=variant)[0]
algorithms_data_product_second_variation = \
    automated_decision_making_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=variant)[0]
raw_hybrid = \
    raw_data_as_data_product.add_links(hybrid_products, role_name="from", stereotype_instances=can_use)[0]
derived_hybrid = \
    derived_data_as_data_product.add_links(hybrid_products, role_name="from", stereotype_instances=can_use)[0]
algorithms_hybrid = \
    algorithms_as_data_product.add_links(hybrid_products, role_name="from", stereotype_instances=can_use)[0]

raw_composite = \
    raw_data_as_data_product.add_links(composite_products, role_name="from", stereotype_instances=can_use)[0]
derived_composite = \
    derived_data_as_data_product.add_links(composite_products, role_name="from", stereotype_instances=can_use)[0]
algorithms_composite = \
    algorithms_as_data_product.add_links(composite_products, role_name="from", stereotype_instances=can_use)[0]

# ** orchestration_decision **

orchestration_decision = CClass(decision, "Which approach is chosen for the creation of a data product?")
add_decision_option_link(orchestration_decision, migration,
                         "Migrating from a legacy architecture")
add_decision_option_link(orchestration_decision, start_from_scratch,
                         "Starting with greenfield development")


migration_mdm = \
    mdm.add_links(migration, role_name="from", stereotype_instances=can_use)[0]
migration_strangler_fig_pattern = \
    strangler_fig_pattern.add_links(migration, role_name="from", stereotype_instances=can_use)[0]
migration_zero_trust = \
    zero_trust_architecture.add_links(migration, role_name="from", stereotype_instances=can_use)[0]
migration_cqrs = \
    cqrs.add_links(migration, role_name="from", stereotype_instances=can_use)[0]

# ** data_product_layer_decision **

data_product_layer_decision = CClass(decision, "Which Architectural Elements should be offered in the Data Product Anatomy?")
add_decision_option_link(data_product_layer_decision, change_data_capture,
                         "Implement a Change Data Capture component")
add_decision_option_link(data_product_layer_decision,immutable_change_audit_log,
                             "Implement a immutable log component")
add_decision_option_link(data_product_layer_decision, internal_storages,
                               "Implement an internal storage for each data product")
add_decision_option_link(data_product_layer_decision, data_catalogue,
                               "Implement a Data Catalogue component")
add_decision_option_link(data_product_layer_decision, observation_plane,
                               "Implement an observation plane")
add_decision_option_link(data_product_layer_decision, control_plane,
                               "Implement a control plane")
add_force_relations({change_data_capture: {real_time_data_access: positive,
                                              understandability: positive,
                                              accessible: positive,
                                              production_grade_integrations: positive},
                     immutable_change_audit_log: {reproducibility: positive,
                                                  traceability: positive,
                                                  verifiability: positive,
                                                  immutability: very_positive,
                                                  observability: positive,
                                                  understandability: very_positive,
                                                  data_lineage: positive,
                                                  governance: very_positive},
                     data_catalogue: {standardised_transformation: positive,
                                     duplication: negative,
                                     obscurity: negative,
                                     discoverability: positive,
                                     data_search: positive,
                                     data_enrichment: positive,
                                     autonomous: positive,
                                     accessible: very_positive,
                                     up_to_date: positive}
                        })


internal_storage_source_of_truth = \
    maintaining_source_of_truth.add_links(internal_storages, role_name="from", stereotype_instances=enables)[0]
internal_storage_data_marts = \
    data_marts.add_links(internal_storages, role_name="from", stereotype_instances=can_be_realized_with)[0]

data_catalogue_register_datasets = \
    register_datasets.add_links(data_catalogue, role_name="from", stereotype_instances=enables)[0]
register_datasets_domain_data = \
    domain_datasets.add_links(register_datasets, role_name="from", stereotype_instances=includes)[0]
register_datasets_core_data = \
    core_datasets.add_links(register_datasets, role_name="from", stereotype_instances=includes)[0]

immutable_change_audit_log_versioning = \
    versioning.add_links(immutable_change_audit_log, role_name="from", stereotype_instances=enables)[0]
immutable_change_audit_log_alerting = \
    triggering.add_links(immutable_change_audit_log, role_name="from", stereotype_instances=enables)[0]
versioning_sync = \
    incremental_sync.add_links(versioning, role_name="from", stereotype_instances=enables)[0]
versioning_dataset = \
    dataset_versioning.add_links(versioning, role_name="from", stereotype_instances=can_use)[0]
versioning_view = \
    view_versioning.add_links(versioning, role_name="from", stereotype_instances=can_use)[0]

# ** deploy_decision **

deploy_decision = CClass(decision, "How to deploy a data product?")
add_decision_option_link(deploy_decision, k8s,
                               "Use kubernetes")
add_decision_option_link(deploy_decision, docker,
                               "Use a containerised architecture")

k8s_docker = \
    docker.add_links(k8s, role_name="from", stereotype_instances=includes)[0]
k8s_IaaS = \
    infrastructure_as_code.add_links(k8s, role_name="from", stereotype_instances=can_use)[0]
k8s_FaaS = \
    function_as_a_service.add_links(k8s, role_name="from", stereotype_instances=can_use)[0]

docker_containerisation = \
    containerisation.add_links(docker, role_name="from", stereotype_instances=can_be_realized_with)[0]
docker_infrastructure_as_code = \
    infrastructure_as_code.add_links(docker, role_name="from", stereotype_instances=can_use)[0]
docker_templated_data_pipeline = \
    templated_data_pipeline.add_links(docker, role_name="from", stereotype_instances=can_use)[0]
templated_data_pipeline_ci_cd_process = \
    ci_cd_process.add_links(templated_data_pipeline, role_name="from", stereotype_instances=leads_to)[0]

# ** data_product_self_serve_management_decision **

data_product_self_serve_management_decision = CClass(decision, "How does the data product interact with other data products, self-serve platform and management layer?")
add_decision_option_link(data_product_self_serve_management_decision, schema_manager,
                         "Implement a Schema Registry component")
add_decision_option_link(data_product_self_serve_management_decision,central_data_product_catalogue,
                             "Implement an Central Data Product Catalogue component")
add_decision_option_link(data_product_self_serve_management_decision, event_streaming,
                               "Implement an Event Streaming Backbone")
add_decision_option_link(data_product_self_serve_management_decision, shared_storage,
                               "Implement a shared storage")
add_decision_option_link(data_product_self_serve_management_decision, api_invocation,
                               "Implement API Invocation")
add_force_relations({schema_manager: {understandability: positive,
                                          duplication: positive,
                                          reproducibility: very_positive,
                                          interoperability: positive},
                     central_data_product_catalogue: {discoverability: positive,
                                                      understandability: positive,
                                                      observability: positive}
                        })

event_streaming_pub_sub = \
    pub_sub.add_links(event_streaming, role_name="from", stereotype_instances=uses)[0]
central_data_product_catalogue_centrally_manage_monitor_govern_data = \
    centrally_manage_monitor_govern_data.add_links(central_data_product_catalogue, role_name="from", stereotype_instances=leads_to)[0]
api_invocation_read = \
    storage_read_api.add_links(api_invocation, role_name="from", stereotype_instances=leads_to)[0]
api_invocation_cloud = \
    cloud_storage_api.add_links(api_invocation, role_name="from", stereotype_instances=leads_to)[0]
api_invocation_rest = \
    rest_apis.add_links(api_invocation, role_name="from", stereotype_instances=can_be_realized_with)[0]
api_invocation_grpc = \
    remote_procedure_invocation.add_links(api_invocation, role_name="from", stereotype_instances=can_be_realized_with)[0]
shared_storage_storage_read = \
    storage_read_api.add_links(shared_storage, role_name="from", stereotype_instances=can_be_realized_with)[0]
shared_storage_cloud_storage = \
    cloud_storage_api.add_links(shared_storage, role_name="from", stereotype_instances=can_be_realized_with)[0]



# ** consumer_decision **

consumer_decision = CClass(decision, "How can the consumer interact with the information from the data product?")
add_decision_option_link(consumer_decision, sql_layer,
                               "Implement a SQL component")
add_decision_option_link(consumer_decision, rest_apis,
                               "Implement a REST API component")
add_decision_option_link(consumer_decision, non_functional,
                         "Implement a Non-functional component")
add_force_relations({cache: {duplication: negative},
                     sql_layer: {understandability: positive,
                                 accelerate_decision_making: very_positive,
                                 more_granular_data: very_positive},
                     rest_apis: {understandability: positive,
                                 control_over_data_schema: positive,
                                 accessible: positive,
                                 addressible: positive,
                                 interoperability: positive}
                        })

rest_apis_observation_port = \
    observation_port.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
observation_port_quality_monitoring = \
    quality_monitoring.add_links(observation_port, role_name="from", stereotype_instances=realizes)[0]
rest_apis_discovery_port = \
    discovery_port.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
rest_apis_control_port = \
    control_port.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
discovery_port_data_marketplace = \
    data_marketplace.add_links(discovery_port, role_name="from", stereotype_instances=enables)[0]

non_functional_cache = \
    cache.add_links(non_functional, role_name="from", stereotype_instances=can_use)[0]
non_functional_security_controls = \
    security_controls.add_links(non_functional, role_name="from", stereotype_instances=can_use)[0]
non_functional_query_catalogue = \
    query_catalogue.add_links(non_functional, role_name="from", stereotype_instances=can_use)[0]
security_controls_request_access = \
    request_access.add_links(security_controls, role_name="from", stereotype_instances=can_use)[0]
security_controls_encryption = \
    encryption.add_links(security_controls, role_name="from", stereotype_instances=can_use)[0]
request_access_attribute = \
    attribute_based_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_role = \
    role_based_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_row = \
    row_based_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_api = \
    api_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_run = \
    run_time_environment_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_stream = \
    stream_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]

# decision links
add_links({data_product_type_decision: [deploy_decision],
           deploy_decision: [data_product_self_serve_management_decision, consumer_decision, orchestration_decision],
           orchestration_decision: [data_product_layer_decision],
           data_product_self_serve_management_decision: [data_product_layer_decision],
           consumer_decision: [data_product_layer_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=data_product_type_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[data_product_type_decision,
                                              deploy_decision, orchestration_decision, data_product_self_serve_management_decision,
                                              consumer_decision, data_product_layer_decision])
data_product_type_view = CBundle("data_product_type_decision",
                                    elements=data_product_type_decision.class_object.get_connected_elements(
                                             stop_elements_exclusive=forces_class_objects + [
                                                 deploy_decision.class_object,
                                                 orchestration_decision.class_object,
                                                 data_product_self_serve_management_decision.class_object,
                                                 consumer_decision.class_object,
                                                 data_product_layer_decision.class_object
                                             ,]))

deploy_decision_view = CBundle("deploy_decision",
                                    elements=deploy_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            consumer_decision.class_object,
                                            data_product_layer_decision.class_object
                                            , ]))

orchestration_decision_view = CBundle("orchestration_decision",
                                    elements=orchestration_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            consumer_decision.class_object,
                                            data_product_layer_decision.class_object
                                            , ]))

data_product_self_serve_management_decision_view = CBundle("data_product_self_serve_management_decision",
                                    elements=data_product_self_serve_management_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            consumer_decision.class_object,
                                            data_product_layer_decision.class_object
                                            , ]))

consumer_decision_view = CBundle("consumer_decision",
                                    elements=consumer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            data_product_layer_decision.class_object
                                            , ]))

data_product_layer_decision_view = CBundle("data_product_layer_decision",
                                    elements=data_product_layer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            consumer_decision.class_object
                                            , ]))

data_as_a_product_views = [
    _all, {},
    inter_decision_links_view, {},
    data_product_type_view, {},
    orchestration_decision_view, {},
    data_product_layer_decision_view, {},
    consumer_decision_view, {},
    data_product_self_serve_management_decision_view, {},
    deploy_decision_view, {},
]








