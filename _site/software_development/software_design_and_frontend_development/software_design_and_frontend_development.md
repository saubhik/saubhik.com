#### Software Design and front-end development

Software architecture analyses the system requirements and provides a high-level design. Decomposes
the software into sub-systems and studying their interaction.

Software architecture is global organisation of software system that helps in:
1. Division into sub-divisions, and thus helps in understanding the system
2. Sets the policies & definition of interactions
3. defines the constraints of the system (risk of data leak, data protection methods etc.)
4. acts as key communication between stakeholders
5. faster implementations of new changes

Strong dependency between software components in an application is not desired:
1. reduced scalability: any new function added will impact all the components
2. implementation of new features becomes difficult
3. reduced stability

Design patterns are associated with code commonalities.
Software architecture is associated with structure & organisation of high-level sub-systems of 
a system.

Decomposition is breaking down large software component into smaller, independent parts. Risk
and complexity in development is reduced.

Cohesion is a measure of the relatedness within a module. High cohesion reduces module complexity,
and increases stability. Coupling measures how the software components are interdependent. Low
coupling is a simpler software.

Circular dependency: whenever two components are invoking each other. This increases the
interdependence. Not desired.

Qualities of a good software architecture:
1. simple
2. decomposed to the maximum possible extent
3. low coupling
4. high cohesion
5. separation of concerns (each module, or sub-system, or component should have a well-defined
purpose)
6. no circular dependency (module A can call module B, but not vice versa)

Attributes contain information about the design and development of a component. Connectors
define the relationship between the different components of a software architecture.

Modules are components that can be built & deployed independently of the system. They are
connected to the application through well defined entry points and interfaces.

Components are critical to the functioning of the software application; their addition or 
removal has a huge impact on the application. On the other hand, modules usually add additional 
functionalities to the application, and their addition or removal has minimal effect on the 
application.

Modular architecture:
1. independent modules can be deployed independently
2. increased extensibility
3. lesser dependencies in the application
4. increased stability

Components perform the basic operations, such as adding a heading, body, or footer in the 
WordPress blog. Modules, on the other hand, are independent pieces of an application that 
add some function to the application. The addition of a theme to the WordPress blog, as you 
saw in the video, is one example. 

Another distinction between the two is that components are critical to the functioning of 
the application, while modules may or may not be. Take the example of a mobile phone. When 
you are designing the architecture of a mobile phone, the ROM, battery, LCD, etc. will be the 
components, while the headphones, memory cards, sim cards, etc. will act as modules. Any 
addition or deletion of the modules will have minimal impact on the application, whereas 
the same will not be the case with components.

WhatsApp example: Suppose that you built the main application such that the core structure 
consists of only users and conversations. The media component is connected through the 
Media_ID to the conversations. The media component is built independently of the main 
application such that it is up to to the discretion of the user to use the media or not. 
This acts as a module in the WhatsApp application. 

An architectural style is a high-level design guide or framework that provides guidelines,
framework and a solution for implementing the software architecture.

Design patterns are localised, architectural patterns are global.

Benefits of architectural styles:
1. basic understanding of system
2. decomposition is done into interacting agents
3. implementation can be used in other problems as well

Commonly used architectural styles:
1. component based
2. layered
3. client server
4. peer to peer
5. event bus

whatsapp, the architecture above, is component-based: consisting of components, connectors, and
interfaces. Objective is reusability of components in an application.

client server: server and multiple clients, server provides the services as per clients' 
requests. eg. internet

Advantages of the client-server style are as follows:
1. Information can be fetched at any point of time
2. Information doesn’t depend on any peer computer   
3. It is beneficial for building collaborative projects
4. It is useful in accessing files remotely
5. It eases the burden on the client to act as a server
6. It enhances the security of the network

Peer to peer: role of client, server gets interchanged. Any node can become a super-node. They
act as servers. Roles can change dynamically, via an algorithm. Peer-to-peer is mainly used in 
file sharing and messaging applications where security is extremely important and transfer 
through a third party server is not desired. 

Layered: Decomposed into layers. One layer provides service to the next higher layer. Main aim
is to create layers that have a specific role and no logical interdependence with other layers.
Separation of concern. Also closed layer structure. If A -> B -> C, A cannot directly send
request to C.

Event driven: consists of source, event listener, channel, notifier. Used when there is a need
to capture the change in state of a system. Loosely coupled, high scalability, asynchronous.
Code is scattered and retrieved via asynchronous callbacks.

Reference Architecture: 
Domain-specific template that is used to build a general set of requirements to build the 
software application. It describes the high-level components along with their interactions 
in a given application domain. Lists down the reusable elements & industry best practices in
the domain.

To create a reference architecture, the existing architectures are first collected and 
analysed. This is done to find the common requirements that exist in a domain. Once all the 
common requirements are gathered, they are collated to create a general framework for reference. So, yes this is how will you create the reference architecture.

Benefits:
1. It helps in understanding the overview of the domain.
2. It saves cost.
3. It facilitates mergers/acquisitions as the same standards are used to build the applications.
4. It makes the comparison between the applications easier.

With evolution of software architecture, the reference architecture evolves as well.

The Kruchten's 4+1 view model divides the software architecture into the following views:
1. Logical view: It represents the functional requirements of the system.
2. Development view: This represents the system components and the way they interact with 
each other. Programmer's perspective. Describe how the development of the system will be done 
using UML components and packages.
3. Process view: It represents the non-functional requirements of the system.
4. Physical view: It represents the network topology of the software components.
5. Scenarios: These represent how the rest of the views work together to create one prototype.
Describes the relationships between the objects of the system and the processes that happen.

These views form the representation of the system from the viewpoint of different stakeholders.
As the views separate concerns, they make organising easier, which, in turn, leads to better 
modelling of the system.

Separation of concerns refers to separating different functional aspects of the software. 
It ensures that there is minimal functional overlapping in software architecture. Coupling is
how much each component knows about the others.

Use repository-based architecture, to use database management systems, for data retrieval,
storage and access. There is a central repository.

