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
# https://www.microservice-api-patterns.org/patterns/quality/referenceManagement/LinkedInformationHolder
linked_information_holder = CClass(pattern, "Linked Information Holder")
# https://www.microservice-api-patterns.org/patterns/quality/referenceManagement/EmbeddedEntity
embedded_entity = CClass(pattern, "Embedded Entity")
processing_resource = CClass(pattern, "Processing Resource")
# from remoting patterns:
object_identifier = CClass(pattern, "Object Identifier")
# Command Query Responsibility Segregation. https://martinfowler.com/bliki/CQRS.html
cqrs = CClass(pattern, "CQRS")
eventual_consistency = CClass(pattern, "Eventual Consistency")

# practices
api_contract_specified = CClass(practice, "Explicitly Specify the API Contract")
api_contract_specified_first = CClass(practice, "Specify the API Contract First")
api_contract_extracted = CClass(practice, "Extract API Contract from Domain Model")
domain_model_defines_api_contract = CClass(practice, "Domain Model Defines API Contract")
bounded_context_defines_api_contract = CClass(practice, "Bounded Context Defines API Contract")
bounded_context_defines_api_contract = CClass(practice, "Bounded Context Defines API Contract")
api_code_first = CClass(practice, "Write API Code First which Defines the Contract")

expose_domain_model_as_API = CClass(practice, "Expose the Whole Domain Model in 1:1 Relation as API")
expose_domain_model_subset_as_API = CClass(practice, "Expose Domain Model Subset as API")
expose_bounded_contexts_as_APIs = CClass(practice, "Expose Bounded Contexts as APIs")
expose_each_bounded_context_as_an_API = CClass(practice, "Expose Each Bounded Context as an API",
                                               superclasses=expose_bounded_contexts_as_APIs)
expose_selected_bounded_contexts_as_an_API = CClass(practice, "Expose Selected Bounded Contexts as APIs",
                                                    superclasses=expose_bounded_contexts_as_APIs)
interface_bounded_context_as_API = CClass(practice,
                                          "Introduce and Expose Interface Bounded Context as an API",
                                          superclasses=expose_bounded_contexts_as_APIs)
shared_kernel_as_API = CClass(practice, "Expose a Shared Kernel between Client and Server as an API")

entities_as_API_resources = CClass(practice, "Entities as API Resources")
domain_services_as_API_resources = CClass(practice, "Domain Services as API Resources")
aggregate_roots_as_API_resources = CClass(practice, "Aggregate Roots as API Resources")
domain_processes_as_API_resources = CClass(practice, "Domain or Business Processes as API Resources")
bounded_contexts_as_API_resources = CClass(practice, "Bounded Contexts as API Resources")

crud_style_operations_on_resources = CClass(practice, "CRUD-Style Operations on Resources")
domain_operations_on_resources = CClass(practice, "Domain Operations on Resources")
encode_operations_as_commands_in_the_payload = CClass(practice, "Encode Operations as Commands in the Payload")
expose_domain_events_as_state_transitions = CClass(practice, "Expose Domain Events as State Transitions")
expose_domain_events_via_feeds_or_pub_sub = CClass(practice, "Expose Domain Events via Feeds or Pub/Sub")

use_distributed_links = CClass(practice, "Use Distributed or Hypermedia Links in the Payload")
pass_object_ids = CClass(practice, "Pass Object Identifiers in the Payload")
embed_linked_data = CClass(practice, "Embed Linked Data in the Payload")

cqrs_API = CClass(practice, "Expose Segregated Command and Query Resources in API")

# forces
brittle_interface = CClass(force, "Brittle Interfaces")
avoid_exposing_domain_model_details_in_api = CClass(force, "Avoid Exposing Domain Model Details in API")
chatty_api = CClass(force, "Chatty API")
minimize_api_calls = CClass(force, "Minimize API calls")
performance = CClass(force, "Performance")
scalability = CClass(force, "Scalability")
api_complexity = CClass(force, "API Complexity")
api_usability = CClass(force, "API Usability")
api_evolvability = CClass(force, "API Evolvability")
api_modifiability = CClass(force, "API Modifiability")
data_consistency = CClass(force, "Data Consistency")
message_size = CClass(force, "Message Size")
coupling_of_clients_to_server = CClass(force, "Coupling of Clients to Server")
protocol_complexity_in_client = CClass(force, "Protocol Complexity in Client")
design_and_implementation_effort = CClass(force, "Design and Implementation Effort")
interface_design_limits_domain_model_design = CClass(force, "Interface Design Limits Domain Model Design")
clients_need_to_manage_crossing_model_boundaries = CClass(force, "Clients Need to Manage Crossing Model Boundaries")
maintainability_of_api_and_consumers = CClass(force, "Maintainability of API and API Consumers")
reliability = CClass(force, "Reliability")
eventual_consistency_support = CClass(force, "Eventual Consistency Support")
separation_of_api_contract_and_domain_concerns = CClass(force, "Separation of API Contract and Domain Concerns")
api_understandability = CClass(force, "API Understandability")
can_lead_to_anemic_domain_model = CClass(force, "Can Lead to Anemic Domain Model Anti-Pattern")
api_stability = CClass(force, "API Stability")
domain_model_flexibility = CClass(force, "Domain Model Flexibility")
initial_effort_required = CClass(force, "Initial Effort Required")
support_for_external_or_public_clients = CClass(force, "Support for External or Public Clients")

# links between practices
api_contract_specified_first_is_contract_specified = \
    api_contract_specified_first.add_links(api_contract_specified,
                                           role_name="to", stereotype_instances=is_a)[0]
api_contract_specified_can_be_realized_with_interface_bounded_context_or_shared_kernel = \
    api_contract_specified.add_links([interface_bounded_context_as_API, shared_kernel_as_API],
                                     role_name="to", stereotype_instances=can_be_realized_with)[0]
api_contract_extracted_can_be_realized_with_domain_model_subset = \
    api_contract_extracted.add_links(expose_domain_model_subset_as_API,
                                     role_name="to", stereotype_instances=can_be_realized_with)[0]
domain_model_defines_api_contract_can_be_realized_with_1_1_domain_model = \
    domain_model_defines_api_contract.add_links(expose_domain_model_as_API,
                                                role_name="to", stereotype_instances=can_be_realized_with)[0]
domain_model_defines_api_contract_can_be_realized_with_domain_model_subset = \
    domain_model_defines_api_contract.add_links(expose_domain_model_subset_as_API,
                                                role_name="to", stereotype_instances=can_be_realized_with)[0]
bounded_context_defines_api_contract_can_be_realized_with_bounded_context_apis = \
    bounded_context_defines_api_contract.add_links([expose_each_bounded_context_as_an_API,
                                                    expose_selected_bounded_contexts_as_an_API],
                                                   role_name="to", stereotype_instances=can_be_realized_with)[0]
might_be_based_on_shared_kernel = \
    add_stereotyped_link_with_how_tagged_value(interface_bounded_context_as_API,
                                               shared_kernel_as_API, can_be_realized_with,
                                               "might be based on a shared kernel")
domain_events_via_feeds_or_pub_sub_extension = \
    add_stereotyped_link_with_how_tagged_value(expose_domain_events_as_state_transitions,
                                               expose_domain_events_via_feeds_or_pub_sub, extension,
                                               "events might be exposed to clients via feeds or publish/subscribe")
domain_process_resource_is_an_aggregate_resource = \
    domain_processes_as_API_resources.add_links(aggregate_roots_as_API_resources, role_name="to",
                                                stereotype_instances=can_use)[0]

encode_operations_variant_of_domain_operations_on_resources = \
    domain_operations_on_resources.add_links(encode_operations_as_commands_in_the_payload, role_name="to",
                                             stereotype_instances=variant)[0]

cqrs_api_use_cqrs = \
    cqrs_API.add_links(cqrs, role_name="to", stereotype_instances=uses)[0]
cqrs_api_enables_eventual_consistency = \
    cqrs_API.add_links(eventual_consistency, role_name="to", stereotype_instances=enables)[0]
cqrs_API_can_use_encode_operations_as_commands_in_the_payload = \
    cqrs_API.add_links(encode_operations_as_commands_in_the_payload, role_name="to", stereotype_instances=can_use)[0]

use_distributed_links_uses_linked_information_holder = \
    use_distributed_links.add_links(linked_information_holder, role_name="to", stereotype_instances=uses)[0]
pass_object_ids_uses_object_id = \
    pass_object_ids.add_links(object_identifier, role_name="to", stereotype_instances=uses)[0]
embed_linked_data_uses_embedded_entity = \
    embed_linked_data.add_links(embedded_entity, role_name="to", stereotype_instances=uses)[0]

domain_process_can_use_processing_resource = \
    domain_processes_as_API_resources.add_links(processing_resource, role_name="to", stereotype_instances=can_use)[0]

# decisions, options, and contexts

# ** domain_model_mapping_decision **

domain_model_mapping_decision = CClass(decision, "How to Map a Domain Model and its Elements to an API?")
add_decision_option_link(domain_model_mapping_decision, expose_domain_model_as_API,
                         "Map Domain Model Fully to the API")
add_decision_option_link(domain_model_mapping_decision, expose_domain_model_subset_as_API,
                         "Map Selected Elements of the Domain Model to the API")
add_decision_option_link(domain_model_mapping_decision, expose_each_bounded_context_as_an_API,
                         "Map Each Bounded Context to APIs")
add_decision_option_link(domain_model_mapping_decision, expose_selected_bounded_contexts_as_an_API,
                         "Map Selected Bounded Contexts to APIs")
add_decision_option_link(domain_model_mapping_decision, interface_bounded_context_as_API,
                         "Introduce and Expose an Additional Interface Bounded Context as an API")
add_decision_option_link(domain_model_mapping_decision, shared_kernel_as_API,
                         "Identify Shared Kernel between Communication Participants and Expose it as an API")
add_links({domain_model_mapping_decision: domain_model_and_api}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

add_force_relations({expose_domain_model_as_API: {brittle_interface: very_negative,
                                                  avoid_exposing_domain_model_details_in_api: negative,
                                                  clients_need_to_manage_crossing_model_boundaries: positive,
                                                  api_complexity: very_negative,
                                                  api_usability: negative,
                                                  minimize_api_calls: negative,
                                                  api_modifiability: negative,
                                                  design_and_implementation_effort: positive},
                     expose_domain_model_subset_as_API: {brittle_interface: neutral,
                                                         avoid_exposing_domain_model_details_in_api: neutral,
                                                         clients_need_to_manage_crossing_model_boundaries: positive,
                                                         api_complexity: neutral,
                                                         api_usability: neutral,
                                                         minimize_api_calls: negative,
                                                         api_modifiability: negative,
                                                         design_and_implementation_effort: positive,
                                                         },
                     expose_each_bounded_context_as_an_API: {brittle_interface: negative,
                                                             avoid_exposing_domain_model_details_in_api: negative,
                                                             clients_need_to_manage_crossing_model_boundaries: negative,
                                                             api_complexity: negative,
                                                             api_usability: negative,
                                                             minimize_api_calls: negative,
                                                             api_modifiability: negative,
                                                             design_and_implementation_effort: positive,
                                                             },
                     expose_selected_bounded_contexts_as_an_API: {brittle_interface: neutral,
                                                                  avoid_exposing_domain_model_details_in_api: neutral,
                                                                  clients_need_to_manage_crossing_model_boundaries: negative,
                                                                  api_complexity: neutral,
                                                                  api_usability: neutral,
                                                                  minimize_api_calls: negative,
                                                                  api_modifiability: neutral,
                                                                  design_and_implementation_effort: positive,
                                                                  },
                     interface_bounded_context_as_API: {brittle_interface: positive,
                                                        avoid_exposing_domain_model_details_in_api: positive,
                                                        clients_need_to_manage_crossing_model_boundaries: very_positive,
                                                        api_complexity: positive,
                                                        api_usability: positive,
                                                        minimize_api_calls: positive,
                                                        api_modifiability: positive,
                                                        design_and_implementation_effort: negative,
                                                        },
                     shared_kernel_as_API: {brittle_interface: positive,
                                            avoid_exposing_domain_model_details_in_api: positive,
                                            clients_need_to_manage_crossing_model_boundaries: very_positive,
                                            api_complexity: positive,
                                            api_usability: positive,
                                            minimize_api_calls: positive,
                                            api_modifiability: positive,
                                            design_and_implementation_effort: negative,
                                            },
                     })

# ** api_as_contract_decision **

api_as_contract_decision = CClass(decision,
                                  "Which Approach is Chosen for Defining the API Contract " +
                                  "in Relation to the Domain Model?")
add_decision_option_link(api_as_contract_decision, api_contract_specified,
                         "Design the API Contract before or Independently from the Domain Model")
add_decision_option_link(api_as_contract_decision, api_contract_extracted,
                         "Design the API Contract by Selecting Elements of the Domain Model to be Exposed")
add_decision_option_link(api_as_contract_decision, domain_model_defines_api_contract,
                         "Use the Elements of the Domain Model as the Elements of the API Contract")
add_decision_option_link(api_as_contract_decision, bounded_context_defines_api_contract,
                         "Use the Elements of a Bounded Context as the Elements of the API Contract")
add_decision_option_link(api_as_contract_decision, api_code_first,
                         "Write the API Code First and Design the API Contract as You Code the API")
add_links({api_as_contract_decision: api_contract}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

add_force_relations({api_contract_specified: {separation_of_api_contract_and_domain_concerns: positive,
                                              api_stability: positive,
                                              domain_model_flexibility: positive,
                                              initial_effort_required: neutral,
                                              api_modifiability: neutral,
                                              maintainability_of_api_and_consumers: neutral,
                                              can_lead_to_anemic_domain_model: neutral,
                                              support_for_external_or_public_clients: very_positive,
                                              },
                     api_contract_extracted: {separation_of_api_contract_and_domain_concerns: positive,
                                              api_stability: positive,
                                              domain_model_flexibility: positive,
                                              initial_effort_required: neutral,
                                              api_modifiability: neutral,
                                              maintainability_of_api_and_consumers: neutral,
                                              can_lead_to_anemic_domain_model: neutral,
                                              support_for_external_or_public_clients: positive
                                              },
                     domain_model_defines_api_contract: {separation_of_api_contract_and_domain_concerns: negative,
                                                         api_stability: very_negative,
                                                         domain_model_flexibility: very_negative,
                                                         initial_effort_required: neutral,
                                                         api_modifiability: neutral,
                                                         maintainability_of_api_and_consumers: neutral,
                                                         can_lead_to_anemic_domain_model: neutral,
                                                         support_for_external_or_public_clients: neutral
                                                         },
                     bounded_context_defines_api_contract: {separation_of_api_contract_and_domain_concerns: negative,
                                                            api_stability: very_negative,
                                                            domain_model_flexibility: very_negative,
                                                            initial_effort_required: neutral,
                                                            api_modifiability: neutral,
                                                            maintainability_of_api_and_consumers: neutral,
                                                            can_lead_to_anemic_domain_model: neutral,
                                                            support_for_external_or_public_clients: neutral
                                                            },
                     api_code_first: {separation_of_api_contract_and_domain_concerns: very_negative,
                                      api_stability: very_negative,
                                      domain_model_flexibility: very_negative,
                                      initial_effort_required: very_positive,
                                      api_modifiability: negative,
                                      maintainability_of_api_and_consumers: negative,
                                      can_lead_to_anemic_domain_model: very_negative,
                                      support_for_external_or_public_clients: very_negative
                                      }
                     })

# ** designing_API_resources_decision **

designing_API_resources_decision = CClass(decision,
                                          "Which Domain Model Elements Should be Offered as Resources " +
                                          "or Endpoints in an API?")
add_decision_option_link(designing_API_resources_decision, entities_as_API_resources,
                         "Offer Entities as API Resources")
add_decision_option_link(designing_API_resources_decision, domain_services_as_API_resources,
                         "Offer Domain Services as API Resources")
add_decision_option_link(designing_API_resources_decision, aggregate_roots_as_API_resources,
                         "Offer Aggregate Roots as API Resources")
add_decision_option_link(designing_API_resources_decision, bounded_contexts_as_API_resources,
                         "Offer Bounded Contexts as API Resources")
add_decision_option_link(designing_API_resources_decision, domain_processes_as_API_resources,
                         "Offer Domain or Business Processes as API Resources")
add_links({designing_API_resources_decision: identified_interface_elements}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

add_force_relations({entities_as_API_resources: {avoid_exposing_domain_model_details_in_api: very_negative,
                                                 data_consistency: very_negative,
                                                 chatty_api: negative,
                                                 performance: negative,
                                                 scalability: negative,
                                                 api_complexity: negative,
                                                 maintainability_of_api_and_consumers: negative,
                                                 reliability: negative,
                                                 coupling_of_clients_to_server: negative
                                                 },
                     domain_services_as_API_resources: {avoid_exposing_domain_model_details_in_api: neutral,
                                                        data_consistency: positive,
                                                        chatty_api: neutral,
                                                        performance: very_positive,
                                                        scalability: very_positive,
                                                        api_complexity: positive,
                                                        maintainability_of_api_and_consumers: positive,
                                                        reliability: positive,
                                                        coupling_of_clients_to_server: positive
                                                        },
                     aggregate_roots_as_API_resources: {avoid_exposing_domain_model_details_in_api: positive,
                                                        data_consistency: very_positive,
                                                        chatty_api: positive,
                                                        performance: positive,
                                                        scalability: positive,
                                                        api_complexity: positive,
                                                        maintainability_of_api_and_consumers: positive,
                                                        reliability: positive,
                                                        coupling_of_clients_to_server: positive
                                                        },
                     domain_processes_as_API_resources: {avoid_exposing_domain_model_details_in_api: positive,
                                                         data_consistency: very_positive,
                                                         chatty_api: positive,
                                                         performance: positive,
                                                         scalability: positive,
                                                         api_complexity: positive,
                                                         maintainability_of_api_and_consumers: positive,
                                                         reliability: positive,
                                                         coupling_of_clients_to_server: positive
                                                         },
                     bounded_contexts_as_API_resources: {avoid_exposing_domain_model_details_in_api: positive,
                                                         data_consistency: neutral,
                                                         chatty_api: positive,
                                                         performance: positive,
                                                         scalability: positive,
                                                         api_complexity: negative,
                                                         maintainability_of_api_and_consumers: neutral,
                                                         reliability: neutral,
                                                         coupling_of_clients_to_server: neutral
                                                         },
                     })

# ** decision: should command and query be segregated? **
no_cqrs_API = CClass(do_nothing_design_solution, "Do Not Segregate Queries and Commands in an API")
cqrs_decision = CClass(decision,
                       "Segregate Resources for Reading and Updating Information in an API?")
add_decision_option_link(cqrs_decision, cqrs_API,
                         "Yes")
add_decision_option_link(cqrs_decision, no_cqrs_API,
                         "No")

add_force_relations({cqrs_API: {api_complexity: negative,
                                data_consistency: negative,
                                scalability: positive,
                                eventual_consistency_support: positive
                                },
                     no_cqrs_API: {api_complexity: positive,
                                   data_consistency: positive,
                                   scalability: negative,
                                   eventual_consistency_support: negative}})
add_links({cqrs_decision: identified_interface_elements}, role_name="context",
          stereotype_instances=decide_for_all_instances_of)

# ** operation_design_decision **

operation_design_decision = CClass(decision,
                                   "How to Design the Operations of a Resource?")
add_decision_option_link(operation_design_decision, crud_style_operations_on_resources,
                         "Design Operations Like Primitive Datastore Operations")
add_decision_option_link(operation_design_decision, domain_operations_on_resources,
                         "Design Coarser Grained, Explicit Domain Operations")
add_decision_option_link(operation_design_decision, encode_operations_as_commands_in_the_payload,
                         "Group Operations on Resource and Select Operations in the Payload")
add_decision_option_link(operation_design_decision, expose_domain_events_as_state_transitions,
                         "Expose State Transition Domain Events to Clients")
add_decision_option_link(operation_design_decision, expose_domain_events_via_feeds_or_pub_sub,
                         "Expose Event Feed Via a Feed or Publish/Subscribe to Clients")
add_links({operation_design_decision: operation}, role_name="context",
          stereotype_instances=decide_for_all_instances_of)

add_force_relations({crud_style_operations_on_resources: {avoid_exposing_domain_model_details_in_api: negative,
                                                          chatty_api: very_negative,
                                                          performance: very_negative,
                                                          scalability: very_negative,
                                                          interface_design_limits_domain_model_design: negative,
                                                          maintainability_of_api_and_consumers: negative,
                                                          data_consistency: negative,
                                                          reliability: negative,
                                                          coupling_of_clients_to_server: negative,
                                                          api_understandability: positive,
                                                          },
                     domain_operations_on_resources: {avoid_exposing_domain_model_details_in_api: positive,
                                                      chatty_api: positive,
                                                      performance: positive,
                                                      scalability: positive,
                                                      interface_design_limits_domain_model_design: positive,
                                                      maintainability_of_api_and_consumers: positive,
                                                      data_consistency: positive,
                                                      reliability: positive,
                                                      coupling_of_clients_to_server: positive,
                                                      api_understandability: positive,
                                                      },
                     encode_operations_as_commands_in_the_payload: {
                         avoid_exposing_domain_model_details_in_api: positive,
                         chatty_api: positive,
                         performance: positive,
                         scalability: positive,
                         interface_design_limits_domain_model_design:
                             positive,
                         maintainability_of_api_and_consumers: neutral,
                         data_consistency: positive,
                         reliability: positive,
                         coupling_of_clients_to_server: positive,
                         api_understandability: negative,
                         },
                     expose_domain_events_as_state_transitions: {
                         avoid_exposing_domain_model_details_in_api: very_positive,
                         chatty_api: positive,
                         performance: positive,
                         scalability: very_positive,
                         interface_design_limits_domain_model_design: positive,
                         maintainability_of_api_and_consumers: positive,
                         data_consistency: positive,
                         reliability: positive,
                         coupling_of_clients_to_server: positive,
                         api_understandability: negative,
                         },
                     expose_domain_events_via_feeds_or_pub_sub: {
                         avoid_exposing_domain_model_details_in_api: very_positive,
                         chatty_api: positive,
                         performance: positive,
                         scalability: very_positive,
                         interface_design_limits_domain_model_design: positive,
                         maintainability_of_api_and_consumers: positive,
                         data_consistency: positive,
                         reliability: positive,
                         coupling_of_clients_to_server: positive,
                         api_understandability: negative,
                         },
                     })

# ** link_mapping_decision **
link_mapping_decision = CClass(decision, "How to Map Links between Domain Model Elements to the API?")
do_nothing_for_links = CClass(do_nothing_design_solution)
add_decision_option_link(link_mapping_decision, do_nothing_for_links,
                         "Do Not Offer the Link Via the API")
add_decision_option_link(link_mapping_decision, use_distributed_links,
                         "Pass Distributed or Hypermedia Links in the Payload to Represent Domain Model Links")
add_decision_option_link(link_mapping_decision, pass_object_ids,
                         "Pass Object Identifiers in the Messages to Represent Domain Model Links")
add_decision_option_link(link_mapping_decision, embed_linked_data,
                         "Pass Embedded Data in the Messages to Include Perhaps Needed Data")
add_links({link_mapping_decision: domain_model_element_link}, role_name="context",
          stereotype_instances=decide_for_some_instances_of)

add_force_relations({use_distributed_links: {data_consistency: positive,
                                             api_evolvability: positive,
                                             api_modifiability: positive,
                                             message_size: very_positive,
                                             avoid_exposing_domain_model_details_in_api: very_positive,
                                             coupling_of_clients_to_server: very_positive,
                                             protocol_complexity_in_client: negative,
                                             minimize_api_calls: negative,
                                             performance: negative,
                                             scalability: negative},
                     pass_object_ids: {data_consistency: positive,
                                       api_evolvability: positive,
                                       api_modifiability: positive,
                                       message_size: very_positive,
                                       avoid_exposing_domain_model_details_in_api: negative,
                                       coupling_of_clients_to_server: negative,
                                       protocol_complexity_in_client: positive,
                                       minimize_api_calls: negative,
                                       performance: negative,
                                       scalability: negative},
                     embed_linked_data: {data_consistency: negative,
                                         api_evolvability: negative,
                                         api_modifiability: negative,
                                         message_size: negative,
                                         avoid_exposing_domain_model_details_in_api: neutral,
                                         coupling_of_clients_to_server: positive,
                                         protocol_complexity_in_client: positive,
                                         minimize_api_calls: positive,
                                         performance: positive,
                                         scalability: positive},
                     })

# decision links
add_links({domain_model_mapping_decision: [designing_API_resources_decision, api_as_contract_decision],
           designing_API_resources_decision: [cqrs_decision, operation_design_decision, link_mapping_decision],
           api_as_contract_decision: domain_model_mapping_decision},
          role_name="next decision", stereotype_instances=consider_if_not_decided_yet)

# decision views
forces_class_objects = [f.class_object for f in force.all_classes]

_all = CBundle("_all", elements=domain_model_mapping_decision.class_object.get_connected_elements())
inter_decision_links_view = CBundle("inter_decision_links",
                                    elements=[domain_model_mapping_decision, designing_API_resources_decision,
                                              api_as_contract_decision, cqrs_decision, operation_design_decision,
                                              link_mapping_decision])
domain_model_mapping_view = CBundle("domain_model_mapping_decision",
                                    elements=domain_model_mapping_decision.class_object.get_connected_elements(
                                        stop_elements_inclusive=[api.class_object,
                                                                 domain_model.class_object],
                                        stop_elements_exclusive=forces_class_objects + [
                                            api_contract_specified.class_object,
                                            api_contract_extracted.class_object,
                                            domain_model_defines_api_contract.class_object,
                                            bounded_context_defines_api_contract.class_object,
                                            link_mapping_decision.class_object,
                                            operation_design_decision.class_object,
                                            designing_API_resources_decision.class_object,
                                            api_as_contract_decision.class_object
                                        ]))
api_as_contract_view = CBundle("api_as_contract_decision",
                               elements=api_as_contract_decision.class_object.get_connected_elements(
                                   stop_elements_inclusive=[domain_model_mapping_decision.class_object,
                                                            api_contract.class_object,
                                                            domain_model.class_object],
                                   stop_elements_exclusive=forces_class_objects + [
                                       domain_model_mapping_decision.class_object]))
designing_API_resources_decision_view = CBundle("designing_API_resources_decision",
                                                elements=designing_API_resources_decision.class_object.get_connected_elements(
                                                    stop_elements_inclusive=[identified_interface_elements.class_object,
                                                                             encode_operations_as_commands_in_the_payload.class_object,
                                                                             ],
                                                    stop_elements_exclusive=forces_class_objects + [
                                                        cqrs_decision.class_object,
                                                        link_mapping_decision.class_object,
                                                        operation_design_decision.class_object,
                                                        domain_model_mapping_decision.class_object,
                                                    ]))
cqrs_decision_view = CBundle("cqrs_decision",
                             elements=cqrs_decision.class_object.get_connected_elements(
                                 stop_elements_inclusive=[identified_interface_elements.class_object,
                                                          encode_operations_as_commands_in_the_payload.class_object],
                                 stop_elements_exclusive=forces_class_objects + [
                                     designing_API_resources_decision.class_object]))
designing_API_resources_decision_view = CBundle("designing_API_resources_decision",
                                                elements=designing_API_resources_decision.class_object.get_connected_elements(
                                                    stop_elements_inclusive=[identified_interface_elements.class_object,
                                                                             encode_operations_as_commands_in_the_payload.class_object],
                                                    stop_elements_exclusive=forces_class_objects + [
                                                        cqrs_decision.class_object,
                                                        link_mapping_decision.class_object,
                                                        domain_model_mapping_decision.class_object,
                                                        operation_design_decision.class_object]))
operation_design_decision_view = CBundle("operation_design_decision",
                                         elements=operation_design_decision.class_object.get_connected_elements(
                                             stop_elements_inclusive=[message.class_object, cqrs_API.class_object],
                                             stop_elements_exclusive=forces_class_objects + [
                                                 domain_model_mapping_decision.class_object,
                                                 designing_API_resources_decision.class_object, ]))
link_mapping_decision_view = CBundle("link_mapping_decision",
                                     elements=link_mapping_decision.class_object.get_connected_elements(
                                         stop_elements_inclusive=[message.class_object],
                                         stop_elements_exclusive=forces_class_objects + [
                                             domain_model_mapping_decision.class_object,
                                             designing_API_resources_decision.class_object, ]))

ddd_api_views = [
    _all, {},
    inter_decision_links_view, {},
    domain_model_mapping_view, {},
    api_as_contract_view, {},
    designing_API_resources_decision_view, {},
    operation_design_decision_view, {},
    link_mapping_decision_view, {},
    cqrs_decision_view, {}
]
