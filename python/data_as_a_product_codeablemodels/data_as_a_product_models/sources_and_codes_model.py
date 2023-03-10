from python.data_as_a_product_codeablemodels.data_as_a_product_models.data_as_a_product_model import *
from codeable_models import CClass, add_links
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
    "tiny url": "tinyurl.com/data-as-a-product-s1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})

s1_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product, orchestration_decision, interface_decision,
            automated_decision_making_model_as_data_product, register_datasets, request_access, service_locator, non_functional, input_port, output_port,clear_ownership,
            data_catalogue, query_catalogue, quality_monitoring, data_product_type_decision, data_product_layer_decision, data_product_self_serve_management_decision,
            request_access_engine, security, discoverability, interoperability, trustworthiness, start_from_scratch]
add_links({s1: s1_codes}, role_name="contained_code")

s2 = CClass(source, "s2", values={
    "title": "Designing Data Products",
    "url": "https://towardsdatascience.com/designing-data-products-b6b93edf3d23",
    "archive url": "https://bit.ly/data-as-a-product-s2",
    "tiny url": "tinyurl.com/data-as-a-product-s2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s2_codes = [algorithms_as_data_product, understandability, raw_data_as_data_product, orchestration_decision, input_port, output_port,
            derived_data_as_data_product, decision_support_model_as_data_product, automated_decision_making_model_as_data_product, interface_decision,
            rest_apis, api_invocation, sql_layer, data_product_type_decision, time_to_market, start_from_scratch, data_product_self_serve_management_decision]
add_links({s2: s2_codes}, role_name="contained_code")

s3 = CClass(source, "s3", values={
    "title": "Building a data mesh to support an ecosystem of data products at Adevinta",
    "url": "https://medium.com/adevinta-tech-blog/building-a-data-mesh-to-support-an-ecosystem-of-data-products-at-adevinta-4c057d06824d",
    "archive url": "https://bit.ly/data-as-a-product-s3",
    "tiny url": "tinyurl.com/data-as-a-product-s3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s3_codes = [accelerate_decision_making, more_granular_data, sql_layer, observation_plane, api_invocation,
            observation_port, schema_manager, understandability, rest_apis, query_catalogue,
            quality_monitoring, request_access, domain_datasets, orchestration_decision,
            core_datasets, standardised_transformation, duplication, non_functional,  data_product_type_decision,
            data_catalogue, data_product_layer_decision, interface_decision, aggregations, input_port, output_port, clear_ownership, self_serve,
            trustworthiness, interoperability, start_from_scratch, data_product_self_serve_management_decision]
add_links({s3: s3_codes}, role_name="contained_code")

s4 = CClass(source, "s4", values={
    "title": "What is a Data Product?",
    "url": "https://www.k2view.com/what-is-a-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s4",
    "tiny url": "tinyurl.com/data-as-a-product-s4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s4_codes = [change_data_capture, event_streaming, virtualisation, data_onboarding, non_functional, deploy_decision,
            incremental_sync, data_product_layer_decision, data_product_self_serve_management_decision,
            quality_monitoring, request_access, internal_storages, immutable_change_audit_log, orchestration_decision,
            role_based_access_control, data_marts, security, accessible, data_storage_infrastructure, data_product_type_decision,
            ci_cd_process, encryption, cloud_acceleration, legacy_modernization, source_aligned_data_product, consumer_aligned_data_product,
            master_database, multi_cloud_deployment, clear_ownership, continuity, infrastructure_to_manage, hybrid_deployment]
add_links({s4: s4_codes}, role_name="contained_code")

s5 = CClass(source, "s5", values={
    "title": "What is a data product?",
    "url": "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/what-is-data-product",
    "archive url": "https://bit.ly/data-as-a-product-s5",
    "tiny url": "tinyurl.com/data-as-a-product-s5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s5_codes = [time_bounded_backwards_compatibility, request_access, orchestration_decision, data_product_self_serve_management_decision,
            rest_apis, sql_layer, domain_datasets, core_datasets, data_onboarding, non_functional,api_invocation,
            central_data_product_catalogue, encryption, cache, quality_monitoring, start_from_scratch,  data_product_type_decision,
            accessible, addressible, data_catalogue, data_product_layer_decision, clear_ownership, aggregations]
add_links({s5: s5_codes}, role_name="contained_code")

s6 = CClass(source, "s6", values={
    "title": "Data Products: The Definitive Guide",
    "url": "https://lakefs.io/blog/data-products/",
    "archive url": "https://bit.ly/data-as-a-product-s6",
    "tiny url": "tinyurl.com/data-as-a-product-s6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s6_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product, orchestration_decision,
        automated_decision_making_model_as_data_product, algorithms_as_data_product, data_product_type_decision,
            rest_apis, quality_monitoring, request_access, role_based_access_control, start_from_scratch, deploy_decision,
            infrastructure_as_code, schema_manager, ci_cd_process, data_product_self_serve_management_decision, non_functional,
            versioning, container_orchestration_system, quality, api_invocation, versioning_force]
add_links({s6: s6_codes}, role_name="contained_code")

s7 = CClass(source, "s7", values={
    "title": "Designing Data Products",
    "url": "https://www.datamesh-architecture.com/data-product-canvas",
    "archive url": "https://bit.ly/data-as-a-product-s7",
    "tiny url": "tinyurl.com/data-as-a-product-s7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s7_codes = [mdm, rest_apis, decision_support_model_as_data_product, data_product_type_decision, interface_decision, master_database,
             sql_layer, data_catalogue, schema_manager, orchestration_decision, data_product_layer_decision, api_invocation,
             core_datasets, domain_datasets, versioning, versioning_force, observation_port, start_from_scratch, migration, observation_plane,
            quality, completeness, raw_data_as_data_product, data_product_self_serve_management_decision, source_aligned_data_product, aggregations,
            consumer_aligned_data_product, input_port, output_port, metadata_lake, metastore, clear_ownership]
add_links({s7: s7_codes}, role_name="contained_code")

s8 = CClass(source, "s8", values={
    "title": "How to identify Data Products? Welcome ???Data Product Flow???",
    "url": "https://www.agilelab.it/blog/how-to-identify-data-products-welcome-data-product-flow",
    "archive url": "https://bit.ly/data-as-a-product-s8",
    "tiny url": "tinyurl.com/data-as-a-product-s8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s8_codes = [rest_apis, api_invocation, data_product_self_serve_management_decision, source_aligned_data_product, aggregations, consumer_aligned_data_product,
            output_port, clear_ownership, data_product_type_decision, interface_decision,
            triggering, time_bounded_backwards_compatibility, cqrs, migration, multiple_independent_read_only_views, start_from_scratch,
             immutable_change_audit_log, immutability, data_lineage, orchestration_decision, data_product_layer_decision]
add_links({s8: s8_codes}, role_name="contained_code")

s9 = CClass(source, "s9", values={
    "title": "Building data products as a competitive differentiator",
    "url": "https://towardsdatascience.com/data-as-a-product-vs-data-products-what-are-the-differences-b43ddbb0f123",
    "archive url": "https://bit.ly/data-as-a-product-s9",
    "tiny url": "tinyurl.com/data-as-a-product-s9",
    "author type": "Practitioner",
    "type": "Slides",
    "example": False,
    "source code": False})
s9_codes = [decision_support_model_as_data_product, rest_apis, data_product_type_decision, data_product_self_serve_management_decision,
             infrastructure_as_code, automated_decision_making_model_as_data_product, raw_data_as_data_product, master_database,
            quality_monitoring, event_streaming, data_product_layer_decision, orchestration_decision, api_invocation,
            feature_layer, interoperability, core_datasets, derived_data_as_data_product, start_from_scratch,
            query_catalogue, data_catalogue, mdm, central_data_product_catalogue, orchestration, migration]
add_links({s9: s9_codes}, role_name="contained_code")

s10 = CClass(source, "s10", values={
    "title": "How to treat your Data-as-a-Product",
    "url": "https://www.montecarlodata.com/blog-how-to-treat-your-data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s10",
    "tiny url": "tinyurl.com/data-as-a-product-s10",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s10_codes = [sql_layer, time_bounded_backwards_compatibility, data_product_self_serve_management_decision,
             quality_monitoring, output_port, clear_ownership, interface_decision]

add_links({s10: s10_codes}, role_name="contained_code")

s11 = CClass(source, "s11", values={
    "title": "Nine Principles for Designing Great Data Products",
    "url": "https://www.frog.co/designmind/nine-principles-for-designing-great-data-products",
    "archive url": "https://bit.ly/data-as-a-product-s11",
    "tiny url": "tinyurl.com/data-as-a-product-s11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s11_codes = [quality_monitoring, observation_port, understandability, trustworthiness, transparency, interface_decision,
             start_from_scratch, orchestration_decision, observation_plane, data_product_layer_decision]
add_links({s11: s11_codes}, role_name="contained_code")

s12 = CClass(source, "s12", values={
    "title": "How to unlock the full value of data? Manage it like a product",
    "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights/how-to-unlock-the-full-value-of-data-manage-it-like-a-product",
    "archive url": "https://bit.ly/data-as-a-product-s12",
    "tiny url": "tinyurl.com/data-as-a-product-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s12_codes = [role_based_access_control, immutable_change_audit_log, quality_monitoring, data_product_layer_decision, non_functional, data_product_self_serve_management_decision]
add_links({s12: s12_codes}, role_name="contained_code")

s13 = CClass(source, "s13", values={
    "title": "Data Product Specification",
    "url": "https://github.com/agile-lab-dev/Data-Product-Specification",
    "archive url": "https://bit.ly/data-as-a-product-s13",
    "tiny url": "tinyurl.com/data-as-a-product-s13",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": True})
s13_codes = [internal_storages, data_storage_infrastructure, sql_layer, interface_decision, data_product_self_serve_management_decision, observation_port, versioning_force, versioning, data_product_layer_decision, observation_plane,
             input_port, output_port, clear_ownership, deploy_decision]
add_links({s13: s13_codes}, role_name="contained_code")

s14 = CClass(source, "s14", values={
    "title": "Data Product Pyramid: Implementing a Business Strategy using Data Products",
    "url": "http://dataception.com/blogs/Data-Product-Pyramid/Data-Product-Pyramid.html",
    "archive url": "https://bit.ly/data-as-a-product-s14",
    "tiny url": "tinyurl.com/data-as-a-product-s14",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s14_codes = [raw_data_as_data_product, derived_data_as_data_product, decision_support_model_as_data_product, orchestration_decision, input_port, output_port, clear_ownership, batch_proccessing,
             data_product_type_decision, single_container_design, virtualisation, deploy_decision, containerisation, data_product_self_serve_management_decision, interface_decision,
             cache, container_orchestration_system, sql_layer, no_sql_system, unified_batch_stream, data_marketplace, query_catalogue, start_from_scratch]
add_links({s14: s14_codes}, role_name="contained_code")

s15 = CClass(source, "s15", values={
    "title": "Deploying Data Products at the speed of the business",
    "url": "http://dataception.com/Data-Mesh-Deploying-Data-Products-at-the-speed-of-the-business.html#TechnicalArchitecture",
    "archive url": "https://bit.ly/data-as-a-product-s15",
    "tiny url": "tinyurl.com/data-as-a-product-s15",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s15_codes = [infrastructure_as_code, reproducibility, time_to_market, duplication, discoverability, non_functional, deploy_decision,
             rest_apis, central_data_product_catalogue, data_catalogue, single_container_design, raw_data_as_data_product, interface_decision,
             derived_data_as_data_product, data_product_type_decision, orchestration_decision, containerisation, api_invocation,
             end_to_end, role_based_access_control, schema_manager, start_from_scratch, data_product_self_serve_management_decision,
             request_access, no_sql_system, versioning, incremental_sync, internal_storages, function_as_a_service, versioning_force, data_storage_infrastructure,
              cache, virtualisation, sql_layer, accessible, data_onboarding, data_product_layer_decision,
             aggregations, output_port, batch_proccessing, VMs, clear_ownership]
add_links({s15: s15_codes}, role_name="contained_code")

s16 = CClass(source, "s16", values={
    "title": "The Data Product ABCs ??? A Framework for Bringing Product Thinking to Data",
    "url": "datasciencecentral.com/data-product-framework/",
    "archive url": "https://bit.ly/data-as-a-product-s16",
    "tiny url": "tinyurl.com/data-as-a-product-s16",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s16_codes = [sql_layer, data_catalogue, schema_manager, reproducibility, data_product_layer_decision, data_product_self_serve_management_decision, interface_decision,
             input_port, output_port, clear_ownership]
add_links({s16: s16_codes}, role_name="contained_code")

s17 = CClass(source, "s17", values={
    "title": "Data Mesh 101: Data as a Product",
    "url": "https://www.youtube.com/watch?v=VhXP7LjELyw",
    "archive url": "https://bit.ly/data-as-a-product-s17",
    "tiny url": "tinyurl.com/data-as-a-product-s17",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s17_codes = [event_streaming, rest_apis, time_bounded_backwards_compatibility, versioning, versioning_force, schema_manager , data_product_layer_decision, api_invocation,
             infrastructure_as_code, real_time_data_access, scalable, duplication, immutability, addressible, snapshots_ETL, snapshots_via_ReqResAPI,
             control_over_data_schema, change_data_capture, data_product_self_serve_management_decision]
add_links({s17: s17_codes}, role_name="contained_code")

s18 = CClass(source, "s18", values={
    "title": "Top 4 Considerations for Designing a Data Product",
    "url": "https://datafloq.com/read/4-considerations-designing-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s18",
    "tiny url": "tinyurl.com/data-as-a-product-s18",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s18_codes = [register_datasets, orchestration, data_product_self_serve_management_decision, orchestration_decision, rest_apis, api_invocation, virtualisation, cache, pub_sub, start_from_scratch]
add_links({s18: s18_codes}, role_name="contained_code")

s19 = CClass(source, "s19", values={
    "title": "Data Mesh: is the argument a strawman?",
    "url": "https://medium.com/slalom-data-ai/data-mesh-is-the-argument-a-strawman-3cffaf55ce5e",
    "archive url": "https://bit.ly/data-as-a-product-s19",
    "tiny url": "tinyurl.com/data-as-a-product-s19",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s19_codes = [infrastructure_as_code, understandability, virtualisation, api_invocation, versioning_force, deploy_decision,
             schema_manager, versioning, ci_cd_process, quality_monitoring, triggering, data_storage_infrastructure,
             standardised_transformation, data_product_self_serve_management_decision, batch_proccessing, shared_storage,
             clear_ownership]
add_links({s19: s19_codes}, role_name="contained_code")

s20 = CClass(source, "s20", values={
    "title": "Intuit???s Data Mesh Strategy",
    "url": "https://medium.com/intuit-engineering/intuits-data-mesh-strategy-778e3edaa017",
    "archive url": "https://bit.ly/data-as-a-product-s20",
    "tiny url": "tinyurl.com/data-as-a-product-s20",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s20_codes = [change_data_capture, rest_apis, schema_manager, quality_monitoring, api_invocation,
              discovery_port, unified_batch_stream, orchestration_decision, non_functional,
              domain_datasets , data_product_layer_decision, data_product_self_serve_management_decision,
             event_streaming, virtualisation, event_bus, data_marts, security, metastore, metadata_lake, clear_ownership,
             feature_layer, central_data_product_catalogue, start_from_scratch,
             request_access, register_datasets, real_time_data_access, api_gateway, interface_decision]
add_links({s20: s20_codes}, role_name="contained_code")

s21 = CClass(source, "s21", values={
    "title": "Data as a Product: Applying Product Thinking Into Data",
    "url": "https://atlan.com/data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s21",
    "tiny url": "tinyurl.com/data-as-a-product-s21",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s21_codes = [reproducibility, function_as_a_service, deploy_decision, aggregations, clear_ownership,  data_product_type_decision,]
add_links({s21: s21_codes}, role_name="contained_code")

s22 = CClass(source, "s22", values={
    "title": "Don???t Call It A ???Data Product??? Unless It Meets These 5 Requirements",
    "url": "https://insidebigdata.com/2022/06/09/dont-call-it-a-data-product-unless-it-meets-these-5-requirements/",
    "archive url": "https://bit.ly/data-as-a-product-s22",
    "tiny url": "tinyurl.com/data-as-a-product-s22",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s22_codes = [quality_monitoring, observation_port, triggering, end_to_end, observation_plane,
             data_product_layer_decision, interface_decision, clear_ownership]
add_links({s22: s22_codes}, role_name="contained_code")

s23 = CClass(source, "s23", values={
    "title": "Data Mesh in practice: Product thinking and development (Part III)",
    "url": "https://www.thoughtworks.com/insights/articles/data-mesh-in-practice-product-thinking-and-development",
    "archive url": "https://bit.ly/data-as-a-product-s23",
    "tiny url": "tinyurl.com/data-as-a-product-s23",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s23_codes = [open_access, central_data_product_catalogue, request_access, start_from_scratch, data_product_self_serve_management_decision,  data_product_type_decision,
             mdm, orchestration_decision, migration, non_functional, master_database, source_aligned_data_product, consumer_aligned_data_product, aggregations,
             input_port, output_port, clear_ownership, interface_decision]
add_links({s23: s23_codes}, role_name="contained_code")

s24 = CClass(source, "s24", values={
    "title": "Make your data product more than a feature",
    "url": "https://www.finddataops.com/p/make-your-data-product-more-than",
    "archive url": "https://bit.ly/data-as-a-product-s24",
    "tiny url": "tinyurl.com/data-as-a-product-s24",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s24_codes = [schema_manager, data_product_self_serve_management_decision, input_port, output_port, clear_ownership, interface_decision]
add_links({s24: s24_codes}, role_name="contained_code")

s25 = CClass(source, "s25", values={
    "title": "An Introduction to the Data Product Management Landscape",
    "url": "https://blog.insightdatascience.com/an-introduction-to-the-data-product-management-landscape-ef930afe6de5",
    "archive url": "https://bit.ly/data-as-a-product-s25",
    "tiny url": "tinyurl.com/data-as-a-product-s25",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s25_codes = [end_to_end, maintaining_source_of_truth, reproducibility, start_from_scratch, orchestration_decision, data_storage_infrastructure, deploy_decision,
             time_to_market, discovery_port, data_catalogue, data_product_layer_decision, interface_decision, metastore, metadata_lake, shared_storage, clear_ownership,
             unified_batch_stream, quality_monitoring, duplication, discoverability, standardised_transformation, data_product_self_serve_management_decision]
add_links({s25: s25_codes}, role_name="contained_code")

s26 = CClass(source, "s26", values={
    "title": "Data Mesh to Go: How to Get the Data Product",
    "url": "https://www.innoq.com/en/blog/data-mesh-to-go-how-to-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s26",
    "tiny url": "tinyurl.com/data-as-a-product-s26",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s26_codes = [event_streaming, data_product_self_serve_management_decision]
add_links({s26: s26_codes}, role_name="contained_code")

s27 = CClass(source, "s27", values={
    "title": "Anatomy of a Data Product",
    "url": "https://rkakodker.com/anatomy-of-a-data-product/",
    "archive url": "https://bit.ly/data-as-a-product-s27",
    "tiny url": "tinyurl.com/data-as-a-product-s27",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": False,
    "source code": False})
s27_codes = [raw_data_as_data_product, derived_data_as_data_product, data_product_type_decision, sql_layer, non_functional,
             request_access, decision_support_model_as_data_product, automated_decision_making_model_as_data_product, interface_decision,
             feature_layer, data_product_layer_decision, data_product_self_serve_management_decision, input_port, output_port]
add_links({s27: s27_codes}, role_name="contained_code")

s28 = CClass(source, "s28", values={
    "title": "The data product lifecycle",
    "url": "https://blog.dataminded.com/the-data-product-lifecycle-4903c9752527",
    "archive url": "https://bit.ly/data-as-a-product-s28",
    "tiny url": "tinyurl.com/data-as-a-product-s28",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s28_codes = [run_tests, infrastructure_as_code, start_from_scratch, versioning_force,
             versioning, unified_batch_stream, quality_monitoring, data_product_self_serve_management_decision,
             ci_cd_process, orchestration_decision, batch_proccessing]
add_links({s28: s28_codes}, role_name="contained_code")

s29 = CClass(source, "s29", values={
    "title": "Data-as-a-Product: unlock the energy in your data",
    "url": "https://www.kinandcarta.com/en/insights/2022/02/how-to-adopt-a-data-as-a-product-mindset/",
    "archive url": "https://bit.ly/data-as-a-product-s29",
    "tiny url": "tinyurl.com/data-as-a-product-s29",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s29_codes = [maintaining_source_of_truth, end_to_end, interoperability, trustworthiness, output_port, interface_decision]
add_links({s29: s29_codes}, role_name="contained_code")

s30 = CClass(source, "s30", values={
    "title": "Recipe for building your first Data Product in a Data Mesh",
    "url": "https://medium.com/google-cloud/recipe-for-building-your-first-data-product-in-a-data-mesh-78b52338ef59",
    "archive url": "https://bit.ly/data-as-a-product-s30",
    "tiny url": "tinyurl.com/data-as-a-product-s30",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s30_codes = [query_catalogue, infrastructure_as_code, ci_cd_process, start_from_scratch, orchestration_decision, api_invocation,
             templated_data_pipeline, pub_sub, sql_layer, unified_batch_stream, containerisation, deploy_decision, data_product_self_serve_management_decision,
             rest_apis, orchestration, data_onboarding, single_container_design, data_catalogue, end_to_end, entry_barrier,
             centrally_manage_monitor_govern_data, data_product_layer_decision, function_as_a_service, batch_proccessing]
add_links({s30: s30_codes}, role_name="contained_code")

s31 = CClass(source, "s31", values={
    "title": "Build a data mesh on Google Cloud with Dataplex, now generally available",
    "url": "https://cloud.google.com/blog/products/data-analytics/build-a-data-mesh-on-google-cloud-with-dataplex-now-generally-available",
    "archive url": "https://bit.ly/data-as-a-product-s31",
    "tiny url": "tinyurl.com/data-as-a-product-s31",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s31_codes = [centrally_manage_monitor_govern_data, agility, manual_toil, security, orchestration_decision, non_functional,
             quality, discoverability, data_catalogue, central_data_product_catalogue, sql_layer, start_from_scratch,
             immutable_change_audit_log, request_access, data_product_layer_decision, data_product_self_serve_management_decision,
             data_search, data_enrichment, observability, autonomous, function_as_a_service, deploy_decision, metadata_lake, metastore, clear_ownership]
add_links({s31: s31_codes}, role_name="contained_code")

s32 = CClass(source, "s32", values={
    "title": "Build a modern, distributed Data Mesh with Google Cloud",
    "url": "https://services.google.com/fh/files/misc/build-a-modern-distributed-datamesh-with-google-cloud-whitepaper.pdf",
    "archive url": "https://bit.ly/data-as-a-product-s32",
    "tiny url": "tinyurl.com/data-as-a-product-s32",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s32_codes = [internal_storages, data_marketplace, discoverability, start_from_scratch, orchestration_decision, function_as_a_service,
             query_catalogue, rest_apis, service_locator, central_data_product_catalogue, immutable_change_audit_log, data_storage_infrastructure,
             data_catalogue, sql_layer, data_product_layer_decision, data_product_self_serve_management_decision, batch_proccessing, clear_ownership,
             triggering, request_access, quality_monitoring, deploy_decision, non_functional, containerisation, api_invocation,
             unified_batch_stream, container_orchestration_system, pub_sub, single_container_design, accessible, standardised_transformation, understandability]
add_links({s32: s32_codes}, role_name="contained_code")

s33 = CClass(source, "s33", values={
    "title": "Data as a Product: Make It Real with Event-Driven, Serverless Data Pipelines",
    "url": "https://www.fst.network/post/data-product",
    "archive url": "https://bit.ly/data-as-a-product-s33",
    "tiny url": "tinyurl.com/data-as-a-product-s33",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s33_codes = [rest_apis, single_container_design, triggering, data_product_layer_decision, start_from_scratch, orchestration_decision, containerisation, deploy_decision, api_invocation,
             event_streaming, shared_storage, internal_storages, time_to_market, infrastructure_as_code, data_product_self_serve_management_decision, function_as_a_service,
             output_port, clear_ownership, data_storage_infrastructure, interface_decision ]
add_links({s33: s33_codes}, role_name="contained_code")

s34 = CClass(source, "s34", values={
    "title": "#2 Explain Data Product in 8 Minutes with practical examples",
    "url": "dataproductbusiness.com/post/explain-data-product-in-8-minutes-with-practical-examples",
    "archive url": "https://bit.ly/data-as-a-product-s34",
    "tiny url": "tinyurl.com/data-as-a-product-s34",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s34_codes = [rest_apis, automated_decision_making_model_as_data_product, data_product_type_decision, data_product_self_serve_management_decision,
             decision_support_model_as_data_product, derived_data_as_data_product, raw_data_as_data_product, event_streaming, api_invocation,
             versioning, triggering, versioning_force]
add_links({s34: s34_codes}, role_name="contained_code")

s35 = CClass(source, "s35", values={
    "title": "Develop Your Data as a Product",
    "url": "https://towardsdatascience.com/develop-your-data-as-a-product-f9ba268c4e20",
    "archive url": "https://bit.ly/data-as-a-product-s35",
    "tiny url": "tinyurl.com/data-as-a-product-s35",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s35_codes = [ci_cd_process, immutable_change_audit_log, quality_monitoring, versioning, triggering, orchestration_decision, versioning_force,
              container_orchestration_system, run_tests, quality, data_product_layer_decision, start_from_scratch, deploy_decision, function_as_a_service]
add_links({s35: s35_codes}, role_name="contained_code")

s36 = CClass(source, "s36", values={
    "title": "Data mesh: A perspective on using Azure Synapse Analytics to build data products",
    "url": "https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/data-mesh-a-perspective-on-using-azure-synapse-analytics-to/ba-p/3644657",
    "archive url": "https://bit.ly/data-as-a-product-s36",
    "tiny url": "tinyurl.com/data-as-a-product-s36",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s36_codes = [sql_layer, quality_monitoring, internal_storages, data_product_layer_decision, function_as_a_service,
             immutable_change_audit_log, rest_apis, unified_batch_stream, non_functional, api_invocation, versioning_force,
             request_access, role_based_access_control, versioning, data_product_self_serve_management_decision, data_storage_infrastructure,
             attribute_based_access_control, multi_tenancy_model, single_subscription_single_workspace_dedicated_artifacts_per_domain,
             single_subscription_multiple_workspaces, event_streaming, encryption, deploy_decision, input_port, output_port, batch_proccessing,
             shared_storage, clear_ownership, interface_decision]
add_links({s36: s36_codes}, role_name="contained_code")

s37 = CClass(source, "s37", values={
    "title": "Describe and organize data products and resources in a data mesh",
    "url": "https://cloud.google.com/architecture/describe-organize-data-products-resources-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s37",
    "tiny url": "tinyurl.com/data-as-a-product-s37",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s37_codes = [data_catalogue, rest_apis, pub_sub, data_product_layer_decision, data_product_self_serve_management_decision, api_invocation,
             sql_layer, templated_data_pipeline, grouping, start_from_scratch, orchestration_decision, output_port, metadata_lake, metastore,
             clear_ownership, interface_decision]
add_links({s37: s37_codes}, role_name="contained_code")

s38 = CClass(source, "s38", values={
    "title": "Build data products in a data mesh",
    "url": "https://cloud.google.com/architecture/build-data-products-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s38",
    "tiny url": "tinyurl.com/data-as-a-product-s38",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s38_codes = [rest_apis, sql_layer, event_streaming, versioning, data_product_layer_decision, orchestration_decision, versioning_force,
             request_access, pub_sub, triggering, change_data_capture, start_from_scratch, non_functional, api_invocation, deploy_decision,
             separate_subscriptions_separate_workspace_per_domain, data_product_self_serve_management_decision, source_aligned_data_product, consumer_aligned_data_product,
             metadata_lake, metastore, batch_proccessing, shared_storage, data_storage_infrastructure,  data_product_type_decision,
             dataset_versioning, cqrs, filtering, migration]
add_links({s38: s38_codes}, role_name="contained_code")

s39 = CClass(source, "s39", values={
    "title": "Discover and consume data products in a data mesh",
    "url": "https://cloud.google.com/architecture/discover-consume-data-products-data-mesh",
    "archive url": "https://bit.ly/data-as-a-product-s39",
    "tiny url": "tinyurl.com/data-as-a-product-s39",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s39_codes = [central_data_product_catalogue, sql_layer, rest_apis, migration, non_functional, api_invocation,
             pub_sub, orchestration_decision, deploy_decision, data_product_self_serve_management_decision, batch_proccessing,
             unified_batch_stream, container_orchestration_system, cqrs, discoverability, accessible, data_search, start_from_scratch]
add_links({s39: s39_codes}, role_name="contained_code")

s40 = CClass(source, "s40", values={
    "title": "How to think of Data as a Product",
    "url": "https://www.ellie.ai/blogs/how-to-think-of-data-as-a-product",
    "archive url": "https://bit.ly/data-as-a-product-s40",
    "tiny url": "tinyurl.com/data-as-a-product-s40",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s40_codes = [feature_layer, central_data_product_catalogue, rest_apis, data_product_layer_decision, api_invocation, input_port, output_port, shared_storage, data_storage_infrastructure,
             start_from_scratch, orchestration_decision, data_product_self_serve_management_decision, non_functional, interface_decision, deploy_decision]
add_links({s40: s40_codes}, role_name="contained_code")

s41 = CClass(source, "s41", values={
    "title": "What is Data as a Product, and What to Consider Implementing It?",
    "url": "https://mastheadata.com/what-is-data-as-a-product-and-what-to-consider-implementing-it/",
    "archive url": "https://bit.ly/data-as-a-product-s41",
    "tiny url": "tinyurl.com/data-as-a-product-s41",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s41_codes = [unified_batch_stream, event_streaming, pub_sub, rest_apis, cqrs, migration, schema_manager, start_from_scratch, api_invocation,
             snapshots_ETL, fast_data_propagation, handle_large_data_volumes, orchestration_decision, data_product_self_serve_management_decision,
             addressible, control_over_data_schema, output_port, batch_proccessing, clear_ownership, interface_decision]
add_links({s41: s41_codes}, role_name="contained_code")

s42 = CClass(source, "s42", values={
    "title": "How Dell IT is Driving Data-as-a-product",
    "url": "https://www.dell.com/en-us/blog/how-dell-it-is-driving-data-as-a-product/",
    "archive url": "https://bit.ly/data-as-a-product-s42",
    "tiny url": "tinyurl.com/data-as-a-product-s42",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s42_codes = [data_marketplace, start_from_scratch, orchestration_decision, central_data_product_catalogue, discoverability, data_product_self_serve_management_decision,
             source_aligned_data_product, aggregations, consumer_aligned_data_product, metadata_lake, metastore, clear_ownership,  data_product_type_decision, data_product_layer_decision]
add_links({s42: s42_codes}, role_name="contained_code")

s43 = CClass(source, "s43", values={
    "title": "Treating data as a product at Adevinta",
    "url": "https://medium.com/adevinta-tech-blog/treating-data-as-a-product-at-adevinta-c1dce5d394c5",
    "archive url": "https://bit.ly/data-as-a-product-s43",
    "tiny url": "tinyurl.com/data-as-a-product-s43",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s43_codes = [single_subscription_dedicated_workpasce_per_domain, raw_data_as_data_product,
             data_product_type_decision, data_marts, start_from_scratch, deploy_decision, migration,
             sql_layer, data_catalogue, container_orchestration_system, data_product_layer_decision, orchestration_decision,
             templated_data_pipeline, data_marketplace, cqrs, query_catalogue, data_product_self_serve_management_decision,
             request_access, unified_batch_stream, understandability, infrastructure_as_code, non_functional,
             aggregations, metadata_lake, metastore, batch_proccessing, clear_ownership]
add_links({s43: s43_codes}, role_name="contained_code")

s44 = CClass(source, "s44", values={
    "title": "An Operating Model for Data Products",
    "url": "https://towardsdatascience.com/an-operating-model-for-data-products-fba6b268f698",
    "archive url": "https://bit.ly/data-as-a-product-s44",
    "tiny url": "tinyurl.com/data-as-a-product-s44",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s44_codes = [event_streaming, mdm, migration, unified_batch_stream, orchestration_decision, data_product_self_serve_management_decision, master_database,
             source_aligned_data_product, consumer_aligned_data_product, batch_proccessing, clear_ownership,  data_product_type_decision]
add_links({s44: s44_codes}, role_name="contained_code")

s45 = CClass(source, "s45", values={
    "title": "The Anatomy of a Data Product",
    "url": "https://towardsdatascience.com/the-anatomy-of-a-data-product-d3140f068311",
    "archive url": "https://bit.ly/data-as-a-product-s45",
    "tiny url": "tinyurl.com/data-as-a-product-s45",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s45_codes = [zero_trust_architecture, rest_apis, change_data_capture, start_from_scratch, api_invocation,
             core_datasets, domain_datasets, orchestration_decision, data_product_layer_decision, containerisation,
             event_streaming, immutable_change_audit_log, register_datasets, deploy_decision, migration,
             single_container_design, data_marketplace, container_orchestration_system, time_bounded_backwards_compatibility, versioning, versioning_force,
             triggering, central_data_product_catalogue, interoperability, discoverability, data_product_self_serve_management_decision,
             metadata_lake, metastore, clear_ownership]
add_links({s45: s45_codes}, role_name="contained_code")

s46 = CClass(source, "s46", values={
    "title": "Topology of a Data Product Team",
    "url": "https://towardsdatascience.com/topology-of-a-data-product-team-75dc5471fccf",
    "archive url": "https://bit.ly/data-as-a-product-s46",
    "tiny url": "tinyurl.com/data-as-a-product-s46",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s46_codes = [central_data_product_catalogue, virtualisation, sql_layer, data_product_self_serve_management_decision,
             clear_ownership]
add_links({s46: s46_codes}, role_name="contained_code")

s47 = CClass(source, "s47", values={
    "title": "Data Mesh / Data Product Security Pattern",
    "url": "https://towardsdatascience.com/data-mesh-data-product-security-pattern-c5b93a27e82e",
    "archive url": "https://bit.ly/data-as-a-product-s47",
    "tiny url": "tinyurl.com/data-as-a-product-s47",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s47_codes = [central_data_product_catalogue, schema_manager, row_based_access_control, stream_access_control, run_time_environment_access_control,
            api_access_control, role_based_access_control, encryption, deploy_decision, non_functional, containerisation, orchestration_decision,
             attribute_based_access_control, immutable_change_audit_log, request_access, container_orchestration_system, single_container_design,
             understandability, data_catalogue, data_product_layer_decision, data_product_self_serve_management_decision,
             VMs, clear_ownership, cloud_acceleration, multi_cloud_deployment, hybrid_deployment]
add_links({s47: s47_codes}, role_name="contained_code")

s48 = CClass(source, "s48", values={
    "title": "Data Mesh Patterns: Enterprise Data Product Catalog",
    "url": "https://towardsdatascience.com/data-mesh-pattern-enterprise-data-product-catalog-ba4bf072d7c3",
    "archive url": "https://bit.ly/data-as-a-product-s48",
    "tiny url": "tinyurl.com/data-as-a-product-s48",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s48_codes = [central_data_product_catalogue, data_catalogue, immutable_change_audit_log, migration,
             schema_manager, change_data_capture, event_streaming, incremental_sync, master_database,
             sql_layer, mdm, centralization, understandability, data_lineage, data_product_self_serve_management_decision,
             reproducibility, verifiability, duplication, orchestration_decision, data_product_layer_decision
             ]
add_links({s48: s48_codes}, role_name="contained_code")

s49 = CClass(source, "s49", values={
    "title": "Applying Data Mesh principles to an IoT data architecture",
    "url": "https://www.acagroup.be/en/blog/applying-data-mesh-principles-to-an-iot-data-architecture/",
    "archive url": "https://bit.ly/data-as-a-product-s49",
    "tiny url": "tinyurl.com/data-as-a-product-s49",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s49_codes = [rest_apis, internal_storages, sql_layer, discovery_port, virtualisation, control_port, start_from_scratch, orchestration_decision, api_invocation,
             discoverability, understandability, quality_monitoring, central_data_product_catalogue, infrastructure_as_code, unified_batch_stream,  data_product_type_decision,
             pub_sub, data_product_layer_decision, data_product_self_serve_management_decision, control_plane, interface_decision, data_storage_infrastructure,
             source_aligned_data_product, aggregations, consumer_aligned_data_product, input_port, output_port, metadata_lake, metastore, deploy_decision,
             batch_proccessing, clear_ownership]
add_links({s49: s49_codes}, role_name="contained_code")

s50 = CClass(source, "s50", values={
    "title": "The Fundamentals of Building Better Data Products",
    "url": "https://www.mindtheproduct.com/fundamentals-building-better-data-products/#:~:text=As%20I%20see%20it%20there,products%2C%20and%20data%20as%20insight",
    "archive url": "https://bit.ly/data-as-a-product-s50",
    "tiny url": "tinyurl.com/data-as-a-product-s50",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s50_codes = [time_bounded_backwards_compatibility]
add_links({s50: s50_codes}, role_name="contained_code")

s51 = CClass(source, "s51", values={
    "title": "The Unfortunate Reality about Data Pipelines",
    "url": "https://thenewstack.io/the-unfortunate-reality-about-data-pipelines/",
    "archive url": "https://bit.ly/data-as-a-product-s51",
    "tiny url": "tinyurl.com/data-as-a-product-s51",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s51_codes = [time_bounded_backwards_compatibility, event_streaming, data_product_self_serve_management_decision, versioning_force,
             versioning, ci_cd_process, real_time_data_access, trustworthiness, batch_proccessing, clear_ownership]
add_links({s51: s51_codes}, role_name="contained_code")

s52 = CClass(source, "s52", values={
    "title": "The next generation of Data Platforms is the Data Mesh",
    "url": "https://medium.com/paypal-tech/the-next-generation-of-data-platforms-is-the-data-mesh-b7df4b825522",
    "archive url": "https://bit.ly/data-as-a-product-s52",
    "tiny url": "tinyurl.com/data-as-a-product-s52",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s52_codes = [data_marts, control_port, discovery_port, data_onboarding, observation_plane, interface_decision, api_invocation,  data_product_type_decision,
             observation_port, rest_apis, data_product_self_serve_management_decision, control_plane, data_product_layer_decision,
             event_streaming, request_access, versioning, versioning_force, accessible, non_functional, source_aligned_data_product, consumer_aligned_data_product,
             aggregations, input_port, output_port, metadata_lake, metastore, clear_ownership]
add_links({s52: s52_codes}, role_name="contained_code")


s53 = CClass(source, "s53", values={
    "title": "Data Mesh Patterns: Change Data Capture",
    "url": "https://towardsdatascience.com/data-mesh-pattern-deep-dive-change-data-capture-eb3090178c34",
    "archive url": "https://bit.ly/data-as-a-product-s53",
    "tiny url": "tinyurl.com/data-as-a-product-s53",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s53_codes = [change_data_capture, event_streaming, central_data_product_catalogue, data_product_self_serve_management_decision,
             immutable_change_audit_log, accessible, pub_sub, data_catalogue, real_time_data_access,
             understandability, data_product_layer_decision, batch_proccessing, clear_ownership]
add_links({s53: s53_codes}, role_name="contained_code")

s54 = CClass(source, "s54", values={
    "title": "Data Mesh Patterns: Immutable Change / Audit Log",
    "url": "https://towardsdatascience.com/data-mesh-patterns-immutable-change-audit-log-aec93da33648",
    "archive url": "https://bit.ly/data-as-a-product-s54",
    "tiny url": "tinyurl.com/data-as-a-product-s54",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s54_codes = [immutable_change_audit_log, change_data_capture, central_data_product_catalogue, schema_manager,
            reproducibility, traceability, verifiability, data_product_self_serve_management_decision, data_lineage, immutability, data_product_layer_decision, ]
add_links({s54: s54_codes}, role_name="contained_code")

s55 = CClass(source, "s55", values={
    "title": "Data Mesh Architecture Patterns",
    "url": "https://towardsdatascience.com/data-mesh-architecture-patterns-98cc1014f251",
    "archive url": "https://bit.ly/data-as-a-product-s55",
    "tiny url": "tinyurl.com/data-as-a-product-s55",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s55_codes = [change_data_capture, event_streaming, central_data_product_catalogue, data_catalogue, immutable_change_audit_log, real_time_data_access, autonomous, accessible, discoverability,
             understandability, observability, reproducibility, traceability, data_lineage, governance , data_product_layer_decision, data_product_self_serve_management_decision,
             clear_ownership]
add_links({s55: s55_codes}, role_name="contained_code")

s56 = CClass(source, "s56", values={
    "title": "Data Mesh Solution and Accelerator Patterns",
    "url": "https://towardsdatascience.com/data-mesh-solution-and-accelerator-patterns-acffbf6e350",
    "archive url": "https://bit.ly/data-as-a-product-s56",
    "tiny url": "tinyurl.com/data-as-a-product-s56",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s56_codes = [change_data_capture, event_streaming, immutable_change_audit_log, real_time_data_access, zero_trust_architecture, mdm, discoverability, data_product_layer_decision, orchestration_decision,
             understandability, data_lineage, accessible, observability, role_based_access_control, attribute_based_access_control, cqrs, non_functional, master_database,
             strangler_fig_pattern, data_product_self_serve_management_decision, migration, clear_ownership]
add_links({s56: s56_codes}, role_name="contained_code")

s57 = CClass(source, "s57", values={
    "title": "Data mesh and monoliths integration patterns",
    "url": "https://medium.com/agile-lab-engineering/data-mesh-and-monoliths-integration-patterns-78ecf9f4daa1",
    "archive url": "https://bit.ly/data-as-a-product-s57",
    "tiny url": "tinyurl.com/data-as-a-product-s57",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s57_codes = [strangler_fig_pattern, migration, schema_manager, orchestration_decision, data_product_layer_decision, source_aligned_data_product, consumer_aligned_data_product, input_port, output_port,
             batch_proccessing, clear_ownership,  data_product_type_decision, interface_decision,
             time_bounded_backwards_compatibility, immutable_change_audit_log, event_streaming, data_product_self_serve_management_decision]
add_links({s57: s57_codes}, role_name="contained_code")

p1 = CClass(source, "p1", values={
    "title": "Interview Expert A",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p1",
    "tiny url": "https://tinyurl.com/data-as-a-product-p1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p1_codes = [metastore, raw_data_as_data_product, internal_storages, infrastructure_to_manage, legacy_modernization, aggregations, consumer_aligned_data_product,
            metadata_lake, batch_proccessing, shared_storage, VMs, clear_ownership, self_serve,
            stateless, master_database,
            central_data_product_catalogue, data_modeling_tool, data_lineage, immutable_change_audit_log, event_streaming,
            real_time_data_access, rest_apis, sql_layer, mdm, governance, control_port, reference_data_management, reference_database,
            security, end_to_end_consistency, overarching_management_layer, api_invocation, understandability,
            data_onboarding, quality, control_plane, infrastructure_provisioning, data_storage_infrastructure, orchestration_component, data_catalogue,
            strangler_fig_pattern, continuity, start_from_scratch, single_container_design,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
             deploy_decision, orchestration_decision, interface_decision, shared_kafka_environment, query_catalogue]
add_links({p1: p1_codes}, role_name="contained_code")

p2 = CClass(source, "p2", values={
    "title": "Interview Expert A",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p2",
    "tiny url": "https://tinyurl.com/data-as-a-product-p2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p2_codes = [strangler_fig_pattern, mdm, start_from_scratch, derived_data_as_data_product, overarching_management_layer,
            event_streaming, file_based_ingestion_pattern, immutable_change_audit_log, change_data_capture, orchestration_component,
            security, quality_monitoring, quality, control_port, observation_port, infrastructure_provisioning, ci_cd_process,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
            deploy_decision, orchestration_decision, interface_decision, cloud_acceleration, legacy_modernization, input_port, output_port, hybrid_deployment,
            metadata_lake, metastore, batch_proccessing, master_database, reference_database, latency, clear_ownership, infrastructure_to_manage]
add_links({p2: p2_codes}, role_name="contained_code")

p3 = CClass(source, "p3", values={
    "title": "Interview Expert C",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p3",
    "tiny url": "https://tinyurl.com/data-as-a-product-p3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p3_codes = [raw_data_as_data_product, discovery_port, discoverability, accessible, data_catalogue, strangler_fig_pattern,
            cqrs, start_from_scratch, stale, central_data_product_catalogue, real_time_data_access,
            shared_storage, query_catalogue, event_streaming, api_invocation,
            data_lineage, schema_manager, control_plane, observation_plane, change_data_capture, immutable_change_audit_log,
            data_onboarding, observation_port, containerisation, container_orchestration_system, VMs, zero_trust_runtime_environment,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
            deploy_decision, orchestration_decision, interface_decision, legacy_modernization, aggregations, input_port, output_port,
            batch_proccessing, master_database, reference_database, data_storage_infrastructure, clear_ownership, self_serve,
            end_to_end_consistency]
add_links({p3: p3_codes}, role_name="contained_code")

p4 = CClass(source, "p4", values={
    "title": "Interview Expert D",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p4",
    "tiny url": "https://tinyurl.com/data-as-a-product-p4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p4_codes = [raw_data_as_data_product, derived_data_as_data_product, quality_monitoring, internal_storages,
            observation_port, control_port, discovery_port, input_port, output_port, metastore,
            data_catalogue, immutable_change_audit_log, latency, clear_ownership, data_storage_infrastructure,
            containerisation, container_orchestration_system, VMs, zero_trust_runtime_environment,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
            deploy_decision, orchestration_decision, interface_decision]
add_links({p4: p4_codes}, role_name="contained_code")


p5 = CClass(source, "p5", values={
    "title": "Interview Expert E",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p5",
    "tiny url": "https://tinyurl.com/data-as-a-product-p5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p5_codes = [raw_data_as_data_product, algorithms_as_data_product, low_level_events,
            strangler_fig_pattern, mdm, event_streaming, table, blob_storage, schema_manager, non_functional,
            data_catalogue, metastore, container_orchestration_system,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
            deploy_decision, orchestration_decision, interface_decision, source_aligned_data_product, aggregations, consumer_aligned_data_product,
            master_database, data_storage_infrastructure, clear_ownership, stale, self_serve, end_to_end_consistency]
add_links({p5: p5_codes}, role_name="contained_code")

p6 = CClass(source, "p6", values={
    "title": "Interview Expert F",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p6",
    "tiny url": "https://tinyurl.com/data-as-a-product-p6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p6_codes = [raw_data_as_data_product, strangler_fig_pattern, zero_trust_architecture, schema_manager, event_streaming,
            data_catalogue, overarching_management_layer, observation_port, control_port, data_storage_infrastructure,
            containerisation, input_port, output_port, metadata_lake, metastore, batch_proccessing, shared_storage, master_database, multi_cloud_deployment,
            clear_ownership, self_serve, continuity,
            data_product_layer_decision, data_product_self_serve_management_decision, data_product_type_decision,
            deploy_decision, orchestration_decision, interface_decision]
add_links({p6: p6_codes}, role_name="contained_code")

p7 = CClass(source, "p7", values={
    "title": "Interview Expert G",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p7",
    "tiny url": "https://tinyurl.com/data-as-a-product-p7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p7_codes = [raw_data_as_data_product, algorithms_as_data_product, strangler_fig_pattern, interface_decision, data_storage_infrastructure,
            mdm, query_catalogue, event_streaming, data_marts, data_product_layer_decision, data_product_self_serve_management_decision,
            internal_storages, schema_manager, immutable_change_audit_log, data_catalogue, output_port, master_database, deploy_decision]
add_links({p7: p7_codes}, role_name="contained_code")

p8 = CClass(source, "p8", values={
    "title": "Interview Expert G",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p8",
    "tiny url": "https://tinyurl.com/data-as-a-product-p8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p8_codes = [algorithms_as_data_product, raw_data_as_data_product, derived_data_as_data_product, data_product_layer_decision, interface_decision,
            mdm, request_access, zero_trust_architecture, strangler_fig_pattern, data_catalogue, data_product_self_serve_management_decision,
            central_data_product_catalogue, schema_manager, discovery_port, observation_port, deploy_decision, cloud_acceleration, master_database, hybrid_deployment,
            source_aligned_data_product, aggregations, consumer_aligned_data_product, input_port, output_port, metadata_lake, metastore, data_storage_infrastructure,
            clear_ownership, orchestration_decision,  data_product_type_decision]
add_links({p8: p8_codes}, role_name="contained_code")

p9 = CClass(source, "p9", values={
    "title": "Interview Expert I",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p9",
    "tiny url": "https://tinyurl.com/data-as-a-product-p9",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p9_codes = [hybrid_products, automated_decision_making_model_as_data_product, data_product_type_decision,
            raw_data_as_data_product, strangler_fig_pattern, zero_trust_architecture, cqrs, shared_storage,
            data_product_self_serve_management_decision, central_data_product_catalogue, api_invocation,
            batch_proccessing, overarching_management_layer, interface_decision, data_catalogue, data_product_layer_decision,
            discovery_port]
add_links({p9: p9_codes}, role_name="contained_code")


p10 = CClass(source, "p10", values={
    "title": "Interview Expert K",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p10",
    "tiny url": "https://tinyurl.com/data-as-a-product-p10",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p10_codes = [raw_data_as_data_product, hybrid_products, mdm, strangler_fig_pattern, schema_manager,
             data_product_type_decision, data_product_self_serve_management_decision, change_data_capture,
             event_streaming, api_invocation, containerisation, deploy_decision, data_product_layer_decision]
add_links({p10: p10_codes}, role_name="contained_code")

p11 = CClass(source, "p11", values={
    "title": "Interview Expert J",
    "url": "https://github.com/TomEijk/Data_as_a_Product_GLR/tree/master/python/data_as_a_product_codeablemodels/field_notes_open_coding_axial_coding",
    "archive url": "https://bit.ly/data-as-a-product-p11",
    "tiny url": "https://tinyurl.com/data-as-a-product-p11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
p11_codes = [raw_data_as_data_product, data_product_type_decision, derived_data_as_data_product, mdm, strangler_fig_pattern,
             control_port, interface_decision, input_port, observation_port, input_port, output_port, containerisation, multi_cloud_deployment,
             VMs, function_as_a_service, deploy_decision]


















