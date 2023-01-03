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
            obscurity, low_level_events_and_aggregation_layer, data_catalogue,
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

s21 = CClass(source, "s21", values={
    "title": "Data as a Product: Applying Product Thinking Into Data",
    "url": "https://atlan.com/data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s21",
    "tiny url": "https://tinyurl.com/data-as-a-product-s21",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s21_codes = [re_use]
add_links({s21: s21_codes}, role_name="contained_code")

s22 = CClass(source, "s22", values={
    "title": "Don’t Call It A “Data Product” Unless It Meets These 5 Requirements",
    "url": "https://insidebigdata.com/2022/06/09/dont-call-it-a-data-product-unless-it-meets-these-5-requirements/",
    "archive url": "https://bit.ly/data-as-a-product-s22",
    "tiny url": "https://tinyurl.com/data-as-a-product-s22",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s22_codes = [quality_monitoring, observation_plane, triggering, trustworty_decision, communication_decision, end_to_end]
add_links({s22: s22_codes}, role_name="contained_code")

s23 = CClass(source, "s23", values={
    "title": "Data Mesh in practice: Product thinking and development (Part III)",
    "url": "https://www.thoughtworks.com/insights/articles/data-mesh-in-practice-product-thinking-and-development",
    "archive url": "https://bit.ly/data-as-a-product-s23",
    "tiny url": "https://tinyurl.com/data-as-a-product-s23",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s23_codes = [open_access, security_decision, central_data_product_catalogue, keep_track_metadata_decision, request_access,
             discoverable_data_products_decision]
add_links({s23: s23_codes}, role_name="contained_code")

s24 = CClass(source, "s24", values={
    "title": "Make your data product more than a feature",
    "url": "https://www.finddataops.com/p/make-your-data-product-more-than",
    "archive url": "https://bit.ly/data-as-a-product-s24",
    "tiny url": "https://tinyurl.com/data-as-a-product-s24",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s24_codes = [schema_manager, trustworty_decision]
add_links({s24: s24_codes}, role_name="contained_code")

s25 = CClass(source, "s25", values={
    "title": "An Introduction to the Data Product Management Landscape",
    "url": "https://blog.insightdatascience.com/an-introduction-to-the-data-product-management-landscape-ef930afe6de5",
    "archive url": "https://bit.ly/data-as-a-product-s25",
    "tiny url": "https://tinyurl.com/data-as-a-product-s25",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s25_codes = [end_to_end, maintaining_source_of_truth, communication_decision, trustworty_decision, re_use,
             time_to_market, discovery_port, data_catalogue]
add_links({s25: s25_codes}, role_name="contained_code")

s26 = CClass(source, "s26", values={
    "title": "Data Mesh to Go: How to Get the Data Product",
    "url": "https://www.innoq.com/en/blog/data-mesh-to-go-how-to-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s26",
    "tiny url": "https://tinyurl.com/data-as-a-product-s26",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s26_codes = [low_level_events_and_aggregation_layer, data_product_anatomy_decision]
add_links({s26: s26_codes}, role_name="contained_code")

s27 = CClass(source, "s27", values={
    "title": "Anatomy of a Data Product",
    "url": "https://rkakodker.com/anatomy-of-a-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s27",
    "tiny url": "https://tinyurl.com/data-as-a-product-s27",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s27_codes = [raw_data_as_data_product, derived_data_as_data_product, data_product_type_decision, sql_layer,
             request_access, decision_support_model_as_data_product, automated_decision_making_model_as_data_product, data_access_decision,
             discoverable_data_products_decision, feature_layer, data_product_anatomy_decision]
add_links({s27: s27_codes}, role_name="contained_code")

s28 = CClass(source, "s28", values={
    "title": "The data product lifecycle",
    "url": "https://blog.dataminded.com/the-data-product-lifecycle-4903c9752527",
    "archive url": "https://bit.ly/data-as-a-product-s28",
    "tiny url": "https://tinyurl.com/data-as-a-product-s28",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s28_codes = [run_tests, trustworty_decision, infrastructure_decision, infrastructure_as_code,
             versioning, unified_batch_stream, quality_monitoring, swamp, data_product_governance,
             ci_cd_process]
add_links({s28: s28_codes}, role_name="contained_code")

s29 = CClass(source, "s29", values={
    "title": "Data-as-a-Product: unlock the energy in your data",
    "url": "https://www.kinandcarta.com/en/insights/2022/02/how-to-adopt-a-data-as-a-product-mindset/",
    "archive url": "https://bit.ly/data-as-a-product-s29",
    "tiny url": "https://tinyurl.com/data-as-a-product-s29",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s29_codes = [maintaining_source_of_truth, end_to_end, trustworty_decision, communication_decision]
add_links({s29: s29_codes}, role_name="contained_code")

s30 = CClass(source, "s30", values={
    "title": "Recipe for building your first Data Product in a Data Mesh",
    "url": "https://medium.com/google-cloud/recipe-for-building-your-first-data-product-in-a-data-mesh-78b52338ef59",
    "archive url": "https://bit.ly/data-as-a-product-s30",
    "tiny url": "https://tinyurl.com/data-as-a-product-s30",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s30_codes = [query_catalogue, infrastructure_as_code, ci_cd_process, keep_track_metadata_decision, infrastructure_decision,
             templated_data_pipeline, pub_sub, sql_layer, communication_decision, data_access_decision, unified_batch_stream,
             rest_apis, orchestration, data_integration_service, containerisation, data_catalogue]
add_links({s30: s30_codes}, role_name="contained_code")

s31 = CClass(source, "s31", values={
    "title": "Build a data mesh on Google Cloud with Dataplex, now generally available",
    "url": "https://cloud.google.com/blog/products/data-analytics/build-a-data-mesh-on-google-cloud-with-dataplex-now-generally-available",
    "archive url": "https://bit.ly/data-as-a-product-s31",
    "tiny url": "https://tinyurl.com/data-as-a-product-s31",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s31_codes = [centrally_manage_monitor_govern_data, data_productivity, analytics_agility, manual_toil, security,
             quality, discovery, infrastructure_decision, data_catalogue, keep_track_metadata_decision, universal_metadata_registry, sql_layer,
             data_access_decision, immutable_change_audit_log, request_access, discoverable_data_products_decision]
add_links({s31: s31_codes}, role_name="contained_code")

s32 = CClass(source, "s32", values={
    "title": "Build a modern, distributed Data Mesh with Google Cloud",
    "url": "https://services.google.com/fh/files/misc/build-a-modern-distributed-datamesh-with-google-cloud-whitepaper.pdf",
    "archive url": "https://bit.ly/data-as-a-product-s32",
    "tiny url": "https://tinyurl.com/data-as-a-product-s32",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s32_codes = [internal_storages, store_decision, data_marketplace, discoverable_data_products_decision, discoverability,
             gain_knowledge, query_catalogue, rest_apis, search_engine, central_data_product_catalogue, immutable_change_audit_log,
             keep_track_metadata_decision, data_catalogue, universal_metadata_registry, sql_layer, data_access_decision,
             open_source_data_and_analytics_processing_service, triggering, communication_decision, request_access, quality_monitoring,
             unified_batch_stream, k8s, pub_sub, containerisation, infrastructure_decision]
add_links({s32: s32_codes}, role_name="contained_code")

s33 = CClass(source, "s33", values={
    "title": "Data as a Product: Make It Real with Event-Driven, Serverless Data Pipelines",
    "url": "https://www.fst.network/post/data-product",
    "archive url": "https://bit.ly/data-as-a-product-s33",
    "tiny url": "https://tinyurl.com/data-as-a-product-s33",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s33_codes = [rest_apis, containerisation, data_access_decision, triggering, communication_decision, infrastructure_decision,
             event_streaming, quality_monitoring, trustworty_decision, ]
add_links({s33: s33_codes}, role_name="contained_code")

s34 = CClass(source, "s34", values={
    "title": "#2 Explain Data Product in 8 Minutes with practical examples",
    "url": "dataproductbusiness.com/post/explain-data-product-in-8-minutes-with-practical-examples",
    "archive url": "https://bit.ly/data-as-a-product-s34",
    "tiny url": "https://tinyurl.com/data-as-a-product-s34",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s34_codes = [rest_apis, automated_decision_making_model_as_data_product, data_access_decision, data_product_type_decision,
             decision_support_model_as_data_product, derived_data_as_data_product, raw_data_as_data_product, event_streaming,
             versioning, infrastructure_decision, communication_decision]
add_links({s34: s34_codes}, role_name="contained_code")

s35 = CClass(source, "s35", values={
    "title": "Develop Your Data as a Product",
    "url": "https://towardsdatascience.com/develop-your-data-as-a-product-f9ba268c4e20",
    "archive url": "https://bit.ly/data-as-a-product-s35",
    "tiny url": "https://tinyurl.com/data-as-a-product-s35",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s35_codes = [ci_cd_process, immutable_change_audit_log, quality_monitoring, versioning, triggering, infrastructure_decision,
             keep_track_metadata_decision, trustworty_decision, communication_decision]
add_links({s35: s35_codes}, role_name="contained_code")

s36 = CClass(source, "s36", values={
    "title": "Data mesh: A perspective on using Azure Synapse Analytics to build data products",
    "url": "https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/data-mesh-a-perspective-on-using-azure-synapse-analytics-to/ba-p/3644657",
    "archive url": "https://bit.ly/data-as-a-product-s36",
    "tiny url": "https://tinyurl.com/data-as-a-product-s36",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s36_codes = [sql_layer, quality_monitoring, internal_storages, data_access_decision, trustworty_decision, store_decision,
             immutable_change_audit_log, keep_track_metadata_decision, rest_apis, unified_batch_stream, communication_decision,
             request_access, discoverable_data_products_decision, role_based_access_control, security_decision, versioning,
             attribute_based_access_control, multi_tenancy_model, single_subscription_single_workspace_dedicated_artifacts_per_domain,
             single_subscription_multiple_workspaces]
add_links({s36: s36_codes}, role_name="contained_code")

s37 = CClass(source, "s37", values={
    "title": "Describe and organize data products and resources in a data mesh",
    "url": "https://cloud.google.com/architecture/describe-organize-data-products-resources-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s37",
    "tiny url": "https://tinyurl.com/data-as-a-product-s37",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s37_codes = [data_catalogue, keep_track_metadata_decision, rest_apis, data_access_decision, pub_sub, communication_decision,
             sql_layer]
add_links({s37: s37_codes}, role_name="contained_code")

s38 = CClass(source, "s38", values={
    "title": "Build data products in a data mesh",
    "url": "https://cloud.google.com/architecture/build-data-products-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s38",
    "tiny url": "https://tinyurl.com/data-as-a-product-s38",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s38_codes = [rest_apis, sql_layer, event_streaming, versioning, data_access_decision, infrastructure_decision,
             communication_decision, request_access, discoverable_data_products_decision, pub_sub, triggering, change_data_capture,
             keep_track_metadata_decision, separate_subscriptions_separate_workspace_per_domain, structural_decision]
add_links({s38: s38_codes}, role_name="contained_code")

s39 = CClass(source, "s39", values={
    "title": "Discover and consume data products in a data mesh",
    "url": "https://cloud.google.com/architecture/discover-consume-data-products-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s39",
    "tiny url": "https://tinyurl.com/data-as-a-product-s39",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s39_codes = [central_data_product_catalogue, sql_layer, data_access_decision, keep_track_metadata_decision, rest_apis,
             open_source_data_and_analytics_processing_service, data_product_anatomy_decision, pub_sub, communication_decision,
             unified_batch_stream]
add_links({s39: s39_codes}, role_name="contained_code")

s40 = CClass(source, "s40", values={
    "title": "How to think of Data as a Product",
    "url": "https://www.ellie.ai/blogs/how-to-think-of-data-as-a-product",
    "archive url": "https://bit.ly/data-as-a-product-s40",
    "tiny url": "https://tinyurl.com/data-as-a-product-s40",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s40_codes = [feature_layer, central_data_product_catalogue, keep_track_metadata_decision, data_product_anatomy_decision]
add_links({s40: s40_codes}, role_name="contained_code")

s41 = CClass(source, "s41", values={
    "title": "What is Data as a Product, and What to Consider Implementing It?",
    "url": "https://mastheadata.com/what-is-data-as-a-product-and-what-to-consider-implementing-it/",
    "archive url": "https://bit.ly/data-as-a-product-s41",
    "tiny url": "https://tinyurl.com/data-as-a-product-s41",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s41_codes = [unified_batch_stream, communication_decision, event_streaming, pub_sub, rest_apis, cqrs, schema_manager,
             trustworty_decision, indirect_data_publishing_and_consumption, snapshots_ETL, fast_data_propagation, handle_large_data_volumes,
             limit_recipients, addressability_subscriptions, control_over_data_schema]
add_links({s41: s41_codes}, role_name="contained_code")

s42 = CClass(source, "s42", values={
    "title": "How Dell IT is Driving Data-as-a-product",
    "url": "https://www.dell.com/en-us/blog/how-dell-it-is-driving-data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s42",
    "tiny url": "https://tinyurl.com/data-as-a-product-s42",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s42_codes = [data_marketplace, central_data_product_catalogue, keep_track_metadata_decision, discoverable_data_products_decision]
add_links({s42: s42_codes}, role_name="contained_code")

s43 = CClass(source, "s43", values={
    "title": "Treating data as a product at Adevinta",
    "url": "https://medium.com/adevinta-tech-blog/treating-data-as-a-product-at-adevinta-c1dce5d394c5",
    "archive url": "https://bit.ly/data-as-a-product-s43",
    "tiny url": "https://tinyurl.com/data-as-a-product-s43",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s43_codes = [single_subscription_dedicated_workpasce_per_domain, structural_decision, raw_data_as_data_product,
             data_product_type_decision, low_level_events_and_aggregation_layer, data_marts, store_decision,
             data_product_anatomy_decision, sql_layer, data_catalogue, keep_track_metadata_decision, k8s,
             templated_data_pipeline, infrastructure_decision, data_access_decision, data_marketplace, cqrs,
             indirect_data_publishing_and_consumption, query_catalogue]
add_links({s43: s43_codes}, role_name="contained_code")

s44 = CClass(source, "s44", values={
    "title": "An Operating Model for Data Products",
    "url": "https://towardsdatascience.com/an-operating-model-for-data-products-fba6b268f698",
    "archive url": "https://bit.ly/data-as-a-product-s44",
    "tiny url": "https://tinyurl.com/data-as-a-product-s44",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s44_codes = [event_streaming, mdm, infrastructure_decision, communication_decision, unified_batch_stream, ]
add_links({s44: s44_codes}, role_name="contained_code")

s45 = CClass(source, "s45", values={
    "title": "The Anatomy of a Data Product",
    "url": "https://towardsdatascience.com/the-anatomy-of-a-data-product-d3140f068311",
    "archive url": "https://bit.ly/data-as-a-product-s45",
    "tiny url": "https://tinyurl.com/data-as-a-product-s45",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s45_codes = [zero_trust_architecture, rest_apis, security_decision, data_access_decision, change_data_capture,
             core_datasets, data_product_anatomy_decision, keep_track_metadata_decision, domain_datasets,
             event_streaming, communication_decision, immutable_change_audit_log, register_datasets, discoverable_data_products_decision,
             containerisation, data_marketplace, infrastructure_decision, k8s, time_bounded_backwards_compatibility, versioning, oauth2,
             triggering, central_data_product_catalogue]
add_links({s45: s45_codes}, role_name="contained_code")

s46 = CClass(source, "s46", values={
    "title": "Topology of a Data Product Team",
    "url": "https://towardsdatascience.com/topology-of-a-data-product-team-75dc5471fccf",
    "archive url": "https://bit.ly/data-as-a-product-s46",
    "tiny url": "https://tinyurl.com/data-as-a-product-s46",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s46_codes = [universal_metadata_registry, keep_track_metadata_decision, virtualisation]
add_links({s46: s46_codes}, role_name="contained_code")

s47 = CClass(source, "s47", values={
    "title": "Data Mesh / Data Product Security Pattern",
    "url": "https://towardsdatascience.com/data-mesh-data-product-security-pattern-c5b93a27e82e",
    "archive url": "https://bit.ly/data-as-a-product-s47",
    "tiny url": "https://tinyurl.com/data-as-a-product-s47",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s47_codes = [central_data_product_catalogue, schema_manager, data_product_governance, trustworty_decision,
             keep_track_metadata_decision, immutable_change_audit_log]
add_links({s47: s47_codes}, role_name="contained_code")

s48 = CClass(source, "s48", values={
    "title": "Data Mesh Patterns: Enterprise Data Product Catalog",
    "url": "https://towardsdatascience.com/data-mesh-pattern-enterprise-data-product-catalog-ba4bf072d7c3",
    "archive url": "https://bit.ly/data-as-a-product-s48",
    "tiny url": "https://tinyurl.com/data-as-a-product-s48",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s48_codes = [central_data_product_catalogue, keep_track_metadata_decision, data_catalogue, immutable_change_audit_log,
             schema_manager, trustworty_decision, change_data_capture, lineage_repository, event_streaming, incremental_sync,
             sql_layer, communication_decision, data_access_decision]
add_links({s48: s48_codes}, role_name="contained_code")

s49 = CClass(source, "s49", values={
    "title": "Applying Data Mesh principles to an IoT data architecture",
    "url": "https://www.acagroup.be/en/blog/applying-data-mesh-principles-to-an-iot-data-architecture/",
    "archive url": "https://bit.ly/data-as-a-product-s49",
    "tiny url": "https://tinyurl.com/data-as-a-product-s49",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s49_codes = [rest_apis, internal_storages, sql_layer, discovery_port, virtualisation, data_access_decision, control_plane,
             data_product_anatomy_decision, discoverable_data_products_decision, store_decision, keep_track_metadata_decision]
add_links({s49: s49_codes}, role_name="contained_code")

s50 = CClass(source, "s50", values={
    "title": "The Fundamentals of Building Better Data Products",
    "url": "https://www.mindtheproduct.com/fundamentals-building-better-data-products/#:~:text=As%20I%20see%20it%20there,products%2C%20and%20data%20as%20insight",
    "archive url": "https://bit.ly/data-as-a-product-s50",
    "tiny url": "https://tinyurl.com/data-as-a-product-s50",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s50_codes = [time_bounded_backwards_compatibility, keep_track_metadata_decision]
add_links({s50: s50_codes}, role_name="contained_code")

s51 = CClass(source, "s51", values={
    "title": "The Unfortunate Reality about Data Pipelines",
    "url": "https://thenewstack.io/the-unfortunate-reality-about-data-pipelines/",
    "archive url": "https://bit.ly/data-as-a-product-s51",
    "tiny url": "https://tinyurl.com/data-as-a-product-s51",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s51_codes = [time_bounded_backwards_compatibility, keep_track_metadata_decision, event_streaming, communication_decision,
             versioning, infrastructure_decision, ci_cd_process, real_time_data_access, high_fidelity, multiple_environments]
add_links({s51: s51_codes}, role_name="contained_code")

s52 = CClass(source, "s52", values={
    "title": "The next generation of Data Platforms is the Data Mesh",
    "url": "https://medium.com/paypal-tech/the-next-generation-of-data-platforms-is-the-data-mesh-b7df4b825522",
    "archive url": "https://bit.ly/data-as-a-product-s52",
    "tiny url": "https://tinyurl.com/data-as-a-product-s52",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s52_codes = [data_marts, store_decision, control_plane, data_product_anatomy_decision, discovery_port,
             observation_plane, rest_apis, data_access_decision, discoverable_data_products_decision, trustworty_decision,
             event_streaming, communication_decision]
add_links({s52: s52_codes}, role_name="contained_code")


s53 = CClass(source, "s53", values={
    "title": "Data Mesh Patterns: Change Data Capture",
    "url": "https://towardsdatascience.com/data-mesh-pattern-deep-dive-change-data-capture-eb3090178c34",
    "archive url": "https://bit.ly/data-as-a-product-s53",
    "tiny url": "https://tinyurl.com/data-as-a-product-s53",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s53_codes = [change_data_capture, keep_track_metadata_decision, event_streaming, communication_decision, central_data_product_catalogue,
             immutable_change_audit_log, non_intrusive, consumption, production_grade_integrations, pub_sub, data_catalogue]
add_links({s53: s53_codes}, role_name="contained_code")

s54 = CClass(source, "s54", values={
    "title": "Data Mesh Patterns: Immutable Change / Audit Log",
    "url": "https://towardsdatascience.com/data-mesh-patterns-immutable-change-audit-log-aec93da33648",
    "archive url": "https://bit.ly/data-as-a-product-s54",
    "tiny url": "https://tinyurl.com/data-as-a-product-s54",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s54_codes = [immutable_change_audit_log, change_data_capture, central_data_product_catalogue, schema_manager, keep_track_metadata_decision,
             trustworty_decision, reproducibility, traceability, verifiability]
add_links({s54: s54_codes}, role_name="contained_code")















































