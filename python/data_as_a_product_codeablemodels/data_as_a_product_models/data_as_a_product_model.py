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
observation_plane = CClass(pattern, "Observation Port")
schema_manager = CClass(pattern, "Schema Registry")
change_data_capture = CClass(pattern, "Change Data Capture")
data_integration_service = CClass(pattern, "Use a data integration service that helps users efficiently build and manage ETL/ELT pipelines")
immutable_change_audit_log = CClass(pattern, "Immutable Change Audit Log")
cqrs = CClass(pattern, "CQRS")
feature_layer = CClass(pattern, "Feature Store")
central_data_product_catalogue = CClass(pattern, "Central Data Product Catalogue")
discovery_port = CClass(pattern, "Discovery Port")
event_bus = CClass(pattern, "Event Bus")
data_marts = CClass(pattern, "Incrementally build business process-centric data marts")
templated_data_pipeline = CClass(pattern, "Templated Data Pipeline")
pub_sub = CClass(pattern, "Pub/Sub")
api_gateway = CClass(pattern, "API Gateway")
strangler_fig_pattern = CClass(pattern, "Strangler-Fig")
control_plane = CClass(pattern, "Control Port")
zero_trust_architecture = CClass(pattern, "Zero Trust Architecture")
mdm = CClass(pattern, "Master Data Management")

# practices
raw_data_as_data_product = CClass(practice, "Expose Data Product as Raw Data")
derived_data_as_data_product = CClass(practice, "Expose Data Product as Derived Data")
decision_support_model_as_data_product = CClass(practice, "Expose Data Product as Decision Support Model")
automated_decision_making_model_as_data_product = CClass(practice, "Expose Data Product as Automated Decision-making Model")
register_datasets = CClass(practice, "Register datasets")
request_access_engine = CClass(practice, "Request access to datasets in search engine")
request_access = CClass(practice, "Fine-grained Access Control")
quality_monitoring = CClass(practice, "Provide a single integrated experience for monitoring")
algorithms_as_data_product = CClass(practice, "Expose Data Product as an algorithm")
domain_datasets = CClass(practice, "The domain datasets belong to a specific domain")
core_datasets = CClass(practice, "Core datasets are those that are useful for more than one domain")
event_streaming = CClass(practice, "Event Streaming")
virtualisation = CClass(practice, "Virtualisation")
incremental_sync = CClass(practice, "Incremental Sync")
role_based_access_control = CClass(practice, "Role-based Access Control")
encryption = CClass(practice, "Encryption")
time_bounded_backwards_compatibility = CClass(practice, "Time-bounded Backwards Compatibility")
ci_cd_process = CClass(practice, " CI/CD process")
versioning = CClass(practice, "Versioning")
k8s = CClass(practice, "Kubernetes Operator")
infrastructure_as_code = CClass(practice, "Infrastructure as Code")
containerisation = CClass(pattern, "Single-container design")
unified_batch_stream = CClass(practice, "Create a component for unified batch and stream data processing")
open_access = CClass(practice, "Open Access")
maintaining_source_of_truth = CClass(practice, "Maintaining a single source of truth")
run_tests = CClass(practice, "Run automated testing on your data product")
centrally_manage_monitor_govern_data = CClass(practice, "Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts")
snapshots_ETL = CClass(practice, "Send snapshots via nightly ETL")
snapshots_via_ReqResAPI = CClass(practice, "Send snapshots via Req/Res API")
oauth2 = CClass(practice, "OAUTH2")
dataset_versioning = CClass(practice, "Dataset Versioning")
view_versioning = CClass(practice, "View Versioning")
self_service_capability = CClass(practice, "Service should be provided as self-serve capability")
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

# forces
security = CClass(force, "Security")
meet_sla = CClass(force, "Meet SLAs")
discoverability = CClass(force, "Discoverability")
internal_complexity = CClass(force, "Internal Complexity")
complexity_for_user = CClass(force, "Complexity for User")
accelerate_decision_making = CClass(force, "Accelerate Decision Making")
more_granular_data = CClass(force, "More granular data")
understandability = CClass(force, "Understandability")
prioritise = CClass(force, "Prioritise")
standardised_transformation =  CClass(force, "Standardised Transformation")
duplication = CClass(force, "Duplication")
obscurity = CClass(force, "Obscurity")
trustworthiness = CClass(force, "Trustworthiness")
interoperability = CClass(force, "Interoperability")
compliance = CClass(force, "Compliance")
provenance = CClass(force, "Provenance")
accuracy = CClass(force, "Data Accuracy")
completeness = CClass(force, "Completeness")
integrity = CClass(force, "Integrity")
multiple_independent_read_only_views = CClass(force, "Multiple independent read-only views")
re_use = CClass(force, "Re-use aspects by allowing other teams to find and build upon existing work")
time_to_market = CClass(force, "Time-to-Market")
conflicting_definitions = CClass(force, "Conflicting definitions")
periodic_execution = CClass(force, "Execution at periodic intervals")
consistency = CClass(force, "Consistently Applied Security")
stability = CClass(force, "Stability")
swamp = CClass(force, "Turning the data lake into a swamp")
data_productivity = CClass(force, "Data Productivity")
analytics_agility = CClass(force, "Analytics Agility")
manual_toil = CClass(force, "Manual Toil")
quality = CClass(force, "Data Quality")
discovery = CClass(force, "Discovery")
gain_knowledge = CClass(force, "Quickly gain knowledge on data set")
fast_data_propagation = CClass(force, "Fast data propagation")
handle_large_data_volumes = CClass(force, "Handle large data volumes")
limit_recipients = CClass(force, "Limit receptions")
addressability_subscriptions = CClass(force, "Addressability of subscriptions")
control_over_data_schema = CClass(force, "Control over data schema")
real_time_data_access = CClass(force, "Real-time Data Access")
high_fidelity = CClass(force, "High fidelity")
multiple_environments = CClass(force, "Can be deployed in multiple environments")
non_intrusive = CClass(force, "Non-intrusive")
consumption = CClass(force, "Consumption")
production_grade_integrations = CClass(force, "Production Grade Integrations")
reproducibility = CClass(force, "Reproducibility")
traceability = CClass(force, "Traceability")
verifiability = CClass(force, "Verifiability")
unified = CClass(force, "Unified")
up_to_date = CClass(force, "Up-to-date")
protected = CClass(force, "Protected")
accessible = CClass(force, "Accessible")
addressible = CClass(force, "Addressable")
structured_code = CClass(force, "Structured code")
immutability = CClass(force, "Immutability")
bi_temporality_data = CClass(force, "Bi-temporality of data")
transparency = CClass(force, "Transparency")
user_experience = CClass(force, "User Experience")
data_integration_speed = CClass(force, "Data Integration Speed")
scalable = CClass(force, "Scalable")
frictions = CClass(force, "Frictions")
entry_barrier = CClass(force, "Entry Barrier")
data_search = CClass(force, "Data Search")
data_enrichment = CClass(force, "Data Enrichment")
autonomous = CClass(force, "Autonomous")
delegated_ownership = CClass(force, "Delegated Ownership")
observability = CClass(force, "Observability")
structured_data = CClass(force, "Structured Data")
on_demand = CClass(force, "On-Demand")
grouping_related_data_resources = CClass(force, "Grouping Related Data Resources")
allows_for_filtering = CClass(force, "Allows For Filtering")
centralization = CClass(force, "Centralization")
data_lineage = CClass(force, "Data Lineage")
self_documenting = CClass(force, "Self-Documenting")
ability_to_gauge_data_quality = CClass(force, "Ability to gauge data quality")
governance = CClass(force, "Governance")
debugging = CClass(force, "Debugging")
easy_data_migration_between_products = CClass(force, "Easy Data Migration Between Products")
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
add_force_relations({raw_data_as_data_product: {internal_complexity: very_positive,
                                                complexity_for_user: very_negative},
                     derived_data_as_data_product: {internal_complexity: positive,
                                                    complexity_for_user: negative},
                     algorithms_as_data_product: {internal_complexity: neutral,
                                                  complexity_for_user: neutral}
                     })

algorithms_data_product_first_variation = \
    decision_support_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=uses)[0]
algorithms_data_product_second_variation = \
    automated_decision_making_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=uses)[0]


# ** orchestration_decision **

orchestration_decision = CClass(decision, "Which approach is chosen for orchestrating the data product")
add_decision_option_link(orchestration_decision, mdm,
                         "Implement a Master Data Management pattern")
add_decision_option_link(orchestration_decision,zero_trust_architecture,
                             "Implement a Zero Trust pattern")
add_decision_option_link(orchestration_decision, cqrs,
                               "Implement a CQRS pattern")
add_decision_option_link(orchestration_decision, strangler_fig_pattern,
                               "Implement a Strangler-Fig pattern")
add_force_relations({mdm: {centralization: positive,
                          discoverability: positive},
                     cqrs: {multiple_independent_read_only_views: positive,
                            allows_for_filtering: positive},
                     strangler_fig_pattern: {easy_data_migration_between_products: very_positive,
                                             decomposition: positive}
                        })

# ** data_product_layer_decision **

data_product_layer_decision = CClass(decision, "Which architectural elements should be offered in the Data Product layer?")
add_decision_option_link(data_product_layer_decision, change_data_capture,
                         "Implement a Change Data Capture component")
add_decision_option_link(data_product_layer_decision,immutable_change_audit_log,
                             "Implement a immutable log component")
add_decision_option_link(data_product_layer_decision, internal_storages,
                               "Implement an internal storage for each data product")
add_decision_option_link(data_product_layer_decision, data_catalogue,
                               "Implement a Data Catalogue component")
add_decision_option_link(data_product_layer_decision, feature_layer,
                               "Implement a Feature Store component")
add_force_relations({change_data_capture: {real_time_data_access: positive,
                                              complexity_for_user: negative,
                                              non_intrusive: positive,
                                              consumption: positive,
                                              production_grade_integrations: positive},
                     immutable_change_audit_log: {reproducibility: positive,
                                                  traceability: positive,
                                                  verifiability: positive,
                                                  immutability: very_positive,
                                                  bi_temporality_data: positive,
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
                                     delegated_ownership: positive,
                                     consumption: very_positive,
                                     up_to_date: positive},
                    feature_layer: {interoperability: positive,
                                    stability: positive}
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

feature_layer_unified_batch_stream = \
    unified_batch_stream.add_links(feature_layer, role_name="from", stereotype_instances=enables)[0]

# ** infrastructure_layer_decision **

infrastructure_layer_decision = CClass(decision, "Which architectural elements should be offered in the Infrastructure layer?")
add_decision_option_link(infrastructure_layer_decision, schema_manager,
                         "Implement a Schema Registry component")
add_decision_option_link(infrastructure_layer_decision,central_data_product_catalogue,
                             "Implement an Central Data Product Catalogue component")
add_decision_option_link(infrastructure_layer_decision, k8s,
                               "Implement a kubernetes operator")
add_decision_option_link(infrastructure_layer_decision, self_service_capability,
                               "Implement a Data Catalogue component")
add_force_relations({schema_manager: {understandability: positive,
                                          duplication: positive,
                                          conflicting_definitions: negative,
                                          re_use: very_positive,
                                          interoperability: positive},
                     central_data_product_catalogue: {discoverability: positive,
                                                      understandability: positive,
                                                      observability: positive},
                    k8s: {structured_code: positive}
                        })

central_data_product_catalogue_centrally_manage_monitor_govern_data = \
    centrally_manage_monitor_govern_data.add_links(central_data_product_catalogue, role_name="from", stereotype_instances=leads_to)[0]

k8s_event_streaming_backbone = \
    event_streaming.add_links(k8s, role_name="from", stereotype_instances=can_be_realized_with)[0]
event_streaming_pub_sub = \
    pub_sub.add_links(event_streaming, role_name="from", stereotype_instances=uses)[0]

self_service_capability_containerisation = \
    containerisation.add_links(self_service_capability, role_name="from", stereotype_instances=can_be_realized_with)[0]
self_service_capability_infrastructure_as_code = \
    infrastructure_as_code.add_links(self_service_capability, role_name="from", stereotype_instances=can_use)[0]
self_service_capability_templated_data_pipeline = \
    templated_data_pipeline.add_links(self_service_capability, role_name="from", stereotype_instances=can_use)[0]
templated_data_pipeline_ci_cd_process = \
    ci_cd_process.add_links(templated_data_pipeline, role_name="from", stereotype_instances=leads_to)[0]

# ** data_access_layer_decision **

data_access_layer_decision = CClass(decision, "Which architectural elements should be offered in the Data Access layer?")
add_decision_option_link(data_access_layer_decision, virtualisation,
                         "Implement a Virtualisation component")
add_decision_option_link(data_access_layer_decision,cache,
                             "Implement a Cache component")
add_decision_option_link(data_access_layer_decision, sql_layer,
                               "Implement a SQL component")
add_decision_option_link(data_access_layer_decision, rest_apis,
                               "Implement a REST API component")
add_decision_option_link(data_access_layer_decision, query_catalogue,
                               "Implement a Query Catalogue component")
add_decision_option_link(data_access_layer_decision, security_controls,
                               "Implement a Security Controls component")
add_force_relations({virtualisation: {data_integration_speed: very_positive},
                     cache: {duplication: negative},
                     sql_layer: {internal_complexity: positive,
                                 complexity_for_user: positive,
                                 accelerate_decision_making: very_positive,
                                 more_granular_data: very_positive},
                     rest_apis: {internal_complexity: positive,
                                 complexity_for_user: negative,
                                 control_over_data_schema: positive,
                                 accessible: positive,
                                 addressible: positive,
                                 interoperability: positive},
                     query_catalogue: {trustworthiness: positive,
                                        interoperability: positive,
                                        discoverability: positive,
                                        gain_knowledge: very_positive,
                                        frictions: negative,
                                        entry_barrier: negative}
                        })


rest_apis_observation_plane = \
    observation_plane.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
observation_plane_quality_monitoring = \
    quality_monitoring.add_links(observation_plane, role_name="from", stereotype_instances=realizes)[0]
rest_apis_discovery_port = \
    discovery_port.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
rest_apis_control_plane = \
    control_plane.add_links(rest_apis, role_name="from", stereotype_instances=includes)[0]
discovery_port_data_marketplace = \
    data_marketplace.add_links(discovery_port, role_name="from", stereotype_instances=enables)[0]

security_controls_request_access = \
    request_access.add_links(security_controls, role_name="from", stereotype_instances=can_use)[0]
security_controls_encryption = \
    encryption.add_links(security_controls, role_name="from", stereotype_instances=can_use)[0]
security_controls_oauth2 = \
    oauth2.add_links(security_controls, role_name="from", stereotype_instances=can_use)[0]
request_access_attribute = \
    attribute_based_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]
request_access_role = \
    role_based_access_control.add_links(request_access, role_name="from", stereotype_instances=can_use)[0]

# decision links
add_links({data_product_type_decision: [orchestration_decision],
           orchestration_decision: [data_product_layer_decision, infrastructure_layer_decision, data_access_layer_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=data_product_type_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[data_product_type_decision,
                                              orchestration_decision, data_product_layer_decision, infrastructure_layer_decision,
                                              data_access_layer_decision])
data_product_type_view = CBundle("data_product_type_decision",
                                    elements=data_product_type_decision.class_object.get_connected_elements(
                                             stop_elements_exclusive=forces_class_objects + [
                                                 orchestration_decision.class_object,
                                                 data_product_layer_decision.class_object,
                                                 infrastructure_layer_decision.class_object,
                                                 data_access_layer_decision.class_object
                                             ,]))

orchestration_decision_view = CBundle("orchestration_decision",
                                    elements=orchestration_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            data_product_layer_decision.class_object,
                                            infrastructure_layer_decision.class_object,
                                            data_access_layer_decision.class_object
                                            , ]))

data_product_layer_decision_view = CBundle("data_product_layer_decision",
                                    elements=data_product_layer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            orchestration_decision.class_object,
                                            infrastructure_layer_decision.class_object,
                                            data_access_layer_decision.class_object
                                            , ]))

infrastructure_layer_decision_view = CBundle("infrastructure_layer_decision",
                                    elements=infrastructure_layer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_layer_decision.class_object,
                                            data_access_layer_decision.class_object
                                            , ]))

data_access_layer_decision_view = CBundle("data_access_layer_decision",
                                    elements=data_access_layer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_layer_decision.class_object,
                                            infrastructure_layer_decision.class_object
                                            , ]))

data_as_a_product_views = [
    _all, {},
    inter_decision_links_view, {},
    data_product_type_view, {},
    orchestration_decision_view, {},
    data_product_layer_decision_view, {},
    infrastructure_layer_decision_view, {},
    data_access_layer_decision_view, {}
]








