### Distributed Systems & Scalable Architecture

**Scalability**: The ability to scale the system as the user demand rises.
**Distributed system**: The user load is distributed across various server systems. 
How to efficiently manage user traffic?

We focus on:
1.  Improve efficiency of system without hardware changes. (Techniques - Caching, Indexing, 
Denormalisation)
2. Horizontal Scaling (load balancers, service bus & queues, microservices, global caches 
e.g. Redis) and Vertical scaling

_Monolithic_ applications does not need communication mechanisms since all of the application is 
written as a single entity to a single platform, as opposed to _distributed_ applications.

Features of a distributed system:
1. **Scalability** - ability to handle a lot of users concurrently, and expand when demand rises.
2. **Availability** - application should be up and running at all times so to give users the best 
experience. (Up-time)
3. **Performance** - (low latency, performance) System should be able to return the required results 
within the earliest possible time.
Latency is the time or lag required to perform some action or to produce some result.
4. **Throughput** - System should be able to address to maximum number of requests per second.
Throughput is the number of such actions executed or results produced per unit of time.
5. **Reliability** - System should try to create a reliable connection between users and system. 
(connect to different server if current server gets disconnected) 

#### Software development techniques:
* **caching** is the process of storing frequently or recently used data in the main memory of 
the system or RAM so as to make the repeated retrieval of the requested data faster. 
Cache the data that is frequently accessed and hardly changes.

`@EnableCaching`: This annotation triggers the post processor that inspects every spring bean for 
the presence of caching annotations (`Cachable`, `CachePut`, `CacheEvict`) on public methods.

`@Cacheable`: It creates a cache with the name specified as the parameter to the annotation and 
stores the returned result of the method in this cache for fast retrieval the next time the 
method is called.

`@CachePut`: With the @CachePut annotation, a method updates the contents of the cache with the 
value which is passed as the parameter to the annotation every time the method is called.

`@CachePut` updates the contents of the cache each time the method is called, i.e. it doesn’t 
interfere with the execution of the method, whereas the `@Cacheable` annotation doesn’t update the 
cache. It simply stores the return result of the method the first time that method is called, and 
then it simply returns the data stored in the cache instead of executing the method on future 
calls to the method. This process continues until the contents of the cache are cleared using the 
`@CacheEvict` annotation.

* **indexing** optimises the performance of a system by making the searching of records from 
database effectively fast. Index table comprises of indexed key, data reference columns.

**Primary index**: The entries in index and table are sorted according to the key on which the 
indexing is done. Usually primary key is chosen in primary indexing.

**Clustered index**: Grouping done on the basis of some secondary key in the table so that the 
index table is much smaller than any original table in the database.

* **de-normalisation**
Database normalisation is organising columns and tables of a relational database in order to 
minimise redundancy. De-normalisation is the process of attempting to optimise the read performance 
of a database by adding redundant data or by grouping data so that the database can find the 
information it seeks quickly. Tables are merged to store different attributes of the records 
together.

> More transactions, then go for normalisation.
> More reads than inserts & updates & deletions, then go for denormalisation.


#### Hardware related techniques:
* **Vertical scaling** (scaling up)
The process of adding more physical resources such as memory storage, CPU and RAM to an 
existing server for improving the performance.
* **Horizontal scaling** (scaling out)
The process of adding more servers to existing system is scaling out.

microservices
load balancers
message queues
global cache

Advantages of vertical scaling
1. consumes less power
2. easy setup
3. optimal use of network resources
4. easy debugging - identify points of failure

Disadvantages of vertical scaling
1. server is single point of failure
2. vendor lock in
3. after a certain point, adding expensive hardware may only provide diminishing returns and a
minimal increase in performance

Advantages of horizontal scaling
1. more fault tolerant - no single point of failure
2. improves availability of application
3. easier to upgrade

Disadvantages of horizontal scaling
1. difficult to debug
2. increase in utility costs
3. requires more networking resources

### Horizontal Scaling

__Monolithic application__: This refers to a single-tiered software application in which the user 
interface, business logic and data access codes are combined into a single program on a 
single platform.

**Microservices architecture**: (SOA - Service Oriented Architecture) Architectural style in 
which the application is structured as a collection of small autonomous services that are decided 
based on the needs of business domain.

* The microservices architecture divides a large complex application into smaller independent 
components and helps to develop and deploy them individually, whereas a large complex monolithic 
application makes it difficult to develop the application because all the functions are tightly 
coupled.

* Also, each service can be developed in different technologies as per the requirement and 
integrated into one single application. Whereas in a monolithic application, all the functions 
have to be developed using the same technology stack

* In microservices, if there has to be some development or version change of one of the services, 
then the specific service can be updated and deployed without affecting other parts of the 
microservices. Whereas in a monolithic application, the complete application needs to be taken 
down for any simple change that is required.

**Scaling Out with Load Balancers**
Select the appropriate server to serve a client's request.
A load balancer:
1. Distributes client requests efficiently across multiple servers
2. Ensures high availability and reliability of servers
3. Provides flexibility of adding and removing servers from the server pool

The various algorithms that load balancers employ are:
1. **round-robin algorithm**: Client requests are assigned to the servers in the order they 
are received by the load balancer.
2. **weighted round-robin algorithm**: The architecture assigns weights to servers, according 
to which they are allotted to serve the incoming requests, i.e. if the weights of two servers — 
server 1 and server 2 — are 4 and 1, respectively, then server 1 would serve four requests only, 
after which, server 2 would get one request.
3. **least connected algorithm**: In this algorithm, the server with the least active 
connections serves the new incoming request, i.e. the server that is serving the least number of 
requests will serve the new incoming request.
4. **random algorithm**: This algorithm selects a random server from the pool of servers and 
passes the new client request to this server.
5. **IP hash algorithm**: This algorithm becomes particularly useful when requests from a 
similar network need to be assigned to the same server across server sessions. In this algorithm, 
the IP address is hashed and based on that the server is decided. This way, the requests from the 
same network get served by the same server every time. These sessions are also known as **sticky 
sessions**.

**Message Queues & Topics for IPC (Inter-Process Communication) & Inter-Thread 
Communication, Scaling out with Queues**

A message queue is a system that stores messages as they travel between various components of 
application architecture. 

> Queues are point to point model, maintains order of delivery, acknowledgement is 
prevalent, only one consumer receives the message.

> Topics are publish-subscribe model, multiple clients can subscribe to a message, no
order is maintained, no acknowledgement.

**Topics**:
In queues, each message is processed by a single consumer, topics and subscriptions provide a 
one-to-many form of communication in a publish-subscribe pattern (pub-sub model). Doesn't 
maintain order. No acknowledgement.


**Scaling out with Global Caches**

Caching. If required data is in cache, it's called Cache Hit. If absent, its called Cache Miss.
To remove stale cached data, we use Cache Eviction. 

Cache Eviction Policies:
1. TTL Time To Live
2. LRU Least Recently Used

Data that can be cached: Read often, but not changed. Examples:
Configuration settings, Localisation and Internalisation data, Session data, Application objects.

Caches are typically stored in the server memory, such as the RAM. However, in a distributed system,
several servers may exist in the server pool. Therefore, you need to employ a scaling technique that
stores data in the global cache in order to provide a centralised caching mechanism that is globally
available to all the servers in the distributed system. 
Redis is an open source data store that is commonly used in the industry as a global cache. 

REDIS: (written in ANSI C)
1. All data is stored in RAM, optimised for speed
2. Atomicity of operations & transactions
3. Data expiration
3. Configurable eviction policies when memory is running low
 
Redis is a data structure store that you can use to store various data structures such as sets, 
hash-maps, integers, lists, strings and so on.

