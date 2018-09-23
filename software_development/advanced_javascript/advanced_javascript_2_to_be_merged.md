## Scope & Closure

Any variable declared outside any function or method is part of the global scope.

Any variable declared inside a function has its own scope, known as local scope.

`Block Scoping`: The `let` keyword uses block scoping.

```javascript
var x = "cookie";
function dessert() {
    if (true) {
        let x = "doughnut";
        // this prints doughnut
        console.log(x);
    }
    // this prints cookie since `let` keyword uses block scoping
    console.log(x);
}

dessert();
```

Some more examples:

```javascript
var a = 1;
function four() {
    if (true) {
        var a = 4;
    }
    // this prints 4
    console.log(a);
}
```

vs this:

```javascript
var a = 1
function four() {
    if (true) {
        let a = 4;
    }
    // this prints 1
    console.log(a);
}
```

## Hoisting

```javascript
var x = 1;

function f() {
    console.log(x);
    var x = 2;
    console.log(x);
}

// this prints:
// undefined
// 2
f()
```

JS always moves variable declarations with var, to the top of the scope making the code equivalent to:

```javascript
var x = 1;
function f() {
    var x;
    console.log(x);
    x = 2;
    console.log(x);
}

f();
```

But remember that the following:

```javascript
var x = 1;
function f() {
    console.log(x);
}
// this prints 1
f();
```

This concept is called `Hoisting`. `Hoisting` is a process in which JS moves all the variable declarations declared with `var` to the top of the program before execution.

JS only hoists declarations, not initialisations.

You can even call functions before they are even declared in the JS code, due to hoisting!

This code works perfectly fine!

```javascript
function printName() {
    name = 5;
    console.log("My name is " + name);
    var name;
}

// this prints
// My name is 5
printName();
```

## Closure

```javascript
function welcome(name) {
    var greeting = "Welcome! " + name;
    var message = function() {
        console.log(greeting);
    };
    return message;
}

var sayHello = welcome("Alice");
// this prints
// Welcome! Alice
sayHello();
```

In JS, whenever you declare another function inside an already existing function, you are creating a `closure`.

```javascript
a = (function () {
    var privatefunction = function () {
        alert('hello');
    }

    return {
        publicfunction : function () {
            privatefunction();
        }
    }
})();
```

`a` is now an object, with a method `publicfunction` ( `a.publicfunction()` ) which calls `privatefunction`, which only exists inside the closure. You can NOT call `privatefunction` directly (i.e. `a.privatefunction()` ), just `publicfunction()`.

To count the number of times a user clicked a button,

```javascript
 var updateClickCount=(function(){
    var counter=0;

    return function(){
     ++counter;
     // do something with counter
    }
})();
```

The self-invoking function only runs once. It sets the counter to zero (`0`), and returns a function expression.

This way `updateClickCount` becomes a function. The "wonderful" part is that it can access the counter in the parent scope.

This is called a JavaScript `closure`. It makes it possible for a function to have `"private"` variables.

The counter is protected by the scope of the anonymous function, and can only be changed using the add function!

[source](https://stackoverflow.com/questions/2728278/what-is-a-practical-use-for-a-closure-in-javascript)


## Callbacks

`Callbacks` help in imparting an async nature to JS.

`Synchronous` code means that if you have 2 lines of code (say `s1` followed by `s2`) then `s2` cannot begin to execute until `s1` has finished executing. It is like a queue of processes and before a certain process finishes, the next process cannot start running.

`Asynchronous` code means that you can have 2 lines of code where the second line of code can execute even before the first line executes. This happens through `callbacks` & `promises`.

```javascript
console.log("Begin...");
setTimeout(function() {
    console.log("After 2 seconds...");
}, 2000);
console.log("End...")
```

The above first prints `Begin...` and then `End...` and then `After 2 seconds...`.

A `callback function` is a function passed into another function as an argument, which is invoked inside the outside function to complete some kind of action.

JS is an event-driven language. Instead of waiting for a response before moving on, JS will keep executing while listening for other events. `Callbacks` make sure that certain code doesn't execute before some other code has finished execution.

## Event Bubbling & Capturing

In `event bubbling`, the event is first captured and handled by the innermost element and then propagated to outer elements.

In `event capturing`, the event is first captured by the outermost element & propagated to the inner elements.

Two ways of preventing capturing & bubbling:

1. `stopPropagation()`, prevents further propagation of the current event in the bubbling phase
2. `preventDefault()`, tells the user that if the event does not get explicitly handled, its default action should not be taken

## Map, Reduce & Filter

```javascript
var numbers = [1,2,3,4];
var triples = numbers.map(function(x) { return x*3 });
// this prints [3,6,9,12]
console.log(triples);
```

An anonymous callback function was used above.

```javascript
var numbers = [12, 17, 19, 22];
var even = numbers.filter(function(x) {
    return x%2 == 0
});
// prints [12, 22]
console.log(even)
```

```javascript
var total = [1,2,3,4].reduce(function(sum, currentValue) {
    return sum + currentValue
});
// prints 10
console.log(total)
```

The first param in the anonymous callback function for `reduce` is called the `accumulator` (accumulates whatever the return statement defines) and the second param is the `current value`.

## Promises

`Promises` are used to make code synchronous, like callback functions.

Using `Promises` the execution of a complete block of code can be postponed to happen at a later time. This "later time" is usually when async operation has finished execution. Other operations can keep running without any interruption.

3 states for `Promise`:
1. `pending`: beginning state of any promise object. Promise object has not received any information if the ongoing async operation has been completed successfully or not.
2. `fulfilled`: Promise object changes its state from `pending` to `fulfilled` when it comes to know that the associated async operation has completed successfully.
3. `rejected`: Promise object assumes this state when it finds out that the associated async operation has not completed successfully.

```javascript
const promise = new Promise(function(resolve, reject) {
    // code here ...
})
```

A code example:

```javascript
var success;
const info = new Promise(function(resolve, reject) {
    if (success == true) {
        const details = {
            name: "London Coffee House",
            location: "Downing Street, London",
            cuisine: "Coffee, Pastries & Desserts"
        };
        resolve(details);
    } else {
        reject(new Error("Sorry! Could not fetch data at the moment!"));
    }
});

const display = function() {
    info
        .then(function(coffeeShopDetails) {
            // ... if resolve is called in promise
            console.log("Let's go here for coffee!");
            console.log(coffeeShopDetails);
        })

        .catch(function(error) {
            // ... if reject is called in promise
            console.log(error.message);
        })
};

display();
```

We make variables `const` so their values cannot be changed later.

It is preferred to use `promises` over `callbacks` as we can have `callback hell`, in which a callback function is embedding inside another callback function, which is embedded inside another & so on.

## async / await

The word `async` before a function means the function always returns a `promise`.

```javascript
async function f() {
    return 1;
}
f().then(alert); // 1
```

This is equivalent to

```javascript
function f() {
    return Promise.resolve(1);
}

f().then(alert); // 1
```

`await` works only inside `async` functions. `await` makes JS wait until that `promise` settles & returns its result.

```javascript
async function f() {
    let promise = new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve("done!")
        }, 1000)
    });

    let result = await promise;

    alert(result);
}

f();
```

Whatever one can do with `async-await` can be done with `promises` as well.

## Comparing callbacks, promises & async/await

Suppose we had to print the alphabets a, b & c in this order, after random intervals of time.

We can code something like this:

```javascript
function print(x) {
    setTimeout(function() {
        console.log(x)
    }, Math.random() * 100);
}

function printLetters() {
    print("a");
    print("b");
    print("c");
}

// this prints in random order!
printLetters();
```

This is because the `print` function defined above is asynchronous!

We can solve this problem using `callbacks`.

```javascript
function print(x, func) {
    setTimeout(function() {
        console.log(x);
        func();
    }, Math.random() * 100);
}

function printLetters() {
    print("a", function() {
        print("b", function() {
            print("c", function() {
            })
        })
    })
}

printLetters();
```

But there are so many nested functions that makes the code messy. This is called `callback hell`. This must be avoided.

So we can use `Promises`.

```javascript
function print(x) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log(x);
            resolve();
        }, Math.random() * 100)
    })
}

// create a Promise chain
function printLetters() {
    print("a")
        .then(function() {
            return print("b");
        })
        .then(function() {
            return print("c");
        })
}

printLetters();
```

We will now use `async/await` to improve readability.

```javascript
function print(x) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log(x);
            resolve();
        }, Math.random() * 100)
    })
}

async function printLetters() {
    await print("a");
    await print("b");
    await print("c");
}

printLetters()
```

## Difference between ES5 & ES6 & Babel

`ECMAScript` is a coding language standard & JS is simply the implementation of that standard. `ES` denotes `ECMAScript`. The digit after `ES` denotes the version of `ES`.

Notable differences between `ES5` & `ES6` are:
1. `=>` arrow functions
2. `let` & `const`
3. spread operator
4. string manipulation
5. import/export commands

Many old browsers don't support JS written in ES6. Therefore, `Babel` was created which is a `transpiler`, a type of compiler that takes source code of a program written in one programming language as its input & produces the equivalent source code in another programming language (also known as a `source-to-source compiler`). 

`Babel` converts `ES6` to `ES5` code.

1. `let` & `const` is introduced in `ES6`. These are not hoisted unlike `var`.
2. Arrow functions, `=>`. 

```javascript
numbers.map(x => x + 2);
``` 

is equivalent to

```javascript
numbers.map(function (x) {
  return x + 2;
});
```
3. spread operators, `...` in `ES6`

```javascript
let numbers = [12, 33, 87, 63];
let numberNew = [45];
[numberNew, ...numbers]
```

is equivalent to

```javascript
var numbers = [12, 33, 87, 63];
var numberNew = [45];
[numberNew].concat(numbers);
```

So to copy one array to another array, we can do

```javascript
let numbers = [12, 33, 87, 63];
let newArray = [...numbers];
```

which is equivalent to

```javascript
var numbers = [12, 33, 87, 63];
var newArray = [].concat(numbers);
```

4. String manipulation using template literals

```javascript
const name = "new"
function func(x) {
  return x + "Hello!";
};
let helloString = `This is a ${name} string: ${name} ${func(name)}`;
```

Use backtick (`).

The above is equivalent to:

```javascript
var name = "new";
function func(x) {
  return x + "Hello!";
};
var helloString = "This is a " + name + " string: " + name + " " + func(name);
```

5. `ES6` has introduced modular import & export.

## Lexical Scoping in ES6

```javascript
// ES5
var name = "hello board";
var boards = {
    name: "new board";
    print: function() {
        console.log(this.name);
    }
};
// this prints "new board"
boards.print();

// ES6
var name = "hello board";
var boards = {
    name: "new board";
    print: () => console.log(this.name);
};
// this prints "hello board"
// this takes global scope
boards.print();
```

## OOP in JS

OOP in JS is not a full-fledged feature: the classes are merely functions themselves.

Javascript is basically a functional programming language. Even though the class keyword has been introduced in JS as well, but internally the “class” is just a function! So, it is not a true or robust object oriented programming language.

```javascript
class Boards {
    constructor() {
        this.name = "This is a boards class";
    }
}

class Projects extends Boards {
    constructor() {
        // super must be declared within constructor
        super(name);
    }
}

var results = new Projects();
console.log(results.name);
```

That's it for JS for now!