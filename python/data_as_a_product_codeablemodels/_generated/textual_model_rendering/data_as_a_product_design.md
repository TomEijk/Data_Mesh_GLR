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

#### Solution 3: Expose Data Product as Decision Support Model
**Evidences:** s1, s2, s6, s7, s9, s14, s27, s34

**Forces:**
- Internal Complexity (-) [s2]
- Complexity for User (+) [s2]

#### Solution 4: Expose Data Product as Automated Decision-making Model
**Evidences:** s1, s2, s6, s9, s27, s34

**Forces:**
- Internal Complexity (--) [s2]
- Complexity for User (++) [s2]

#### Solution 5: Expose Data Product as an algorithm
**Evidences:** s2, s6

**Forces:**
- Internal Complexity (o) [s2]
- Complexity for User (o) [s2]

#### **Next Decision**: How to deploy a data product using subscriptions and workspaces?
#### **Next Decision**: What is the anatomy of a Data Product?


## Decision: How to make data products discoverable?
**Evidences:** s1, s3, s4, s5, s6, s14, s15, s18, s20, s23, s25, s27, s31, s32, s36, s38, s42, s43, s45, s49, s52

**Context:** 

### **Solution Options**
#### Solution 1: Service Locator
**Evidences:** s1, s32


#### Solution 2: Discovery Port
**Evidences:** s20, s25, s49, s52


#### Solution 3: Data Marketplace
**Evidences:** s14, s32, s42, s43, s45




## Decision: How to keep track of metadata?
**Evidences:** s1, s3, s4, s5, s7, s8, s9, s10, s12, s14, s15, s16, s17, s18, s19, s20, s23, s25, s27, s28, s30, s31, s32, s35, s36, s37, s38, s39, s40, s42, s43, s45, s46, s47, s48, s49, s51, s53, s54

**Context:** 

### **Solution Options**
#### Solution 1: Data Catalogue
**Evidences:** s1, s3, s5, s7, s9, s15, s16, s25, s30, s31, s32, s37, s43, s48, s53

**Forces:**
- Standardised Transformation (+) [s3, s19, s25]
- Duplication (-) [s3, s15, s17, s25]
- Obscurity (-) [s3, s19]
- Discoverability (+) [s1, s15, s25, s32]

#### Solution 2: Query Catalogue
**Evidences:** s1, s3, s9, s14, s30, s32, s43

**Forces:**
- Trustworthiness (+) [s1, s3]
- Interoperability (+) [s1, s3, s9]
- Discoverability (+) [s1, s15, s25, s32]
- Quickly gain knowledge on data set (++) [s32]

#### Solution 3: Change Data Capture
**Evidences:** s4, s17, s20, s38, s45, s48, s53, s54

**Forces:**
- Real-time Data Access (+) [s17, s20, s51]
- Complexity for User (-) []
- Non-intrusive (+) [s53]
- Consumption (+) [s53]
- Production Grade Integrations (+) [s53]

#### Solution 4: Virtualisation
**Evidences:** s4, s14, s15, s18, s19, s20, s46, s49

**Forces:**
- Data Integration Speed (++) []

#### Solution 5: Immutable Change Audit Log
**Evidences:** s4, s8, s12, s31, s32, s35, s36, s45, s47, s48, s53, s54

**Forces:**
- Reproducibility (+) [s54]
- Traceability (+) [s54]
- Verifiability (+) [s54]
- Immutability (++) [s8, s17]
- Bi-temporality of data (+) [s8]

#### Solution 6: Central Data Product Catalogue
**Evidences:** s5, s9, s15, s20, s23, s31, s32, s39, s40, s42, s45, s46, s47, s48, s53, s54

**Forces:**
- Discoverability (+) [s1, s15, s25, s32]



## Decision: How to make a data product trustworty?
**Evidences:** s1, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s15, s16, s17, s19, s20, s22, s24, s25, s28, s29, s32, s33, s35, s36, s41, s45, s47, s48, s50, s51, s52, s54

**Context:** 

### **Solution Options**
#### Solution 1: Provide a single integrated experience for monitoring
**Evidences:** s1, s3, s4, s5, s6, s9, s10, s11, s12, s19, s20, s22, s25, s28, s32, s33, s35, s36

**Forces:**
- Data Quality (o) [s6]
- Data Accuracy (o) [s6, s7]
- User Experience (+) [s11]
- Meet SLAs (+) [s22]

#### Solution 2: The observability plane brings an interface between built-in observability of the data quantum and REST clients
**Evidences:** s3, s7, s11, s13, s22, s52

**Forces:**
- Understandability (+) [s3]
- Data Accuracy (+) [s6, s7]
- Completeness (+) [s7]
- Integrity (+) [s7]
- Transparency (+) [s11]
- Trustworthiness (+) [s1, s3, s11]

#### Solution 3: Schema Manager
**Evidences:** s3, s6, s7, s15, s16, s17, s19, s20, s24, s41, s47, s48, s54

**Forces:**
- Understandability (+) [s3]
- Duplication (+) [s3, s15, s17, s25]
- Conflicting definitions (-) [s20]
- Re-use aspects by allowing other teams to find and build upon existing work (++) [s15, s16, s25]
- Interoperability (+) [s1, s3, s9]

#### Solution 4: Maintaining a single source of truth
**Evidences:** s25, s29


#### Solution 5: Run tests on your data product
**Evidences:** s28


#### Solution 6: Time-bounded Backwards Compatibility
**Evidences:** s5, s8, s10, s17, s45, s50, s51




## Decision: How can the user interact with data products?
**Evidences:** s2, s3, s5, s6, s7, s8, s9, s10, s13, s14, s15, s16, s17, s18, s20, s27, s30, s31, s32, s33, s34, s36, s37, s38, s39, s41, s42, s43, s45, s48, s49, s52

**Context:** 

### **Solution Options**
#### Solution 1: Attach a Data Access REST API to each Data Product
**Evidences:** s2, s3, s5, s6, s7, s8, s9, s15, s17, s18, s20, s30, s32, s33, s34, s36, s37, s38, s39, s41, s45, s49, s52

**Forces:**
- Internal Complexity (+) [s2]
- Complexity for User (-) [s2]
- Control over data schema (+) [s17, s41]
- Accessible (+) [s5, s15]
- Addressable (+) [s5, s17]

#### Solution 2: Attach a SQL layer to each Data Product
**Evidences:** s2, s3, s5, s7, s10, s13, s14, s15, s16, s27, s30, s31, s32, s36, s37, s38, s39, s43, s48, s49

**Forces:**
- Internal Complexity (+) [s2]
- Complexity for User (+) [s2]
- Accelerate Decision Making (++) [s3]
- More granular data (++) [s3]

#### Solution 3: NoSQL system
**Evidences:** s14, s15




## Decision: What is the anatomy of a Data Product?
**Evidences:** s3, s5, s7, s8, s9, s20, s27, s32, s39, s40, s43, s45, s49, s52

**Context:** 

### **Solution Options**
#### Solution 1: The domain datasets belong to a specific domain
**Evidences:** s3, s5, s7, s20, s45

**Forces:**
- Prioritise (+) [s3]
- Unified (+) []
- Up-to-date (+) []
- Protected (+) []
- Accessible (+) [s5]

#### Solution 2: Core datasets are those that are useful for more than one domain
**Evidences:** s3, s5, s7, s9, s45

**Forces:**
- Prioritise (+) [s3]
- Trustworthiness (+) [s3]
- Interoperability (+) [s3, s9]

#### Solution 3: Feature Layer
**Evidences:** s9, s20, s27, s40

**Forces:**
- Interoperability (+) [s3, s9]
- Stability (+) [s20]

#### Solution 4: Open source data and analytics processing service
**Evidences:** s32, s39


#### Solution 5: Control Plane
**Evidences:** s49, s52


#### **Next Decision**: Where can we store the data?
#### **Next Decision**: How to make a data product trustworty?
#### **Next Decision**: How to secure your data products?
#### **Next Decision**: How to make data products discoverable?


## Decision: How can data products communicate?
**Evidences:** s4, s5, s8, s9, s14, s15, s17, s18, s19, s20, s22, s25, s26, s28, s29, s30, s32, s33, s34, s35, s36, s37, s38, s39, s41, s43, s44, s45, s48, s51, s52, s53

**Context:** 

### **Solution Options**
#### Solution 1: Event Streaming
**Evidences:** s4, s9, s17, s20, s26, s33, s34, s38, s41, s44, s45, s48, s51, s52, s53

**Forces:**
- Real-time Data Access (+) [s17, s20, s51]
- High fidelity (+) [s51]
- Scalable (+) [s17]
- Duplication (+) [s15, s17, s25]
- Immutability (+) [s8, s17]
- Addressable (+) [s5, s17]

#### Solution 2: Use a data integration service that helps users efficiently build and manage ETL/ELT pipelines
**Evidences:** s4, s5, s15, s30


#### Solution 3: Triggering
**Evidences:** s8, s19, s22, s32, s33, s35, s38, s45


#### Solution 4: CQRS
**Evidences:** s8, s41, s43

**Forces:**
- Multiple independent read-only views (+) [s8]

#### Solution 5: end-to-end connection
**Evidences:** s15, s22, s25, s29


#### Solution 6: Create a component for unified batch and stream data processing
**Evidences:** s14, s20, s25, s28, s30, s32, s36, s39, s41, s44

**Forces:**
- Execution at periodic intervals (+) [s20]

#### Solution 7: Event Bus
**Evidences:** s20

**Forces:**
- Real-time Data Access (+) [s17, s20, s51]

#### Solution 8: Pub/Sub
**Evidences:** s18, s30, s32, s37, s38, s39, s41, s53

**Forces:**
- Fast data propagation (+) [s41]
- Handle large data volumes (++) [s41]
- Limit receptions (+) [s41]
- Addressability of subscriptions (+) [s41]

#### Solution 9: Indirect data publishing and consumption
**Evidences:** s41, s43


#### Solution 10: Send snapshots via nightly ETL
**Evidences:** s17, s41

**Forces:**
- Control over data schema (-) [s17, s41]

#### Solution 11: Send snapshots via Req/Res API
**Evidences:** s17

**Forces:**
- Control over data schema (+) [s17, s41]



## Decision: How to secure your data products?
**Evidences:** s1, s3, s4, s5, s6, s12, s15, s20, s23, s27, s31, s32, s36, s38, s45

**Context:** 

### **Solution Options**
#### Solution 1: Role-based Access Control
**Evidences:** s4, s6, s12, s15, s36


#### Solution 2: Fine-grained Access Control
**Evidences:** s1, s3, s4, s5, s6, s15, s20, s23, s27, s31, s32, s36, s38


#### Solution 3: Encryption
**Evidences:** s4, s5


#### Solution 4: Open Access
**Evidences:** s23


#### Solution 5: Attribute-based Access Control
**Evidences:** s36


#### Solution 6: Zero Trust Architecture
**Evidences:** s45


#### Solution 7: OAUTH2
**Evidences:** s45




## Decision: Where can we store the data?
**Evidences:** s4, s5, s13, s14, s15, s18, s20, s32, s36, s43, s49, s52

**Context:** 

### **Solution Options**
#### Solution 1: Internal storages where the data product is deployed, not exposed to consumers
**Evidences:** s4, s13, s15, s32, s36, s49


#### Solution 2: Implement a highly available in-memory cache
**Evidences:** s5, s14, s15, s18

**Forces:**
- Duplication (-) [s15]

#### Solution 3: Incrementally build business process-centric data marts
**Evidences:** s4, s20, s43, s52




## Decision: How can we manage and provision the infrastucture
**Evidences:** s4, s6, s7, s9, s13, s14, s15, s17, s18, s19, s20, s23, s28, s30, s31, s32, s33, s34, s35, s36, s38, s43, s44, s45, s51

**Context:** 

### **Solution Options**
#### Solution 1: Infrastructure as Code
**Evidences:** s6, s9, s15, s17, s19, s28, s30

**Forces:**
- Compliance (+) [s7]
- Provenance (+) []
- Discoverability (+) [s15, s32]
- Re-use aspects by allowing other teams to find and build upon existing work (+) [s15]
- Time-to-Market (+) [s15]
- Duplication (+) [s15, s17]

#### Solution 2:  CI/CD process
**Evidences:** s4, s6, s19, s28, s30, s35, s51

**Forces:**
- Can be deployed in multiple environments (+) [s51]

#### Solution 3: Versioning
**Evidences:** s6, s7, s13, s15, s17, s19, s28, s34, s35, s36, s38, s45, s51

**Forces:**
- Can be deployed in multiple environments (+) [s51]

#### Solution 4: K8s
**Evidences:** s6, s14, s32, s43, s45

**Forces:**
- Structured code (+) [s6]

#### Solution 5: Master Data Management
**Evidences:** s7, s9, s23, s44


#### Solution 6: Run containers that are invocable via requests or events
**Evidences:** s14, s15, s30, s32, s33, s45


#### Solution 7: Orchestrator
**Evidences:** s9, s18, s30


#### Solution 8: API Gateway
**Evidences:** s20

**Forces:**
- Consistently Applied Security (+) [s20]

#### Solution 9: Templated Data Pipeline
**Evidences:** s30, s43


#### Solution 10: Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts
**Evidences:** s31

**Forces:**
- Data Productivity (++) [s31]
- Analytics Agility (++) [s31]
- Manual Toil (-) [s31]
- Security (+) [s31]
- Data Quality (+) [s6, s31]
- Discovery (+) [s31]



## Decision: How to deploy a data product using subscriptions and workspaces?
**Evidences:** s36, s38, s43

**Context:** 

### **Solution Options**
#### Solution 1:  A single Subscription with a single workspace
**Evidences:** s36


#### Solution 2: A single Subscription with a single workspace with dedicated artifacts for each domain
**Evidences:** s36


#### Solution 3:  A Subscription with multiple workspaces
**Evidences:** s36


#### Solution 4: A single Azure Subscription with separate workspaces for each domain
**Evidences:** s43


#### Solution 5: Separate subscriptions with separate workspaces for each domain
**Evidences:** s38


#### **Next Decision**: How can the user interact with data products?
#### **Next Decision**: How to keep track of metadata?
#### **Next Decision**: How can we manage and provision the infrastucture
#### **Next Decision**: How can data products communicate?


# Forces: 
- Security [s1, s31]
- Meet SLAs [s22]
- Discoverability [s1, s15, s25, s32]
- Internal Complexity [s2]
- Complexity for User [s2]
- Accelerate Decision Making [s3]
- More granular data [s3]
- Understandability [s3]
- Prioritise [s3, s19]
- Standardised Transformation [s3, s19, s25]
- Duplication [s3, s15, s17, s25]
- Obscurity [s3, s19]
- Trustworthiness [s1, s3, s11]
- Interoperability [s1, s3, s9]
- Compliance [s7]
- Provenance []
- Data Accuracy [s6, s7]
- Completeness [s7]
- Integrity [s7]
- Multiple independent read-only views [s8]
- Re-use aspects by allowing other teams to find and build upon existing work [s15, s16, s21, s25]
- Time-to-Market [s15, s25]
- Conflicting definitions [s20]
- Execution at periodic intervals [s20]
- Consistently Applied Security [s20]
- Stability [s20]
- Turning the data lake into a swamp [s28]
- Data Productivity [s31]
- Analytics Agility [s31]
- Manual Toil [s31]
- Data Quality [s6, s31]
- Discovery [s31]
- Quickly gain knowledge on data set [s32]
- Fast data propagation [s41]
- Handle large data volumes [s41]
- Limit receptions [s41]
- Addressability of subscriptions [s41]
- Control over data schema [s17, s41]
- Real-time Data Access [s17, s20, s51]
- High fidelity [s51]
- Can be deployed in multiple environments [s51]
- Non-intrusive [s53]
- Consumption [s53]
- Production Grade Integrations [s53]
- Reproducibility [s54]
- Traceability [s54]
- Verifiability [s54]
- Unified [s4]
- Up-to-date [s4]
- Protected [s4]
- Accessible [s4, s5, s15]
- Addressable [s5, s17]
- Structured code [s6]
- Immutability [s8, s17]
- Bi-temporality of data [s8]
- Transparency [s11]
- User Experience [s11]
- Data Integration Speed [s2]
- Scalable [s17]


