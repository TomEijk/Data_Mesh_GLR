# API design


## Decision: How to Map a Domain Model and its Elements to an API?
**Evidences:** s1, s3, s4, s6, s8, s9, s10, s13, s14, s20, s21, s22, s23, s27, s29, s32

**Context:** Domain Model and API

### **Solution Options**
#### Solution 1: Expose the Whole Domain Model in 1:1 Relation as API
**Evidences:** s1, s3, s9

**Forces:**
- Brittle Interfaces (--) [s1, s23]
- Avoid Exposing Domain Model Details in API (-) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (+) [s3, s4]
- API Complexity (--) [s1, s6, s29]
- API Usability (-) [s1, s14]
- Minimize API calls (-) [s1]
- API Modifiability (-) [s1, s3, s4, s23]
- Design and Implementation Effort (+) [s3, s21, s23, s29]

#### Solution 2: Expose Domain Model Subset as API
**Evidences:** s3, s6, s9

**Forces:**
- Brittle Interfaces (o) [s1, s23]
- Avoid Exposing Domain Model Details in API (o) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (+) [s3, s4]
- API Complexity (o) [s1, s6, s29]
- API Usability (o) [s1, s14]
- Minimize API calls (-) [s1]
- API Modifiability (-) [s1, s3, s4, s23]
- Design and Implementation Effort (+) [s3, s21, s23, s29]

#### Solution 3: Expose Each Bounded Context as an API
**Evidences:** s1, s4, s13, s14, s20, s27, s29, s32

**Forces:**
- Brittle Interfaces (-) [s1, s23]
- Avoid Exposing Domain Model Details in API (-) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (-) [s3, s4]
- API Complexity (-) [s1, s6, s29]
- API Usability (-) [s1, s14]
- Minimize API calls (-) [s1]
- API Modifiability (-) [s1, s3, s4, s23]
- Design and Implementation Effort (+) [s3, s21, s23, s29]

#### Solution 4: Expose Selected Bounded Contexts as APIs
**Evidences:** s1, s3, s4, s13, s14, s20, s21, s22, s23, s27, s29, s32

**Forces:**
- Brittle Interfaces (o) [s1, s23]
- Avoid Exposing Domain Model Details in API (o) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (-) [s3, s4]
- API Complexity (o) [s1, s6, s29]
- API Usability (o) [s1, s14]
- Minimize API calls (-) [s1]
- API Modifiability (o) [s1, s3, s4, s23]
- Design and Implementation Effort (+) [s3, s21, s23, s29]

#### Solution 5: Introduce and Expose Interface Bounded Context as an API
**Evidences:** s1, s3, s23

**Forces:**
- Brittle Interfaces (+) [s1, s23]
- Avoid Exposing Domain Model Details in API (+) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (++) [s3, s4]
- API Complexity (+) [s1, s6, s29]
- API Usability (+) [s1, s14]
- Minimize API calls (+) [s1]
- API Modifiability (+) [s1, s3, s4, s23]
- Design and Implementation Effort (-) [s3, s21, s23, s29]

#### Solution 6: Expose a Shared Kernel between Client and Server as an API
**Evidences:** s1, s3

**Forces:**
- Brittle Interfaces (+) [s1, s23]
- Avoid Exposing Domain Model Details in API (+) [s1, s3, s4, s10, s29, s32]
- Clients Need to Manage Crossing Model Boundaries (++) [s3, s4]
- API Complexity (+) [s1, s6, s29]
- API Usability (+) [s1, s14]
- Minimize API calls (+) [s1]
- API Modifiability (+) [s1, s3, s4, s23]
- Design and Implementation Effort (-) [s3, s21, s23, s29]

#### **Next Decision**: Which Domain Model Elements Should be Offered as Resources or Endpoints in an API?
#### **Next Decision**: Which Approach is Chosen for Defining the API Contract in Relation to the Domain Model?


## Decision: Which Approach is Chosen for Defining the API Contract in Relation to the Domain Model?
**Evidences:** s1, s3, s5, s8, s10, s13, s14, s17, s18, s21, s25, s27, s30, s31, s32

**Context:** API Contract

### **Solution Options**
#### Solution 1: Explicitly Specify the API Contract
**Evidences:** s3, s8, s10, s13, s17, s18, s21, s30, s31, s32

**Forces:**
- Separation of API Contract and Domain Concerns (+) [s1, s3, s5, s10, s13, s30, s32]
- API Stability (+) [s10, s30, s31]
- Domain Model Flexibility (+) [s10]
- Initial Effort Required (o) [s17, s30, s31]
- API Modifiability (o) [s1, s3, s5, s17, s18, s30, s31]
- Maintainability of API and API Consumers (o) [s5, s10, s17, s30]
- Can Lead to Anemic Domain Model Anti-Pattern (o) [s8, s17]
- Support for External or Public Clients (++) [s18]

#### Solution 2: Extract API Contract from Domain Model
**Evidences:** s3, s10, s13, s17, s18

**Forces:**
- Separation of API Contract and Domain Concerns (+) [s1, s3, s5, s10, s13, s30, s32]
- API Stability (+) [s10, s30, s31]
- Domain Model Flexibility (+) [s10]
- Initial Effort Required (o) [s17, s30, s31]
- API Modifiability (o) [s1, s3, s5, s17, s18, s30, s31]
- Maintainability of API and API Consumers (o) [s5, s10, s17, s30]
- Can Lead to Anemic Domain Model Anti-Pattern (o) [s8, s17]
- Support for External or Public Clients (+) [s18]

#### Solution 3: Domain Model Defines API Contract
**Evidences:** s3, s10, s13, s18

**Forces:**
- Separation of API Contract and Domain Concerns (-) [s1, s3, s5, s10, s13, s30, s32]
- API Stability (--) [s10, s30, s31]
- Domain Model Flexibility (--) [s10]
- Initial Effort Required (o) [s17, s30, s31]
- API Modifiability (o) [s1, s3, s5, s17, s18, s30, s31]
- Maintainability of API and API Consumers (o) [s5, s10, s17, s30]
- Can Lead to Anemic Domain Model Anti-Pattern (o) [s8, s17]
- Support for External or Public Clients (o) [s18]

#### Solution 4: Bounded Context Defines API Contract
**Evidences:** s3, s13, s27

**Forces:**
- Separation of API Contract and Domain Concerns (-) [s1, s3, s5, s10, s13, s30, s32]
- API Stability (--) [s10, s30, s31]
- Domain Model Flexibility (--) [s10]
- Initial Effort Required (o) [s17, s30, s31]
- API Modifiability (o) [s1, s3, s5, s17, s18, s30, s31]
- Maintainability of API and API Consumers (o) [s5, s10, s17, s30]
- Can Lead to Anemic Domain Model Anti-Pattern (o) [s8, s17]
- Support for External or Public Clients (o) [s18]

#### Solution 5: Write API Code First which Defines the Contract
**Evidences:** s17, s30

**Forces:**
- Separation of API Contract and Domain Concerns (--) [s1, s3, s5, s10, s13, s30, s32]
- API Stability (--) [s10, s30, s31]
- Domain Model Flexibility (--) [s10]
- Initial Effort Required (++) [s17, s30, s31]
- API Modifiability (-) [s1, s3, s5, s17, s18, s30, s31]
- Maintainability of API and API Consumers (-) [s5, s10, s17, s30]
- Can Lead to Anemic Domain Model Anti-Pattern (--) [s8, s17]
- Support for External or Public Clients (--) [s18]

#### **Next Decision**: How to Map a Domain Model and its Elements to an API?


## Decision: Which Domain Model Elements Should be Offered as Resources or Endpoints in an API?
**Evidences:** s1, s2, s5, s6, s9, s10, s12, s13, s14, s16, s17, s18, s19, s20, s21, s25, s26, s27, s28, s29, s32

**Context:** Identified Interface Elements

### **Solution Options**
#### Solution 1: Entities as API Resources
**Evidences:** s1, s2, s5, s6, s12, s13, s14, s16, s17, s18, s19, s21, s32

**Forces:**
- Avoid Exposing Domain Model Details in API (--) [s1, s2, s5, s10, s17, s18, s29, s32]
- Data Consistency (--) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Chatty API (-) [s1, s5, s18]
- Performance (-) [s1, s16, s18]
- Scalability (-) [s1, s5, s16, s18, s20, s28, s29]
- API Complexity (-) [s1, s5, s6, s12, s18, s25, s29]
- Maintainability of API and API Consumers (-) [s5, s6, s10, s17, s29]
- Reliability (-) [s5]
- Coupling of Clients to Server (-) [s2, s5, s6, s10, s14, s18, s20, s27]

#### Solution 2: Domain Services as API Resources
**Evidences:** s9, s13, s19

**Forces:**
- Avoid Exposing Domain Model Details in API (o) [s1, s2, s5, s10, s17, s18, s29, s32]
- Data Consistency (+) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Chatty API (o) [s1, s5, s18]
- Performance (++) [s1, s16, s18]
- Scalability (++) [s1, s5, s16, s18, s20, s28, s29]
- API Complexity (+) [s1, s5, s6, s12, s18, s25, s29]
- Maintainability of API and API Consumers (+) [s5, s6, s10, s17, s29]
- Reliability (+) [s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s10, s14, s18, s20, s27]

#### Solution 3: Aggregate Roots as API Resources
**Evidences:** s1, s2, s5, s6, s10, s12, s13, s17, s18, s19, s25, s26, s27, s28

**Forces:**
- Avoid Exposing Domain Model Details in API (+) [s1, s2, s5, s10, s17, s18, s29, s32]
- Data Consistency (++) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Chatty API (+) [s1, s5, s18]
- Performance (+) [s1, s16, s18]
- Scalability (+) [s1, s5, s16, s18, s20, s28, s29]
- API Complexity (+) [s1, s5, s6, s12, s18, s25, s29]
- Maintainability of API and API Consumers (+) [s5, s6, s10, s17, s29]
- Reliability (+) [s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s10, s14, s18, s20, s27]

#### Solution 4: Bounded Contexts as API Resources
**Evidences:** s1, s2, s5, s20, s25, s26, s29

**Forces:**
- Avoid Exposing Domain Model Details in API (+) [s1, s2, s5, s10, s17, s18, s29, s32]
- Data Consistency (o) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Chatty API (+) [s1, s5, s18]
- Performance (+) [s1, s16, s18]
- Scalability (+) [s1, s5, s16, s18, s20, s28, s29]
- API Complexity (-) [s1, s5, s6, s12, s18, s25, s29]
- Maintainability of API and API Consumers (o) [s5, s6, s10, s17, s29]
- Reliability (o) [s5]
- Coupling of Clients to Server (o) [s2, s5, s6, s10, s14, s18, s20, s27]

#### Solution 5: Domain or Business Processes as API Resources
**Evidences:** s5, s10, s20

**Forces:**
- Avoid Exposing Domain Model Details in API (+) [s1, s2, s5, s10, s17, s18, s29, s32]
- Data Consistency (++) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Chatty API (+) [s1, s5, s18]
- Performance (+) [s1, s16, s18]
- Scalability (+) [s1, s5, s16, s18, s20, s28, s29]
- API Complexity (+) [s1, s5, s6, s12, s18, s25, s29]
- Maintainability of API and API Consumers (+) [s5, s6, s10, s17, s29]
- Reliability (+) [s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s10, s14, s18, s20, s27]

#### **Next Decision**: Segregate Resources for Reading and Updating Information in an API?
#### **Next Decision**: How to Design the Operations of a Resource?
#### **Next Decision**: How to Map Links between Domain Model Elements to the API?


## Decision: Segregate Resources for Reading and Updating Information in an API?
**Evidences:** s5, s6, s8, s11, s12, s15, s16, s24, s25, s27, s28

**Context:** Identified Interface Elements

### **Solution Options**
#### Solution 1: Expose Segregated Command and Query Resources in API
**Evidences:** s5, s6, s8, s11, s12, s15, s16, s24, s25, s27, s28

**Forces:**
- API Complexity (-) [s5, s6, s11, s12, s15, s25]
- Data Consistency (-) [s5, s12, s16, s25, s27, s28]
- Scalability (+) [s5, s8, s11, s16, s24, s28]
- Eventual Consistency Support (+) [s5, s15, s16, s24, s25, s27, s28]

#### Solution 2: Do Not Segregate Queries and Commands in an API
**Evidences:** s5, s6, s8, s11, s12, s15, s16, s24, s25, s27, s28

**Forces:**
- API Complexity (+) [s5, s6, s11, s12, s15, s25]
- Data Consistency (+) [s5, s12, s16, s25, s27, s28]
- Scalability (-) [s5, s8, s11, s16, s24, s28]
- Eventual Consistency Support (-) [s5, s15, s16, s24, s25, s27, s28]



## Decision: How to Design the Operations of a Resource?
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s14, s15, s16, s17, s18, s19, s20, s21, s24, s25, s26, s27, s28, s29

**Context:** Operation

### **Solution Options**
#### Solution 1: CRUD-Style Operations on Resources
**Evidences:** s1, s2, s3, s5, s6, s7, s8, s10, s11, s12, s14, s15, s16, s17, s18, s19, s20, s21, s29

**Forces:**
- Avoid Exposing Domain Model Details in API (-) [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29]
- Chatty API (--) [s1, s5, s11, s18]
- Performance (--) [s1, s11, s16, s18]
- Scalability (--) [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- Interface Design Limits Domain Model Design (-) [s3, s10]
- Maintainability of API and API Consumers (-) [s5, s6, s7, s10, s17, s29]
- Data Consistency (-) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Reliability (-) [s4, s5]
- Coupling of Clients to Server (-) [s2, s5, s6, s8, s10, s14, s18, s20, s27]
- API Understandability (+) [s6, s7, s15, s16, s17]

#### Solution 2: Domain Operations on Resources
**Evidences:** s1, s2, s3, s4, s5, s6, s7, s9, s10, s11, s12, s15, s16, s18, s20, s25

**Forces:**
- Avoid Exposing Domain Model Details in API (+) [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29]
- Chatty API (+) [s1, s5, s11, s18]
- Performance (+) [s1, s11, s16, s18]
- Scalability (+) [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- Interface Design Limits Domain Model Design (+) [s3, s10]
- Maintainability of API and API Consumers (+) [s5, s6, s7, s10, s17, s29]
- Data Consistency (+) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Reliability (+) [s4, s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s8, s10, s14, s18, s20, s27]
- API Understandability (+) [s6, s7, s15, s16, s17]

#### Solution 3: Encode Operations as Commands in the Payload
**Evidences:** s6, s15, s16

**Forces:**
- Avoid Exposing Domain Model Details in API (+) [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29]
- Chatty API (+) [s1, s5, s11, s18]
- Performance (+) [s1, s11, s16, s18]
- Scalability (+) [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- Interface Design Limits Domain Model Design (+) [s3, s10]
- Maintainability of API and API Consumers (o) [s5, s6, s7, s10, s17, s29]
- Data Consistency (+) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Reliability (+) [s4, s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s8, s10, s14, s18, s20, s27]
- API Understandability (-) [s6, s7, s15, s16, s17]

#### Solution 4: Expose Domain Events as State Transitions
**Evidences:** s2, s3, s4, s5, s9, s11, s12, s14, s16, s20, s24, s25, s26, s27, s28, s29

**Forces:**
- Avoid Exposing Domain Model Details in API (++) [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29]
- Chatty API (+) [s1, s5, s11, s18]
- Performance (+) [s1, s11, s16, s18]
- Scalability (++) [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- Interface Design Limits Domain Model Design (+) [s3, s10]
- Maintainability of API and API Consumers (+) [s5, s6, s7, s10, s17, s29]
- Data Consistency (+) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Reliability (+) [s4, s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s8, s10, s14, s18, s20, s27]
- API Understandability (-) [s6, s7, s15, s16, s17]

#### Solution 5: Expose Domain Events via Feeds or Pub/Sub
**Evidences:** s2, s20, s24, s27, s28

**Forces:**
- Avoid Exposing Domain Model Details in API (++) [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29]
- Chatty API (+) [s1, s5, s11, s18]
- Performance (+) [s1, s11, s16, s18]
- Scalability (++) [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- Interface Design Limits Domain Model Design (+) [s3, s10]
- Maintainability of API and API Consumers (+) [s5, s6, s7, s10, s17, s29]
- Data Consistency (+) [s1, s2, s5, s10, s12, s16, s18, s20, s21, s25, s27, s28, s29]
- Reliability (+) [s4, s5]
- Coupling of Clients to Server (+) [s2, s5, s6, s8, s10, s14, s18, s20, s27]
- API Understandability (-) [s6, s7, s15, s16, s17]



## Decision: How to Map Links between Domain Model Elements to the API?
**Evidences:** s1, s2, s3, s8, s10, s14, s18, s31

**Context:** Link

### **Solution Options**
#### Solution 1: None
**Evidences:** s1, s2, s31


#### Solution 2: Use Distributed or Hypermedia Links in the Payload
**Evidences:** s1, s2, s3, s8, s10, s18, s31

**Forces:**
- Data Consistency (+) [s1, s2, s10, s18]
- API Evolvability (+) [s1, s18, s31]
- API Modifiability (+) [s1, s3, s18, s31]
- Message Size (++) [s1]
- Avoid Exposing Domain Model Details in API (++) [s1, s2, s3, s10, s18]
- Coupling of Clients to Server (++) [s2, s8, s10, s14, s18]
- Protocol Complexity in Client (-) [s2, s8, s10]
- Minimize API calls (-) [s1, s2]
- Performance (-) [s1, s18]
- Scalability (-) [s1, s8, s18]

#### Solution 3: Pass Object Identifiers in the Payload
**Evidences:** s1, s2, s18, s31

**Forces:**
- Data Consistency (+) [s1, s2, s10, s18]
- API Evolvability (+) [s1, s18, s31]
- API Modifiability (+) [s1, s3, s18, s31]
- Message Size (++) [s1]
- Avoid Exposing Domain Model Details in API (-) [s1, s2, s3, s10, s18]
- Coupling of Clients to Server (-) [s2, s8, s10, s14, s18]
- Protocol Complexity in Client (+) [s2, s8, s10]
- Minimize API calls (-) [s1, s2]
- Performance (-) [s1, s18]
- Scalability (-) [s1, s8, s18]

#### Solution 4: Embed Linked Data in the Payload
**Evidences:** s1, s2

**Forces:**
- Data Consistency (-) [s1, s2, s10, s18]
- API Evolvability (-) [s1, s18, s31]
- API Modifiability (-) [s1, s3, s18, s31]
- Message Size (-) [s1]
- Avoid Exposing Domain Model Details in API (o) [s1, s2, s3, s10, s18]
- Coupling of Clients to Server (+) [s2, s8, s10, s14, s18]
- Protocol Complexity in Client (+) [s2, s8, s10]
- Minimize API calls (+) [s1, s2]
- Performance (+) [s1, s18]
- Scalability (+) [s1, s8, s18]



## Decision: How can the user interact with data products?
**Evidences:** 

**Context:** 

### **Solution Options**


## Decision: What type of data product can be developed?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Expose Data Product as Raw Data
**Evidences:** 

**Forces:**
- Internal Complexity (++) []
- Complexity for User (--) []

#### Solution 2: Expose Data Product as Derived Data
**Evidences:** 

**Forces:**
- Internal Complexity (+) []
- Complexity for User (-) []

#### Solution 3: Expose Data Product as Decision Support Model
**Evidences:** 

**Forces:**
- Internal Complexity (-) []
- Complexity for User (+) []

#### Solution 4: Expose Data Product as Automated Decision-making Model
**Evidences:** 

**Forces:**
- Internal Complexity (--) []
- Complexity for User (++) []

#### Solution 5: Expose Data Product as an algorithm
**Evidences:** 

**Forces:**
- Internal Complexity (o) []
- Complexity for User (o) []

#### **Next Decision**: How to deploy a data product using subscriptions and workspaces?
#### **Next Decision**: What is the anatomy of a Data Product?


## Decision: How to make data products discoverable?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Register datasets
**Evidences:** 

**Forces:**
- Security (+) []
- Discoverability (++) []

#### Solution 2: Fine-grained Access Control
**Evidences:** 

**Forces:**
- Security (++) []
- Discoverability (o) []

#### Solution 3: Discovery Port
**Evidences:** 


#### Solution 4: Data Marketplace
**Evidences:** 




## Decision: How to keep track of metadata?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Data Catalogue
**Evidences:** 

**Forces:**
- Standardised Transformation (+) []
- Duplication (-) []
- Obscurity (-) []

#### Solution 2: Use example notebooks or SQL queries to describe the dataset
**Evidences:** 

**Forces:**
- Discoverability (+) []
- Quickly gain knowledge on data set (++) []

#### Solution 3: Change Data Capture
**Evidences:** 

**Forces:**
- Real-time Data Access (+) []
- Complexity for User (-) []
- Non-intrusive (+) []
- Consumption (+) []
- Production Grade Integrations (+) []

#### Solution 4: Virtualisation
**Evidences:** 


#### Solution 5: Data Product Governance
**Evidences:** 

**Forces:**
- Turning the data lake into a swamp (-) []

#### Solution 6: Immutable Change Audit Log
**Evidences:** 

**Forces:**
- Reproducibility (+) []
- Traceability (+) []
- Verifiability (+) []

#### Solution 7: Lineage Repository
**Evidences:** 


#### Solution 8: Universal Metadata Registry
**Evidences:** 


#### Solution 9: Central Data Product Catalogue
**Evidences:** 

**Forces:**
- Discoverability (+) []



## Decision: How to make a data product trustworty?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Provide a single integrated experience for monitoring
**Evidences:** 


#### Solution 2: The observability plane brings an interface between built-in observability of the data quantum and REST clients
**Evidences:** 

**Forces:**
- Understandability (+) []
- Accuracy (+) []
- Completeness (+) []
- Integrity (+) []

#### Solution 3: Schema Manager
**Evidences:** 

**Forces:**
- Understandability (+) []
- Duplication (+) []
- Conflicting definitions (-) []

#### Solution 4: Maintaining a single source of truth
**Evidences:** 


#### Solution 5: Run tests on your data product
**Evidences:** 


#### Solution 6: Time-bounded Backwards Compatibility
**Evidences:** 




## Decision: How can the user interact with data products?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Attach a Data Access REST API to each Data Product
**Evidences:** 

**Forces:**
- Internal Complexity (+) []
- Complexity for User (-) []
- Control over data schema (+) []

#### Solution 2: Attach a SQL layer to each Data Product
**Evidences:** 

**Forces:**
- Internal Complexity (+) []
- Complexity for User (+) []
- Accelerate Decision Making (++) []
- More granular data (++) []

#### Solution 3: NoSQL system
**Evidences:** 




## Decision: What is the anatomy of a Data Product?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: The domain datasets belong to a specific domain
**Evidences:** 

**Forces:**
- Prioritise (+) []

#### Solution 2: Core datasets are those that are useful for more than one domain
**Evidences:** 

**Forces:**
- Prioritise (+) []
- Trustworthiness (+) []
- Interoperability (+) []

#### Solution 3: Low level events and aggregation layer
**Evidences:** 


#### Solution 4: Feature Layer
**Evidences:** 

**Forces:**
- Interoperability (+) []
- Stability (+) []

#### Solution 5: Open source data and analytics processing service
**Evidences:** 


#### Solution 6: Control Plane
**Evidences:** 


#### **Next Decision**: Where can we store the data?
#### **Next Decision**: How to make a data product trustworty?
#### **Next Decision**: How to secure your data products?
#### **Next Decision**: How to make data products discoverable?


## Decision: How can data products communicate?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Event Streaming
**Evidences:** 

**Forces:**
- Real-time Data Access (+) []
- High fidelity (+) []

#### Solution 2: Use a data integration service that helps users efficiently build and manage ETL/ELT pipelines
**Evidences:** 


#### Solution 3: Triggering
**Evidences:** 


#### Solution 4: CQRS
**Evidences:** 

**Forces:**
- Multiple independent read-only views (+) []

#### Solution 5: end-to-end connection
**Evidences:** 


#### Solution 6: Create a component for unified batch and stream data processing
**Evidences:** 

**Forces:**
- Execution at periodic intervals (+) []

#### Solution 7: Event Bus
**Evidences:** 


#### Solution 8: Pub/Sub
**Evidences:** 

**Forces:**
- Fast data propagation (+) []
- Handle large data volumes (++) []
- Limit receptions (+) []
- Addressability of subscriptions (+) []

#### Solution 9: Indirect data publishing and consumption
**Evidences:** 


#### Solution 10: Send snapshots via ETL
**Evidences:** 

**Forces:**
- Control over data schema (+) []



## Decision: How to secure your data products?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Role-based Access Control
**Evidences:** 


#### Solution 2: Encryption
**Evidences:** 


#### Solution 3: Open Access
**Evidences:** 


#### Solution 4: Attribute-based Access Control
**Evidences:** 


#### Solution 5: Zero Trust Architecture
**Evidences:** 


#### Solution 6: OAUTH2
**Evidences:** 




## Decision: Where can we store the data?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Internal storages where the data product is deployed, not exposed to consumers
**Evidences:** 


#### Solution 2: Implement a highly available in-memory cache
**Evidences:** 


#### Solution 3: Incrementally build business process-centric data marts
**Evidences:** 




## Decision: How can we manage and provision the infrastucture
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1: Infrastructure as Code
**Evidences:** 

**Forces:**
- Compliance (+) []
- Provenance (+) []
- Discoverability (+) []
- Re-use aspects by allowing other teams to find and build upon existing work (+) []
- Time-to-Market (+) []
- Duplication (+) []

#### Solution 2:  CI/CD process
**Evidences:** 

**Forces:**
- Can be deployed in multiple environments (+) []

#### Solution 3: Versioning
**Evidences:** 

**Forces:**
- Can be deployed in multiple environments (+) []

#### Solution 4: K8s
**Evidences:** 


#### Solution 5: Master Data Management
**Evidences:** 


#### Solution 6: Run containers that are invocable via requests or events
**Evidences:** 


#### Solution 7: orchestration
**Evidences:** 

**Forces:**
- Consistency (+) []

#### Solution 8: Templated Data Pipeline
**Evidences:** 


#### Solution 9: Centrally manage, monitor, and govern data across data lakes, data warehouses, and data marts
**Evidences:** 

**Forces:**
- Data Productivity (++) []
- Analytics Agility (++) []
- Manual Toil (-) []
- Security (+) []
- Quality (+) []
- Discovery (+) []



## Decision: How to deploy a data product using subscriptions and workspaces?
**Evidences:** 

**Context:** 

### **Solution Options**
#### Solution 1:  A single Subscription with a single workspace
**Evidences:** 


#### Solution 2: A single Subscription with a single workspace with dedicated artifacts for each domain
**Evidences:** 


#### Solution 3:  A Subscription with multiple workspaces
**Evidences:** 


#### Solution 4: A single Azure Subscription with separate workspaces for each domain
**Evidences:** 


#### Solution 5: Separate subscriptions with separate workspaces for each domain
**Evidences:** 


#### **Next Decision**: How can the user interact with data products?
#### **Next Decision**: How to keep track of metadata?
#### **Next Decision**: How can we manage and provision the infrastucture
#### **Next Decision**: How can data products communicate?


# Forces: 
- Brittle Interfaces [s1, s23]
- Avoid Exposing Domain Model Details in API [s1, s2, s3, s4, s5, s7, s10, s17, s18, s29, s32]
- Chatty API [s1, s5, s11, s18]
- Minimize API calls [s1, s2]
- Performance [s1, s11, s16, s18]
- Scalability [s1, s4, s5, s8, s11, s16, s18, s20, s24, s28, s29]
- API Complexity [s1, s5, s6, s11, s12, s15, s18, s25, s29]
- API Usability [s1, s5, s14]
- API Evolvability [s1, s5, s18, s31]
- API Modifiability [s1, s3, s4, s5, s17, s18, s23, s30, s31]
- Data Consistency [s1, s2, s5, s10, s12, s16, s18, s20, s21, s22, s25, s27, s28, s29]
- Message Size [s1]
- Coupling of Clients to Server [s2, s5, s6, s8, s10, s14, s18, s20, s22, s23, s27]
- Protocol Complexity in Client [s2, s8, s10]
- Design and Implementation Effort [s3, s21, s23, s29, s30]
- Interface Design Limits Domain Model Design [s3, s10]
- Clients Need to Manage Crossing Model Boundaries [s3, s4]
- Maintainability of API and API Consumers [s5, s6, s7, s10, s17, s29, s30]
- Reliability [s4, s5]
- Eventual Consistency Support [s5, s15, s16, s24, s25, s27, s28]
- Separation of API Contract and Domain Concerns [s1, s3, s5, s10, s13, s24, s29, s30, s32]
- API Understandability [s6, s7, s15, s16, s17, s30, s31, s32]
- Can Lead to Anemic Domain Model Anti-Pattern [s8, s17]
- API Stability [s10, s23, s30, s31]
- Domain Model Flexibility [s10]
- Initial Effort Required [s17, s30, s31]
- Support for External or Public Clients [s18]
- Security []
- Discoverability []
- Internal Complexity []
- Complexity for User []
- Accelerate Decision Making []
- More granular data []
- Understandability []
- Prioritise []
- Standardised Transformation []
- Duplication []
- Obscurity []
- Trustworthiness []
- Interoperability []
- Compliance []
- Provenance []
- Accuracy []
- Completeness []
- Integrity []
- Multiple independent read-only views []
- Re-use aspects by allowing other teams to find and build upon existing work []
- Time-to-Market []
- Conflicting definitions []
- Execution at periodic intervals []
- Consistency []
- Stability []
- Turning the data lake into a swamp []
- Data Productivity []
- Analytics Agility []
- Manual Toil []
- Quality []
- Discovery []
- Quickly gain knowledge on data set []
- Fast data propagation []
- Handle large data volumes []
- Limit receptions []
- Addressability of subscriptions []
- Control over data schema []
- Real-time Data Access []
- High fidelity []
- Can be deployed in multiple environments []
- Non-intrusive []
- Consumption []
- Production Grade Integrations []
- Reproducibility []
- Traceability []
- Verifiability []


