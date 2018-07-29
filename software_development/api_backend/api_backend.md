### API backend

API is an interface using which a front-end service or other services (e.g. a data analysis service) 
can access back-end data. This interface enables multiple clients to interact with a common back end.

Advantages of using an API:
1. make data accessible across different services
2. access data for the same service across multiple platforms such as a mobile app, website, etc.
3. scale your service or application by putting different APIs on different computers
4. update the back end without changing the front end

HTTP requests/verbs:
1. **GET**: It is used to retrieve information from a server. A GET request must be idempotent, i.e. 
it should return the same results no matter how many times the GET request is sent
2. **POST**: It is used to create a new resource or to send information to the server
3. **DELETE**: It is used to delete an existing resource from the server
4. **PUT**: It is generally used to update an already existing resource in its entirety
5. **PATCH**: It is generally used to update a portion of an already existing resource

APIs are of 2 types:
1. **SOAP** (Simple Object Access Protocol): APIs of this type use XML for providing messaging
services.
2. **REST** (Representational State Transfer): APIs of this type uses simple URLs instead of huge
XML codes for providing messaging services.

API endpoints are one end of a communication channel. They are the points through which an API
interacts with another system. Each endpoint is the location from which APIs can access the resources
they need to carry out their functions.

```java
@Controller
public class MovieController {
    
    @Autowired
    MovieService movieService;
     
    @RequestMapping(value="/movie/add", method=RequestMethod.POST, consumes="application/json")
    public ResponseEntity<Movie> addMovie(@RequestBody Movie movie) {
        movieService.addMovie(movie);
        return new ResponseEntity<Movie>(movie, HttpStatus.OK);
    }
}
```

REST keyword stands for “Representational State Transfer” and it technically means creating the 
representation of an object's current state and transferring the representation over the network. 
It was developed during the foundation of HTTP protocol by Roy Fielding.

Characteristics of REST:
1. APIs are used for client-server communication and REST is an API style that defines how APIs 
should be structured and represented.
2. The representation which is transferred over the network is in XML or JSON (JavaScript Object 
Notation) format.
3. Data and functionalities (such as methods) can be seen as resources provided by a server, and 
both data and functionalities can be accessed using URIs in a REST API.
4. Every resource is uniquely addressable using a uniform and minimal set of commands. For the 
HTTP protocol, we have commands such as GET, POST, PUT and DELETE.
5. Rest is stateless, meaning RESTful Web Service should not keep a client state on the server, 
i.e. the result of each request should not dependent on request that has taken place in past or 
request that will take place in future.
6. Caching is a core tenant in REST Architecture, especially for GET requests. In the context of 
REST APIs, caching means HTTP caching where server response can be stored in the client (such as a 
browser), so that a client need not make a GET request for the same resource again and again.

The Spring framework provides `@RestController` annotation to create the restful web services, 
the function of this annotation is the combination of `@Controller` and `@ResponseBody`. The 
purpose of `@Controller` annotation is to map the model object with the corresponding view template 
whereas `@RestController` returns the object/data and is written into HTTP response in the form of 
JSON.

`@ResponseBody` annotation also performs the similar function on the request mapping methods by 
returning the object/data into HTTP response. Using `@RestController`, you need not add the 
`@ResponseBody` annotation to each request mapping methods.

JPA (Java Persistence Architecture) API is a Java specification for accessing, persisting, 
and managing data between Java objects / classes and a relational database. JPA providers develop 
a JPA implementation that meets the requirements of the JPA specification. Hibernate is a JPA 
Provider, as well as others such as EclipseLink and TopLink. With a JPA implementation in place 
Java objects can now be persisted to a relational database, since there is underlying code to 
perform the work.

Java provides a no argument constructor if no other constructor defined in the class. In Java 
API (e.g.JPA) an instance of the object is required before the data values of the object can be set, 
as the definition of how the values are applied are defined through instance members of the object. 
If a class only has a constructor that takes some arguments then it may not be possible for the 
library to construct an instance unless a separate no argument constructor is defined.  

`@Repository` - This annotation marks the class as Data Access Object (DAO) which consists of all 
the different operations that you can apply to its associating data in the database. A repository 
interface helps to extend the CRUD repository which is a spring data interface with inbuilt 
functions such as `save`, `findbyId`, `delete`, `count` and also you can add any other functions as per 
the requirement. The instance of the repository class in the controller class is used to access the 
tables for a particular entity.

```java 
@Repository
public interface MoviesRepository extends CrudRepository<Movies, Integer> {}
```

Here `Movies` is the entity that is managed by the repository, and `Integer` is the data type of
the primary key of the entity.

```java 
@GetMapping("/api/findmoviebyid/")
public String findMoviesById(@RequestParam("id") int id) {
    boolean result = moviesRepository.findById(id).isPresent();
    if (result == false)
        return "movie id doesn't exist";
    return moviesRepository.findById(id).get().toString();;
}


@GetMapping("/api/upcomingmovies/")
public Iterable<Movies> getAllUpcomingMovies() {
    return moviesRepository.findUpcomingMovies();
}
```

`findById()` is inbuilt JPA method.
For custom queries for which we don't have inbuilt JPA methods:

```java 
@Query(nativeQuery=true, value="SELECT * FROM MOVIES WHERE release_date > NOW();")
List<Movies> findUpcomingMovies();
```

`@Modifying` - This annotation marks a method, so that the execution of the method will 
update/add data to the database.

`@Transactional` - This annotation ensures the transaction propagation is handled automatically.


