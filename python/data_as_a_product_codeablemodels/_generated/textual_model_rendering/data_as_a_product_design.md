# API design


## Decision: What strategy can be used for data product implementation?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s44, s45, s47, s48, s49, s56, s57, p1, p2, p3, p4, p5, p6, p8

**Context:** 

### **Solution Options**
#### Solution 1: Cloud Acceleration
**Evidences:** s4, s47, p2, p8

**Forces:**
- Accelerate Decision Making (+) [s3]
- Time-to-Market (+) [s2, s15, s25, s33]
- Scalable (++) []
- Agility (+) [s31]
- Accessibility (++) [s4, s5, s15, s32, s39, s56, p3]
- Control over data schema (-) [s41]
- Security (-) [s1, s4, s20, s31, p1, p2]
- Trustworthiness (-) [s1, s3, s11]

#### Solution 2: Legacy Modernization
**Evidences:** s4, p1, p2, p3

**Forces:**
- More granular data (+) [s3]
- Understandability for User (+) [s2, s3, s11, s32, s43, s47, s48, s49, s56, p1]
- Fast data propagation (+) [s41]
- Real-time Data Access (++) [s20, s56, p1, p3]
- Entry Barrier (-) [s30]
- Latency (-) [p2, p4]
- Stale (-) [p3, p5]

#### Solution 3: Greenfield Development
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s45, s49, p1, p2, p3

**Forces:**
- Accelerate Decision Making (++) [s3]
- Standardised Transformation (+) [s3, s25, s32]
- Fast data propagation (+) [s41]
- Scalable (+) []
- Duplication (-) [s3, s15, s25, s48]
- Time-to-Market (--) [s2, s15, s25, s33]
- Interoperability (-) [s1, s3, s9, s45]

#### **Next Decision**: What type of data product can be developed?


## Decision: What type of data product can be developed?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s14, s15, s21, s23, s27, s34, s38, s42, s43, s44, s49, s52, s57, p1, p2, p3, p4, p5, p6, p8, p9, p10

**Context:** 

### **Solution Options**
#### Solution 1: Source-aligned Data Product
**Evidences:** s4, s7, s8, s23, s38, s42, s44, s49, s52, s57, p5, p8

**Forces:**
- Understandability for User (++) [s2, s3, s43, s49, p1]
- Reproducibility (+) [s15, s21]
- Time-to-Market (+) [s2, s15]
- Discoverability (-) [s1, s15, s42, s49, p3]
- Standardised Transformation (-) [s3]
- Interoperability (-) [s1, s3, s9]

#### Solution 2: Aggregations
**Evidences:** s3, s5, s7, s8, s15, s21, s23, s42, s43, s49, s52, p1, p3, p5, p8

**Forces:**
- Discoverability (+) [s1, s15, s42, s49, p3]
- Accelerate Decision Making (+) [s3]
- Understandability for User (+) [s2, s3, s43, s49, p1]
- Interoperability (+) [s1, s3, s9]
- Security (-) [s1, s4, p1, p2]
- Control over data schema (-) []
- Immutability (-) [s8]

#### Solution 3: Consumer-aligned Data Product
**Evidences:** s4, s7, s8, s23, s38, s42, s44, s49, s52, s57, p1, p5, p8

**Forces:**
- Discoverability (+) [s1, s15, s42, s49, p3]
- Understandability for User (+) [s2, s3, s43, s49, p1]
- Agility (+) []
- Accessibility (+) [s4, s5, s15, s52, p3]
- Grouping (+) []
- Filtering (++) [s38]
- Completeness (-) [s7]
- Data Lineage (-) [s8, p1, p3]
- Governance (-) [p1]

#### **Next Decision**: What architectural components should be included in the anatomy of a data product?
#### **Next Decision**: How does the data product interact with other data products, self-serve platform, government layer and consumers?
#### **Next Decision**: What are the elements of a data product interface/contract?


## Decision: What architectural components should be included in the anatomy of a data product?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s11, s12, s13, s15, s16, s17, s20, s22, s25, s27, s30, s31, s32, s33, s35, s36, s37, s38, s40, s42, s43, s45, s47, s48, s49, s52, s53, s54, s55, s56, s57, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10

**Context:** 

### **Solution Options**
#### Solution 1: Change Data Capture
**Evidences:** s4, s17, s20, s38, s45, s48, s53, s54, s55, s56, p2, p3, p10

**Forces:**
- Accelerate Decision Making (+) [s3]
- Fast data propagation (+) []
- Interoperability (+) [s1, s3, s9, s45]
- Data Quality (++) [s7, s31, s35, p1, p2]
- Traceability (+) [s54, s55]
- Understandability for User (-) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, p1]
- Data Lineage (-) [s8, s48, s54, s55, s56, p1, p3]
- Governance (-) [s55, p1]

#### Solution 2: Immutable Change Audit Log
**Evidences:** s4, s8, s12, s31, s32, s35, s36, s45, s47, s48, s53, s54, s55, s56, s57, p1, p2, p3, p4, p7

**Forces:**
- Security (+) [s1, s4, s20, s31, p1, p2]
- Traceability (++) [s54, s55]
- Verifiability (+) [s48, s54]
- Governance (+) [s55, p1]
- Manual Toil (-) [s31]
- Latency (-) [p2, p4]

#### Solution 3: Metastore
**Evidences:** s7, s20, s25, s31, s37, s38, s42, s43, s45, s49, s52, p1, p2, p4, p5, p6, p8

**Forces:**
- Discoverability (++) [s1, s15, s25, s31, s32, s42, s45, s49, s55, s56, p3]
- Interoperability (+) [s1, s3, s9, s45]
- Data Lineage (+) [s8, s48, s54, s55, s56, p1, p3]
- Governance (+) [s55, p1]
- Scalable (+) [s17]
- Observability (+) [s31, s55, s56]
- Entry Barrier (-) [s30]

#### Solution 4: Data Catalogue
**Evidences:** s1, s3, s5, s7, s9, s15, s16, s25, s30, s31, s32, s37, s43, s47, s48, s53, s55, p1, p3, p4, p5, p6, p7, p8, p9

**Forces:**
- Discoverability (++) [s1, s15, s25, s31, s32, s42, s45, s49, s55, s56, p3]
- Accelerate Decision Making (+) [s3]
- Understandability for User (+) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, p1]
- Data Search (+) [s31]
- Reproducibility (+) [s15, s16, s25, s48, s54, s55]
- Traceability (+) [s54, s55]
- Data Lineage (+) [s8, s48, s54, s55, s56, p1, p3]
- Clear Ownership (++) [s1, s3, s4, s5, s7, s8, s13, s15, s16, s20, s22, s25, s31, s32, s33, s36, s37, s42, s43, s45, s47, s49, s52, s53, s55, s56, s57, p1, p2, p3, p4, p5, p6, p8]
- Accessibility (+) [s4, s5, s15, s32, s52, s53, s55, s56, p3]
- Manual Toil (--) [s31]
- Entry Barrier (-) [s30]
- Centralization (--) [s48]
- Governance (-) [s55, p1]

#### Solution 5: Data Onboarding
**Evidences:** s4, s5, s15, s30, s52, p1, p3

**Forces:**
- Accelerate Decision Making (+) [s3]
- Time-to-Market (+) [s15, s25, s33]
- Fast data propagation (+) []
- Agility (+) [s31]
- Duplication (-) [s3, s15, s17, s25, s48]
- Manual Toil (-) [s31]
- Data Quality (-) [s7, s31, s35, p1, p2]
- Governance (-) [s55, p1]

#### Solution 6: Internal Storage(s)
**Evidences:** s4, s13, s15, s32, s33, s36, s49, p1, p4, p7

**Forces:**
- Accessibility (+) [s4, s5, s15, s32, s52, s53, s55, s56, p3]
- Autonomous (++) [s31, s55]
- Understandability for User (-) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, p1]
- Duplication (-) [s3, s15, s17, s25, s48]

#### Solution 7: Control Plane
**Evidences:** s49, s52, p1, p3

**Forces:**
- Centralization (+) [s48]
- Control over data schema (++) [s17]
- Interoperability (+) [s1, s3, s9, s45]
- Data Quality (+) [s7, s31, s35, p1, p2]
- Governance (+) [s55, p1]
- Transparency (+) [s11]
- Manual Toil (-) [s31]
- Entry Barrier (-) [s30]

#### Solution 8: Observability Plane
**Evidences:** s3, s7, s11, s13, s22, s52, p3

**Forces:**
- Observability (++) [s31, s55, s56]
- Accelerate Decision Making (+) [s3]
- Reproducibility (+) [s15, s16, s25, s48, s54, s55]
- Traceability (+) [s54, s55]
- Manual Toil (-) [s31]
- Entry Barrier (-) [s30]

#### **Next Decision**: How to deploy a data product?


## Decision: What are the elements of a data product interface/contract?
**Evidences:** s1, s2, s3, s7, s8, s10, s11, s13, s14, s15, s16, s20, s22, s23, s24, s25, s27, s29, s33, s36, s37, s40, s41, s49, s52, s57, p1, p2, p3, p4, p5, p6, p7, p8, p9

**Context:** 

### **Solution Options**
#### Solution 1: Observation Port
**Evidences:** s3, s7, s11, s13, s22, s52, p2, p3, p4, p6, p8

**Forces:**
- Observability (++) []
- Accelerate Decision Making (+) [s3]
- Data Quality (+) [s7, p1, p2]
- Scalable (+) []
- Manual Toil (-) []

#### Solution 2: Control Port
**Evidences:** s49, s52, p1, p2, p4, p6

**Forces:**
- Security (+) [s1, s20, p1, p2]
- Governance (++) [p1]
- Interoperability (+) [s1, s3, s29]
- Scalable (+) []
- Entry Barrier (+) []
- Agility (-) []
- Manual Toil (-) []
- Latency (-) [p2, p4]
- Clear Ownership (-) [s1, s3, s7, s8, s10, s13, s14, s15, s16, s20, s22, s23, s24, s25, s33, s36, s37, s41, s49, s52, s57, p1, p2, p3, p4, p5, p6, p8]

#### Solution 3: Discovery Port
**Evidences:** s20, s25, s49, s52, p3, p4, p8, p9

**Forces:**
- Discoverability (++) [s1, s15, s25, s49, p3]
- Accelerate Decision Making (+) [s3]
- Standardised Transformation (+) [s3, s25]
- Duplication (-) [s3, s15, s25]
- Governance (-) [p1]

#### Solution 4: Overarching Management Layer
**Evidences:** p1, p2, p6, p9

**Forces:**
- Control over data schema (+) [s41]
- Interoperability (+) [s1, s3, s29]
- Governance (++) [p1]
- Scalable (+) []
- Autonomous (-) []
- Agility (-) []
- Entry Barrier (-) []

#### Solution 5: Input Port
**Evidences:** s1, s2, s3, s7, s13, s14, s16, s23, s24, s27, s36, s40, s49, s52, s57, p2, p3, p4, p6, p8

**Forces:**
- Accelerate Decision Making (+) [s3]
- Accessibility (++) [s15, s52, p3]
- Agility (+) []
- Fast data propagation (+) [s41]
- Handle large data volumes (+) [s41]
- Scalable (+) []
- Duplication (-) [s3, s15, s25]
- Data Quality (-) [s7, p1, p2]
- Data Lineage (-) [s8, p1, p3]

#### Solution 6: Output Port
**Evidences:** s1, s2, s3, s7, s8, s10, s13, s14, s15, s16, s23, s24, s27, s29, s33, s36, s37, s40, s41, s49, s52, s57, p2, p3, p4, p6, p7, p8

**Forces:**
- Accelerate Decision Making (+) [s3]
- Accessibility (+) [s15, s52, p3]
- More granular data (+) [s3]
- Fast data propagation (+) [s41]
- Scalable (+) []
- Self-serve Capability (+) [s3, p1, p3, p5, p6]
- Security (-) [s1, s20, p1, p2]
- Duplication (-) [s3, s15, s25]
- Data Quality (-) [s7, p1, p2]
- Stale (-) [p3, p5]
- Latency (-) [p2, p4]

#### **Next Decision**: How to deploy a data product?


## Decision: How does the data product interact with other data products, self-serve platform, government layer and consumers?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s12, s13, s14, s15, s16, s17, s18, s19, s20, s23, s24, s25, s26, s27, s28, s30, s31, s32, s33, s34, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s51, s52, s53, s54, s55, s56, s57, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10

**Context:** 

### **Solution Options**
#### Solution 1: Schema Registry
**Evidences:** s3, s6, s7, s15, s16, s17, s19, s20, s24, s41, s47, s48, s54, s57, p3, p5, p6, p7, p8, p10

**Forces:**
- Standardised Transformation (++) [s3, s19, s25, s32]
- Centralization (+) [s48]
- Discoverability (+) [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56, p3]
- Interoperability (+) [s1, s3, s9, s45]
- Data Quality (+) [s6, s7, s31, p1, p2]
- Versioning (+) [s6, s7, s13, s15, s17, s19, s28, s34, s36, s38, s45, s51, s52]
- Governance (+) [s55, p1]
- Entry Barrier (-) [s30]
- Time-to-Market (-) [s2, s15, s25, s33]

#### Solution 2: Central Data Product Catalogue
**Evidences:** s5, s9, s15, s20, s23, s31, s32, s39, s40, s42, s45, s46, s47, s48, s49, s53, s54, s55, p1, p3, p8, p9

**Forces:**
- Discoverability (++) [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56, p3]
- Centralization (+) [s48]
- Interoperability (+) [s1, s3, s9, s45]
- Accessibility (+) [s4, s5, s15, s32, s39, s52, s53, s55, s56, p3]
- Governance (++) [s55, p1]
- Observability (+) [s31, s55, s56]
- Entry Barrier (-) [s30]
- Autonomous (-) [s31, s55]
- Agility (-) [s31]
- Accelerate Decision Making (-) [s3]

#### Solution 3: Metadata lake
**Evidences:** s7, s20, s25, s31, s37, s38, s42, s43, s45, s49, s52, p1, p2, p6, p8

**Forces:**
- Discoverability (+) [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56, p3]
- Centralization (+) [s48]
- Accelerate Decision Making (+) [s3]
- Standardised Transformation (+) [s3, s19, s25, s32]
- Interoperability (++) [s1, s3, s9, s45]
- Completeness (+) [s7]
- Data Lineage (+) [s8, s48, s54, s55, s56, p1, p3]
- Governance (+) [s55, p1]
- Entry Barrier (-) [s30]
- Data Search (-) [s31, s39]
- Understandability for User (-) [s2, s3, s19, s32, s43, s47, s48, s49, s53, s55, s56, p1]

#### Solution 4: Event Streaming Backbone
**Evidences:** s4, s9, s17, s20, s26, s33, s34, s36, s38, s41, s44, s45, s48, s51, s52, s53, s55, s56, s57, p1, p2, p3, p5, p6, p7, p10

**Forces:**
- Fast data propagation (+) [s41]
- Scalable (+) [s17]
- Real-time Data Access (+) [s17, s20, s51, s53, s55, s56, p1, p3]
- Multiple independent read-only views (+) [s8]
- Agility (+) [s31]
- Data Quality (-) [s6, s7, s31, p1, p2]
- Understandability for User (-) [s2, s3, s19, s32, s43, s47, s48, s49, s53, s55, s56, p1]

#### Solution 5: Batch processing
**Evidences:** s14, s15, s19, s28, s30, s32, s36, s38, s39, s41, s43, s44, s49, s51, s53, s57, p1, p2, p3, p6, p9

**Forces:**
- Handle large data volumes (++) [s41]
- Time-to-Market (+) [s2, s15, s25, s33]
- Reproducibility (+) [s15, s16, s25, s48, s54, s55]
- Fast data propagation (-) [s41]
- Real-time Data Access (-) [s17, s20, s51, s53, s55, s56, p1, p3]
- Agility (-) [s31]
- Latency (-) [p2, p4]

#### Solution 6: Shared Storage
**Evidences:** s19, s25, s33, s36, s38, s40, p1, p3, p6, p9

**Forces:**
- Data Quality (+) [s6, s7, s31, p1, p2]
- Completeness (+) [s7]
- Accessibility (+) [s4, s5, s15, s32, s39, s52, s53, s55, s56, p3]
- Interoperability (+) [s1, s3, s9, s45]
- Time-to-Market (+) [s2, s15, s25, s33]
- Scalable (+) [s17]
- Control over data schema (-) [s17, s41]
- Data Lineage (-) [s8, s48, s54, s55, s56, p1, p3]
- Immutability (-) [s8, s17, s54]
- Transparency (-) []
- Addressable (-) [s5, s17, s41]

#### Solution 7: Master database
**Evidences:** s4, s7, s9, s23, s44, s48, s56, p1, p2, p3, p5, p6, p7, p8

**Forces:**
- End-to-end consistency (++) [p1, p3, p5]
- Data Quality (+) [s6, s7, s31, p1, p2]
- Autonomous (-) [s31, s55]
- Scalable (-) [s17]

#### Solution 8: Reference database
**Evidences:** p1, p2, p3

**Forces:**
- Understandability for User (++) [s2, s3, s19, s32, s43, s47, s48, s49, s53, s55, s56, p1]
- End-to-end consistency (+) [p1, p3, p5]
- Completeness (+) [s7]
- Transparency (+) []
- Entry Barrier (-) [s30]
- Stale (-) [p3, p5]

#### Solution 9: Data Product Policy Enforcement Mechanisms
**Evidences:** s1, s3, s4, s5, s6, s12, s15, s20, s23, s27, s31, s32, s36, s38, s39, s40, s43, s47, s52, s56, p5

**Forces:**
- Security (++) [s1, s4, s20, s31, p1, p2]
- Governance (+) [s55, p1]
- Data Quality (+) [s6, s7, s31, p1, p2]
- Agility (-) [s31]
- Manual Toil (-) [s31]
- Self-serve Capability (-) [s3, p1, p3, p5, p6]

#### **Next Decision**: How to deploy a data product?


## Decision: How to deploy a data product?
**Evidences:** s4, s6, s13, s14, s15, s19, s21, s25, s30, s31, s32, s33, s35, s36, s38, s39, s40, s43, s45, s47, s49, p1, p2, p3, p4, p5, p6, p7, p8, p10

**Context:** 

### **Solution Options**
#### Solution 1: Function-as-a-Service
**Evidences:** s15, s21, s30, s31, s32, s33, s35, s36

**Forces:**
- Agility (+) [s31]
- Time-to-Market (+) [s15, s25, s33]
- Infrastructure workload (+) [s4, p1, p2]
- Scalable (+) []
- Stateless (+) [p1]
- Self-serve Capability (+) [p1, p3, p5, p6]
- Security (-) [s4, s31, p1, p2]
- Latency (-) [p2, p4]
- Discoverability (-) [s15, s25, s31, s32, s39, s45, s49, p3]
- Data Enrichment (-) [s31]

#### Solution 2: Containerisation
**Evidences:** s14, s15, s30, s32, s33, s45, s47, p3, p4, p6, p10

**Forces:**
- Scalable (+) []
- Agility (+) [s31]
- Standardised Transformation (+) [s19, s25, s32]
- Entry Barrier (-) [s30]
- Understandability for User (-) [s19, s32, s43, s47, s49, p1]
- Infrastructure workload (-) [s4, p1, p2]

#### Solution 3: Data Storage Infrastructure
**Evidences:** s4, s13, s15, s19, s25, s32, s33, s36, s38, s40, s49, p1, p3, p4, p5, p6, p7, p8

**Forces:**
- Scalable (+) []
- Fast data propagation (+) []
- Handle large data volumes (+) []
- Accessibility (+) [s4, s15, s32, s39, p3]
- Security (-) [s4, s31, p1, p2]
- Duplication (-) [s15, s25]
- Data Lineage (-) [p1, p3]
- Data Search (-) [s31, s39]

#### Solution 4: VMs
**Evidences:** s15, s47, p1, p3, p4

**Forces:**
- Security (+) [s4, s31, p1, p2]
- Control over data schema (+) []
- Versioning (+) [s6, s13, s15, s19, s35, s36, s38, s45]
- Agility (-) [s31]
- Infrastructure workload (-) [s4, p1, p2]
- Scalable (-) []

#### Solution 5: Hybrid Deployment
**Evidences:** s4, s47, p2, p8

**Forces:**
- Accessibility (+) [s4, s15, s32, s39, p3]
- Interoperability (+) [s45]
- Scalable (+) []
- Continuity (+) [s4, p1, p6]
- Infrastructure workload (+) [s4, p1, p2]
- Agility (+) [s31]
- Time-to-Market (+) [s15, s25, s33]
- Understandability for User (-) [s19, s32, s43, s47, s49, p1]
- Governance (-) [p1]
- Security (-) [s4, s31, p1, p2]
- Discoverability (-) [s15, s25, s31, s32, s39, s45, s49, p3]
- Clear Ownership (-) [s4, s13, s14, s15, s19, s21, s25, s31, s32, s33, s36, s43, s45, s47, s49, p1, p2, p3, p4, p5, p6, p8]
- Centralization (-) []

#### Solution 6: Multi-Cloud Deployment
**Evidences:** s4, s47, p6

**Forces:**
- Scalable (+) []
- Agility (+) [s31]
- Time-to-Market (+) [s15, s25, s33]
- Infrastructure workload (+) [s4, p1, p2]
- Understandability for User (-) [s19, s32, s43, s47, s49, p1]
- Security (-) [s4, s31, p1, p2]
- Interoperability (-) [s45]
- Governance (-) [p1]
- Latency (-) [p2, p4]



# Forces: 
- Security [s1, s4, s20, s31, p1, p2]
- Discoverability [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56, p3]
- Accelerate Decision Making [s3]
- More granular data [s3]
- Understandability for User [s2, s3, s11, s19, s32, s43, s47, s48, s49, s53, s55, s56, p1]
- Standardised Transformation [s3, s19, s25, s32]
- Duplication [s3, s15, s17, s25, s48]
- Trustworthiness [s1, s3, s11, s29, s51]
- Interoperability [s1, s3, s9, s29, s45]
- Completeness [s7]
- Multiple independent read-only views [s8]
- Time-to-Market [s2, s15, s25, s33]
- Agility [s31]
- Manual Toil [s31]
- Data Quality [s6, s7, s31, s35, p1, p2]
- Fast data propagation [s41]
- Handle large data volumes [s41]
- Control over data schema [s17, s41]
- Real-time Data Access [s17, s20, s51, s53, s55, s56, p1, p3]
- Reproducibility [s15, s16, s21, s25, s48, s54, s55]
- Traceability [s54, s55]
- Verifiability [s48, s54]
- Accessibility [s4, s5, s15, s32, s39, s52, s53, s55, s56, p3]
- Addressable [s5, s17, s41]
- Immutability [s8, s17, s54]
- Transparency [s11]
- Scalable [s17]
- Entry Barrier [s30]
- Data Search [s31, s39]
- Data Enrichment [s31]
- Autonomous [s31, s55]
- Observability [s31, s55, s56]
- Grouping [s37]
- Filtering [s38]
- Centralization [s48]
- Data Lineage [s8, s48, s54, s55, s56, p1, p3]
- Governance [s55, p1]
- Versioning [s6, s7, s13, s15, s17, s19, s28, s34, s35, s36, s38, s45, s51, s52]
- Continuity [s4, p1, p6]
- Infrastructure workload [s4, p1, p2]
- End-to-end consistency [p1, p3, p5]
- Stateless [p1]
- Self-serve Capability [s3, p1, p3, p5, p6]
- Stale [p3, p5]
- Clear Ownership [s1, s3, s4, s5, s7, s8, s10, s13, s14, s15, s16, s19, s20, s21, s22, s23, s24, s25, s31, s32, s33, s36, s37, s41, s42, s43, s44, s45, s46, s47, s49, s51, s52, s53, s55, s56, s57, p1, p2, p3, p4, p5, p6, p8]
- Latency [p2, p4]


