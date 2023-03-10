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

file_based_ingestion_pattern = CClass(pattern, 'file_based_ingestion_pattern')
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
observation_plane = CClass(pattern, "Observability Plane")
control_plane = CClass(pattern, "Control Plane")
storage_read_api = CClass(pattern, "Storage Read API")
cloud_storage_api = CClass(pattern, "Cloud Storage API")
event_streaming = CClass(pattern, "Event Streaming Backbone")
api_invocation = CClass(pattern, "API Invocation")
data_modeling_tool = CClass(pattern, "Data Modeling Tool")
orchestration_component = CClass(pattern, "Orchestration Component")
VMs = CClass(pattern, "VMs")
zero_trust_runtime_environment = CClass(pattern, "Zero trust runtime environment")
input_port = CClass(pattern, "Input Port")
output_port = CClass(pattern, "Output Port")
metastore = CClass(pattern, 'Metastore')
table = CClass(pattern, 'Dataset table')
blob_storage = CClass(pattern, 'Blob Storage')
legacy_modernization = CClass(pattern, "Legacy Modernization")
cloud_acceleration = CClass(pattern, "Cloud Acceleration")
legacy_modernization = CClass(pattern, "Legacy Modernization")
cloud_acceleration = CClass(pattern, "Cloud Acceleration")
metadata_lake = CClass(pattern, "Metadata lake")
data_storage_infrastructure = CClass(pattern, "Data Storage Infrastructure")

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
container_orchestration_system = CClass(practice, "Container Orchestration System")
infrastructure_as_code = CClass(practice, "Infrastructure as Code")
single_container_design = CClass(pattern, "Single-container design")
unified_batch_stream = CClass(practice, "Create a component for unified batch and stream data processing")
open_access = CClass(practice, "Open Access")
maintaining_source_of_truth = CClass(practice, "Maintaining a single source of truth")
run_tests = CClass(practice, "Run automated testing on your data product")
centrally_manage_monitor_govern_data = CClass(practice, "Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts")
snapshots_ETL = CClass(practice, "Send snapshots via nightly ETL")
snapshots_via_ReqResAPI = CClass(practice, "Send snapshots via Req/Res API")
dataset_versioning = CClass(practice, "Dataset Versioning")
schema_versioning = CClass(practice, "Schema Versioning")
data_contracts = CClass(practice, "Data Contracts")
active_metadata = CClass(practice, "Active metadata")
passive_metadata = CClass(practice, "Passive metadata")
containerisation = CClass(practice, "Containerisation")
hybrid_deployment = CClass(practice, "Hybrid Deployment")
multi_cloud_deployment = CClass(practice, "Multi-Cloud Deployment")
security_controls = CClass(practice, "Security Controls")
triggering = CClass(practice, "Alterting")
sql_layer = CClass(practice, "Attach a DBQuery Endpoint to each Data Product")
rest_apis = CClass(practice, "Attach REST APIs to each data product")
cache = CClass(practice, "Implement a highly available in-memory cache")
internal_storages = CClass(practice, "Internal Storage(s)")
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
non_functional = CClass(practice, "Data Product Policy Enforcement Mechanisms")
function_as_a_service = CClass(practice, "Function-as-a-Service")
run_time_environment_access_control = CClass(practice, "Run-time Environment Access Control")
row_based_access_control = CClass(practice, "Row-based Access Control")
api_access_control = CClass(practice, "API Access Control")
stream_access_control = CClass(practice, "Stream Access Control")
shared_storage = CClass(practice, "Shared Storage")
remote_procedure_invocation = CClass(practice, "gRPC")
graphQL = CClass(practice, "GraphQL")
metadata_management = CClass(practice, "Metadata Management")
reference_data_management = CClass(practice, "Reference Data Management")
overarching_management_layer = CClass(practice, "Overarching Management Layer")
infrastructure_provisioning = CClass(practice, "Infrastructure Provisioning")
storage_layer = CClass(practice, "Storage Layer")
lakehouse = CClass(practice, "Lakehouse Architecture")
shared_kafka_environment = CClass(practice, "Shared Event Streaming Environment")
source_aligned_data_product = CClass(practice, "Source-aligned Data Product")
consumer_aligned_data_product = CClass(practice, "Consumer-aligned Data Product")
transformed_data = CClass(practice, "Multiple raw data sets untransformed")
pre_transformed_data = CClass(practice, "Pre-transformed data")
low_level_events = CClass(practice, 'Low-level events')
aggregations = CClass(practice, 'Aggregations')
start_federated = CClass(practice, "Starting federated")
start_central = CClass(practice, "Starting central and decentralize at a later stage")
start_hybrid = CClass(practice, "Starting central and federated at the same time")
synchronous = CClass(practice, "Synchronous")
asynchronous = CClass(practice, "Asynchronous")
bitemporal_data = CClass(practice, "Bitemporal data")
multi_model_access = CClass(practice, "Multimodal access")
immutable_read_only_access = CClass(practice, "Immutable read-only access")
static_coupling = CClass(practice, "Static Coupling")
dynamic_coupling = CClass(practice, "Dynamic Coupling")
runtime_data = CClass(practice, "Provide information about runtime")
build_time_libraries = CClass(practice, "Provide information about build-time libraries")
crud = CClass(practice, 'CRUD-style operations')
policy_enforcement = CClass(practice, 'Policy Enforcement')
full_data_movement = CClass(practice, 'Full Data Movement')
incremental_data_movement = CClass(practice, 'Incremental Data Movement')
schema_validation_fail = CClass(practice, 'Attaching metadata about events that didn???t pass the schema validation')
non_programmatic_transformation = CClass(practice, 'Non-programmatic')
programmatic_transformation = CClass(practice, 'Programmatic')
dataflow_based_transformation = CClass(practice, 'Data flow based')
ml_bases_transformation = CClass(practice, 'ML based')
time_variant_transformation = CClass(practice, 'Time-variant')
conc_logical_phys = CClass(practice, 'Describes the translations being made between the conceptual model, logical model, and physical model')
batch_proccessing = CClass(practice, 'Batch processing')
schema_enforcement = CClass(practice, 'Schema enforcement')
schema_evolution = CClass(practice, 'Schema evolution')
data_quality_management = CClass(practice, 'Data quality management')
retention_policies = CClass(practice, 'Retention policies')
reference_database = CClass(practice, 'Reference database')
master_database = CClass(practice, 'Master database')
transformation_processes = CClass(practice, 'Transformation Processes')

# forces
security = CClass(force, "Security")
discoverability = CClass(force, "Discoverability")
accelerate_decision_making = CClass(force, "Accelerate Decision Making")
more_granular_data = CClass(force, "More granular data")
understandability = CClass(force, "Understandability for User")
standardised_transformation = CClass(force, "Standardised Transformation")
duplication = CClass(force, "Duplication")
trustworthiness = CClass(force, "Trustworthiness")
interoperability = CClass(force, "Interoperability")
completeness = CClass(force, "Completeness")
multiple_independent_read_only_views = CClass(force, "Multiple independent read-only views")
time_to_market = CClass(force, "Time-to-Market")
agility = CClass(force, "Agility")
manual_toil = CClass(force, "Manual Toil")
quality = CClass(force, "Data Quality")
fast_data_propagation = CClass(force, "Fast data propagation")
handle_large_data_volumes = CClass(force, "Handle large data volumes")
control_over_data_schema = CClass(force, "Control over data schema")
real_time_data_access = CClass(force, "Real-time Data Access")
reproducibility = CClass(force, "Reproducibility")
traceability = CClass(force, "Traceability")
verifiability = CClass(force, "Verifiability")
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
versioning_force = CClass(force, "Versioning")
continuity = CClass(force, "Continuity")
infrastructure_to_manage = CClass(force, "Infrastructure workload")
end_to_end_consistency = CClass(force, "End-to-end consistency")
stateless = CClass(force, "Stateless")
self_serve = CClass(force, "Self-serve Capability")
stale = CClass(force, "Stale")
clear_ownership = CClass(force, "Clear Ownership")
latency = CClass(force, "Latency")

# decisions, options, and contexts

# ** orchestration_decision **

orchestration_decision = CClass(decision, "What strategy can be used for data product implementation?")
add_decision_option_link(orchestration_decision, cloud_acceleration,
                         "Migration of enterprise systems to the cloud")
add_decision_option_link(orchestration_decision, legacy_modernization,
                         "Migration from legacy systems to modern data products")
add_decision_option_link(orchestration_decision, start_from_scratch,
                         "Starting with greenfield development")
add_force_relations({start_from_scratch: {accelerate_decision_making: very_positive,
                                          standardised_transformation: positive,
                                          fast_data_propagation: positive,
                                          scalable: positive,
                                          duplication: negative,
                                          time_to_market: very_negative,
                                          interoperability: negative},
                     cloud_acceleration: {accelerate_decision_making: positive,
                                          time_to_market: positive,
                                          scalable: very_positive,
                                          agility: positive,
                                          accessible: very_positive,
                                          control_over_data_schema: negative,
                                          security: negative,
                                          trustworthiness: negative},
                     legacy_modernization: {more_granular_data: positive,
                                            understandability: positive,
                                            fast_data_propagation: positive,
                                            real_time_data_access: very_positive,
                                            entry_barrier: negative,
                                            latency: negative,
                                            stale: negative}
                     })

leg_fed = \
    start_federated.add_links(legacy_modernization, role_name="from", stereotype_instances=can_be_realized_with)[0]
leg_central = \
    start_central.add_links(legacy_modernization, role_name="from", stereotype_instances=can_be_realized_with)[0]
leg_hybrid = \
    start_hybrid.add_links(legacy_modernization, role_name="from", stereotype_instances=can_be_realized_with)[0]

cloud_fed = \
    start_federated.add_links(cloud_acceleration, role_name="from", stereotype_instances=can_be_realized_with)[0]
cloud_central = \
    start_central.add_links(cloud_acceleration, role_name="from", stereotype_instances=can_be_realized_with)[0]
cloud_hybrid = \
    start_hybrid.add_links(cloud_acceleration, role_name="from", stereotype_instances=can_be_realized_with)[0]

green_federated = \
    start_federated.add_links(start_from_scratch, role_name="from", stereotype_instances=can_be_realized_with)[0]
green_central = \
    start_central.add_links(start_from_scratch, role_name="from", stereotype_instances=can_be_realized_with)[0]
green_hybrid = \
    start_hybrid.add_links(start_from_scratch, role_name="from", stereotype_instances=can_be_realized_with)[0]

federated_mdm = \
    mdm.add_links(start_federated, role_name="from", stereotype_instances=can_use)[0]
federated_cqrs = \
    cqrs.add_links(start_federated, role_name="from", stereotype_instances=can_use)[0]
federated_zero = \
    zero_trust_architecture.add_links(start_federated, role_name="from", stereotype_instances=can_use)[0]
federated_strang = \
    strangler_fig_pattern.add_links(start_federated, role_name="from", stereotype_instances=can_use)[0]

central_mdm = \
    mdm.add_links(start_central, role_name="from", stereotype_instances=can_use)[0]
central_cqrs = \
    cqrs.add_links(start_central, role_name="from", stereotype_instances=can_use)[0]
central_zero = \
    zero_trust_architecture.add_links(start_central, role_name="from", stereotype_instances=can_use)[0]
central_strang = \
    strangler_fig_pattern.add_links(start_central, role_name="from", stereotype_instances=can_use)[0]

hybrid_mdm = \
    mdm.add_links(start_hybrid, role_name="from", stereotype_instances=can_use)[0]
hybrid_cqrs = \
    cqrs.add_links(start_hybrid, role_name="from", stereotype_instances=can_use)[0]
hybrid_zero = \
    zero_trust_architecture.add_links(start_hybrid, role_name="from", stereotype_instances=can_use)[0]
hybrid_strang = \
    strangler_fig_pattern.add_links(start_hybrid, role_name="from", stereotype_instances=can_use)[0]

# ** data_product_type_decision **

data_product_type_decision = CClass(decision, "What type of data product can be developed?")
add_decision_option_link(data_product_type_decision, source_aligned_data_product,
                         "Generate a data product close to the operational database")
add_decision_option_link(data_product_type_decision, aggregations,
                         "Aggregate data from different data products")
add_decision_option_link(data_product_type_decision, consumer_aligned_data_product,
                         "Generate a data product close to the consumer")
add_force_relations({source_aligned_data_product: {understandability: very_positive,
                                              reproducibility: positive,
                                              time_to_market: positive,
                                              discoverability: negative,
                                              standardised_transformation: negative,
                                              interoperability: negative},
                     aggregations: {discoverability: positive,
                                    accelerate_decision_making: positive,
                                    understandability: positive,
                                    interoperability: positive,
                                    security: negative,
                                    control_over_data_schema: negative,
                                    immutability: negative},
                     consumer_aligned_data_product: {discoverability: positive,
                                                     understandability: positive,
                                                     agility: positive,
                                                     accessible: positive,
                                                     grouping: positive,
                                                     filtering: very_positive,
                                                     completeness: negative,
                                                     data_lineage: negative,
                                                     governance: negative}
                     })

algorithms_data_product_first_variation = \
    decision_support_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=can_use)[0]
algorithms_data_product_second_variation = \
    automated_decision_making_model_as_data_product.add_links(algorithms_as_data_product, role_name="from", stereotype_instances=can_use)[0]
transformed_data_derived = \
    transformed_data.add_links(derived_data_as_data_product, role_name="from", stereotype_instances=can_use)[0]
pre_transformed_data_derived = \
    pre_transformed_data.add_links(derived_data_as_data_product, role_name="from", stereotype_instances=can_use)[0]
low_level_events_derived = \
    low_level_events.add_links(derived_data_as_data_product, role_name="from", stereotype_instances=can_use)[0]
aggregations_derived = \
    derived_data_as_data_product.add_links(aggregations, role_name="from", stereotype_instances=can_use)[0]
aggregations_raw = \
    raw_data_as_data_product.add_links(aggregations, role_name="from", stereotype_instances=can_use)[0]
source_derived = \
    derived_data_as_data_product.add_links(source_aligned_data_product, role_name="from", stereotype_instances=can_use)[0]
source_raw = \
    raw_data_as_data_product.add_links(source_aligned_data_product, role_name="from", stereotype_instances=can_use)[0]
consumer_derived = \
    derived_data_as_data_product.add_links(consumer_aligned_data_product, role_name="from", stereotype_instances=can_use)[0]
consumer_raw = \
    raw_data_as_data_product.add_links(consumer_aligned_data_product, role_name="from", stereotype_instances=can_use)[0]
consumer_algorithm = \
    algorithms_as_data_product.add_links(consumer_aligned_data_product, role_name="from", stereotype_instances=can_use)[0]
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

# ** data_product_layer_decision **

data_product_layer_decision = CClass(decision, "What architectural components should be included in the anatomy of a data product?")
add_decision_option_link(data_product_layer_decision, change_data_capture,
                          "Implement a Change Data Capture component")
add_decision_option_link(data_product_layer_decision,immutable_change_audit_log,
                              "Implement a Immutable Log component")
add_decision_option_link(data_product_layer_decision,metastore,
                              "Implement a Metastore")
add_decision_option_link(data_product_layer_decision, data_catalogue,
                               "Implement a Data Catalogue component")
add_decision_option_link(data_product_layer_decision, data_onboarding,
                               "Implement Data Onboarding")
add_decision_option_link(data_product_layer_decision, internal_storages,
                               "Implement an Internal Storage for each Data Product")
add_decision_option_link(data_product_layer_decision, control_plane,
                               "Implement a Control Plane")
add_decision_option_link(data_product_layer_decision, observation_plane,
                                "Implement an Observation Plane")
add_force_relations({change_data_capture: {accelerate_decision_making: positive,
                                           fast_data_propagation: positive,
                                           interoperability: positive,
                                           quality: very_positive,
                                           traceability: positive,
                                           understandability: negative,
                                           data_lineage: negative,
                                           governance: negative},
                     metastore: {discoverability: very_positive,
                                 interoperability: positive,
                                 data_lineage: positive,
                                 governance: positive,
                                 scalable:positive,
                                 observability: positive,
                                 entry_barrier: negative},
                     data_catalogue: {discoverability: very_positive,
                                      accelerate_decision_making: positive,
                                      understandability: positive,
                                      data_search: positive,
                                      reproducibility: positive,
                                      traceability: positive,
                                      data_lineage: positive,
                                      clear_ownership: very_positive,
                                      accessible: positive,
                                      manual_toil: very_negative,
                                      entry_barrier: negative,
                                      centralization: very_negative,
                                      governance: negative},
                     immutable_change_audit_log: {security: positive,
                                                  traceability: very_positive,
                                                  verifiability: positive,
                                                  governance: positive,
                                                  manual_toil: negative,
                                                  latency: negative},
                     data_onboarding: {accelerate_decision_making: positive,
                                       time_to_market: positive,
                                       fast_data_propagation: positive,
                                       agility: positive,
                                       duplication: negative,
                                       manual_toil: negative,
                                       quality: negative,
                                       governance: negative},
                     control_plane: {centralization: positive,
                                     control_over_data_schema: very_positive,
                                     interoperability: positive,
                                     quality: positive,
                                     governance: positive,
                                     transparency: positive,
                                     manual_toil: negative,
                                     entry_barrier: negative},
                     observation_plane: {observability: very_positive,
                                         accelerate_decision_making: positive,
                                         reproducibility: positive,
                                         traceability: positive,
                                         manual_toil: negative,
                                         entry_barrier: negative},
                     internal_storages: {accessible: positive,
                                         autonomous: very_positive,
                                         understandability: negative,
                                         duplication: negative
                                         }
                     })

full_cdc = \
    full_data_movement.add_links(change_data_capture, role_name="from", stereotype_instances=enables)[0]
incremental_cdc = \
    incremental_data_movement.add_links(change_data_capture, role_name="from", stereotype_instances=enables)[0]

metastore_schema_versioning = \
    schema_versioning.add_links(metastore, role_name="from", stereotype_instances=enables)[0]
metastore_fail_schema = \
    schema_validation_fail.add_links(metastore, role_name="from", stereotype_instances=includes)[0]
metastore_active = \
    active_metadata.add_links(metastore, role_name="from", stereotype_instances=enables)[0]
immutable_dataset_versioning = \
    dataset_versioning.add_links(immutable_change_audit_log, role_name="from", stereotype_instances=enables)[0]
immutable_change_audit_log_alerting = \
    triggering.add_links(immutable_change_audit_log, role_name="from", stereotype_instances=enables)[0]

data_catalogue_passive = \
    passive_metadata.add_links(data_catalogue, role_name="from", stereotype_instances=enables)[0]
data_catalogue_register_datasets = \
    register_datasets.add_links(data_catalogue, role_name="from", stereotype_instances=enables)[0]
register_datasets_domain_data = \
    domain_datasets.add_links(register_datasets, role_name="from", stereotype_instances=includes)[0]
register_datasets_core_data = \
    core_datasets.add_links(register_datasets, role_name="from", stereotype_instances=includes)[0]

internal_storage_source_of_truth = \
    maintaining_source_of_truth.add_links(internal_storages, role_name="from", stereotype_instances=enables)[0]
internal_storage_data_marts = \
    data_marts.add_links(internal_storages, role_name="from", stereotype_instances=can_be_realized_with)[0]

control_onboarding = \
    data_onboarding.add_links(control_plane, role_name="from", stereotype_instances=can_use)[0]
control_storage = \
    internal_storages.add_links(control_plane, role_name="from", stereotype_instances=can_use)[0]

catalog_onboarding = \
    data_catalogue.add_links(data_onboarding, role_name="from", stereotype_instances=can_use)[0]
immutable_onboarding = \
    immutable_change_audit_log.add_links(data_onboarding, role_name="from", stereotype_instances=can_use)[0]
prog_onboarding = \
    transformation_processes.add_links(data_onboarding, role_name="from", stereotype_instances=can_use)[0]
prog_onboarding = \
    programmatic_transformation.add_links(transformation_processes, role_name="from", stereotype_instances=can_use)[0]
nonprog_onboarding = \
    non_programmatic_transformation.add_links(transformation_processes, role_name="from", stereotype_instances=can_use)[0]
dataflow_onboarding = \
    dataflow_based_transformation.add_links(transformation_processes, role_name="from", stereotype_instances=can_use)[0]
ml_onboarding = \
    ml_bases_transformation.add_links(transformation_processes, role_name="from", stereotype_instances=can_use)[0]
time_variant_onboarding = \
    time_variant_transformation.add_links(transformation_processes, role_name="from", stereotype_instances=can_use)[0]

# ** interface_decision **

interface_decision = CClass(decision, "What are the elements of a data product interface/contract?")
add_decision_option_link(interface_decision, observation_port,
                         "Implement an observation port")
add_decision_option_link(interface_decision, control_port,
                             "Implement a control port")
add_decision_option_link(interface_decision, discovery_port,
                               "Implement a discovery port")
add_decision_option_link(interface_decision, overarching_management_layer,
                               "Implement an overarching management layer")
add_decision_option_link(interface_decision, input_port,
                               "Implement an input port")
add_decision_option_link(interface_decision, output_port,
                               "Implement an input port")
add_force_relations({observation_port: {observability: very_positive,
                                        accelerate_decision_making: positive,
                                        quality: positive,
                                        scalable: positive,
                                        manual_toil: negative},
                     discovery_port: {discoverability: very_positive,
                                      accelerate_decision_making: positive,
                                      standardised_transformation: positive,
                                      duplication: negative,
                                      governance: negative},
                     control_port: {security: positive,
                                    governance: very_positive,
                                    interoperability: positive,
                                    scalable: positive,
                                    entry_barrier: positive,
                                    agility: negative,
                                    manual_toil: negative,
                                    latency: negative,
                                    clear_ownership: negative},
                     overarching_management_layer: {control_over_data_schema: positive,
                                                    interoperability: positive,
                                                    governance: very_positive,
                                                    scalable: positive,
                                                    autonomous: negative,
                                                    agility: negative,
                                                    entry_barrier: negative},
                     input_port: {accelerate_decision_making: positive,
                                  accessible: very_positive,
                                  agility: positive,
                                  fast_data_propagation: positive,
                                  handle_large_data_volumes: positive,
                                  scalable: positive,
                                  duplication: negative,
                                  quality: negative,
                                  data_lineage: negative},
                     output_port: {accelerate_decision_making: positive,
                                   accessible: positive,
                                   more_granular_data: positive,
                                   fast_data_propagation: positive,
                                   scalable: positive,
                                   self_serve: positive,
                                   security: negative,
                                   duplication: negative,
                                   quality: negative,
                                   stale: negative,
                                   latency: negative}
                        })

observation_port_quality_monitoring = \
    quality_monitoring.add_links(observation_port, role_name="from", stereotype_instances=realizes)[0]
discovery_port_data_marketplace = \
    data_marketplace.add_links(discovery_port, role_name="from", stereotype_instances=enables)[0]

control_port_policy = \
    policy_enforcement.add_links(control_port, role_name="from", stereotype_instances=enables)[0]
policy_retention = \
    retention_policies.add_links(policy_enforcement, role_name="from", stereotype_instances=includes)[0]

overarching_management_layer_control = \
    control_port.add_links(overarching_management_layer, role_name="from", stereotype_instances=includes)[0]
overarching_management_layer_discovery= \
    discovery_port.add_links(overarching_management_layer, role_name="from", stereotype_instances=includes)[0]
overarching_management_layer_observation = \
    observation_port.add_links(overarching_management_layer, role_name="from", stereotype_instances=includes)[0]

input_static = \
    static_coupling.add_links(input_port, role_name="from", stereotype_instances=realizes)[0]
input_dynamic = \
    dynamic_coupling.add_links(input_port, role_name="from", stereotype_instances=enables)[0]

output_static = \
    static_coupling.add_links(output_port, role_name="from", stereotype_instances=realizes)[0]
output_dynamic = \
    dynamic_coupling.add_links(output_port, role_name="from", stereotype_instances=enables)[0]
output_multimodal = \
    multi_model_access.add_links(output_port, role_name="from", stereotype_instances=realizes)[0]
output_bitemporal = \
    bitemporal_data.add_links(output_port, role_name="from", stereotype_instances=enables)[0]
output_immutable = \
    immutable_read_only_access.add_links(output_port, role_name="from", stereotype_instances=realizes)[0]

synchronous_static = \
    synchronous.add_links(static_coupling, role_name="from", stereotype_instances=realizes)[0]
asynchronous_static = \
    asynchronous.add_links(static_coupling, role_name="from", stereotype_instances=enables)[0]
build_in_static = \
    build_time_libraries.add_links(static_coupling, role_name="from", stereotype_instances=enables)[0]

synchronous_dynamic = \
    synchronous.add_links(dynamic_coupling, role_name="from", stereotype_instances=realizes)[0]
asynchronous_dynamic = \
    asynchronous.add_links(dynamic_coupling, role_name="from", stereotype_instances=enables)[0]
run_time_dynamic = \
    runtime_data.add_links(dynamic_coupling, role_name="from", stereotype_instances=enables)[0]

sync_crud = \
    crud.add_links(synchronous, role_name="from", stereotype_instances=enables)[0]
sync_rest = \
    rest_apis.add_links(synchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
async_rest = \
    rest_apis.add_links(asynchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
sync_graphql = \
    graphQL.add_links(synchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
sync_grpc = \
    remote_procedure_invocation.add_links(synchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
async_grpc = \
    remote_procedure_invocation.add_links(asynchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
sync_sql = \
    sql_layer.add_links(synchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]
async_sql = \
    sql_layer.add_links(asynchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]

async_pub = \
    pub_sub.add_links(asynchronous, role_name="from", stereotype_instances=can_be_realized_with)[0]

# ** data_product_self_serve_management_decision **

data_product_self_serve_management_decision = CClass(decision, "How does the data product interact with other data products, self-serve platform, government layer and consumers?")
add_decision_option_link(data_product_self_serve_management_decision, schema_manager,
                         "Implement a Schema Registry component")
add_decision_option_link(data_product_self_serve_management_decision,central_data_product_catalogue,
                             "Implement an Central Data Product Catalogue component")
add_decision_option_link(data_product_self_serve_management_decision,metadata_lake,
                             "Implement a metadata lake")
add_decision_option_link(data_product_self_serve_management_decision, event_streaming,
                               "Implement an Event Streaming Backbone")
add_decision_option_link(data_product_self_serve_management_decision, batch_proccessing,
                               "Implement batch processing via push or pull")
add_decision_option_link(data_product_self_serve_management_decision, shared_storage,
                               "Implement a shared storage")
add_decision_option_link(data_product_self_serve_management_decision, master_database,
                               "Implement a master database")
add_decision_option_link(data_product_self_serve_management_decision, reference_database,
                               "Implement a reference database")
add_decision_option_link(data_product_self_serve_management_decision, non_functional,
                         "Implement Data Product Policy Enforcement Mechanisms")
add_force_relations({schema_manager: {standardised_transformation: very_positive,
                                      centralization: positive,
                                      discoverability: positive,
                                      interoperability: positive,
                                      quality: positive,
                                      versioning_force: positive,
                                      governance: positive,
                                      entry_barrier: negative,
                                      time_to_market: negative},
                     central_data_product_catalogue: {discoverability: very_positive,
                                                      centralization: positive,
                                                      interoperability: positive,
                                                      accessible: positive,
                                                      governance: very_positive,
                                                      observability: positive,
                                                      entry_barrier: negative,
                                                      autonomous: negative,
                                                      agility: negative,
                                                      accelerate_decision_making: negative},
                     metadata_lake: {discoverability: positive,
                                     centralization: positive,
                                     accelerate_decision_making: positive,
                                     standardised_transformation: positive,
                                     interoperability: very_positive,
                                     completeness: positive,
                                     data_lineage: positive,
                                     governance: positive,
                                     entry_barrier: negative,
                                     data_search: negative,
                                     understandability: negative},
                     batch_proccessing: {handle_large_data_volumes: very_positive,
                                         time_to_market: positive,
                                         reproducibility: positive,
                                         fast_data_propagation: negative,
                                         real_time_data_access: negative,
                                         agility: negative,
                                         latency: negative},
                     event_streaming: {fast_data_propagation: positive,
                                       scalable: positive,
                                       real_time_data_access: positive,
                                       multiple_independent_read_only_views: positive,
                                       agility: positive,
                                       quality: negative,
                                       understandability: negative},
                     shared_storage: {quality: positive,
                                      completeness: positive,
                                      accessible: positive,
                                      interoperability: positive,
                                      time_to_market: positive,
                                      scalable: positive,
                                      control_over_data_schema: negative,
                                      data_lineage: negative,
                                      immutability: negative,
                                      transparency: negative,
                                      addressible: negative},
                     master_database: {end_to_end_consistency: very_positive,
                                       quality: positive,
                                       autonomous: negative,
                                       scalable: negative},
                     reference_database: {understandability: very_positive,
                                          end_to_end_consistency: positive,
                                          completeness: positive,
                                          transparency: positive,
                                          entry_barrier: negative,
                                          stale: negative},
                     non_functional: {security: very_positive,
                                      governance: positive,
                                      quality: positive,
                                      agility: negative,
                                      manual_toil: negative,
                                      self_serve: negative}
                        })

schema_evolution_registry = \
    schema_evolution.add_links(schema_manager, role_name="from", stereotype_instances=enables)[0]
schema_enforcement_registry = \
    schema_enforcement.add_links(schema_manager, role_name="from", stereotype_instances=enables)[0]

metadata_lake_blob = \
    blob_storage.add_links(metadata_lake, role_name="from", stereotype_instances=can_use)[0]

central_data_product_catalogue_centrally_manage_monitor_govern_data = \
    centrally_manage_monitor_govern_data.add_links(central_data_product_catalogue, role_name="from", stereotype_instances=enables)[0]
central_data_product_models = \
    conc_logical_phys.add_links(central_data_product_catalogue, role_name="from", stereotype_instances=enables)[0]

batch_blob = \
    blob_storage.add_links(batch_proccessing, role_name="from", stereotype_instances=can_be_realized_with)[0]
batch_table = \
    table.add_links(batch_proccessing, role_name="from", stereotype_instances=can_be_realized_with)[0]

shared_storage_storage_read = \
    storage_read_api.add_links(shared_storage, role_name="from", stereotype_instances=can_be_realized_with)[0]
shared_storage_cloud_storage = \
    cloud_storage_api.add_links(shared_storage, role_name="from", stereotype_instances=can_be_realized_with)[0]

non_functional_cache = \
    cache.add_links(non_functional, role_name="from", stereotype_instances=can_use)[0]
non_functional_quality = \
    data_quality_management.add_links(non_functional, role_name="from", stereotype_instances=can_use)[0]
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

# ** deploy_decision **

deploy_decision = CClass(decision, "How to deploy a data product?")
add_decision_option_link(deploy_decision, function_as_a_service,
                               "Use a serverless architecture")
add_decision_option_link(deploy_decision, containerisation,
                               "Use a containerised architecture")
add_decision_option_link(deploy_decision, data_storage_infrastructure,
                                "Use a Data Storage Infrastructure")
add_decision_option_link(deploy_decision, VMs,
                                "Use virtual machines")
add_decision_option_link(deploy_decision, hybrid_deployment,
                                "Use hybrid deployment")
add_decision_option_link(deploy_decision, multi_cloud_deployment,
                                "Use multi clouds")
add_force_relations({function_as_a_service: {agility: positive,
                                             time_to_market: positive,
                                             infrastructure_to_manage: positive,
                                             scalable: positive,
                                             stateless: positive,
                                             self_serve: positive,
                                             security: negative,
                                             latency: negative,
                                             discoverability: negative,
                                             data_enrichment: negative},
                     containerisation: {scalable: positive,
                                        agility: positive,
                                        standardised_transformation: positive,
                                        entry_barrier: negative,
                                        understandability: negative,
                                        infrastructure_to_manage: negative},
                     VMs: {security: positive,
                           control_over_data_schema: positive,
                           versioning_force: positive,
                           agility: negative,
                           infrastructure_to_manage: negative,
                           scalable: negative},
                     data_storage_infrastructure: {scalable: positive,
                                                   fast_data_propagation: positive,
                                                   handle_large_data_volumes: positive,
                                                   accessible: positive,
                                                   security: negative,
                                                   duplication: negative,
                                                   data_lineage: negative,
                                                   data_search: negative},
                     hybrid_deployment: {accessible: positive,
                                         interoperability: positive,
                                         scalable: positive,
                                         continuity: positive,
                                         infrastructure_to_manage: positive,
                                         agility: positive,
                                         time_to_market: positive,
                                         understandability: negative,
                                         governance: negative,
                                         security: negative,
                                         discoverability: negative,
                                         clear_ownership: negative,
                                         centralization: negative},
                     multi_cloud_deployment: {scalable: positive,
                                              agility: positive,
                                              time_to_market: positive,
                                              infrastructure_to_manage: positive,
                                              understandability: negative,
                                              security: negative,
                                              interoperability: negative,
                                              governance: negative,
                                              latency: negative}
                     })

container_orchestration_system_containerisation = \
    container_orchestration_system.add_links(containerisation, role_name="from", stereotype_instances=includes)[0]
container_orchestration_system_IaaS = \
    infrastructure_as_code.add_links(container_orchestration_system, role_name="from", stereotype_instances=can_use)[0]

containerisation_zero_run_time_environment = \
    zero_trust_runtime_environment.add_links(containerisation, role_name="from", stereotype_instances=can_use)[0]
ontainerisation_zero_run_time_environment = \
    zero_trust_runtime_environment.add_links(VMs, role_name="from", stereotype_instances=can_use)[0]
containerisation_kafka_environment = \
    shared_kafka_environment.add_links(containerisation, role_name="from", stereotype_instances=can_use)[0]
ontainerisation_kafka_environment = \
    shared_kafka_environment.add_links(VMs, role_name="from", stereotype_instances=can_use)[0]

containerisation_single_container_design = \
    single_container_design.add_links(containerisation, role_name="from", stereotype_instances=can_be_realized_with)[0]
containerisation_infrastructure_as_code = \
    infrastructure_as_code.add_links(containerisation, role_name="from", stereotype_instances=can_use)[0]
containerisation_templated_data_pipeline = \
    templated_data_pipeline.add_links(containerisation, role_name="from", stereotype_instances=can_use)[0]
templated_data_pipeline_ci_cd_process = \
    ci_cd_process.add_links(templated_data_pipeline, role_name="from", stereotype_instances=leads_to)[0]

# decision links
add_links({orchestration_decision: [data_product_type_decision],
           data_product_type_decision: [data_product_layer_decision, data_product_self_serve_management_decision, interface_decision],
           data_product_layer_decision: [deploy_decision],
           data_product_self_serve_management_decision: [deploy_decision],
           interface_decision: [deploy_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=data_product_type_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[data_product_type_decision,
                                              deploy_decision, orchestration_decision, data_product_self_serve_management_decision,
                                              data_product_layer_decision, interface_decision])

orchestration_decision_view = CBundle("orchestration_decision",
                                    elements=orchestration_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            data_product_layer_decision.class_object,
                                            interface_decision.class_object
                                            , ]))

data_product_type_view = CBundle("data_product_type_decision",
                                    elements=data_product_type_decision.class_object.get_connected_elements(
                                             stop_elements_exclusive=forces_class_objects + [
                                                 deploy_decision.class_object,
                                                 orchestration_decision.class_object,
                                                 interface_decision.class_object,
                                                 data_product_self_serve_management_decision.class_object,
                                                 data_product_layer_decision.class_object
                                             ,]))

data_product_layer_decision_view = CBundle("data_product_layer_decision",
                                    elements=data_product_layer_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            interface_decision.class_object,
                                            data_product_self_serve_management_decision.class_object
                                            , ]))

interface_view = CBundle("interface_decision",
                                    elements=interface_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_self_serve_management_decision.class_object
                                            , ]))

data_product_self_serve_management_decision_view = CBundle("data_product_self_serve_management_decision",
                                    elements=data_product_self_serve_management_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            deploy_decision.class_object,
                                            orchestration_decision.class_object,
                                            data_product_layer_decision.class_object,
                                            interface_decision.class_object
                                            , ]))

deploy_decision_view = CBundle("deploy_decision",
                                    elements=deploy_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            orchestration_decision.class_object,
                                            interface_decision.class_object,
                                            data_product_self_serve_management_decision.class_object,
                                            data_product_layer_decision.class_object
                                            , ]))

data_as_a_product_views = [
    _all, {},
    inter_decision_links_view, {},
    orchestration_decision_view, {},
    data_product_type_view, {},
    data_product_layer_decision_view, {},
    interface_view, {},
    data_product_self_serve_management_decision_view, {},
    deploy_decision_view, {}
]








