## Software Requirements

How to gather, analyze, and trace requirements through the software development cycle.

System engineering:
System engineering involves several phases, beginning in conception and ending in the final product, followed by maintenance.

Constituents of a system:
1. Software
	* Data Structures and Algorithms
	* Design and Architecture
	* Documentation & Test Cases
2. Hardware
3. People
4. Database
5. Documentation for the system eg. user manual

System requirements can be of 2 types, whether it is a
* Customer funded project (requirements provided by customer)
* product for the market (market research is done which leads to market requirements document, potential user base and their preference of technologies like mobile/web interface are researched)

Market requirements document is refined into a system requirements document (example, which OS? Android or iOS or both etc).

System Requirement Document:
1. Product requirements specifications - represent the functionalities of the product as a whole. Example: BookMyShow's product specification could be to allow booking and cancellation of tickets for movies, events, plays and sports.
2. System requirements specifications - SysRS. System constitutes hardware, software, people, database and documentation.
3. Hardware requirements specifications - example, specifications of the server the website needs to run on.
4. Software requirements specifications - what all features need to be developed for the particular software application
5. Functional requirements specifications - describe the functions of a system.

For example, IRCTC website:
1. Product requirement specification: ticket booking & cancellation, booking accomodation (hotels), catering services booking.
2. System requirement specification: hosted only through a web interface (no mobile app)
3. Functional requirement specification: advance ticket reservation, tatkal reservation etc.
4. Hardware requirement specification: internal memory requirements, number of clients to be supported
5. Software requirement specification: for a selected date & destination, display all existing trains irrespective of seat availability

Focus will be on software requirements.
These specifiations often overlap. Tatkal booking facility can come under both functional and software requirement specifications.

**Software Requirement Specification (SRS)**
An agreement between all stakeholders about the expectations from the software.

Requirements engineering:
1. use of time-tested established techniques & principles
2. use of languages & tools to document the requirements
3. baselining requirements
4. tracking the requirements

Why?
1. to understand customer's needs
2. to assess feasibility
3. to negotiate a reasonable solution
4. to specify an unambiguous solution
5. to validate the specifications
6. to manage specifications with ongoing development

4 broad steps in requirements engineering:
1. Requirements gathering
	* identify elicitation methods:eg. interviews, surveys, brainstorming sessions with stakeholders
	* identify the business & technical needs
	* identify the key people
	* identify the domain & operational constraints (how big the database will be? & so on)
	* create usage scenarios 
2. Requirements organization
3. Negotiation & discussion (requirements analysis)
4. Requirements specifications

Result of requirement gathering process for IRCTC, example:
1. Scope
	* only online reservation & cancellation
	* can cancel tickets only booked online
	* only desktop version of the website needs to be developed
2. Technical environment:
	* single database for both online & offline booking or more?
3. Usage scenarios:
	* agent booking features - number of tickets one can book
	* user booking features - number of tickets one can book

There are multiple ways to document requirements:
1. Using graphical models (uml use-cases, activity diagrams)
2. using formal models (z, finite state machines, B methods)
3. prototypes
4. usage scenarios / user stories
5. text

After requirement elicitation, organise requirements & then analyse them.

Organising requirements:
1. categorise requirements - hardware or product or software requirement
2. prioritse requirements - how critical is each requirement?

Analysing requirements:
1. is requirement consistent with overall objective of the sytem - no contradictory requirements
2. is the requirement complete or incomplete - (fast is 10 ms or 5 secs)


**Feature creep**: addition of new features in a product due to customer demands and market competition. This can cause compatibility issues, resulting in addition of features. Can result in bloated software. This is addition of requirements after the development phase has started.

Software requirements can be split into:
1. Functional requirements - behavior of a system in terms of its inputs & outputs.
2. Non-functional requirements - refers to quality aspect of a system. (fast response time, clean website etc.)
	* secure, safe, usability, maintainable, reliable, scalable

Example for IRCTC:
Functional requirements: login should be through user ID, password, captcha. After login, user should be directed to welcome screen with booking options. Check availability before booking confirmation.

Non-functional requirements: welcome screen should be loaded within 3 seconds, system should be able to handle a peak load of 1 million users, card details to be accepted only after bank authorisation (secure system)

**Tracking requirements / requirements traceability**
Popular tool is Requirements Traceability Matrix (RTM).
Tracks data of requirements through all phases of development, from baselining till test time. It is referred to at very stage of the process to make sure every requirement maps to a feature and every feature maps to a requirement.
RTM benefits:
1. change impact analysis - which part of the test cases can be reused, which have to re-written
2. regression testing
3. coverage analysis - set of test cases written for requirement 1 can be reused for requirement 2


Start building the RTM after finalising the requirements.

******************************

### Use Cases & Scenarios

Use cases are the next step of the design process, after requirements engineering. Use cases integrate the requirements into a comprehensive package that describes the interaction of the user with the system.

Use case is a list of actions or steps of a software system that involve interactions between a user and the system to achieve a specified goal.

We call the users of the software system as actors. It could be humans, sensors, databases, network ports.

Subject of a use case is the functionality that defines and represents boundaries of business, software system, physical system or device. Example: banking system is a subject which includes use cases like transfer funds, manage accounts etc.

Subject or a system boundary is presented by a rectangle with subject's name. Use cases are inside the rectange and actors are outside the rectangle.

Use Case Analysis:
1. How will the software be used by the users?
2. Who are the users?

Elements of a use case:
1. Actors: any entity interacting with the software/system. Actors can be a person, an organisation, a software/hardware system, another program etc.
2. Goals: functionality that is achieved by the use case
3. Flow: what happens when everything goes right & the use case achieves its goal
4. Associations/relationships: various relationships that relate the system & its components to the actors

Use cases are organised using the following relationships:
1. Generalisation
_Withdraw Cash_ is a generalisation of _Bank ATM transaction_. Base use case could be abstract (incomplete) or concrete (complete). Specialised use case is required if base use case is abstract.
2. Extend
_Help_ is an extended use case of _Bank ATM transaction_. Base use case is complete (concrete) by itself, defined independently. Extending use case is optional.
3. Include
_Bank ATM transaction_ includes _customer authentication_. Base use case is incomplete (abstract use case). Included use case is required.


Good use case:
1. should describe both functionality & result
2. should focus only on requirements & not design elements
3. fix a particular style of writing use cases
4. if there are several flows of the functionality, it is ideal to have a main flow and others as alternate
5. should not have too many CRUD activaties


Styles of writing a use case:
1. graphical style
2. textual style:
	* title
	* actor(s)
	* scope & description
	* stakeholders
	* pre-conditions (eg. menu showed should be from geographically closer restaurants)& triggers
	* post-conditions (eg. feedback from users)
	* flow


Use case should not hold the information about the software design. Also, it should not specify the scale & architecture of the project. These are technical details which should be discussed at a later stage after you have written & defined a use case.


Requirements Vs Use Cases:
A requirement is a general statement that specifies a desired property of a software. A use case is more specific than a requirement. It either implies a requirement or it can be derived from a requirement.
A requirement can be elaborated into several different use cases. Requirements can be non-functional too. Use cases talk about the functionality of a system as a user interacts with the system.


**Scenarios**
1. Scenarios capture the system behavior as is viewed from an outsider, from a user's point of view
2. Captures a real life situation where the end user, a customer, interacts with the system
3. involve the failure aspects & various situations that can happen as the customer interacts & uses the system or a product
4. useful for analysing the requirement because they consider on the flow of how the system agrees & not on a specific functionality
5. can talk about the functionality of the system in a view broader than that of a use case

The Main Success Scenario (MSS) is listed down differently, and the alternate & failure situations are handled differently. MSS is the scenario & steps when everything is going as expected and finally the goal of the use case is achieved.


Use Case vs Scenario:
1. A use case depicts an interaction that a user, as an actor, has with a system. A scenario is the whole sequence of interactions that user has with the system along with the alternates that a use case can go through.

2. A use case involves one main actor & constitutes one functionality that describes how the actor interacts. A scenario may include failure aspects & alternate behavior until the functionality of the system is achieved.


**User Stories**
A very high-level definition of a requirement containing just enough information so that developers can produce a reasonable estimate of the effort to implement it. Used in agile software development to capture a description of a software ffeature from an end-user perspective. The user story describes the type of user, what they want & why.

Example of a user story for authentication & login to a website: "As a user, you should be able to login to a website by your username & password to access the features provided by the website"


Example of a use case for authentication:
1. Use case name: Authenticate on a website
2. Actor: user who wants to login on the website
3. Scope: this use case allows the user to login to the system
4. Stakeholders: None
5. Pre-conditions: the user should have a valid account on the website
6. Post-conditions: the user should see the relevant homepage
7. Flow:
	* the user types the username
	* the user types the password
	* system checks the login credentials are valid
	* system creates a session for the user and provides access to the user


Software requirement is required to maintain coherence between initial need for software, the conceptualised design of the software & the final software.


Adding test cases to user requirements increases reliability as you can predict the way of using requirement & by determining the expected behavior of the system. Test cases bring clarity and also uncover the edge cases which can be hard to identify.


**Additional Points**
The significance of using 'include' relationship in use case diagram is to isolate redundant events flows that are shared by multiple use cases.
Refer [this](https://www.uml-diagrams.org/use-case-include.html).


Airbag control can be an optional use case for the software system for driving the car. It is not mandatory for the system to control the airbags but can be provided. So this is "extends" relationship between both the use casses.


