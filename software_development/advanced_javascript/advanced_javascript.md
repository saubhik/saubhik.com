# Advanced Javascript

## Functions
Each function inherits its properties from  (instance of) `function.prototype`. Internally, `function.prototype` is linked to `object.prototype` - this allows us to do this:

```javascript
// the following is an `anonymous` function
var board = function() {
    console.log("Board funciton");
};

// we can also do this
var obj = {
    // this is a named function
	sum: function add(x, y) {
		return x+y;
	}
};
```

A function without a name is called `anonymous function`, like above.

Each function has a `prototype` property (empty, default), and we can attach properties & methods on this property.

```javascript
// function as constructor
var sum = new Function('num1', 'num2', 'return num1 + num2');
```

Anonymous functions are used in `callbacks`.

`typeof` is used to check the data type of objects.

## Pass by value & Pass by reference

The primitive data types i.e. Number, Boolean, String, etc. are pass by value, but objects are both pass by reference & pass by value.

```javascript
function passByWhat(x, y, z) {
	x = x + 5;
	y.name = "chocolate cookie";
	z = {name: "coffee doughnut"};
}

var a = 2;
var b = {name: "plain cookie"};
var c = {name: "plain doughnut"};

passByWhat(a, b, c);

console.log(a);
console.log(b.name);
console.log(c.name);

// this returns:
// 2
// chocolate cookie
// plain doughnut
```

So for objects, if the entire internal structure of the object is changed, it is like pass by value. If a property of the object is changed, it like pass by reference.

```javascript
// pass by value
x = 17
y = x
x = 99

// pass by reference for objects
x = [1, 2, 3]
y = x
x[0] = 17

x = [1, 2, 3]
y = x
x = [17, 18, 19]
```

## Invoking a function

```javascript
// functional invocation
function board() {
	console.log("Board name is JavaScript");
}
board();

// method invocation
var board = {
	"print": function() {
		console.log("Board name is JavaScript");
	}
};
board.print();

// constructor invocation
var board = function(name) {
	this.name = name
};
var boardName = new board("Board name is Javascript");
console.log(boardName);

// apply invocation
var board = function(firstName, lastName) {
	return firstName + lastName;
};
var boardName = board.apply(null, ["New", "Board"]);
```

By default, `this` refers to the global object. When you run JS code in browser, there is a global object called `window` that can be accessed by any part of JS code. Type in `this` in your DOM inspector.

The value of `this` is determined by how a function is invoked. When a function is called as a property on a parent object, `this` refers to the parent object inside that function.

```javascript
var dessert = {
	name: "cookie",
	change: function() {
		this.name = "doughnut";
	}
};
dessert.change();
console.log(dessert.name);
```

When a function is called with `new` operator, `this` refers to the newly created object.

## bind, call & apply

```javascript
var name = "javascript";
var boardName = {
	name: "New name",
	getName: function() {
		return this.name
	}
};
// this returns "New name"
console.log(boardName.getName());

var getBoardName = boardName.getName;

// this returns "javascript"
console.log(getBoardName());

var getBoardName = getBoardName.bind(boardName);

// this returns "New name"
console.log(getBoardName());

var boardList = function(firstName, lastName) {
	console.log(this.getName() + firstName + lastName);
};

boardList.call(boardName, "javascript", "call");
boardList.apply(boardName, ["javascript", "apply"]);
```

More examples:
```javascript
var person = {firstName: 'Jimi', lastName: 'Hendrix'};

function hello() {
    console.log('Hello ' + this.firstName + ' ' + this.lastName);
}

// bind `this` to `person` inside `hello`
var greeting = hello.bind(person);
greeting();
```

`bind()` returns a new function while `call()` and `apply()` will call the function immediately.

All JS functions have 2 methods, `call()` and `apply()`.

```javascript
var dinner = function(x) {
	this.name = x;
};

var dessert = {
	name: "doughnut"
};

dinner.apply(dessert, ["cookie"]);
console.log(dessert.name); // prints "cookie"

dinner.call(dessert, "cookie");
console.log(dessert.name); // prints "cookie"
```

Some more examples:

```javascript
var number = {
	value: 5,
	change: function () {
		this.value = 7;
	}
};

number.change();
console.log(number.value); // prints 7
```

`Parameters` are used when defining a function, they are the names created in the function definition. `Arguments` are the values the function receives from each parameter when the function is executed (invoked).

## Recursion & Immediately Invoked Functions
