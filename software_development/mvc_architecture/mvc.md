### MVC architecture

Servlet: Java program that runs on a web server that responds to client requests, like
logging in users after verifying credentials. Holds the business logic.

Structure:
1. init() : initialises the servlet, allocates the memory for any process, passes input params
2. service() : doGet(), doPost(), doPut(), doDelete()
3. destroy() : called by container before servlet instance is removed, de-allocates memory.

JSP: Java Server Pages, HTML files consisting of presentation logic, using Java programs to
render web pages

Servlet Container: Helps to map a specific web address to its corresponding servlet. Also
interacts with servlet for user requests.

Major disadvantage of servlet approach is tight coupling between the presentation logic
and the business logic. This decreases maintainability. So we come to MVC architecture.

Model: Data of different components of a website or application. For example, for a blog, the
model would be posts, post attributes like date-time, comments, author, likes.

View: Presentation logic of the website of the application

Controller: Process data as per user's request, retrieves required data from model and maps
the corresponding view needed to present the requested data. Business logic comes here.

Spring Boot helps in developing web application and configuring different classes and
methods according to their functions in the Spring framework using annotations. Thymeleaf
is a Java template engine that can process model data and return responses in HTML or XML.
It is a substitute for JSP, and acts as the View part of MVC.

```java
@Controller
public class HomeController {
    @RequestMapping("/")
    @ResponseBody
    public String index(){    
        return "Welcome to my blog";
    }
}
``` 

The above is an example of a controller. If you remove `@ResponseBody`, the dispatcher
servlet will try to look for an HTML in `resources/template` folder. In presence of this
annotation, it returns the exact string.


