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
s4_codes = [capture_data_change, event_streaming, virtualisation, data_integration_service,
            incremental_sync, data_product_governance, keep_track_metadata_decision, communicaton_decision,
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
            rest_apis, sql_layer, security_decision, data_access_decision, domain_datasets, core_datasets, data_integration_service, communicaton_decision,
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





























