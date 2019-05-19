### Design Patterns and UML diagrams

In scenarios which involve solving a complex, multi-dimensional problem, rather than building 
everything from scratch, it is often useful to use an already existing, well-tested template, and 
which we can customize to suit our own needs. This is where design patterns come into play.
A design pattern provides a general, well-tested & reusable solution to a common design problem. 
These are peer-reviewed software solutions to common problems and issues we run into in software 
development. It can be understood as a “blueprint” of how to solve a complex, multi-dimensional, 
and recurring problem.

Solves flexibility, re-usability and maintainability of a system.

Composition allows loose coupling between objects and run-time flexibility, unlike inheritance.

```java 
class A {
    public void foo() {}
}

// Example of inheritance
class B extends A {
    public void bar() {
        foo();
    }
}

// Example of composition
class C {
    A a = new A();
    public void bar() {
        a.foo();
    }
}   
```

Suppose I want to declare a function `public string bar()` in class `A`. Then code in class `B`
would not compile due to presence of function with same name. This is tight coupling. Combine
objects at run-time using composition.

Some design patterns:
1. **Factory Method Pattern**: Create instances of classes without actually knowing which class
would be used in the creation of the object. The "factory method" is an interface or a base class 
which is visible to the user. This factory method calls the necessary concrete or derived class to 
generate the actual object.
2. **Facade Pattern**: Provide a minimalistic and simple interface to a complex body of code. Acts
as a gateway between the user and a complex set of functions.
3. **Proxy Pattern**: A "proxy" class functioning as an simpler interface to the class for which
it is acting as a proxy. Can also perform some more additional functions to control direct access to
that class.
4. **Strategy Pattern**: Select a suitable algorithm at run time.
5. **Observer Pattern**: Define a one to many dependency between objects so that when one object
changes state ("subject"), all its dependents are notified and updated automatically ("observers").
Encapsulate the core (or common or engine) components in a Subject abstraction, and the variable
(or optional or user interface) components in an Observer hierarchy.
6. **Template Method Pattern**: Define the skeleton of an algorithm in an operation, deferring
some steps to client sub-classes. Template method lets subclasses redefine certain steps of an
algorithm without changing the algorithm's structure, using 'placeholders'. 

These are some of the 23 design pattern by the Gang of Four. `Factory` is a Creational Design
Pattern (how classes and objects are created). `Facade` and `Proxy` are Structural Design Patterns
(how classes and objects relate to each other). `Strategy`, `Observer`, `Template` are Behavioral 
Design Patterns (how classes and objects communicate with each other).





