# API design


## Decision: What type of data product can be developed?
**Evidences:** s1, s2, s6, s7, s9, s14, s15, s27, s34, s43, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Source-aligned Data Product
**Evidences:** 


#### Solution 2: Aggregations
**Evidences:** i5


#### Solution 3: Consumer-aligned Data Product
**Evidences:** 


#### **Next Decision**: What architectural components should be included in the anatomy of a data product?
#### **Next Decision**: How does the data product interact with other data products, self-serve platform, government layer and consumers?
#### **Next Decision**: What are the elements of a data product interface/contract?


## Decision: What strategy can be used for data product implementation?
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s44, s45, s48, s49, s56, s57, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Cloud Acceleration
**Evidences:** 


#### Solution 2: Legacy Modernization
**Evidences:** 


#### Solution 3: Greenfield Development
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s45, s49, i1, i2, i3

**Forces:**
- Entry Barrier (--) [s30]
- Accelerate Decision Making (++) [s3]
- Time-to-Market (--) [s2, s15, s25, s33]

#### **Next Decision**: What type of data product can be developed?


## Decision: What architectural components should be included in the anatomy of a data product?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s11, s12, s13, s15, s16, s17, s20, s22, s25, s27, s30, s31, s32, s33, s35, s36, s37, s38, s40, s43, s45, s47, s48, s49, s52, s53, s54, s55, s56, s57, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Change Data Capture
**Evidences:** s4, s17, s20, s38, s45, s48, s53, s54, s55, s56, i2, i3

**Forces:**
- Real-time Data Access (+) [s17, s20, s53, s55, s56, i1, i3]
- Understandability for User (+) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Accessibility (+) [s4, s5, s15, s32, s52, s53, s55, s56, i3]
- Production Grade Integrations (+) [s53, s56, i1]

#### Solution 2: Immutable Change Audit Log
**Evidences:** s4, s8, s12, s31, s32, s35, s36, s45, s47, s48, s53, s54, s55, s56, s57, i1, i2, i3, i4

**Forces:**
- Reproducibility (+) [s15, s16, s25, s48, s54, s55]
- Traceability (+) [s54, s55]
- Verifiability (+) [s48, s54]
- Immutability (++) [s8, s17, s54]
- Observability (+) [s31, s55, s56]
- Understandability for User (++) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Data Lineage (+) [s8, s48, s54, s55, s56, i1, i3]
- Governance (++) [s55, i1]
- Can be deployed in multiple environments (+) []

#### Solution 3: Metastore
**Evidences:** i1, i4, i5, i6


#### Solution 4: Data Catalogue
**Evidences:** s1, s3, s5, s7, s9, s15, s16, s25, s30, s31, s32, s37, s43, s47, s48, s53, s55, i1, i3, i4, i5, i6

**Forces:**
- Standardised Transformation (+) [s3, s25, s32]
- Duplication (-) [s3, s15, s17, s25, s48]
- Understandability for User (+) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Discoverability (+) [s1, s15, s25, s31, s32, s45, s49, s55, s56, i3]
- Data Search (+) [s31]
- Data Enrichment (+) [s31]
- Autonomous (+) [s31, s55]
- Accessibility (++) [s4, s5, s15, s32, s52, s53, s55, s56, i3]
- Up-to-date (+) [s4, s55, i3]
- Trustworthiness (+) [s1, s3, s11]
- Unified (+) [s4]
- Security (+) [s1, s4, s20, s31, i1, i2]

#### Solution 5: Data Onboarding
**Evidences:** s4, s5, s15, s30, s52, i1, i3

**Forces:**
- Observability (+) [s31, s55, s56]
- Data Quality (+) [s7, s31, s35, i1, i2]
- Standardised Transformation (+) [s3, s25, s32]
- Security (+) [s1, s4, s20, s31, i1, i2]

#### Solution 6: Internal Storage(s)
**Evidences:** s4, s13, s15, s32, s33, s36, s49, i1, i4

**Forces:**
- Infrastructure workload (-) [i1]
- Understandability for User (-) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, i1]

#### Solution 7: Control Plane
**Evidences:** s49, s52, i1, i3

**Forces:**
- Control over data schema (+) [s17]

#### Solution 8: Observability Plane
**Evidences:** s3, s7, s11, s13, s22, s52, i3

**Forces:**
- Understandability for User (+) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Trustworthiness (+) [s1, s3, s11]
- Completeness (+) [s7]
- Integrity (+) [s7]
- Data Quality (o) [s7, s31, s35, i1, i2]
- Accessibility (+) [s4, s5, s15, s32, s52, s53, s55, s56, i3]
- Transparency (++) [s11]
- Observability (+) [s31, s55, s56]
- Data Lineage (+) [s8, s48, s54, s55, s56, i1, i3]

#### **Next Decision**: How to deploy a data product?


## Decision: How to deploy a data product?
**Evidences:** s6, s14, s15, s30, s32, s33, s35, s39, s43, s45, s47, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Function-as-a-Service
**Evidences:** s15, s21, s30, s31, s32, s33, s35, s36


#### Solution 2: Containerisation
**Evidences:** s14, s15, s30, s32, s33, s45, s47, i3, i4, i6

**Forces:**
- Reproducibility (+) [s15]
- Can be deployed in multiple environments (+) []
- Stateless (-) []

#### Solution 3: Lakehouse Architecture
**Evidences:** i5, i6

**Forces:**
- Autonomous (+) []
- Self-serve Capability (+) []
- Governance (+) [i1]

#### Solution 4: VMs
**Evidences:** i3, i4


#### Solution 5: Hybrid Deployment
**Evidences:** 


#### Solution 6: Multi-Cloud Deployment
**Evidences:** 




## Decision: How does the data product interact with other data products, self-serve platform, government layer and consumers?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s12, s13, s14, s15, s16, s17, s18, s19, s20, s23, s24, s26, s27, s30, s31, s32, s33, s34, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s51, s52, s53, s54, s55, s56, s57, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Shared Storage
**Evidences:** s33, i3

**Forces:**
- Versioning (--) [s6, s7, s13, s15, s17, s19, s34, s36, s38, s45, s51, s52]
- Duplication (-) [s3, s15, s17, s48]
- Filtering (-) [s38]
- Control over data schema (-) [s17, s41]

#### Solution 2: Master database
**Evidences:** 


#### Solution 3: Reference database
**Evidences:** 


#### Solution 4: Data Product Policy Enforcement Mechanisms
**Evidences:** s1, s3, s4, s5, s6, s12, s15, s20, s23, s27, s31, s32, s36, s38, s39, s40, s43, s47, s52, s56, i5

**Forces:**
- Security (++) [s1, s4, s20, s31, i1, i2]
- Discoverability (+) [s1, s15, s31, s32, s39, s42, s45, s49, s55, s56, i3]
- Understandability for User (+) [s2, s3, s19, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Trustworthiness (+) [s1, s3, s51]
- Interoperability (+) [s1, s3, s9, s45]
- Accessibility (+) [s4, s5, s15, s32, s39, s52, s53, s55, s56, i3]
- Entry Barrier (-) [s30]
- Autonomous (+) [s31, s55]

#### **Next Decision**: How to deploy a data product?


## Decision: What are the elements of a data product interface/contract?
**Evidences:** s3, s7, s11, s13, s20, s22, s25, s49, s52, i1, i2, i3, i4, i5, i6

**Context:** 

### **Solution Options**
#### Solution 1: Observation Port
**Evidences:** s3, s7, s11, s13, s22, s52, i2, i3, i4, i6

**Forces:**
- Understandability for User (+) [s3, s11, s49, i1]
- Trustworthiness (+) [s3, s11]
- Completeness (+) [s7]
- Integrity (+) [s7]
- Data Quality (o) [s7, i1, i2]
- Accessibility (+) [s52, i3]
- Transparency (++) [s11]
- Observability (+) []
- Data Lineage (+) [i1, i3]

#### Solution 2: Control Port
**Evidences:** s49, s52, i1, i2, i4, i6

**Forces:**
- Control over data schema (+) []
- Governance (+) [i1]
- Security (+) [s20, i1, i2]

#### Solution 3: Discovery Port
**Evidences:** s20, s25, s49, s52, i3, i4

**Forces:**
- Discoverability (+) [s25, s49, i3]
- Accessibility (+) [s52, i3]

#### Solution 4: Overarching Management Layer
**Evidences:** i1, i2, i6

**Forces:**
- Governance (+) [i1]
- End-to-end consistency (+) [i1]

#### Solution 5: Input Port
**Evidences:** i4


#### Solution 6: Output Port
**Evidences:** i4


#### **Next Decision**: How to deploy a data product?


# Forces: 
- Security [s1, s4, s20, s31, i1, i2]
- Discoverability [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56, i3]
- Accelerate Decision Making [s3]
- More granular data [s3]
- Understandability for User [s2, s3, s11, s19, s32, s43, s47, s48, s49, s53, s55, s56, i1]
- Standardised Transformation [s3, s19, s25, s32]
- Duplication [s3, s15, s17, s25, s48]
- Trustworthiness [s1, s3, s11, s29, s51]
- Interoperability [s1, s3, s9, s29, s45]
- Completeness [s7]
- Integrity [s7]
- Multiple independent read-only views [s8]
- Time-to-Market [s2, s15, s25, s33]
- Agility [s31]
- Manual Toil [s31]
- Data Quality [s6, s7, s31, s35, i1, i2]
- Fast data propagation [s41]
- Handle large data volumes [s41]
- Limit receptions [s41]
- Control over data schema [s17, s41]
- Real-time Data Access [s17, s20, s51, s53, s55, s56, i1, i3]
- Can be deployed in multiple environments [s51]
- Production Grade Integrations [s53, s56, i1]
- Reproducibility [s15, s16, s21, s25, s48, s54, s55]
- Traceability [s54, s55]
- Verifiability [s48, s54]
- Unified [s4]
- Up-to-date [s4, s55, i3]
- Accessibility [s4, s5, s15, s32, s39, s52, s53, s55, s56, i3]
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
- Data Lineage [s8, s48, s54, s55, s56, i1, i3]
- Governance [s55, i1]
- Decomposition [s57]
- Versioning [s6, s7, s13, s15, s17, s19, s28, s34, s35, s36, s38, s45, s51, s52]
- Continuity [i1]
- Sustainable solution [i1]
- Infrastructure workload [i1]
- holistic view [i1]
- End-to-end consistency [i1]
- Stateless []
- Self-serve Capability []
- Stale [i3]
- Clear Ownership [i3]
- Latency []


