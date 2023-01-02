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
capture_data_change = CClass(pattern, "Capture Data Change")
data_integration_service = CClass(pattern, "Use a data integration service that helps users efficiently build and manage ETL/ELT pipelines")
internal_storages = CClass(pattern, "Internal storages where the data product is deployed, not exposed to consumers")
immutable_change_audit_log = CClass(pattern, "Immutable Change Audit Log")
cache = CClass(pattern, "Implement a highly available in-memory cache")
lineage_repository = CClass(pattern, "Lineage Repository")
universal_metadata_registry = CClass(pattern, "Universal Metadata Registry")
low_level_events_and_aggregation_layer = CClass(pattern, "Low level events and aggregation layer")
cqrs = CClass(pattern, "CQRS")

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
low_level_events_and_aggregations_layer = CClass(practice, "Low-Level Events and Aggregations Layer")
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
add_decision_option_link(keep_track_metadata_decision, capture_data_change,
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
add_force_relations({data_catalogue: {standardised_transformation: positive,
                                          duplication: negative,
                                          obscurity: negative}
                        })


# ** trustworty_decision **

trustworty_decision = CClass(decision, "How to make a data product trustworty?")
add_decision_option_link(trustworty_decision, quality_monitoring,
                         "Only use one single integrated monitoring experience")
add_decision_option_link(trustworty_decision, observation_plane,
                         "Use an observability plane to observe changes in the data")
add_decision_option_link(trustworty_decision, schema_manager,
                         "Use a schema manager to understand the data as you read the schema")
add_force_relations({observation_plane: {understandability: positive,
                                         accuracy: positive,
                                         completeness: positive,
                                         integrity: positive},
                         schema_manager: {understandability: positive}
                     })
add_decision_option_link(trustworty_decision, time_bounded_backwards_compatibility,
                         "Include backwards compatibility")

# ** data_access_decision **

data_access_decision = CClass(decision, "How can the user interact with data products?")
add_decision_option_link(data_access_decision, rest_apis,
                         "Provide programmatic access through REST APIs")
add_decision_option_link(data_access_decision, sql_layer,
                         "Provide access through SQL queries")
add_force_relations({rest_apis: {internal_complexity: positive,
                                complexity_for_user: negative},
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
add_force_relations({domain_datasets: {prioritise: positive},
                         core_datasets: {prioritise: positive,
                                         trustworthiness: positive,
                                         interoperability: positive
                                         }
                     })
add_decision_option_link(data_product_anatomy_decision, low_level_events_and_aggregations_layer,
                    "Distinguish on aggregation")

# ** communicaton_decision **

communicaton_decision = CClass(decision, "How can data products communicate?")
add_decision_option_link(communicaton_decision, event_streaming,
                         "Messaging through events")
add_decision_option_link(communicaton_decision, data_integration_service,
                         "Use a data integration service for ingestion")
add_decision_option_link(communicaton_decision, triggering,
                                "Use triggers to activate certain actions")
add_decision_option_link(communicaton_decision, cqrs,
"Separate read and update operations for a data store")

add_force_relations({cqrs: {multiple_independent_read_only_views: positive}
                     })
# ** security_decision **

security_decision = CClass(decision, "How to secure your data products?")
add_decision_option_link(security_decision , role_based_access_control,
                         "Provide access based on the user's role")
add_decision_option_link(security_decision, encryption,
                         "Secure with an encryption key")

# ** store_decision **

store_decision = CClass(decision, "Where can we store the data?")
add_decision_option_link(store_decision, internal_storages,
                         "Store data internally inside the data product")
add_decision_option_link(store_decision, cache,
                         "Store the data in a cache")

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
add_force_relations({infrastructure_as_code: {compliance: positive,
                                              provenance: positive}
                     })
































