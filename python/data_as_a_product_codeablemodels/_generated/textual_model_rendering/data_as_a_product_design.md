# API design


## Decision: What type of data product can be developed?
**Evidences:** s1, s2, s6, s7, s9, s14, s15, s27, s34, s43

**Context:** 

### **Solution Options**
#### Solution 1: Expose Data Product as Raw Data
**Evidences:** s1, s2, s6, s7, s9, s14, s15, s27, s34, s43

**Forces:**
- Internal Complexity (++) [s2]
- Complexity for User (--) [s2]

#### Solution 2: Expose Data Product as Derived Data
**Evidences:** s1, s2, s6, s9, s14, s15, s27, s34

**Forces:**
- Internal Complexity (+) [s2]
- Complexity for User (-) [s2]

#### Solution 3: Expose Data Product as an algorithm
**Evidences:** s2, s6

**Forces:**
- Internal Complexity (o) [s2]
- Complexity for User (o) [s2]

#### **Next Decision**: Which approach is chosen for orchestrating the data product


## Decision: Which approach is chosen for orchestrating the data product
**Evidences:** s7, s8, s9, s23, s38, s39, s41, s43, s44, s45, s48, s56, s57

**Context:** 

### **Solution Options**
#### Solution 1: Master Data Management
**Evidences:** s7, s9, s23, s44, s48, s56

**Forces:**
- Centralization (+) [s48]
- Discoverability (+) [s39, s45, s56]

#### Solution 2: Zero Trust Architecture
**Evidences:** s45, s56


#### Solution 3: CQRS
**Evidences:** s8, s38, s39, s41, s43, s56

**Forces:**
- Multiple independent read-only views (+) [s8]
- Allows For Filtering (+) [s38]

#### Solution 4: Strangler-Fig
**Evidences:** s56, s57

**Forces:**
- Easy Data Migration Between Products (++) [s56]
- Decomposition (+) [s57]

#### **Next Decision**: Which architectural elements should be offered in the Data Product layer?
#### **Next Decision**: Which architectural elements should be offered in the Infrastructure layer?
#### **Next Decision**: Which architectural elements should be offered in the Data Access layer?


## Decision: Which architectural elements should be offered in the Data Product layer?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s12, s13, s15, s16, s17, s20, s25, s27, s30, s31, s32, s33, s35, s36, s37, s38, s40, s43, s45, s47, s48, s49, s53, s54, s55, s56, s57

**Context:** 

### **Solution Options**
#### Solution 1: Change Data Capture
**Evidences:** s4, s17, s20, s38, s45, s48, s53, s54, s55, s56

**Forces:**
- Real-time Data Access (+) [s17, s20, s53, s55, s56]
- Complexity for User (-) [s48, s53]
- Non-intrusive (+) [s53]
- Consumption (+) [s53, s55, s56]
- Production Grade Integrations (+) [s53]

#### Solution 2: Immutable Change Audit Log
**Evidences:** s4, s8, s12, s31, s32, s35, s36, s45, s47, s48, s53, s54, s55, s56, s57

**Forces:**
- Reproducibility (+) [s48, s54, s55]
- Traceability (+) [s54, s55]
- Verifiability (+) [s48, s54]
- Immutability (++) [s8, s17, s54]
- Bi-temporality of data (+) [s8]
- Observability (+) [s31, s55, s56]
- Understandability (++) [s3, s32, s47, s48, s55]
- Data Lineage (+) [s48, s54, s55, s56]
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
- Delegated Ownership (+) [s31, s55]
- Consumption (++) [s53, s55, s56]
- Up-to-date (+) [s4, s55]

#### Solution 5: Feature Store
**Evidences:** s9, s20, s27, s40

**Forces:**
- Interoperability (+) [s1, s3, s9, s45]
- Stability (+) [s20]



## Decision: Which architectural elements should be offered in the Infrastructure layer?
**Evidences:** s3, s5, s6, s7, s9, s14, s15, s16, s17, s19, s20, s23, s24, s31, s32, s35, s39, s40, s41, s42, s43, s45, s46, s47, s48, s49, s53, s54, s55, s57

**Context:** 

### **Solution Options**
#### Solution 1: Schema Registry
**Evidences:** s3, s6, s7, s15, s16, s17, s19, s20, s24, s41, s47, s48, s54, s57

**Forces:**
- Understandability (+) [s3, s32, s47, s48, s55]
- Duplication (+) [s3, s15, s17, s48]
- Conflicting definitions (-) [s20]
- Re-use aspects by allowing other teams to find and build upon existing work (++) [s15, s16]
- Interoperability (+) [s3, s9, s45]

#### Solution 2: Central Data Product Catalogue
**Evidences:** s5, s9, s15, s20, s23, s31, s32, s39, s40, s42, s45, s46, s47, s48, s49, s53, s54, s55

**Forces:**
- Discoverability (+) [s15, s31, s32, s39, s42, s45, s49, s55]
- Understandability (+) [s3, s32, s47, s48, s55]
- Observability (+) [s31, s55]

#### Solution 3: Kubernetes Operator
**Evidences:** s6, s14, s32, s35, s39, s43, s45, s47

**Forces:**
- Structured code (+) [s6]

#### Solution 4: Service should be provided as self-serve capability
**Evidences:** 




## Decision: Which architectural elements should be offered in the Data Access layer?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s13, s14, s15, s16, s17, s18, s19, s20, s27, s30, s31, s32, s33, s34, s36, s37, s38, s39, s40, s41, s43, s45, s46, s48, s49, s52

**Context:** 

### **Solution Options**
#### Solution 1: Virtualisation
**Evidences:** s4, s14, s15, s18, s19, s20, s46, s49

**Forces:**
- Data Integration Speed (++) [s2]

#### Solution 2: Implement a highly available in-memory cache
**Evidences:** s5, s14, s15, s18

**Forces:**
- Duplication (-) [s3, s15, s17, s48]

#### Solution 3: Attach a SQL access point to each Data Product
**Evidences:** s2, s3, s5, s7, s10, s13, s14, s15, s16, s27, s30, s31, s32, s36, s37, s38, s39, s43, s46, s48, s49

**Forces:**
- Internal Complexity (+) [s2]
- Complexity for User (+) [s2, s48]
- Accelerate Decision Making (++) [s3]
- More granular data (++) [s3]

#### Solution 4: Attach REST APIs to each data product
**Evidences:** s2, s3, s5, s6, s7, s8, s9, s15, s17, s18, s20, s30, s32, s33, s34, s36, s37, s38, s39, s40, s41, s45, s49, s52

**Forces:**
- Internal Complexity (+) [s2]
- Complexity for User (-) [s2, s48]
- Control over data schema (+) [s17, s41]
- Accessible (+) [s4, s5, s15, s32, s39, s52]
- Addressable (+) [s5, s17]
- Interoperability (+) [s1, s3, s9, s45]

#### Solution 5: Query Catalogue
**Evidences:** s1, s3, s9, s14, s30, s32, s43

**Forces:**
- Trustworthiness (+) [s1, s3]
- Interoperability (+) [s1, s3, s9, s45]
- Discoverability (+) [s1, s15, s31, s32, s39, s45, s49]
- Quickly gain knowledge on data set (++) [s32, s43]
- Frictions (-) [s30]
- Entry Barrier (-) [s30]

#### Solution 6: Security Controls
**Evidences:** 




# Forces: 
- Security [s1, s31]
- Meet SLAs [s22]
- Discoverability [s1, s15, s25, s31, s32, s39, s42, s45, s49, s55, s56]
- Internal Complexity [s2]
- Complexity for User [s2, s48, s53]
- Accelerate Decision Making [s3]
- More granular data [s3]
- Understandability [s3, s32, s47, s48, s55]
- Prioritise [s3, s19]
- Standardised Transformation [s3, s19, s25, s32]
- Duplication [s3, s15, s17, s25, s48]
- Obscurity [s3, s19]
- Trustworthiness [s1, s3, s11, s29]
- Interoperability [s1, s3, s9, s29, s45]
- Compliance [s7]
- Provenance []
- Data Accuracy [s6, s7]
- Completeness [s7]
- Integrity [s7]
- Multiple independent read-only views [s8]
- Re-use aspects by allowing other teams to find and build upon existing work [s15, s16, s21, s25]
- Time-to-Market [s15, s25, s33]
- Conflicting definitions [s20]
- Execution at periodic intervals [s20]
- Consistently Applied Security [s20]
- Stability [s20]
- Turning the data lake into a swamp [s28]
- Data Productivity [s31]
- Analytics Agility [s31]
- Manual Toil [s31]
- Data Quality [s6, s31, s35]
- Discovery [s31]
- Quickly gain knowledge on data set [s32, s43]
- Fast data propagation [s41]
- Handle large data volumes [s41]
- Limit receptions [s41]
- Addressability of subscriptions [s41]
- Control over data schema [s17, s41]
- Real-time Data Access [s17, s20, s51, s53, s55, s56]
- High fidelity [s51]
- Can be deployed in multiple environments [s51]
- Non-intrusive [s53]
- Consumption [s53, s55, s56]
- Production Grade Integrations [s53]
- Reproducibility [s48, s54, s55]
- Traceability [s54, s55]
- Verifiability [s48, s54]
- Unified [s4]
- Up-to-date [s4, s55]
- Protected [s4]
- Accessible [s4, s5, s15, s32, s39, s52]
- Addressable [s5, s17]
- Structured code [s6]
- Immutability [s8, s17, s54]
- Bi-temporality of data [s8]
- Transparency [s11]
- User Experience [s11]
- Data Integration Speed [s2]
- Scalable [s17]
- Frictions [s30]
- Entry Barrier [s30]
- Data Search [s31, s39]
- Data Enrichment [s31]
- Autonomous [s31]
- Delegated Ownership [s31, s55]
- Observability [s31, s55, s56]
- Structured Data [s32]
- On-Demand []
- Grouping Related Data Resources [s37]
- Allows For Filtering [s38]
- Centralization [s48]
- Data Lineage [s48, s54, s55, s56]
- Self-Documenting [s49]
- Ability to gauge data quality [s52]
- Governance [s55]
- Debugging [s56]
- Easy Data Migration Between Products [s56]
- Decomposition [s57]


