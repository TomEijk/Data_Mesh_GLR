from api_ddd_models.api_ddd_model import expose_domain_model_as_API, expose_selected_bounded_contexts_as_an_API, \
    expose_each_bounded_context_as_an_API, expose_bounded_contexts_as_APIs, interface_bounded_context_as_API, \
    shared_kernel_as_API, entities_as_API_resources, aggregate_roots_as_API_resources, \
    bounded_contexts_as_API_resources, designing_API_resources_decision, crud_style_operations_on_resources, \
    domain_operations_on_resources, operation_design_decision, link_mapping_decision, \
    avoid_exposing_domain_model_details_in_api, expose_domain_events_as_state_transitions, \
    expose_domain_events_via_feeds_or_pub_sub, data_consistency, \
    embedded_entity, object_identifier, do_nothing_for_links, api_evolvability, api_modifiability, message_size, \
    performance, scalability, identified_interface_elements, \
    linked_information_holder, brittle_interface, api_complexity, api_usability, minimize_api_calls, \
    domain_events_via_feeds_or_pub_sub_extension, coupling_of_clients_to_server, protocol_complexity_in_client, \
    expose_domain_model_subset_as_API, design_and_implementation_effort, interface_design_limits_domain_model_design, \
    clients_need_to_manage_crossing_model_boundaries, domain_model_mapping_decision, chatty_api, \
    maintainability_of_api_and_consumers, reliability, domain_process_resource_is_an_aggregate_resource, cqrs, \
    eventual_consistency, cqrs_API, cqrs_api_use_cqrs, no_cqrs_API, cqrs_decision, eventual_consistency_support, \
    separation_of_api_contract_and_domain_concerns, api_as_contract_decision, domain_model_defines_api_contract, \
    domain_model_defines_api_contract_can_be_realized_with_1_1_domain_model, api_contract_extracted, \
    api_contract_extracted_can_be_realized_with_domain_model_subset, api_contract_specified, \
    api_contract_specified_can_be_realized_with_interface_bounded_context_or_shared_kernel, \
    bounded_context_defines_api_contract, \
    bounded_context_defines_api_contract_can_be_realized_with_bounded_context_apis, use_distributed_links, \
    use_distributed_links_uses_linked_information_holder, embed_linked_data, embed_linked_data_uses_embedded_entity, \
    pass_object_ids_uses_object_id, pass_object_ids, encode_operations_as_commands_in_the_payload, \
    encode_operations_variant_of_domain_operations_on_resources, api_understandability, \
    cqrs_API_can_use_encode_operations_as_commands_in_the_payload, can_lead_to_anemic_domain_model, \
    domain_services_as_API_resources, api_stability, \
    domain_model_flexibility, domain_processes_as_API_resources, api_code_first, initial_effort_required, \
    support_for_external_or_public_clients, domain_model_defines_api_contract_can_be_realized_with_domain_model_subset, \
    domain_process_can_use_processing_resource, api_contract_specified_first
from api_ddd_models.domain_model import domain_model, value_object, entity, repository, domain_model_element_link, \
    service, shared_kernel, bounded_context, aggregate, layer
from codeable_models import CClass, add_links
from map_models.map_domain_model import operation, api, api_contract
from metamodels.GT_coding import code, source, reference
from metamodels.domain_metamodel import domain_metaclass
from metamodels.guidance_metamodel import decision, design_solution, force, design_solution_dependencies

# add code as superclass to all possible codes used below
for classifier in [decision, domain_metaclass, design_solution, force, design_solution_dependencies,
                   ]:
    classifier.superclasses = classifier.superclasses + [code]

# ### Referenced Sources ###
ddd_vernon_book_2013 = CClass(reference, "vernon2013implementing", values={
    "bibliographic reference": "Vernon, Vaughn: Implementing domain-driven design}" + "Addison-Wesley Professional, 2013",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

ddd_book_2004 = CClass(reference, "DDD Book", values={
    "bibliographic reference": "Eric Evan: Domain-driven design: tackling complexity in the heart of software " + "Addison-Wesley Professional, 2004",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

ddd_quickly_book_2007 = CClass(reference, "DDD Quickly Book", values={
    "bibliographic reference": "Marinescu, Floyd and Avram, Abel" + "Domain-driven design Quickly" + "Lulu. com, 2007",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

infoq_Oliver_Gierke_2016 = CClass(reference, "Oliver Gierke talk in InfoQ", values={
    "bibliographic reference": "Oliver Gierke" + "DDD & REST - Domain Driven APIs for the Web" + "https://www.infoq.com/presentations/ddd-rest/",
    "author type": "Practitioner",
    "type": "Video Streaming"})

youtube_Oliver_Gierke_2016 = CClass(reference, "Oliver Gierke talk in GOTO2015", values={
    "bibliographic reference": "Oliver Gierke" + "GOTO 2015 • DDD & REST - Domain Driven APIs for the Web" + "https://www.youtube.com/watch?v=1RgXgZcj5nM",
    "author type": "Practitioner",
    "type": "Video Streaming"})

rest_in_practice_book_2010 = CClass(reference, "Rest in Practice Book", values={
    "bibliographic reference": "REST in practice: Hypermedia and systems architecture" + "Webber, Jim and Parastatidis, Savas and Robinson, Ian" + "O'Reilly Media, Inc., 2010",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

clean_architecture_2018 = CClass(reference, "Clean Architecture Book", values={
    "bibliographic reference": "Martin, Robert C: Clean architecture: a craftsman's guide to software structure and design " + "Prentice Hall, 2018",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

enterprise_architecture_2002 = CClass(reference, "Enterprise Architecture Book", values={
    "bibliographic reference": "Fowler, Martin: Patterns of enterprise application architecture" + "Addison-Wesley Longman Publishing Co., Inc., 2002",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

# ### Sources ###

s1 = CClass(source, "s1", values={
    "title": "Bounded Context in APIs (1/2)",
    "url": "https://nhpatt.com/bounded-context-in-apis/",
    "archive url": "https://bit.ly/2BsvnjK",
    "tiny url": "tinyurl.com/api-ddd-s1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s1_codes = [domain_model, shared_kernel, bounded_context, identified_interface_elements, aggregate, layer,
            operation, api, domain_model_element_link,
            expose_domain_model_as_API, expose_selected_bounded_contexts_as_an_API,
            expose_each_bounded_context_as_an_API,
            expose_bounded_contexts_as_APIs, interface_bounded_context_as_API,
            shared_kernel_as_API,
            domain_model_mapping_decision,
            entities_as_API_resources,
            aggregate_roots_as_API_resources,
            bounded_contexts_as_API_resources,
            designing_API_resources_decision,
            crud_style_operations_on_resources,
            domain_operations_on_resources,
            operation_design_decision,
            link_mapping_decision,
            linked_information_holder, use_distributed_links, use_distributed_links_uses_linked_information_holder,
            embedded_entity, embed_linked_data, embed_linked_data_uses_embedded_entity,
            object_identifier, pass_object_ids, pass_object_ids_uses_object_id,
            do_nothing_for_links,
            brittle_interface,
            avoid_exposing_domain_model_details_in_api,
            api_complexity,
            api_usability,
            minimize_api_calls,
            chatty_api,
            data_consistency,
            api_evolvability,
            api_modifiability,
            message_size,
            performance,
            scalability,
            api_contract,
            separation_of_api_contract_and_domain_concerns,
            api_as_contract_decision
            ]
add_links({s1: s1_codes}, role_name="contained_code")

s2 = CClass(source, "s2", values={
    "title": "DDD \& REST Domain Driven Apis for the Web",
    "url": "https://www.slideshare.net/SpringCentral/ddd-rest-domain-driven-apis-for-the-web",
    "archive url": "https://bit.ly/2Tm2YkP",
    "tiny url": "tinyurl.com/api-ddd-s2",
    "author type": "Practitioner",
    "type": "Slides",
    "example": True,
    "source code": True})
s2_codes = [api, domain_model, value_object, entity, aggregate, repository, bounded_context,
            operation_design_decision, crud_style_operations_on_resources,
            domain_operations_on_resources, avoid_exposing_domain_model_details_in_api,
            expose_domain_events_as_state_transitions, expose_domain_events_via_feeds_or_pub_sub,
            domain_events_via_feeds_or_pub_sub_extension,
            data_consistency, designing_API_resources_decision, entities_as_API_resources,
            aggregate_roots_as_API_resources, bounded_contexts_as_API_resources,
            link_mapping_decision,
            linked_information_holder, use_distributed_links, use_distributed_links_uses_linked_information_holder,
            embedded_entity, embed_linked_data, embed_linked_data_uses_embedded_entity,
            object_identifier, pass_object_ids, pass_object_ids_uses_object_id,
            domain_model_element_link,
            do_nothing_for_links,
            minimize_api_calls,
            coupling_of_clients_to_server, protocol_complexity_in_client
            ]
add_links({s2: s2_codes}, role_name="contained_code")
add_links({s2: [ddd_book_2004, ddd_quickly_book_2007, infoq_Oliver_Gierke_2016, youtube_Oliver_Gierke_2016,
                rest_in_practice_book_2010]}, role_name="referenced")

s3 = CClass(source, "s3", values={
    "title": "Why the domain model should not be used as resources in REST API?",
    "url": "https://stackoverflow.com/questions/33970716/why-the-domain-model-should-not-be-used-as-resources-in-rest-api",
    "archive url": "https://bit.ly/2Z1D5dh",
    "tiny url": "tinyurl.com/api-ddd-s3",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": True,
    "source code": True})
s3_codes = [api, domain_model, domain_model_mapping_decision, expose_domain_model_as_API,
            expose_domain_model_subset_as_API,
            api_modifiability, design_and_implementation_effort, avoid_exposing_domain_model_details_in_api,
            interface_bounded_context_as_API, shared_kernel_as_API,
            operation_design_decision, crud_style_operations_on_resources, interface_design_limits_domain_model_design,
            domain_operations_on_resources, expose_domain_events_as_state_transitions,
            clients_need_to_manage_crossing_model_boundaries,
            expose_selected_bounded_contexts_as_an_API, bounded_context,
            linked_information_holder, link_mapping_decision, use_distributed_links,
            use_distributed_links_uses_linked_information_holder,
            domain_model_element_link, entity,
            api_contract,
            separation_of_api_contract_and_domain_concerns,
            api_as_contract_decision, domain_model_defines_api_contract,
            domain_model_defines_api_contract_can_be_realized_with_1_1_domain_model,
            api_contract_extracted, api_contract_extracted_can_be_realized_with_domain_model_subset,
            domain_model_defines_api_contract_can_be_realized_with_domain_model_subset,
            api_contract_specified,
            api_contract_specified_can_be_realized_with_interface_bounded_context_or_shared_kernel,
            bounded_context_defines_api_contract,
            bounded_context_defines_api_contract_can_be_realized_with_bounded_context_apis
            ]
add_links({s3: s3_codes}, role_name="contained_code")

s4 = CClass(source, "s4", values={
    "title": "How to clearly define boundaries of a bounded context",
    "url": "https://softwareengineering.stackexchange.com/questions/316819/how-to-clearly-define-boundaries-of-a-bounded-context",
    "archive url": "https://bit.ly/2ByyAyg",
    "tiny url": "tinyurl.com/api-ddd-s4",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": False,
    "source code": True})
s4_codes = [api, domain_model, bounded_context, expose_each_bounded_context_as_an_API,
            domain_model_mapping_decision,
            clients_need_to_manage_crossing_model_boundaries,
            api_modifiability, avoid_exposing_domain_model_details_in_api,
            expose_selected_bounded_contexts_as_an_API,
            domain_operations_on_resources, expose_domain_events_as_state_transitions, operation_design_decision,
            reliability, scalability
            ]
add_links({s4: s4_codes}, role_name="contained_code")
add_links({s4: ddd_book_2004}, role_name="referenced")

s5 = CClass(source, "s5", values={
    "title": "REST API Design - Resource Modeling",
    "url": "https://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling",
    "archive url": "https://bit.ly/38uqLp8",
    "tiny url": "tinyurl.com/api-ddd-s5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s5_codes = [api, operation, designing_API_resources_decision, operation_design_decision,
            entities_as_API_resources, aggregate_roots_as_API_resources, crud_style_operations_on_resources,
            chatty_api, api_modifiability, api_usability, api_evolvability,
            bounded_contexts_as_API_resources,
            api_complexity,
            avoid_exposing_domain_model_details_in_api, maintainability_of_api_and_consumers, data_consistency,
            reliability,
            coupling_of_clients_to_server,
            entity, aggregate, bounded_context,
            expose_domain_events_as_state_transitions,
            domain_processes_as_API_resources, domain_process_can_use_processing_resource,
            domain_process_resource_is_an_aggregate_resource,
            cqrs, eventual_consistency, cqrs_API, cqrs_api_use_cqrs, no_cqrs_API, cqrs_decision, scalability,
            eventual_consistency_support,
            api_contract,
            separation_of_api_contract_and_domain_concerns,
            api_as_contract_decision, domain_operations_on_resources
            ]
add_links({s5: s5_codes}, role_name="contained_code")

s6 = CClass(source, "s6", values={
    "title": "Rest API and DDD",
    "url": "https://stackoverflow.com/questions/35700344/rest-api-and-ddd/35708211",
    "archive url": "https://bit.ly/2ydDqz0",
    "tiny url": "tinyurl.com/api-ddd-s6",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": True,
    "source code": True})
add_links({s6: [entity, aggregate, designing_API_resources_decision,
                aggregate_roots_as_API_resources, operation_design_decision, crud_style_operations_on_resources,
                domain_operations_on_resources,
                encode_operations_as_commands_in_the_payload,
                encode_operations_variant_of_domain_operations_on_resources,
                maintainability_of_api_and_consumers, api_understandability,
                entities_as_API_resources,
                cqrs, eventual_consistency, cqrs_API, cqrs_api_use_cqrs, no_cqrs_API, cqrs_decision,
                cqrs_API_can_use_encode_operations_as_commands_in_the_payload,
                expose_domain_model_subset_as_API, domain_model_mapping_decision, api_complexity,
                coupling_of_clients_to_server]}, role_name="contained_code")

s7 = CClass(source, "s7", values={
    "title": "Introduction to DDD Lite: When microservices in Go are not enough",
    "url": "https://threedots.tech/post/ddd-lite-in-go-introduction/",
    "archive url": "https://bit.ly/3hhN58x",
    "tiny url": "tinyurl.com/api-ddd-s7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s7: [entity, aggregate, domain_model, value_object, repository,
                operation_design_decision, crud_style_operations_on_resources, domain_operations_on_resources,
                api_understandability, maintainability_of_api_and_consumers,
                avoid_exposing_domain_model_details_in_api]}, role_name="contained_code")
add_links({s7: ddd_book_2004}, role_name="referenced")

s8 = CClass(source, "s8", values={
    "title": "REST and DDD: incompatible?",
    "url": "http://dontpanic.42.nl/2012/04/rest-and-ddd-incompatible.html",
    "archive url": "https://bit.ly/2z1ralB",
    "tiny url": "tinyurl.com/api-ddd-s8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
add_links({s8: [domain_model, api, domain_model_mapping_decision,
                api_as_contract_decision, api_contract_specified,
                crud_style_operations_on_resources,
                operation_design_decision, can_lead_to_anemic_domain_model,
                no_cqrs_API, cqrs_API, cqrs_decision, scalability,
                link_mapping_decision, use_distributed_links, coupling_of_clients_to_server,
                protocol_complexity_in_client]}, role_name="contained_code")

s9 = CClass(source, "s9", values={
    "title": "Domain Driven Design - External Data API as Respository or Service",
    "url": "https://stackoverflow.com/questions/2272601/domain-driven-design-external-data-api-as-respository-or-service",
    "archive url": "https://bit.ly/2LWhdsH",
    "tiny url": "tinyurl.com/api-ddd-s9",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": True,
    "source code": False})
add_links({s9: [entity, service, domain_model, api, domain_model_mapping_decision, expose_domain_model_as_API,
                expose_domain_model_subset_as_API, operation_design_decision, domain_operations_on_resources,
                value_object, expose_domain_events_as_state_transitions,
                domain_services_as_API_resources, designing_API_resources_decision
                ]}, role_name="contained_code")

s10 = CClass(source, "s10", values={
    "title": "Conceptual mismatch between DDD Application Services and REST API",
    "url": "https://softwareengineering.stackexchange.com/questions/279369/conceptual-mismatch-between-ddd-application-services-and-rest-api",
    "archive url": "https://bit.ly/2UaoiKv",
    "tiny url": "tinyurl.com/api-ddd-s10",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": True,
    "source code": True})
add_links({s10: [entity, service, domain_model, api, domain_model_mapping_decision, designing_API_resources_decision,
                 domain_operations_on_resources, crud_style_operations_on_resources, data_consistency,
                 maintainability_of_api_and_consumers, coupling_of_clients_to_server,
                 domain_model_defines_api_contract,
                 separation_of_api_contract_and_domain_concerns, api_stability, domain_model_flexibility,
                 use_distributed_links,
                 link_mapping_decision, protocol_complexity_in_client,
                 avoid_exposing_domain_model_details_in_api, interface_design_limits_domain_model_design,
                 api_as_contract_decision, api_contract_specified, api_contract_extracted,
                 aggregate, aggregate_roots_as_API_resources,
                 domain_process_resource_is_an_aggregate_resource,
                 domain_process_can_use_processing_resource,
                 domain_processes_as_API_resources, operation_design_decision
                 ]}, role_name="contained_code")
add_links({s10: rest_in_practice_book_2010}, role_name="referenced")

s11 = CClass(source, "s11", values={
    "title": "Microservices: Overview, Misinterpretations and Misuses",
    "url": "https://medium.com/@shijuvar/microservices-overview-misinterpretations-and-misuses-56a1979edafb",
    "archive url": "https://bit.ly/3jDLwnF",
    "tiny url": "tinyurl.com/api-ddd-s11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
add_links({s11: [entity, value_object, service, aggregate, repository, bounded_context, no_cqrs_API, cqrs_API,
                 cqrs_decision, api_complexity, scalability, performance, chatty_api,
                 crud_style_operations_on_resources, domain_operations_on_resources,
                 operation_design_decision, expose_domain_events_as_state_transitions
                 ]}, role_name="contained_code")

building_ms_book_2015 = CClass(reference, "Building Microservice", values={
    "bibliographic reference": "author_name: book_name}" + "publisher, year",
    "author type": "Practitioner",
    "type": "Practitioner Book"})

add_links({s11: [ddd_book_2004, building_ms_book_2015]},
          role_name="referenced")

s12 = CClass(source, "s12", values={
    "title": "Design a DDD-oriented microservice",
    "url": "https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice",
    "archive url": "https://bit.ly/2X6TmNr",
    "tiny url": "tinyurl.com/api-ddd-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
add_links({s12: [aggregate, entity, domain_model, api,
                 designing_API_resources_decision, entities_as_API_resources,
                 aggregate_roots_as_API_resources, api_complexity, data_consistency,
                 expose_domain_events_as_state_transitions, domain_operations_on_resources,
                 operation_design_decision, no_cqrs_API, cqrs_API, cqrs_decision,
                 crud_style_operations_on_resources
                 ]}, role_name="contained_code")
add_links({s12: ddd_book_2004}, role_name="referenced")

s13 = CClass(source, "s13", values={
    "title": "Apply Domain-Driven Design to microservices architecture",
    "url": "https://www.ibm.com/garage/method/practices/code/domain-driven-design",
    "archive url": "https://bit.ly/2TDgiBJ",
    "tiny url": "tinyurl.com/api-ddd-s13",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
add_links({s13: [domain_model, api, entity, aggregate, api_as_contract_decision, api_contract_specified,
                 api_contract_extracted, domain_model_defines_api_contract,
                 separation_of_api_contract_and_domain_concerns,
                 designing_API_resources_decision, entities_as_API_resources, aggregate_roots_as_API_resources,
                 domain_services_as_API_resources,
                 domain_model_mapping_decision, expose_each_bounded_context_as_an_API,
                 expose_selected_bounded_contexts_as_an_API,
                 bounded_context_defines_api_contract
                 ]}, role_name="contained_code")
add_links({s13: ddd_book_2004}, role_name="referenced")

s14 = CClass(source, "s14", values={
    "title": "Designing APIs and Microservices Using Domain-Driven Design",
    "url": "https://www.slideshare.net/launchany/designing-apis-and-microservices-using-domaindriven-design",
    "archive url": "https://bit.ly/303OJW6",
    "tiny url": "tinyurl.com/api-ddd-s14",
    "author type": "Practitioner",
    "type": "Slides",
    "example": True,
    "source code": False})

add_links({s14: [api_as_contract_decision, domain_model_mapping_decision, bounded_context,
                 api_usability, coupling_of_clients_to_server, expose_each_bounded_context_as_an_API,
                 expose_selected_bounded_contexts_as_an_API, domain_model,
                 designing_API_resources_decision, entities_as_API_resources,
                 operation_design_decision, expose_domain_events_as_state_transitions,
                 link_mapping_decision, crud_style_operations_on_resources,
                 ]}, role_name="contained_code")

s15 = CClass(source, "s15", values={
    "title": "REST Service and CQRS",
    "url": "https://softwareengineering.stackexchange.com/questions/242884/rest-service-and-cqrs",
    "archive url": "https://bit.ly/39hNkxI",
    "tiny url": "tinyurl.com/api-ddd-s15",
    "author type": "Practitioner",
    "type": "Discussion Forum Post",
    "example": True,
    "source code": True})

add_links({s15: [no_cqrs_API, cqrs_API, cqrs_decision, operation_design_decision, crud_style_operations_on_resources,
                 domain_operations_on_resources, encode_operations_as_commands_in_the_payload, api_complexity,
                 eventual_consistency_support, api_understandability
                 ]}, role_name="contained_code")

s16 = CClass(source, "s16", values={
    "title": "Exposing CQRS Through a RESTful API",
    "url": "https://www.infoq.com/articles/rest-api-on-cqrs/",
    "archive url": "https://bit.ly/39gt3J0",
    "tiny url": "tinyurl.com/api-ddd-s16",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s16: [cqrs, no_cqrs_API, cqrs_API, cqrs_decision, data_consistency, eventual_consistency_support,
                 operation_design_decision, expose_domain_events_as_state_transitions, domain_operations_on_resources,
                 entity, entities_as_API_resources, designing_API_resources_decision,
                 crud_style_operations_on_resources,
                 encode_operations_as_commands_in_the_payload,
                 api_understandability, performance, scalability,
                 ]}, role_name="contained_code")
cqrs_document_2010 = CClass(reference, "CQRS Documents by Greg Young", values={
    "bibliographic reference": "Greg Young: https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf " + "cqrsinfo.com, 2010",
    "author type": "Practitioner",
    "type": "Practitioner Book"})
add_links({s16: cqrs_document_2010}, role_name="referenced")

s17 = CClass(source, "s17", values={
    "title": "REST-first design is Imperative, DDD is Declarative [Comparison] - DDD w/ TypeScript",
    "url": "https://khalilstemmler.com/articles/typescript-domain-driven-design/ddd-vs-crud-design/",
    "archive url": "https://bit.ly/2yxndow",
    "tiny url": "tinyurl.com/api-ddd-s17",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s17: [api_as_contract_decision, api_contract_specified, api_contract_extracted,
                 operation_design_decision, crud_style_operations_on_resources, api_code_first,
                 initial_effort_required, api_modifiability, maintainability_of_api_and_consumers,
                 can_lead_to_anemic_domain_model, avoid_exposing_domain_model_details_in_api, api_understandability,
                 entity, aggregate, entities_as_API_resources, aggregate_roots_as_API_resources,
                 designing_API_resources_decision
                 ]}, role_name="contained_code")
add_links({s17: clean_architecture_2018}, role_name="referenced")

s18 = CClass(source, "s18", values={
    "title": "Designing APIs for microservices",
    "url": "https://docs.microsoft.com/en-us/azure/architecture/microservices/design/api-design",
    "archive url": "https://bit.ly/2WL8IpV",
    "tiny url": "tinyurl.com/api-ddd-s18",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s18: [chatty_api,
                 performance, scalability, crud_style_operations_on_resources,
                 domain_operations_on_resources, operation_design_decision, api_evolvability, api_modifiability,
                 api_as_contract_decision, api_contract_specified, api_contract_extracted,
                 domain_model_defines_api_contract, support_for_external_or_public_clients,
                 entity, aggregate, value_object, designing_API_resources_decision, entities_as_API_resources,
                 aggregate_roots_as_API_resources, avoid_exposing_domain_model_details_in_api,
                 data_consistency, api_complexity, coupling_of_clients_to_server,
                 link_mapping_decision, use_distributed_links, pass_object_ids,
                 ]}, role_name="contained_code")

s19 = CClass(source, "s19", values={
    "title": "Moving Towards Domain Driven Design in Go",
    "url": "https://www.calhoun.io/moving-towards-domain-driven-design-in-go/",
    "archive url": "https://bit.ly/3hxvSZ9",
    "tiny url": "tinyurl.com/api-ddd-s19",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s19: [operation_design_decision, crud_style_operations_on_resources,
                 designing_API_resources_decision, entities_as_API_resources,
                 aggregate_roots_as_API_resources, domain_services_as_API_resources
                 ]}, role_name="contained_code")

s20 = CClass(source, "s20", values={
    "title": "Microservices, Apache Kafka, and Domain-Driven Design",
    "url": "https://www.confluent.io/blog/microservices-apache-kafka-domain-driven-design/",
    "archive url": "https://bit.ly/3fUhcm9",
    "tiny url": "tinyurl.com/api-ddd-s20",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
add_links({s20: [operation_design_decision, expose_domain_events_as_state_transitions,
                 coupling_of_clients_to_server, domain_processes_as_API_resources,
                 domain_process_can_use_processing_resource,
                 bounded_contexts_as_API_resources,
                 designing_API_resources_decision, data_consistency,
                 crud_style_operations_on_resources, domain_operations_on_resources, bounded_context,
                 expose_selected_bounded_contexts_as_an_API, expose_each_bounded_context_as_an_API,
                 domain_model_mapping_decision, scalability, domain_model,
                 expose_domain_events_via_feeds_or_pub_sub
                 ]}, role_name="contained_code")
add_links({s20: ddd_book_2004}, role_name="referenced")

s21 = CClass(source, "s21", values={
    "title": "API \& Domain Driven Design",
    "url": "https://docs.google.com/presentation/d/1qNl2BPnLUDoK3ITtAcKBhizUdcLLBhYalOj5npfmj0U/edit#slide=id.gc6fa3c898_0_5",
    "archive url": "https://bit.ly/2JIzf3P",
    "tiny url": "tinyurl.com/api-ddd-s21",
    "author type": "Practitioner",
    "type": "Slides",
    "example": True,
    "source code": True})
r21 = CClass(reference, "r21", values={
    "url": "https://www.youtube.com/watch?v=miZ9Dv1vcQ8",
    "title": "APIs with Domain Driven Design - API-Craft Singapore" + "Jan 13, 2017",
    "author type": "Practitioner",
    "type": "Video Streaming"})
add_links({s21: r21}, role_name="referenced")
add_links(
    {s21: [entity, value_object, repository, aggregate, service, data_consistency, design_and_implementation_effort,
           designing_API_resources_decision, entities_as_API_resources, domain_model_mapping_decision,
           expose_selected_bounded_contexts_as_an_API, shared_kernel,
           api_contract_specified_can_be_realized_with_interface_bounded_context_or_shared_kernel,
           api_as_contract_decision, api_contract_specified,
           operation_design_decision, crud_style_operations_on_resources
           ]}, role_name="contained_code")

s22 = CClass(source, "s22", values={
    "title": "Implementing Domain-Driven Design for Microservice Architecture",
    "url": "https://medium.com/design-and-tech-co/implementing-domain-driven-design-for-microservice-architecture-26eb0333d72e",
    "archive url": "https://bit.ly/37vBiQW",
    "tiny url": "tinyurl.com/api-ddd-s22",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
add_links({s22: [bounded_context, aggregate, service, entity, domain_model_mapping_decision,
                 expose_bounded_contexts_as_APIs, expose_selected_bounded_contexts_as_an_API,
                 coupling_of_clients_to_server, data_consistency
                 ]}, role_name="contained_code")

s23 = CClass(source, "s23", values={
    "title": "Pattern: Decompose by subdomain Context",
    "url": "https://microservices.io/patterns/decomposition/decompose-by-subdomain.html",
    "archive url": "https://bit.ly/3op60SF",
    "tiny url": "tinyurl.com/api-ddd-s23",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
add_links({s23: [api_modifiability, design_and_implementation_effort, brittle_interface, api_stability,
                 coupling_of_clients_to_server,
                 domain_model_mapping_decision, interface_bounded_context_as_API,
                 expose_bounded_contexts_as_APIs, expose_selected_bounded_contexts_as_an_API,
                 ]}, role_name="contained_code")

s24 = CClass(source, "s24", values={
    "title": "Building Microservices with Event Sourcing/CQRS in Go using gRPC, NATS Streaming and CockroachDB",
    "url": "https://medium.com/@shijuvar/building-microservices-with-event-sourcing-cqrs-in-go-using-grpc-nats-streaming-and-cockroachdb-983f650452aa",
    "archive url": "https://bit.ly/3odU9GO",
    "tiny url": "tinyurl.com/api-ddd-s24",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s24: [bounded_context, aggregate, separation_of_api_contract_and_domain_concerns,
                 cqrs, eventual_consistency_support,
                 expose_domain_events_as_state_transitions, no_cqrs_API, cqrs_API, cqrs_decision,
                 operation_design_decision, expose_domain_events_via_feeds_or_pub_sub, scalability
                 ]}, role_name="contained_code")

s25 = CClass(source, "s25", values={
    "title": "Aggregate Oriented Microservices",
    "url": "https://medium.com/@unmeshvjoshi/aggregate-oriented-microservices-d314eb04f2b1",
    "archive url": "https://bit.ly/37JKPnt",
    "tiny url": "tinyurl.com/api-ddd-s25",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
add_links({s25: [designing_API_resources_decision, aggregate_roots_as_API_resources, bounded_contexts_as_API_resources,
                 data_consistency, operation_design_decision, domain_operations_on_resources, bounded_context,
                 aggregate, expose_domain_events_as_state_transitions, api_as_contract_decision,
                 cqrs, no_cqrs_API, cqrs_API, cqrs_decision, api_complexity, eventual_consistency_support
                 ]}, role_name="contained_code")

s26 = CClass(source, "s26", values={
    "title": "Designing a Serverless Application with Domain Driven Design",
    "url": "https://www.susannekaiser.net/conferences/slides/serverlessdays-belfast-2020.pdfn",
    "archive url": "https://bit.ly/3mTeVeN",
    "tiny url": "tinyurl.com/api-ddd-s26",
    "author type": "Practitioner",
    "type": "Slides",
    "example": True,
    "source code": False})
add_links({s26: [bounded_contexts_as_API_resources, designing_API_resources_decision,
                 expose_domain_events_as_state_transitions, operation_design_decision,
                 aggregate_roots_as_API_resources]}, role_name="contained_code")

s27 = CClass(source, "s27", values={
    "title": "Bounded Contexts With Axon",
    "url": "https://dzone.com/articles/bounded-contexts-with-axon",
    "archive url": "https://bit.ly/3lUWnJN",
    "tiny url": "tinyurl.com/api-ddd-s27",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})

add_links({s27: [bounded_context, cqrs, no_cqrs_API, cqrs_API, cqrs_decision, expose_domain_events_as_state_transitions,
                 operation_design_decision, expose_domain_events_via_feeds_or_pub_sub,
                 bounded_context_defines_api_contract,
                 api_as_contract_decision, domain_model_mapping_decision, expose_bounded_contexts_as_APIs,
                 expose_each_bounded_context_as_an_API, expose_selected_bounded_contexts_as_an_API,
                 aggregate_roots_as_API_resources, designing_API_resources_decision,
                 eventual_consistency_support, eventual_consistency, data_consistency,
                 coupling_of_clients_to_server
                 ]}, role_name="contained_code")

s28 = CClass(source, "s28", values={
    "title": "Building Real-Time Web Applications using wolkenkit",
    "url": "https://auth0.com/blog/building-real-time-web-applications-using-wolkenkit/",
    "archive url": "https://bit.ly/375Klc9",
    "tiny url": "tinyurl.com/api-ddd-s28",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})

add_links({s28: [data_consistency, scalability,
                 cqrs, no_cqrs_API, cqrs_API, cqrs_decision, expose_domain_events_as_state_transitions,
                 operation_design_decision, expose_domain_events_via_feeds_or_pub_sub, eventual_consistency_support,
                 eventual_consistency, aggregate_roots_as_API_resources, aggregate, designing_API_resources_decision
                 ]}, role_name="contained_code")

s29 = CClass(source, "s29", values={
    "title": "Uncovering API Implementation",
    "url": "https://dzone.com/articles/uncovering-api-implementation",
    "archive url": "https://bit.ly/3gLxVK1",
    "tiny url": "tinyurl.com/api-ddd-s29",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})

add_links({s29: [data_consistency, operation_design_decision, crud_style_operations_on_resources,
                 expose_domain_events_as_state_transitions, api_complexity, bounded_contexts_as_API_resources,
                 designing_API_resources_decision, design_and_implementation_effort,
                 avoid_exposing_domain_model_details_in_api,
                 separation_of_api_contract_and_domain_concerns,
                 expose_bounded_contexts_as_APIs, expose_selected_bounded_contexts_as_an_API,
                 expose_each_bounded_context_as_an_API, domain_model_mapping_decision,
                 maintainability_of_api_and_consumers, scalability
                 ]}, role_name="contained_code")

s30 = CClass(source, "s30", values={
    "title": "Implementing an API-First Design Methodology",
    "url": "https://dzone.com/articles/implementing-an-api-first-design-methodology",
    "archive url": "https://bit.ly/34i4l9Z",
    "tiny url": "tinyurl.com/api-ddd-s30",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})

add_links({s30: [api_as_contract_decision, api_contract_specified, api_contract_specified_first,
                 api_code_first, api_stability, api_modifiability,
                 separation_of_api_contract_and_domain_concerns, initial_effort_required,
                 design_and_implementation_effort, maintainability_of_api_and_consumers, api_understandability
                 ]}, role_name="contained_code")

s31 = CClass(source, "s31", values={
    "title": "API First Development",
    "url": "https://tanzu.vmware.com/application-modernization-recipes/app-architecture/api-first-development",
    "archive url": "https://bit.ly/2W36EZS",
    "tiny url": "tinyurl.com/api-ddd-s31",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})

add_links({s31: [api_as_contract_decision, api_contract_specified, api_contract_specified_first,
                 api_understandability, api_modifiability, api_stability, api_evolvability, initial_effort_required,
                 link_mapping_decision, pass_object_ids, linked_information_holder, use_distributed_links,
                 object_identifier, do_nothing_for_links
                 ]}, role_name="contained_code")

s32 = CClass(source, "s32", values={
    "title": "The API Design Process",
    "url": "https://www.linkedin.com/pulse/api-design-process-bernard-stibbe/",
    "archive url": "https://bit.ly/37YiYA2",
    "tiny url": "tinyurl.com/api-ddd-s32",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})

add_links({s32: [designing_API_resources_decision, entities_as_API_resources, domain_model_mapping_decision,
                 expose_each_bounded_context_as_an_API, expose_selected_bounded_contexts_as_an_API,
                 api_as_contract_decision, api_contract_specified, api_contract,
                 avoid_exposing_domain_model_details_in_api, api_understandability,
                 separation_of_api_contract_and_domain_concerns
                 ]}, role_name="contained_code")
