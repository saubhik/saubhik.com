### Unit Testing

A unit in a code could be a method, class, sequence of methods, sequence of classes.
Testing individual units in a code is important for a working software which is an integration
of these units.

3 different kinds of test case scenarios:
1. pass case scenario
2. fail case scenario
3. edge case scenario

Test cases should be fast, repeatable, trustworthy, maintainable & isolated.
An object under test can have dependencies on other objects. We replace the other objects
by mocks to simulate their behavior. This is _object mocking_.

JUnit is an open source regression testing tool. Set up a Maven project to include JUnit.
Project Object Model file (POM.xml) is an xml file consisting of all Maven configuration
details used for building the project. Include the following in POM for JUnit:

```java
<dependencies>
    <dependency>
        <groupId>org.junit</groupId>
        <artifactId>junit-api</artifactId>
        <version>5.0.0-ALPHA</version>
    </dependency>
</dependencies>
```

Assertions are methods to determine the pass or fail status of a unit test case.
Import `import org.junit.Assertions` and `import org.junit.Test`. Annotate the test method
with `@Test`. It should be `void` with no parameters.

3 A's of unit testing:
1. Arrange the code
2. Act i.e. invoke the target code
3. Assert i.e. verify the code through assertions

```java
import org.junit.*;

class Example {
    public bool prime(int n) {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

class Test {
    @Test
    @DisplayName("test prime method")
    public void testPrime() {
        // arrange
        bool temp;
        Example example = new Example();
        // act
        temp = example.prime(11);
        // assert
        Assertions.assertTrue(temp)''
    }
}
```

Use the annotations `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll` for methods
which has to run before each or all test methods, or after each or all test methods. Some
assertions are `assertTrue()`, `assertNull()`, `assertnotNull()`, `assertEquals()`.

TDD, Test-Driven Development is a philosophy where you write the test code first, and then
write the code to make the test pass. Re-iterate. Finally refactor the code.

Good test cases should have:
1. high code coverage
2. multiple assertions to verify results from multiple angles
3. if something in the code breaks, should be able to catch it with some assertion

Refactoring is changing the code structure without affecting the code functionality.
Refactoring can be done by:
1. changing variable name
2. changing method name
3. splitting a method into smaller ones

Some refactoring practices:
* Extract Variables: Instead of hard-coding the values, extract the values as a variable
* Extract Class: Create a new class and move the relevant fields and methods from old class
to new class

