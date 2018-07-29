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

The `@Service` annotation tells Spring that it can manage the instantiation of the objects 
of annotated class for us if we use associating Spring annotations in other parts of the 
program, such as `@Autowired`.

Model is a key-value-like class (similar to a hash table) instantiated by the Spring 
framework, and it helps to pass data from the controller to the view template. In the 
instruction above, ‘posts’ act as a key, and its corresponding value would be the post 
data stored in the list. Specifically, Spring would automatically pass the model to the 
view template and allow you to access and render the post data by using the key ‘posts’ 
in thymeleaf.

The `@RequestMapping(“/”)` instruction will tell Spring to execute the 
“public String index(Model model)” method when user is requesting for the `/` path 
under the url and port that the Spring application is listening for incoming client 
requests, which is `localhost:8080` in this case. The instruction set inside the 
method calls the `findAll()` function and stores the information of all the posts in the 
form of a list.

The `model.addAttribute(“posts”, list)` instruction would help in passing the data of 
the posts to the corresponding view template. Then, the method would return to the 
specific HTML file.

```java
@RequestMapping("/")
public String index(Model model) {
    List<Post> list = postService.findAll();
    model.addAttribute("posts",list);
    return "index";
}
```
  
#### File Operations
We use `static` in Java, when we want a variable or function to be shared across all
instances of a class. You can use these variables or function even when you haven't
instantiated the class.

With `final` in Java, we define an entity to be assigned only once. It cannot be
overwritten.

```java
public class FileOperations<T> {
    private static final FileOperations fileoperations = new FileOperations();
    private FileOperations() {}
    public static FileOperations getInstance() {
        return fileOperations;
    }
}
```
The above is an example of Singleton Design Pattern.
We cannot have multiple instances of this class, as then multiple such instances would
try to read or write from a file. There is only one instance of this class.

```java 
List<T> readAllFiles(String dirPath) {
   synchronized (fileOperations) {
       List<T> arrayList = new ArrayList<T>();
       File file = new File(dirPath);
       File[] files = file.listFiles();
       if (files != null) {
           for (File f : files) {
               try {
                   FileInputStream fileInputStream = new FileInputStream(f);
                   ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
                   T readObject = (T) objectInputStream.readObject();
                   if (readObject != null) {
                       arrayList.add(readObject);
                   }
               } catch (FileNotFoundException e) {
                   e.printStackTrace();
               } catch (IOException e) {
                   e.printStackTrace();
               } catch (ClassNotFoundException e) {
                   e.printStackTrace();
               }
           }
       }
       return arrayList;
   }
}
```

Observe the `synchronized`. This helps in situations where multiple threads are trying
to access the same resource at the same time. It lets only one thread access the
`fileOperations` object.

All synchronized blocks synchronized on the same object can only have one thread 
executing inside them at a time.

To `serialize` an object is to convert its state to a byte stream so that the byte
stream can be reverted back into a copy of the object. `ObjectInputStream` is a Java 
built-in class that converts byte streams from the `fileInputStream` variable into 
Java objects. This process is called deserialization.

```java 
List<T> readRecentFiles(final int numberOfFiles, final String DirLocation) {
   synchronized (fileOperations) {
       Map<Long, File> sortByModificationDate = new TreeMap<Long, File>(Collections.reverseOrder());
       List<T> arrayList = new ArrayList<T>();
       try {
           File file = new File(DirLocation);
           File[] files = file.listFiles();
           if (files != null) {
               for (File f : files) {
                   sortByModificationDate.put(f.lastModified(), f);
               }
               int count = numberOfFiles;
               for (Long modifiedOn : sortByModificationDate.keySet()) {
                   FileInputStream fileInputStream = new FileInputStream(sortByModificationDate.get(modifiedOn));
                   ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
                   T readObject = (T) objectInputStream.readObject();
                   if (readObject != null) {
                       arrayList.add(readObject);
                   }
                   count--;
                   if (count <= 0) break;
               }
           }
       } catch (Exception e) {
           System.out.println("Error " + e.getMessage());
       }
       return arrayList;
   }
}

T readFile(final String filePrefix, final String uniqueId) {
   synchronized (fileOperations) {
       T readObject = null;
       try {
           FileInputStream fileInputStream = new FileInputStream(new File(filePrefix + uniqueId));
           ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
           readObject = (T) objectInputStream.readObject();
       } catch (IOException e) {
           System.out.println("Error " + e.getMessage());
       } catch (ClassNotFoundException e) {
           System.out.println("Error " + e.getMessage());
       }
       return readObject;
   }
}

boolean deleteFile(final String filePrefix, final String uniqueId) {
   synchronized (fileOperations) {
       File file = new File(filePrefix + uniqueId);
       return file.delete();
   }
}

public T writeToFile(final String filePrefix, final T object, final String suffix) {
   synchronized (fileOperations) {
       try {

           FileOutputStream fileOutputStream = new FileOutputStream(new File(filePrefix + suffix), true);
           ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
           objectOutputStream.writeObject(object);
           objectOutputStream.close();
           fileOutputStream.close();
       } catch (IOException e) {
           System.out.println("Error " + e.getMessage());
       }
       return object;
   }
}
```

