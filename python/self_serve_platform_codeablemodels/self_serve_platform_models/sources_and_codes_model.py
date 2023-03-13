from python.self_serve_platform_codeablemodels.self_serve_platform_models.self_serve_platform_model import *
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
    "title": "Design considerations for self-serve data platforms",
    "url": "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/self-serve-data-platforms",
    "archive url": "https://bit.ly/self-serve-platform-s1",
    "tiny url": "https://bit.ly/self-serve-platform-s1",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})

s1_codes = [api_catalog, data_catalog, single_data_landing_zone, multiple_data_landing_zones, cdc,
            hub_generic_special_data_landing_zones, data_lineage, mdm, ml_services, data_lake_services,
            complexity, distinguish, domain_agnostic, regional_legal, control_over_data, time_travel,
            redeliveries, scalability, large_scale_enterprise, functional_and_regionally_aligned_data_landing_zones,
            VNetPeering, private_endpoints, flexibility, research_groups]
add_links({s1: s1_codes}, role_name="contained_code")

s2 = CClass(source, "s2", values={
    "title": "Governance: Your Data Mesh Self-Service Depends on It",
    "url": "https://thenewstack.io/governance-your-data-mesh-self-service-depends-on-it/",
    "archive url": "https://tinyurl.com/self-serve-plaform-s2",
    "tiny url": "https://tinyurl.com/self-serve-plaform-s2",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s2_codes = [event_streaming_backbone, register_derived_data_as_data_product, lambda_architecture,
            kappa_architecture]
add_links({s2: s2_codes}, role_name="contained_code")

s3 = CClass(source, "s3", values={
    "title": "Data Mesh From an Engineering Perspective",
    "url": "https://www.datamesh-architecture.com/",
    "archive url": "https://tinyurl.com/self-serve-plaform-s3",
    "tiny url": "https://tinyurl.com/self-serve-plaform-s3",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s3_codes = [data_source_ingestion, distributed_file_storage, storage_function, access_control_management, data_catalog, visualization_function,
            manage_read_write_permissions, searchability, discoverability, centrally_govern, policy_automation, query_engine]
add_links({s3: s3_codes}, role_name="contained_code")

s4 = CClass(source, "s4", values={
    "title": "Your Data Mesh Can’t Be Self-Serve Just for Developers",
    "url": "https://towardsdatascience.com/your-data-mesh-cant-be-self-serve-just-for-developers-34bdeddc257e",
    "archive url": "https://bit.ly/self-serve-platform-s4",
    "tiny url": "https://tinyurl.com/self-serve-platform-s4",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s4_codes = [managed_compute_infrastructure, abstact_away_details, elastic, adapt_to_changing_volumes, data_source_ingestion,
            no_code_transformation, dependable_pipeline_management, automated_issue_detection, alerting, resolution,
            configure_depency, configure_scheduling]
add_links({s4: s4_codes}, role_name="contained_code")

s5 = CClass(source, "s5", values={
    "title": "Data Mesh Principles and Logical Architecture",
    "url": "https://martinfowler.com/articles/data-mesh-principles.html#LogicalArchitectureAMulti-planeDataPlatform",
    "archive url": "https://bit.ly/self-serve-platform-s5",
    "tiny url": "https://tinyurl.com/self-serve-platform-s5",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s5_codes = [distributed_file_storage, storage_function, query_engine, data_transformation_orchestration,
            access_control_management, manage_security_policies_of_dps, manage_emergent_graphs_of_dps,
            discovery_and_explore_dps, declaratively_create_dp, read_dp, version_dp, secure_dp, build_deploy_monitor_dp]
add_links({s5: s5_codes}, role_name="contained_code")

s6 = CClass(source, "s6", values={
    "title": "Data Mesh — A Self-service Infrastructure at DPG Media with Snowflake",
    "url": "https://levelup.gitconnected.com/data-mesh-a-self-service-infrastructure-at-dpg-media-with-snowflake-566f108a98db",
    "archive url": "https://bit.ly/self-serve-platform-s6",
    "tiny url": "https://tinyurl.com/self-serve-platform-s6",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s6_codes = [separating_compute_from_compute, separating_storage_and_compute, scalability, autonomous,
            restore_data_without_backups, in_place_consumption, scale_across_platforms_and_regions]
add_links({s6: s6_codes}, role_name="contained_code")

s7 = CClass(source, "s7", values={
    "title": "Domain centric architecture : Data driven business process powered by Snowflake Data Sharing",
    "url": "https://businesstechnologiesjourney.blogspot.com/2020/12/domain-centric-architecture-data-driven.html",
    "archive url": "https://bit.ly/self-serve-platform-s7",
    "tiny url": "https://tinyurl.com/self-serve-platform-s7",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s7_codes = [in_place_consumption, storage_function, data_movement, global_governance]
add_links({s7: s7_codes}, role_name="contained_code")

s8 = CClass(source, "s8", values={
    "title": "How JPMorgan Chase built a data mesh architecture to drive significant value to enhance their enterprise data platform",
    "url": "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s8",
    "tiny url": "https://tinyurl.com/self-serve-platform-s8",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s8_codes = [in_place_consumption, data_movement, costs, discrepancies, up_to_date, access_control]
add_links({s8: s8_codes}, role_name="contained_code")

s9 = CClass(source, "s9", values={
    "title": "How JPMorgan Chase built a data mesh architecture to drive significant value to enhance their enterprise data platform",
    "url": "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s9",
    "tiny url": "https://tinyurl.com/self-serve-platform-s9",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s9_codes = [in_place_consumption, data_movement, data_catalog, manage_read_write_permissions, autonomous,
            delegated_ownership, global_governance, access_control_management, federated_analytics, compatible_metadata,
            runtime_metadata, metadata_management]
add_links({s9: s9_codes}, role_name="contained_code")

s10 = CClass(source, "s10", values={
    "title": "Aligning Business Intelligence and AI/ML with a Data Mesh Platform on AWS",
    "url": "https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s10",
    "tiny url": "https://tinyurl.com/self-serve-platform-s10",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s10_codes = [data_catalog, metadata_management]
add_links({s10: s10_codes}, role_name="contained_code")

s11 = CClass(source, "s11", values={
    "title": "Data mesh: a new paradigm for data management",
    "url": "https://siliconangle.com/2021/10/27/data-mesh-new-paradigm-data-management/",
    "archive url": "https://bit.ly/self-serve-platform-s11",
    "tiny url": "https://tinyurl.com/self-serve-platform-s11",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s11_codes = [access_control_management, build_deploy_monitor_dp, declaratively_create_dp, distributed_file_storage, document_dp, knowledge_graph, searchability, managed_compute_infrastructure,
             data_transformation_orchestration, policy_automation, query_engine, read_dp, central_search_function, set_privacy_dp, VNetPeering]
add_links({s11: s11_codes}, role_name="contained_code")

s12 = CClass(source, "s12", values={
    "title": "Untangle your mess and knit your mesh: A cross-company point of view",
    "url": "https://www2.deloitte.com/content/dam/Deloitte/be/Documents/technology/consulting_untangle_your_mess_and_knit_your_mesh_deloitte_be_report_en.pdf",
    "archive url": "https://bit.ly/self-serve-platform-s12",
    "tiny url": "https://tinyurl.com/self-serve-platform-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s12_codes = [elastic_performance_engine, scalability, ad_hoc_exploration, bi_reporting, feature_engineering, interactive_applications, understandability,
             data_source_ingestion, unified_batch_stream_processing_service]
add_links({s12: s12_codes}, role_name="contained_code")

s12 = CClass(source, "s12", values={
    "title": "Untangle your mess and knit your mesh: A cross-company point of view",
    "url": "https://www2.deloitte.com/content/dam/Deloitte/be/Documents/technology/consulting_untangle_your_mess_and_knit_your_mesh_deloitte_be_report_en.pdf",
    "archive url": "https://bit.ly/self-serve-platform-s12",
    "tiny url": "https://tinyurl.com/self-serve-platform-s12",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s12_codes = [elastic_performance_engine, scalability, ad_hoc_exploration, bi_reporting, feature_engineering, interactive_applications, understandability,
             data_source_ingestion, unified_batch_stream_processing_service]
add_links({s12: s12_codes}, role_name="contained_code")

s13 = CClass(source, "s13", values={
    "title": "Self-Serve Data Platform",
    "url": "https://www.advancinganalytics.co.uk/blog/2021/8/5/data-mesh-deep-dive",
    "archive url": "https://bit.ly/self-serve-platform-s13",
    "tiny url": "https://tinyurl.com/self-serve-platform-s13",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s13_codes = [infrastructure_as_code, distributed_file_storage, query_engine, data_transformation_orchestration, access_control_management, build_deploy_monitor_dp,
             data_catalog, alerting, data_lineage, data_source_ingestion]
add_links({s13: s13_codes}, role_name="contained_code")

s14 = CClass(source, "s14", values={
    "title": "WELCOME TO THE BLOG & WEBSITE OF PAUL ANDREW",
    "url": "https://www.advancinganalytics.co.uk/blog/2021/8/5/data-mesh-deep-dive",
    "archive url": "https://bit.ly/self-serve-platform-s14",
    "tiny url": "https://tinyurl.com/self-serve-platform-s14",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s14_codes = [research_groups, sql_endpoint, log_management, VNetPeering, usability, software_as_a_service, data_catalog, knowledge_graph]
add_links({s14: s14_codes}, role_name="contained_code")

s15 = CClass(source, "s15", values={
    "title": "WELCOME TO THE BLOG & WEBSITE OF PAUL ANDREW",
    "url": "https://www.advancinganalytics.co.uk/blog/2021/8/5/data-mesh-deep-dive",
    "archive url": "https://bit.ly/self-serve-platform-s15",
    "tiny url": "https://tinyurl.com/self-serve-platform-s15",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s15_codes = [access_control_management, configure_scheduling, configure_depency, configure_thresholds, data_catalog, distributed_file_storage, build_deploy_monitor_dp]
add_links({s15: s15_codes}, role_name="contained_code")

s16 = CClass(source, "s16", values={
    "title": "Data Mesh and Starburst: Self-Service Data Infrastructure",
    "url": "https://www.starburst.io/blog/data-mesh-starburst-self-service-data-infrastructure/",
    "archive url": "https://bit.ly/self-serve-platform-s16",
    "tiny url": "https://tinyurl.com/self-serve-platform-s16",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s16_codes = [storage_function, managed_compute_infrastructure, federated_analytics, in_place_consumption, access_control_management, alerting, query_engine,
             build_deploy_monitor_dp, sql_endpoint,data_catalog, data_lineage]
add_links({s16: s16_codes}, role_name="contained_code")

s17 = CClass(source, "s17", values={
    "title": "Data Mesh and Starburst: Self-Service Data Infrastructure",
    "url": "https://cloud.google.com/architecture/design-self-service-data-platform-data-mesh",
    "archive url": "https://bit.ly/self-serve-platform-s17",
    "tiny url": "https://tinyurl.com/self-serve-platform-s17",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s17_codes = [build_deploy_monitor_dp, data_catalog, mdm, data_transformation_orchestration, policy_automation, dependable_pipeline_management, infrastructure_as_code,
             api_catalog, access_control_management, VNetPeering, manage_security_policies_of_dps, metadata_management, resource_deployment_process,
             inconsistencies_between_deployed_resources_and_declared_code_in_source_control, sql_endpoint, visualization_function, event_streaming_backbone, in_place_consumption, research_groups, uptime_checks,
             accurate_health_representation, alerting, reduce_work_data_product_team]
add_links({s17: s17_codes}, role_name="contained_code")

s18 = CClass(source, "s18", values={
    "title": "The Google Technology Landscape for a Self-Service Data Platform",
    "url": "https://www.linkedin.com/pulse/landscape-technologies-self-service-data-platform-sandeep/?trk=portfolio_article-card_title",
    "archive url": "https://bit.ly/self-serve-platform-s18",
    "tiny url": "https://tinyurl.com/self-serve-platform-s18",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s18_codes = [data_catalog, integration_service, event_streaming_backbone, visualization_function, build_deploy_monitor_dp, unified_batch_stream_processing_service, distributed_file_storage,
             data_transformation_orchestration, log_management, cost_management]
add_links({s18: s18_codes}, role_name="contained_code")

s19 = CClass(source, "s19", values={
    "title": "Turning Airflow into a full self service Data Platform",
    "url": "https://danielrcarletti.medium.com/turning-airflow-into-a-full-self-service-data-platform-b67eccdd3445",
    "archive url": "https://bit.ly/self-serve-platform-s19",
    "tiny url": "https://tinyurl.com/self-serve-platform-s19",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s19_codes = [infrastructure_as_code, easily_replicable]
add_links({s19: s19_codes}, role_name="contained_code")

s20 = CClass(source, "s20", values={
    "title": "Self Service Data Platform",
    "url": "https://dywhin.com/self-service-data-platform/",
    "archive url": "https://bit.ly/self-serve-platform-s20",
    "tiny url": "https://tinyurl.com/self-serve-platform-s20",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s20_codes = [integration_service, data_source_ingestion, visualization_function, infrastructure_as_code]
add_links({s20: s20_codes}, role_name="contained_code")

s21 = CClass(source, "s21", values={
    "title": "Self Service Data Platform",
    "url": "https://radiantadvisors.com/storage/uploads/2c152ae4b.pdf",
    "archive url": "https://bit.ly/self-serve-platform-s21",
    "tiny url": "https://tinyurl.com/self-serve-platform-s21",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s21_codes = [data_catalog, data_lineage, accuracy, speed, workflow_automation_engine]
add_links({s21: s21_codes}, role_name="contained_code")

s22 = CClass(source, "s22", values={
    "title": "Create A Road Map For A Real-Time, Agile, Self-Service Data Platform",
    "url": "https://silo.tips/download/res83321",
    "archive url": "https://bit.ly/self-serve-platform-s22",
    "tiny url": "https://tinyurl.com/self-serve-platform-s22",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s22_codes = [in_place_consumption, integration_service, unified_batch_stream_processing_service, data_source_ingestion, mdm, metadata_management]
add_links({s22: s22_codes}, role_name="contained_code")

s23 = CClass(source, "s23", values={
    "title": "Why zulily created a self-service marketing analytics platform with Tableau and Google BigQuery",
    "url": "https://www.tableau.com/blog/why-zulily-created-self-service-marketing-analytics-platform-tableau-and-google",
    "archive url": "https://bit.ly/self-serve-platform-s23",
    "tiny url": "https://tinyurl.com/self-serve-platform-s23",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s23_codes = [sql_endpoint, mdm]
add_links({s23: s23_codes}, role_name="contained_code")

s24 = CClass(source, "s24", values={
    "title": "How we scale our data platform efficiently and reliably",
    "url": "https://building.nubank.com.br/distributing-the-data-team-to-boost-innovation-reliably/",
    "archive url": "https://bit.ly/self-serve-platform-s24",
    "tiny url": "https://tinyurl.com/self-serve-platform-s24",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s24_codes = [alerting, automated_issue_detection]
add_links({s24: s24_codes}, role_name="contained_code")

s25 = CClass(source, "s25", values={
    "title": "How does the banking industry build a self-service data platform?",
    "url": "https://www.mo4tech.com/how-does-the-banking-industry-build-a-self-service-data-platform.html",
    "archive url": "https://bit.ly/self-serve-platform-s25",
    "tiny url": "https://tinyurl.com/self-serve-platform-s25",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s25_codes = [sql_endpoint, avoids_information_island, integration_service, unified_batch_stream_processing_service]
add_links({s25: s25_codes}, role_name="contained_code")

s26 = CClass(source, "s26", values={
    "title": "How does the banking industry build a self-service data platform?",
    "url": "https://www.mo4tech.com/how-does-the-banking-industry-build-a-self-service-data-platform.html",
    "archive url": "https://bit.ly/self-serve-platform-s26",
    "tiny url": "https://tinyurl.com/self-serve-platform-s26",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s26_codes = [unified_batch_stream_processing_service, access_control_management, container_registry, distributed_file_storage, separating_storage_and_compute, VMs, data_transformation_orchestration]
add_links({s26: s26_codes}, role_name="contained_code")

s27 = CClass(source, "s27", values={
    "title": "How does the banking industry build a self-service data platform?",
    "url": "https://www.mo4tech.com/how-does-the-banking-industry-build-a-self-service-data-platform.html",
    "archive url": "https://bit.ly/self-serve-platform-s27",
    "tiny url": "https://tinyurl.com/self-serve-platform-s27",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s27_codes = [infrastructure_as_code, access_control_management, data_catalog, distributed_file_storage, data_source_ingestion, no_code_transformation, query_engine]
add_links({s27: s27_codes}, role_name="contained_code")

s28 = CClass(source, "s28", values={
    "title": "Applying the Data Mesh Approach Through a Data Product Platform ",
    "url": "https://dzone.com/articles/top-challenges-in-data-mesh-and-how-a-data-product",
    "archive url": "https://bit.ly/self-serve-platform-s28",
    "tiny url": "https://tinyurl.com/self-serve-platform-s28",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s28_codes = [access_control_management, data_transformation_orchestration, infrastructure_as_code]
add_links({s28: s28_codes}, role_name="contained_code")

s29 = CClass(source, "s29", values={
    "title": "The Definitive Guide To Building A Data Mesh With Event Streams",
    "url": "https://dzone.com/articles/top-challenges-in-data-mesh-and-how-a-data-product",
    "archive url": "https://bit.ly/self-serve-platform-s29",
    "tiny url": "https://tinyurl.com/self-serve-platform-s29",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s29_codes = [access_control_management, data_catalog, distributed_file_storage, separating_storage_and_compute, kappa_architecture, lambda_architecture]
add_links({s29: s29_codes}, role_name="contained_code")

s30 = CClass(source, "s30", values={
    "title": "The Definitive Guide To Building A Data Mesh With Event Streams",
    "url": "https://dzone.com/articles/top-challenges-in-data-mesh-and-how-a-data-product",
    "archive url": "https://bit.ly/self-serve-platform-s30",
    "tiny url": "https://tinyurl.com/self-serve-platform-s30",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s30_codes = [container_registry, VMs, api_catalog, infrastructure_as_code, managed_compute_infrastructure, data_catalog, data_transformation_orchestration,
             version_dp, data_lineage, data_source_ingestion, dependable_pipeline_management, distributed_file_storage, separating_storage_and_compute, data_lineage,
             metadata_management, polygot_storage_option]
add_links({s30: s30_codes}, role_name="contained_code")

s31 = CClass(source, "s31", values={
    "title": "Deconstructing Data Mesh Principles",
    "url": "https://medium.com/slalom-data-ai/data-mesh-232e50f42e66",
    "archive url": "https://bit.ly/self-serve-platform-s31",
    "tiny url": "https://tinyurl.com/self-serve-platform-s31",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s31_codes = [access_control_management, dependable_pipeline_management, infrastructure_as_code, log_management,
             data_transformation_orchestration, register_derived_data_as_data_product, separating_storage_and_compute, version_dp, VNetPeering, build_deploy_monitor_dp, integration_service]
add_links({s31: s31_codes}, role_name="contained_code")

s32 = CClass(source, "s32", values={
    "title": "Data Movement in Netflix Studio via Data Mesh",
    "url": "hhttps://netflixtechblog.com/data-movement-in-netflix-studio-via-data-mesh-3fddcceb1059",
    "archive url": "https://bit.ly/self-serve-platform-s32",
    "tiny url": "https://tinyurl.com/self-serve-platform-s32",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s32_codes = [schema_registry, register_derived_data_as_data_product, access_control_management, cdc, knowledge_graph, log_management, sql_endpoint,
             semantic_data_layer, workflow_automation_engine, query_engine ]
add_links({s32: s32_codes}, role_name="contained_code")

s33 = CClass(source, "s33", values={
    "title": "Data Platform in a mesh architecture",
    "url": "https://www.thoughtworks.com/about-us/events/webinars/core-principles-of-data-mesh/data-platform-in-a-mesh-architecture",
    "archive url": "https://bit.ly/self-serve-platform-s33",
    "tiny url": "https://tinyurl.com/self-serve-platform-s33",
    "author type": "Practitioner",
    "type": "Practitioner Audience Article",
    "example": True,
    "source code": False})
s33_codes = [data_catalog, data_lineage, quality_management, build_deploy_monitor_dp, data_transformation_orchestration, query_engine,
             self_serve_ui, ci_cd_process, infrastructure_as_code, dependable_pipeline_management, version_dp, runtime_observability, application_bootstraps, data_source_ingestion, managed_compute_infrastructure,
             separating_compute_from_compute, VMs, access_control_management ,VNetPeering, separating_storage_and_compute, storage_function]
add_links({s33: s33_codes}, role_name="contained_code")






























