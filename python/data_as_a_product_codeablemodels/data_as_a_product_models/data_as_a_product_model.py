from api_ddd_models.domain_model import domain_model, identified_interface_elements, domain_model_and_api, \
    domain_model_element_link
from codeable_models import CClass, add_links, CBundle
from map_models.map_domain_model import api, message, operation, api_contract
from metamodels.guidance_metamodel import do_nothing_design_solution, decision, practice, add_decision_option_link, \
    add_stereotyped_link_with_how_tagged_value, force, negative, uses, positive, can_be_realized_with, extension, \
    consider_if_not_decided_yet, decide_for_some_instances_of, pattern, decide_for_all_instances_of, \
    very_negative, neutral, very_positive, can_use, enables, variant, is_a


def add_force_relations(force_relations_definition):
    for practice in force_relations_definition.keys():
        for force in force_relations_definition[practice]:
            stereotype = (force_relations_definition[practice])[force]
            add_links({practice: force}, role_name="forces", stereotype_instances=stereotype)


# patterns

search_engine = CClass(pattern, "Search Engine")
data_catalogue = CClass(pattern, "Data Catalogue")
query_catalogue = CClass(pattern, "Use example notebooks or SQL queries to describe the dataset")
rest_apis = CClass(pattern, "Attach a Data Access REST API to each Data Product")
sql_layer = CClass(pattern, "Attach a SQL layer to each Data Product")
data_access_decision = CClass(decision, "How can the user interact with data products?")
observation_plane = CClass(pattern, "The observability plane brings an interface between built-in observability of the data quantum and REST clients")
schema_manager = CClass(pattern, "Schema Manager")
change_data_capture = CClass(pattern, "Change Data Capture")
data_integration_service = CClass(pattern, "Use a data integration service that helps users efficiently build and manage ETL/ELT pipelines")
internal_storages = CClass(pattern, "Internal storages where the data product is deployed, not exposed to consumers")
immutable_change_audit_log = CClass(pattern, "Immutable Change Audit Log")
cache = CClass(pattern, "Implement a highly available in-memory cache")
lineage_repository = CClass(pattern, "Lineage Repository")
universal_metadata_registry = CClass(pattern, "Universal Metadata Registry")
low_level_events_and_aggregation_layer = CClass(pattern, "Low level events and aggregation layer")
cqrs = CClass(pattern, "CQRS")
feature_layer = CClass(pattern, "Feature Layer")
central_data_product_catalogue = CClass(pattern, "Central Data Product Catalogue")
end_to_end = CClass(pattern, "end-to-end connection")
no_sql_system = CClass(pattern, "NoSQL system")
orchestration = CClass(pattern, "orchestration")
discovery_port = CClass(pattern, "Discovery Port")
event_bus = CClass(pattern, "Event Bus")
data_marts = CClass(pattern, "Incrementally build business process-centric data marts")
templated_data_pipeline = CClass(pattern, "Templated Data Pipeline")
pub_sub = CClass(pattern, "Pub/Sub")
data_marketplace = CClass(pattern, "Data Marketplace")
open_source_data_and_analytics_processing_service = CClass(pattern, "Open source data and analytics processing service")
attribute_based_access_control = CClass(pattern, "Attribute-based Access Control")
multi_tenancy_model = CClass(pattern, " A single Subscription with a single workspace")
single_subscription_single_workspace_dedicated_artifacts_per_domain = CClass(pattern, "A single Subscription with a single workspace with dedicated artifacts for each domain")
single_subscription_multiple_workspaces = CClass(pattern, " A Subscription with multiple workspaces")
single_subscription_dedicated_workpasce_per_domain = CClass(pattern, "A single Azure Subscription with separate workspaces for each domain")
separate_subscriptions_separate_workspace_per_domain = CClass(pattern, "Separate subscriptions with separate workspaces for each domain")
control_plane = CClass(pattern, "Control Plane")

# practices
raw_data_as_data_product = CClass(practice, "Expose Data Product as Raw Data")
derived_data_as_data_product = CClass(practice, "Expose Data Product as Derived Data")
decision_support_model_as_data_product = CClass(practice, "Expose Data Product as Decision Support Model")
automated_decision_making_model_as_data_product = CClass(practice, "Expose Data Product as Automated Decision-making Model")
register_datasets = CClass(practice, "Register datasets")
request_access = CClass(practice, "Fine-grained Access Control")
quality_monitoring = CClass(practice, "Provide a single integrated experience for monitoring")
algorithms_as_data_product = CClass(practice, "Expose Data Product as an algorithm")
domain_datasets = CClass(practice, "The domain datasets belong to a specific domain")
core_datasets = CClass(practice, "Core datasets are those that are useful for more than one domain")
event_streaming = CClass(practice, "Event Streaming")
virtualisation = CClass(practice, "Virtualisation")
incremental_sync = CClass(practice, "Incremental Sync")
data_product_governance = CClass(practice, "Data Product Governance")
role_based_access_control = CClass(practice, "Role-based Access Control")
encryption = CClass(practice, "Encryption")
time_bounded_backwards_compatibility = CClass(practice, "Time-bounded Backwards Compatibility")
ci_cd_process = CClass(practice, " CI/CD process")
versioning = CClass(practice, "Versioning")
k8s = CClass(practice, "K8s")
mdm = CClass(practice, "Master Data Management")
infrastructure_as_code = CClass(practice, "Infrastructure as Code")
triggering = CClass(practice, "Triggering")
containerisation = CClass(practice, "Run containers that are invocable via requests or events")
unified_batch_stream = CClass(practice, "Create a component for unified batch and stream data processing")
open_access = CClass(practice, "Open Access")
maintaining_source_of_truth = CClass(practice, "Maintaining a single source of truth")
run_tests = CClass(practice, "Run tests on your data product")
centrally_manage_monitor_govern_data = CClass(practice, "Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts")
indirect_data_publishing_and_consumption = CClass(practice, "Indirect data publishing and consumption")
snapshots_ETL = CClass(practice, "Send snapshots via ETL")
zero_trust_architecture = CClass(practice, "Zero Trust Architecture")
oauth2 = CClass(practice, "OAUTH2")

# forces
security = CClass(force, "Security")
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
accuracy = CClass(force, "Accuracy")
completeness = CClass(force, "Completeness")
integrity = CClass(force, "Integrity")
multiple_independent_read_only_views = CClass(force, "Multiple independent read-only views")
re_use = CClass(force, "Re-use aspects by allowing other teams to find and build upon existing work")
time_to_market = CClass(force, "Time-to-Market")
conflicting_definitions = CClass(force, "Conflicting definitions")
periodic_execution = CClass(force, "Execution at periodic intervals")
consistency = CClass(force, "Consistency")
stability = CClass(force, "Stability")
swamp = CClass(force, "Turning the data lake into a swamp")
data_productivity = CClass(force, "Data Productivity")
analytics_agility = CClass(force, "Analytics Agility")
manual_toil = CClass(force, "Manual Toil")
quality = CClass(force, "Quality")
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

# links between practices

register_datasets_search_engine = \
    register_datasets.add_links(search_engine, role_name="to", stereotype_instances=uses)[0]
request_access_search_engine = \
    request_access.add_links(search_engine, role_name="to", stereotype_instances=uses)[0]

# decisions, options, and contexts

# ** data_product_type_decision **

data_product_type_decision = CClass(decision, "What type of data product can be developed?")
add_decision_option_link(data_product_type_decision, raw_data_as_data_product,
                         "Use raw data from the data product")
add_decision_option_link(data_product_type_decision, derived_data_as_data_product,
                         "Use derived data from the data product")
add_decision_option_link(data_product_type_decision, decision_support_model_as_data_product,
                         "The interface to access a data product is a visualisation")
add_decision_option_link(data_product_type_decision, automated_decision_making_model_as_data_product,
                         "The interface to access a data product is an app or website")
add_decision_option_link(data_product_type_decision, algorithms_as_data_product,
                         "Use algorithms to return information or insights")
add_force_relations({raw_data_as_data_product: {internal_complexity: very_positive,
                                                complexity_for_user: very_negative},
                     derived_data_as_data_product: {internal_complexity: positive,
                                                    complexity_for_user: negative},
                     algorithms_as_data_product: {internal_complexity: neutral,
                                                  complexity_for_user: neutral},
                    decision_support_model_as_data_product: {internal_complexity: negative,
                                                             complexity_for_user: positive},
                    automated_decision_making_model_as_data_product: {internal_complexity: very_negative,
                                                                      complexity_for_user: very_positive}
                     })


# ** discoverable_data_products_decision **

discoverable_data_products_decision = CClass(decision, "How to make data products discoverable?")
add_decision_option_link(discoverable_data_products_decision, register_datasets,
                         "Register all the relevant datasets for the data products")
add_decision_option_link(discoverable_data_products_decision, request_access,
                        "Access must be requested to use data inside the data product")
add_decision_option_link(discoverable_data_products_decision,discovery_port,
                             "Access Point to discover data inside the data product")
add_decision_option_link(discoverable_data_products_decision, data_marketplace,
                               "Use a data marketplace to publish datasets")
add_force_relations({register_datasets: {security: positive,
                                         discoverability: very_positive},
                     request_access: {security: very_positive,
                                         discoverability: neutral},
                      })

# ** keep_track_metadata_decision **

keep_track_metadata_decision = CClass(decision, "How to keep track of metadata?")
add_decision_option_link(keep_track_metadata_decision, data_catalogue,
                         "Use a data catalogue to describe the data inside a data product")
add_decision_option_link(keep_track_metadata_decision, query_catalogue,
                         "Provide example codes and queries to help the user understand the data")
add_decision_option_link(keep_track_metadata_decision, change_data_capture,
                         "Identify changes made in the data")
add_decision_option_link(keep_track_metadata_decision, virtualisation,
                         "Providing fast, cost-effective, and centralized access to and integration of all data sources that are important to an organization")
add_decision_option_link(keep_track_metadata_decision, data_product_governance,
                         "Create internal governance policies")
add_decision_option_link(keep_track_metadata_decision, immutable_change_audit_log,
                         "Keep track of data lineage")
add_decision_option_link(keep_track_metadata_decision, lineage_repository,
                         "Pay attention to the transformations")
add_decision_option_link(keep_track_metadata_decision , universal_metadata_registry,
                         "Store the metadata centrally")
add_decision_option_link(keep_track_metadata_decision, central_data_product_catalogue,
                        "Create a catalogue-of-catalogues")
add_force_relations({data_catalogue: {standardised_transformation: positive,
                                          duplication: negative,
                                          obscurity: negative},
                    central_data_product_catalogue: {discoverability: positive},
                    data_product_governance: {swamp: negative},
                    query_catalogue: {discoverability: positive,
                                          gain_knowledge: very_positive},
                    change_data_capture: {real_time_data_access: positive,
                                              complexity_for_user: negative,
                                              non_intrusive: positive,
                                              consumption: positive,
                                              production_grade_integrations: positive},
                    immutable_change_audit_log: {reproducibility: positive,
                                                      traceability: positive,
                                                      verifiability: positive}
                        })


# ** trustworty_decision **

trustworty_decision = CClass(decision, "How to make a data product trustworty?")
add_decision_option_link(trustworty_decision, quality_monitoring,
                         "Only use one single integrated monitoring experience")
add_decision_option_link(trustworty_decision, observation_plane,
                         "Use an observability plane to observe changes in the data")
add_decision_option_link(trustworty_decision, schema_manager,
                         "Use a schema manager to understand the data as you read the schema")
add_decision_option_link(trustworty_decision, maintaining_source_of_truth,
                               "Keep the original version of the data")
add_decision_option_link(trustworty_decision, run_tests,
                        "Run tests before deployment")
add_force_relations({observation_plane: {understandability: positive,
                                         accuracy: positive,
                                         completeness: positive,
                                         integrity: positive},
                         schema_manager: {understandability: positive,
                                          duplication: positive,
                                          conflicting_definitions: negative}
                     })
add_decision_option_link(trustworty_decision, time_bounded_backwards_compatibility,
                         "Include backwards compatibility")

# ** data_access_decision **

data_access_decision = CClass(decision, "How can the user interact with data products?")
add_decision_option_link(data_access_decision, rest_apis,
                         "Provide programmatic access through REST APIs")
add_decision_option_link(data_access_decision, sql_layer,
                         "Provide access through SQL queries")
add_decision_option_link(data_access_decision, no_sql_system,
                           "Use a NoSQL system")
add_force_relations({rest_apis: {internal_complexity: positive,
                                complexity_for_user: negative,
                                control_over_data_schema: positive},
                    sql_layer: {internal_complexity: positive,
                                complexity_for_user: positive,
                                accelerate_decision_making: very_positive,
                                more_granular_data: very_positive}
                     })

# ** data_product_anatomy_decision **

data_product_anatomy_decision = CClass(decision, "What is the anatomy of a Data Product?")
add_decision_option_link(data_product_anatomy_decision, domain_datasets,
                        "Distinguish domain datasets")
add_decision_option_link(data_product_anatomy_decision, core_datasets,
                         "Distinguish core datasets")
add_decision_option_link(data_product_anatomy_decision, low_level_events_and_aggregation_layer,
                                "Implement an aggregation layer")
add_decision_option_link(data_product_anatomy_decision,feature_layer,
                               "Add a special layer for the features")
add_decision_option_link(data_product_anatomy_decision, open_source_data_and_analytics_processing_service,
                            "Add an option to use open source data and convert this to analytical data")
add_decision_option_link(data_product_anatomy_decision, control_plane,
                             "Add a control plane to the data product")
add_force_relations({domain_datasets: {prioritise: positive},
                         core_datasets: {prioritise: positive,
                                         trustworthiness: positive,
                                         interoperability: positive
                                         },
                        feature_layer: {interoperability: positive,
                                        stability: positive}
                     })

# ** communication_decision **

communication_decision = CClass(decision, "How can data products communicate?")
add_decision_option_link(communication_decision, event_streaming,
                         "Messaging through events")
add_decision_option_link(communication_decision, data_integration_service,
                         "Use a data integration service for ingestion")
add_decision_option_link(communication_decision, triggering,
                                "Use triggers to activate certain actions")
add_decision_option_link(communication_decision, cqrs,
"Separate read and update operations for a data store")
add_decision_option_link(communication_decision, end_to_end,
                           "Connect data products end-to-end")
add_decision_option_link(communication_decision,unified_batch_stream,
                             "Schedule stream and batch processing jobs")
add_decision_option_link(communication_decision,event_bus,
                             "Location for all streaming event data")
add_decision_option_link(communication_decision, pub_sub,
                         "Use pub/sub to communicate new events")
add_decision_option_link(communication_decision, indirect_data_publishing_and_consumption,
                                "Process data indirectly, not point-to-point")
add_decision_option_link(communication_decision, snapshots_ETL,
                                "Generate ETL snapshots")
add_force_relations({cqrs: {multiple_independent_read_only_views: positive},
                    unified_batch_stream: {periodic_execution: positive},
                     pub_sub: {fast_data_propagation: positive,
                               handle_large_data_volumes: very_positive,
                               limit_recipients: positive,
                               addressability_subscriptions: positive},
                    snapshots_ETL: {control_over_data_schema: positive},
                    event_streaming: {real_time_data_access: positive,
                                       high_fidelity: positive}
                     })

# ** security_decision **

security_decision = CClass(decision, "How to secure your data products?")
add_decision_option_link(security_decision , role_based_access_control,
                         "Provide access based on the user's role")
add_decision_option_link(security_decision, encryption,
                         "Secure with an encryption key")
add_decision_option_link(security_decision, open_access,
                            "Everyone can use the data product")
add_decision_option_link(security_decision, attribute_based_access_control,
                         "Provide access based on attribute")
add_decision_option_link(security_decision, zero_trust_architecture,
                             "Apply a zero trust between the data products")
add_decision_option_link(security_decision, oauth2,
                             "Apply the OAUTH2 security approach")

# ** store_decision **

store_decision = CClass(decision, "Where can we store the data?")
add_decision_option_link(store_decision, internal_storages,
                         "Store data internally inside the data product")
add_decision_option_link(store_decision, cache,
                         "Store the data in a cache")
add_decision_option_link(store_decision,data_marts,
                             "Store data in a data mart")

# ** infrastructure_decision **

infrastructure_decision = CClass(decision, "How can we manage and provision the infrastucture")
add_decision_option_link(infrastructure_decision, infrastructure_as_code,
                         "Use code instead of manual processes")
add_decision_option_link(infrastructure_decision, ci_cd_process,
                         "Continuously adapt")
add_decision_option_link(infrastructure_decision, versioning,
                         "Keep control of your versions")
add_decision_option_link(infrastructure_decision, k8s,
                         "Use pods")
add_decision_option_link(infrastructure_decision, mdm,
                                  "Use a master data management database")
add_decision_option_link(infrastructure_decision, containerisation,
                            "Containerise all the domains")
add_decision_option_link(infrastructure_decision, orchestration,
                             "Integrate applications into a single offering")
add_decision_option_link(infrastructure_decision, templated_data_pipeline,
                             "Use a templated data pipeline to easily adopt and extend")
add_decision_option_link(infrastructure_decision, centrally_manage_monitor_govern_data,
                            "Manage all data products centrally")
add_force_relations({infrastructure_as_code: {compliance: positive,
                                              provenance: positive,
                                              discoverability: positive,
                                              re_use: positive,
                                              time_to_market: positive,
                                              duplication: positive},
                    orchestration: {consistency: positive},
                    centrally_manage_monitor_govern_data: {data_productivity: very_positive,
                                                            analytics_agility: very_positive,
                                                            manual_toil: negative,
                                                            security: positive,
                                                            quality: positive,
                                                            discovery: positive},
                    versioning: {multiple_environments: positive},
                    ci_cd_process: {multiple_environments: positive}
                     })

# ** structural_decision **

structural_decision = CClass(decision, "How to deploy a data product using subscriptions and workspaces?")
add_decision_option_link(structural_decision, multi_tenancy_model,
                         "Each domain gets a slice of resources")
add_decision_option_link(structural_decision, single_subscription_single_workspace_dedicated_artifacts_per_domain,
                         "Separate the artifacts aligned to various domains")
add_decision_option_link(structural_decision, single_subscription_multiple_workspaces,
                         "Generate multiple workspaces in a single subscription")
add_decision_option_link(structural_decision, single_subscription_dedicated_workpasce_per_domain,
                         "Each domain gets a separate workspace")
add_decision_option_link(structural_decision, separate_subscriptions_separate_workspace_per_domain,
                         "Use separate subscriptions and separate workspaces")

# decision links
add_links({data_product_type_decision: [structural_decision, data_product_anatomy_decision],
           structural_decision: [data_access_decision, keep_track_metadata_decision, infrastructure_decision, communication_decision],
           data_product_anatomy_decision: [store_decision, trustworty_decision, security_decision, discoverable_data_products_decision]},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=data_product_type_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[data_product_type_decision, structural_decision,
                                              data_product_anatomy_decision, data_access_decision, keep_track_metadata_decision,
                                              infrastructure_decision, communication_decision, store_decision, trustworty_decision, security_decision, discoverable_data_products_decision])
data_product_type_view = CBundle("data_product_type_decision",
                                    elements=data_product_type_decision.class_object.get_connected_elements(
                                             stop_elements_exclusive=forces_class_objects + [
                                                 structural_decision.class_object,
                                                 data_product_anatomy_decision.class_object,
                                                 data_access_decision.class_object,
                                                 keep_track_metadata_decision.class_object,
                                                 infrastructure_decision.class_object,
                                                 communication_decision.class_object,
                                                 store_decision.class_object,
                                                 trustworty_decision.class_object,
                                                 security_decision.class_object,
                                                 discoverable_data_products_decision.class_object
                                             ,]))

structural_decision_view = CBundle("structural_decision",
                                    elements=structural_decision.class_object.get_connected_elements(
                                            stop_elements_exclusive=forces_class_objects + [
                                                 data_product_type_decision.class_object,
                                                 data_product_anatomy_decision.class_object,
                                                 data_access_decision.class_object,
                                                 keep_track_metadata_decision.class_object,
                                                 infrastructure_decision.class_object,
                                                 communication_decision.class_object,
                                                 store_decision.class_object,
                                                 trustworty_decision.class_object,
                                                 security_decision.class_object,
                                                 discoverable_data_products_decision.class_object
                                             ,]))


data_product_anatomy_decision_view = CBundle("data_product_anatomy_decision",
                                    elements=data_product_anatomy_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

data_access_decision_view = CBundle("data_access_decision",
                                    elements=data_access_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

keep_track_metadata_decision_view = CBundle("keep_track_metadata_decision",
                                    elements=keep_track_metadata_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

infrastructure_decision_view = CBundle("infrastructure_decision",
                                    elements=infrastructure_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                         , ]))

communication_decision_view = CBundle("communication_decision",
                                    elements=communication_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

store_decision_view = CBundle("store_decision",
                                    elements=store_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

trustworty_decision_view = CBundle("trustworty_decision",
                                    elements=trustworty_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            security_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

security_decision_view = CBundle("security_decision",
                                    elements=security_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            discoverable_data_products_decision.class_object
                                            , ]))

discoverable_data_products_decision_view = CBundle("discoverable_data_products_decision",
                                    elements=discoverable_data_products_decision.class_object.get_connected_elements(
                                        stop_elements_exclusive=forces_class_objects + [
                                            data_product_type_decision.class_object,
                                            structural_decision.class_object,
                                            data_product_anatomy_decision.class_object,
                                            data_access_decision.class_object,
                                            keep_track_metadata_decision.class_object,
                                            infrastructure_decision.class_object,
                                            communication_decision.class_object,
                                            store_decision.class_object,
                                            trustworty_decision.class_object,
                                            security_decision.class_object
                                            , ]))

data_as_a_product_views = [
    _all, {},
    inter_decision_links_view, {},
    structural_decision_view, {},
    data_product_type_view, {},
    data_product_anatomy_decision_view, {},
    data_access_decision_view, {},
    keep_track_metadata_decision_view, {},
    infrastructure_decision_view, {},
    communication_decision_view, {},
    store_decision_view, {},
    trustworty_decision_view, {},
    security_decision_view, {},
    discoverable_data_products_decision_view, {}
]








