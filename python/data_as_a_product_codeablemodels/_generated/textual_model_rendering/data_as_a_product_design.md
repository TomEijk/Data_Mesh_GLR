# API design


## Decision: What type of data product can be developed?
**Evidences:** s1, s2, s6, s7, s9, s14, s15, s27, s34, s43

**Context:** 

### **Solution Options**
#### Solution 1: Expose Data Product as Raw Data
**Evidences:** s1, s2, s6, s7, s9, s14, s15, s27, s34, s43

**Forces:**
- Understandability (-) [s2, s43]

#### Solution 2: Expose Data Product as Derived Data
**Evidences:** s1, s2, s6, s9, s14, s15, s27, s34

**Forces:**
- Understandability (+) [s2, s43]

#### Solution 3: Expose Data Product as an algorithm
**Evidences:** s2, s6

**Forces:**
- Understandability (o) [s2, s43]

#### **Next Decision**: How to deploy a data product?


## Decision: Which approach is chosen for the creation of a data product?
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s44, s45, s48, s49, s56, s57

**Context:** 

### **Solution Options**
#### Solution 1: Migration
**Evidences:** s7, s8, s9, s23, s38, s39, s41, s43, s44, s45, s48, s56, s57


#### Solution 2: Greenfield Development
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s9, s11, s14, s15, s18, s20, s23, s25, s28, s30, s31, s32, s33, s35, s37, s38, s39, s40, s41, s42, s43, s45, s49


#### **Next Decision**: Which Architectural Elements should be offered in the Data Product Anatomy?


## Decision: Which Architectural Elements should be offered in the Data Product Anatomy?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s11, s12, s13, s15, s16, s17, s20, s22, s25, s27, s30, s31, s32, s33, s35, s36, s37, s38, s40, s43, s45, s47, s48, s49, s52, s53, s54, s55, s56, s57

**Context:** 

### **Solution Options**
#### Solution 1: Change Data Capture
**Evidences:** s4, s17, s20, s38, s45, s48, s53, s54, s55, s56

**Forces:**
- Real-time Data Access (+) [s17, s20, s53, s55, s56]
- Understandability (+) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56]
- Accessibility (+) [s4, s5, s15, s32, s52, s53, s55, s56]
- Production Grade Integrations (+) [s53, s56]

#### Solution 2: Immutable Change Audit Log
**Evidences:** s4, s8, s12, s31, s32, s35, s36, s45, s47, s48, s53, s54, s55, s56, s57

**Forces:**
- Reproducibility (+) [s15, s16, s25, s48, s54, s55]
- Traceability (+) [s54, s55]
- Verifiability (+) [s48, s54]
- Immutability (++) [s8, s17, s54]
- Observability (+) [s31, s55, s56]
- Understandability (++) [s3, s11, s32, s43, s47, s48, s49, s53, s55, s56]
- Data Lineage (+) [s8, s48, s54, s55, s56]
- Governance (++) [s55]

#### Solution 3: Internal storages where the data product is deployed, not exposed to consumers
**Evidences:** s4, s13, s15, s32, s33, s36, s49


#### Solution 4: Data Catalogue
**Evidences:** s1, s3, s5, s7, s9, s15, s16, s25, s30, s31, s32, s37, s43, s47, s48, s53, s55

**Forces:**
- Standardised Transformation (+) [s3, s25, s32]
- Duplication (-) [s3, s15, s17, s25, s48]
- Obscurity (-) [s3]
- Discoverability (+) [s1, s15, s25, s31, s32, s45, s49, s55, s56]
- Data Search (+) [s31]
- Data Enrichment (+) [s31]
- Autonomous (+) [s31, s55]
- Accessibility (++) [s4, s5, s15, s32, s52, s53, s55, s56]
- Up-to-date (+) [s4, s55]

#### Solution 5: Observation Plane
**Evidences:** s3, s7, s11, s13, s22, s52


#### Solution 6: Control Plane
**Evidences:** s49, s52




## Decision: How to deploy a data product?
**Evidences:** s6, s14, s15, s30, s32, s33, s35, s39, s43, s45, s47

**Context:** 

### **Solution Options**
#### Solution 1: Kubernetes
**Evidences:** s6, s14, s32, s35, s39, s43, s45, s47


#### Solution 2: Docker
**Evidences:** s14, s15, s30, s32, s33, s45, s47


#### **Next Decision**: How does the data product interact with other data products, self-serve platform and management layer?
#### **Next Decision**: How can the consumer interact with the information from the data product?
#### **Next Decision**: Which approach is chosen for the creation of a data product?


## Decision: How does the data product interact with other data products, self-serve platform and management layer?
**Evidences:** s3, s4, s5, s6, s7, s9, s15, s16, s17, s19, s20, s23, s24, s26, s31, s32, s33, s34, s36, s38, s39, s40, s41, s42, s44, s45, s46, s47, s48, s49, s51, s52, s53, s54, s55, s56, s57

**Context:** 

### **Solution Options**
#### Solution 1: Schema Registry
**Evidences:** s3, s6, s7, s15, s16, s17, s19, s20, s24, s41, s47, s48, s54, s57

**Forces:**
- Understandability (+) [s3, s32, s47, s48, s49, s53, s55, s56]
- Duplication (+) [s3, s15, s17, s48]
- Reproducibility (++) [s15, s16, s48, s54, s55]
- Interoperability (+) [s3, s9, s45]

#### Solution 2: Central Data Product Catalogue
**Evidences:** s5, s9, s15, s20, s23, s31, s32, s39, s40, s42, s45, s46, s47, s48, s49, s53, s54, s55

**Forces:**
- Discoverability (+) [s15, s31, s32, s39, s42, s45, s49, s55, s56]
- Understandability (+) [s3, s32, s47, s48, s49, s53, s55, s56]
- Observability (+) [s31, s55, s56]

#### Solution 3: Event Streaming Backbone
**Evidences:** s4, s9, s17, s20, s26, s33, s34, s36, s38, s41, s44, s45, s48, s51, s52, s53, s55, s56, s57


#### Solution 4: Shared Storage
**Evidences:** 


#### Solution 5: API Invocation
**Evidences:** 


#### **Next Decision**: Which Architectural Elements should be offered in the Data Product Anatomy?


## Decision: How can the consumer interact with the information from the data product?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s12, s13, s14, s15, s16, s17, s18, s20, s23, s27, s30, s31, s32, s33, s34, s36, s37, s38, s39, s40, s41, s43, s45, s46, s47, s48, s49, s52, s56

**Context:** 

### **Solution Options**
#### Solution 1: Attach a SQL access point to each Data Product
**Evidences:** s2, s3, s5, s7, s10, s13, s14, s15, s16, s27, s30, s31, s32, s36, s37, s38, s39, s43, s46, s48, s49

**Forces:**
- Understandability (+) [s2, s3, s32, s43, s47, s48, s49, s56]
- Accelerate Decision Making (++) [s3]
- More granular data (++) [s3]

#### Solution 2: Attach REST APIs to each data product
**Evidences:** s2, s3, s5, s6, s7, s8, s9, s15, s17, s18, s20, s30, s32, s33, s34, s36, s37, s38, s39, s40, s41, s45, s49, s52

**Forces:**
- Understandability (+) [s2, s3, s32, s43, s47, s48, s49, s56]
- Control over data schema (+) [s17, s41]
- Accessibility (+) [s4, s5, s15, s32, s39, s52, s56]
- Addressable (+) [s5, s17]
- Interoperability (+) [s1, s3, s9, s45]

#### Solution 3: Non-Functional Components
**Evidences:** s1, s3, s4, s5, s6, s12, s15, s20, s23, s27, s31, s32, s36, s38, s39, s40, s43, s47, s52, s56


#### **Next Decision**: Which Architectural Elements should be offered in the Data Product Anatomy?


# Forces: 
- Security [s1, s4, s31]
- Discoverability [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56]
- Accelerate Decision Making [s3]
- More granular data [s3]
- Understandability [s2, s3, s11, s32, s43, s47, s48, s49, s53, s55, s56]
- Standardised Transformation [s3, s19, s25, s32]
- Duplication [s3, s15, s17, s25, s48]
- Obscurity [s3, s19]
- Trustworthiness [s1, s3, s11, s29, s51]
- Interoperability [s1, s3, s9, s29, s45]
- Completeness [s7]
- Integrity [s7]
- Multiple independent read-only views [s8]
- Time-to-Market [s2, s15, s25, s33]
- Execution at periodic intervals [s20]
- Consistently Applied Security [s20]
- Stability [s20]
- Turning the data lake into a swamp [s28]
- Agility [s31]
- Manual Toil [s31]
- Data Quality [s6, s7, s31, s35]
- Fast data propagation [s41]
- Handle large data volumes [s41]
- Limit receptions [s41]
- Addressability [s41]
- Control over data schema [s17, s41]
- Real-time Data Access [s17, s20, s51, s53, s55, s56]
- Can be deployed in multiple environments [s51]
- Production Grade Integrations [s53, s56]
- Reproducibility [s15, s16, s21, s25, s48, s54, s55]
- Traceability [s54, s55]
- Verifiability [s48, s54]
- Unified [s4]
- Up-to-date [s4, s55]
- Accessibility [s4, s5, s15, s32, s39, s52, s53, s55, s56]
- Addressable [s5, s17]
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
- Data Lineage [s8, s48, s54, s55, s56]
- Governance [s55]
- Decomposition [s57]


