from data_as_a_product_model import *
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

# ### Sources ###

s1 = CClass(source, "s1", values={
    "title": "Data as a product vs data products. What are the differences?",
    "url": "https://towardsdatascience.com/data-as-a-product-vs-data-products-what-are-the-differences-b43ddbb0f123",
    "archive url": "https://bit.ly/data-as-a-product-s1",
    "tiny url": "https://tinyurl.com/data-as-a-product-s1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})

s1_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product,
            automated_decision_making_model_as_data_product, register_datasets, request_access, search_engine,
            data_catalogue, query_catalogue, quality_monitoring, data_product_type_decision, discoverable_data_products_decision,
            register_datasets_search_engine, request_access_search_engine, security, discoverability,
            keep_track_metadata_decision,trustworty_decision]
add_links({s1: s1_codes}, role_name="contained_code")

s2 = CClass(source, "s2", values={
    "title": "Designing Data Products",
    "url": "https://towardsdatascience.com/designing-data-products-b6b93edf3d23",
    "archive url": "https://bit.ly/data-as-a-product-s2",
    "tiny url": "https://tinyurl.com/data-as-a-product-s2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s2_codes = [algorithms_as_data_product, internal_complexity, complexity_for_user, raw_data_as_data_product,
            derived_data_as_data_product, decision_support_model_as_data_product, automated_decision_making_model_as_data_product,
            rest_apis, sql_layer, data_access_decision]
add_links({s2: s2_codes}, role_name="contained_code")

s3 = CClass(source, "s3", values={
    "title": "Building a data mesh to support an ecosystem of data products at Adevinta",
    "url": "https://medium.com/adevinta-tech-blog/building-a-data-mesh-to-support-an-ecosystem-of-data-products-at-adevinta-4c057d06824d",
    "archive url": "https://bit.ly/data-as-a-product-s3",
    "tiny url": "https://tinyurl.com/data-as-a-product-s3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s3_codes = [accelerate_decision_making, more_granular_data, sql_layer, data_access_decision,
            observation_plane, trustworty_decision, schema_manager, understandability, rest_apis, query_catalogue,
            quality_monitoring, request_access, discoverable_data_products_decision, domain_datasets,
            core_datasets, data_product_anatomy_decision, prioritise, standardised_transformation, duplication,
            obscurity, low_level_events_and_aggregations_layer, data_catalogue,
            trustworthiness, interoperability]
add_links({s3: s3_codes}, role_name="contained_code")

s4 = CClass(source, "s4", values={
    "title": "What is a Data Product?",
    "url": "https://www.k2view.com/what-is-a-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s4",
    "tiny url": "https://tinyurl.com/data-as-a-product-s4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s4_codes = [change_data_capture, event_streaming, virtualisation, data_integration_service,
            incremental_sync, data_product_governance, keep_track_metadata_decision, communication_decision,
            quality_monitoring, request_access, trustworty_decision, internal_storages, immutable_change_audit_log,
            role_based_access_control, cache, security_decision, store_decision, encryption]
add_links({s4: s4_codes}, role_name="contained_code")

s5 = CClass(source, "s5", values={
    "title": "What is a data product?",
    "url": "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/what-is-data-product",
    "archive url": "https://bit.ly/data-as-a-product-s5",
    "tiny url": "https://tinyurl.com/data-as-a-product-s5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s5_codes = [lineage_repository, time_bounded_backwards_compatibility, keep_track_metadata_decision, trustworty_decision, request_access,
            rest_apis, sql_layer, security_decision, data_access_decision, domain_datasets, core_datasets, data_integration_service, communication_decision,
            data_product_anatomy_decision, universal_metadata_registry, encryption, cache, quality_monitoring]
add_links({s5: s5_codes}, role_name="contained_code")

s6 = CClass(source, "s6", values={
    "title": "Data Products: The Definitive Guide",
    "url": "https://lakefs.io/blog/data-products/",
    "archive url": "https://bit.ly/data-as-a-product-s6",
    "tiny url": "https://tinyurl.com/data-as-a-product-s6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s6_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product,
        automated_decision_making_model_as_data_product, algorithms_as_data_product, data_product_type_decision,
            rest_apis, data_access_decision, quality_monitoring, request_access, role_based_access_control, security_decision, discoverable_data_products_decision,
            infrastructure_decision, infrastructure_as_code, schema_manager, trustworty_decision, ci_cd_process,
            versioning, k8s]
add_links({s6: s6_codes}, role_name="contained_code")

s7 = CClass(source, "s7", values={
    "title": "Designing Data Products",
    "url": "https://www.datamesh-architecture.com/data-product-canvas",
    "archive url": "https://bit.ly/data-as-a-product-s7",
    "tiny url": "https://tinyurl.com/data-as-a-product-s7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s7_codes = [mdm, infrastructure_decision, rest_apis, decision_support_model_as_data_product, data_product_type_decision,
            data_access_decision, sql_layer, data_product_governance, lineage_repository, schema_manager, keep_track_metadata_decision,
            trustworty_decision, core_datasets, domain_datasets, data_product_anatomy_decision, versioning, observation_plane,
            accuracy, completeness, integrity, compliance]
add_links({s7: s7_codes}, role_name="contained_code")

s8 = CClass(source, "s8", values={
    "title": "How to identify Data Products? Welcome “Data Product Flow”",
    "url": "https://www.agilelab.it/blog/how-to-identify-data-products-welcome-data-product-flow",
    "archive url": "https://bit.ly/data-as-a-product-s8",
    "tiny url": "https://tinyurl.com/data-as-a-product-s8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s8_codes = [low_level_events_and_aggregation_layer, rest_apis, data_access_decision, data_product_anatomy_decision,
            triggering, time_bounded_backwards_compatibility, cqrs, multiple_independent_read_only_views, keep_track_metadata_decision]
add_links({s8: s8_codes}, role_name="contained_code")

s9 = CClass(source, "s9", values={
    "title": "Building data products as a competitive differentiator",
    "url": "https://tinyurl.com/data-as-a-product-s9",
    "archive url": "https://bit.ly/data-as-a-product-s9",
    "tiny url": "https://tinyurl.com/data-as-a-product-s9",
    "author type": "Practitioner",
    "type": "Slides",
    "example": False,
    "source code": False})
s9_codes = [decision_support_model_as_data_product, rest_apis, data_access_decision, data_product_type_decision,
            infrastructure_decision, infrastructure_as_code, automated_decision_making_model_as_data_product, raw_data_as_data_product,
            quality_monitoring, event_streaming, communication_decision, trustworty_decision, data_product_anatomy_decision,
            feature_layer, interoperability, core_datasets, derived_data_as_data_product, keep_track_metadata_decision,
            query_catalogue, data_catalogue, mdm, central_data_product_catalogue, lineage_repository, universal_metadata_registry]
add_links({s9: s9_codes}, role_name="contained_code")

s10 = CClass(source, "s10", values={
    "title": "",
    "url": "https://www.montecarlodata.com/blog-how-to-treat-your-data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s10",
    "tiny url": "https://tinyurl.com/data-as-a-product-s10",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s10_codes = [sql_layer, data_access_decision, time_bounded_backwards_compatibility, keep_track_metadata_decision,
             quality_monitoring, trustworty_decision, schema_manager, immutable_change_audit_log, triggering,
             communication_decision, ]
add_links({s10: s10_codes}, role_name="contained_code")

s11 = CClass(source, "s11", values={
    "title": "Nine Principles for Designing Great Data Products",
    "url": "https://www.frog.co/designmind/nine-principles-for-designing-great-data-products",
    "archive url": "https://bit.ly/data-as-a-product-s11",
    "tiny url": "https://tinyurl.com/data-as-a-product-s11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s11_codes = [quality_monitoring, trustworty_decision, observation_plane, ]
add_links({s11: s11_codes}, role_name="contained_code")

s12 = CClass(source, "s12", values={
    "title": "How to unlock the full value of data? Manage it like a product",
    "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights/how-to-unlock-the-full-value-of-data-manage-it-like-a-product",
    "archive url": "https://bit.ly/data-as-a-product-s12",
    "tiny url": "https://tinyurl.com/data-as-a-product-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s12_codes = [role_based_access_control, immutable_change_audit_log, quality_monitoring, trustworty_decision,
             keep_track_metadata_decision, security_decision]
add_links({s12: s12_codes}, role_name="contained_code")

s13 = CClass(source, "s13", values={
    "title": "Data Product Specification",
    "url": "https://github.com/agile-lab-dev/Data-Product-Specification",
    "archive url": "https://bit.ly/data-as-a-product-s13",
    "tiny url": "https://tinyurl.com/data-as-a-product-s13",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
s13_codes = [internal_storages, sql_layer, observation_plane, versioning, infrastructure_decision, trustworty_decision,
             store_decision, data_access_decision]
add_links({s13: s13_codes}, role_name="contained_code")

s14 = CClass(source, "s14", values={
    "title": "Data Product Pyramid: Implementing a Business Strategy using Data Products",
    "url": "http://dataception.com/blogs/Data-Product-Pyramid/Data-Product-Pyramid.html",
    "archive url": "https://bit.ly/data-as-a-product-s14",
    "tiny url": "https://tinyurl.com/data-as-a-product-s14",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s14_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product,
             data_product_type_decision, containerisation, infrastructure_decision, virtualisation, keep_track_metadata_decision,
             cache, k8s, sql_layer, data_access_decision,store_decision]
add_links({s14: s14_codes}, role_name="contained_code")

s15 = CClass(source, "s15", values={
    "title": "Deploying Data Products at the speed of the business",
    "url": "http://dataception.com/Data-Mesh-Deploying-Data-Products-at-the-speed-of-the-business.html#TechnicalArchitecture",
    "archive url": "https://bit.ly/data-as-a-product-s15",
    "tiny url": "https://tinyurl.com/data-as-a-product-s15",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s15_codes = [infrastructure_as_code, infrastructure_decision, re_use, time_to_market, discoverability, duplication,
             rest_apis, central_data_product_catalogue, data_catalogue, containerisation, raw_data_as_data_product,
             derived_data_as_data_product, data_product_type_decision, data_access_decision,
             end_to_end, communication_decision, lineage_repository, role_based_access_control, schema_manager, security_decision,
             keep_track_metadata_decision, trustworty_decision, request_access, no_sql_system, versioning, incremental_sync, internal_storages,
             store_decision, discoverable_data_products_decision, cache, virtualisation, sql_layer]
add_links({s15: s15_codes}, role_name="contained_code")

s16 = CClass(source, "s16", values={
    "title": "The Data Product ABCs – A Framework for Bringing Product Thinking to Data",
    "url": "datasciencecentral.com/data-product-framework/",
    "archive url": "https://bit.ly/data-as-a-product-s16",
    "tiny url": "https://tinyurl.com/data-as-a-product-s16",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s16_codes = [sql_layer, data_catalogue, data_access_decision, keep_track_metadata_decision, schema_manager,
             trustworty_decision, data_product_governance, ]
add_links({s16: s16_codes}, role_name="contained_code")

s17 = CClass(source, "s17", values={
    "title": "Data Mesh 101: Data as a Product",
    "url": "https://www.youtube.com/watch?v=VhXP7LjELyw",
    "archive url": "https://bit.ly/data-as-a-product-s17",
    "tiny url": "https://tinyurl.com/data-as-a-product-s17",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s17_codes = [event_streaming, rest_apis, time_bounded_backwards_compatibility, versioning, schema_manager,
             communication_decision, data_access_decision, keep_track_metadata_decision, infrastructure_decision,
             trustworty_decision]
add_links({s17: s17_codes}, role_name="contained_code")

s18 = CClass(source, "s18", values={
    "title": "Top 4 Considerations for Designing a Data Product",
    "url": "https://datafloq.com/read/4-considerations-designing-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s18",
    "tiny url": "https://tinyurl.com/data-as-a-product-s18",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s18_codes = [register_datasets, orchestration, rest_apis, virtualisation, discoverable_data_products_decision,
             infrastructure_decision, data_access_decision, keep_track_metadata_decision, cache]
add_links({s18: s18_codes}, role_name="contained_code")

s19 = CClass(source, "s19", values={
    "title": "Data Mesh: is the argument a strawman?",
    "url": "https://medium.com/slalom-data-ai/data-mesh-is-the-argument-a-strawman-3cffaf55ce5e",
    "archive url": "https://bit.ly/data-as-a-product-s19",
    "tiny url": "https://tinyurl.com/data-as-a-product-s19",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s19_codes = [infrastructure_as_code, prioritise, obscurity, virtualisation, infrastructure_decision,
             schema_manager, trustworty_decision, versioning, ci_cd_process, quality_monitoring, triggering,
             communication_decision, standardised_transformation]
add_links({s19: s19_codes}, role_name="contained_code")

s20 = CClass(source, "s20", values={
    "title": "Intuit’s Data Mesh Strategy",
    "url": "https://medium.com/intuit-engineering/intuits-data-mesh-strategy-778e3edaa017",
    "archive url": "https://bit.ly/data-as-a-product-s20",
    "tiny url": "https://tinyurl.com/data-as-a-product-s20",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s20_codes = [change_data_capture, rest_apis, schema_manager, quality_monitoring, infrastructure_decision,
             data_access_decision, trustworty_decision, discovery_port, unified_batch_stream, conflicting_definitions,
             discoverable_data_products_decision, periodic_execution, communication_decision, domain_datasets,
             event_streaming, virtualisation, event_bus, data_marts, consistency, stability, store_decision,
             orchestration, feature_layer, universal_metadata_registry, keep_track_metadata_decision]
add_links({s20: s20_codes}, role_name="contained_code")
