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
            VNetPeering, private_endpoints, flexibility]
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
s3_codes = [data_source_ingestion, distributed_file_storage, storage_function, access_control_management, data_catalog,
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
            configure_depency, configure_scheduling, configure_depency]
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
            ci_cd, access_control_management, manage_security_policies_of_dps, manage_emergent_graphs_of_dps,
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
add_links({s9: s9_codes}, role_name="contained_code")













