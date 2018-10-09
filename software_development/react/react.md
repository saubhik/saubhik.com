# React

React helps in building web UIs. It follows the latest specification of the ECMAScript which covers Javascript syntax. It does not make any assumption about the rest of our technology stack. Also, DOM manipulation with react is superfast & easy. React also supports a large number of other open-source libraries.

React was introduced by Facebook in 2011.

React is often referred to as the `View` or `V` in a MVC architecture.

React uses the concept of `virtual DOM` which makes applying changes to DOM elements super fast. Using this concept, when an element undergoes a change, one does not need to find the target element in a large DOM tree and update it. Instead, the Virtual DOM is re-rendered and only the changed element is identified and at the end, updated on the Real DOM. This concept makes DOM manipulation superfast and easy.

React follows ECMAScript specification and uses the ES6 edition of this specification, which uses the latest features of JS.

Babel is both a JS compiler as well as transpiler & can be used to convert ES6 code to ES5 code as many browsers still use ES5 standards.

## Bundling & Minification

Bundling reduces the number of HTTP requests sent by the client to the server. Suppose a webpage references to 10 stylesheets and 20 script files. This makes a total of  `1 + 10 + 20 = 31` files to be referenced. The first 1 is because of the webpage.

A **batch size** is the number of files that a browser can reference in parallel. If the batch size is 6, then we need to make a total of  `ceil(31 / 6) = ceil(5.17) = 6` HTTP requests.

If we use **bundling** then we can bundle all the stylesheets into one file & all the scripts into one file. Then we need to reference only `1 + 1 + 1 = 3` files. Now with a batch size of 6, we need to make only `ceil(3 / 6) = 1` HTTP request.

**Minification** shorten's the file's contents, resulting in faster response time & lower bandwidth cost. **Webpack** bundles our files into a single file in a React application.

## Lint & ESLint

ESLint, is a linting utility, which helps us to follow coding guidelines and principles while making us commit fewer errors.

If we write the code:

```javascript
var name = "UpGrad";
var name = "UpGrad Education";
console.log(name);
```

When this is written in a React application which has ESLint configured in its environment, then one can see the message:

```
`name` is already defined no-redeclare
```

`no-redeclare` is one of the ESLint rules. There are different style guides, like `Airbnb Style Guide`, which provides ESLint presets that cover `ES6`, `JSX` etc.

Some more code examples for ESLInt rules:

```javascript
// no-dupe-keys
let student = {
    name: "Srishti",
    roll: "001",
    name: "Srishti"
}

// no-self-compare
if (1 === 1) {
    console.log("1 is equal to 1!");
}

// no-useless-escape
var name = "\'UpGrad";
console.log(name);

// no-unreachable
function add(x, y) {
    return x + y;
    console.log(x + y);
}
add(2, 3);
```

## Single-Page Application vs Multi-Page Application

SPA examples are: github, gmail, and so on. Some components of a web page like header (which stays same throughout pages) need not be re-rendered again and again like in MPAs. One only needs to download such resources once. So SPAs are faster.

Advantages of SPAs over MPAs:

1. Faster loading as downloading resources again is not needed
2. Effective caching; easy local data storage
3. Easy debugging; technologies provide their own debugging tools
4. Decoupling of front-end & back-end
5. Simplified mobile development; same back-end can be used for web applications as well as native mobile applications
6. Rich in responsiveness; better UX

Advantages of MPAs over SPAs:

1. Better SEO (Search Engine Optimisation); architecture being native to search engine crawlers; flexibility to add meta tags to each page.
2. Better in terms of analytics
3. Unlimited scalability; new features can be added easily
4. JS is not mandatory
5. Better security; access control at a funcitonal level

React is one of the popular libraries to build SPAs.

Next we will try to build a Phone Directory application with the functionalities of adding a subscriber, deleting a subscriber, and showing all subscribers' details.

We write `sudo npm i -g create-react-app` to install the `create-react-app` package using `npm`. `i` stands for `install` and `-g` is `global` flag.

Next, go to your folder where you want to create your react app. Then type in `create-react-app phone-directory`. This folder will now consist of all the necessary configuration files that you need as the starter code of a React application.

Next `cd` into the application directory and type `npm start` to start a development server locally on our machine. Any code change that we make will get reflecteted immediately on the browser where the application is running.

We don't need to configure tools like `Babel`, `Webpack` and `ESLint` if we use the `create-react-app` package.

## Folder structure in create-react-app

**.gitignore** file

- It is used by Git to determine which files and directories to ignore before a commit is made.

- It should be committed into the repository to share ignore rules with other users who clone the repository.

- The *node_modules*  folder is included inside the *.gitignore* file so that the user who clones the application is not required to clone this folder. The user simply needs to run the command 

  ```
  npm install
  ```

  in the root folder of the project. This command creates the *node_modules* folder and installs all the dependencies (packages) needed for the application.

**package.json** file

- It consists of the name and version of the application, the combination of which should be unique in order to publish the package.
- It comprises of dependencies that list all the packages needed to be installed for the application.
- It also includes scripts that specify the commands to be run at various points in the application lifecycle.

**package-lock.json** file

- It is automatically generated for any operation where npm modifies either the *node_modules*  tree or the *package.json*  file.
- It locks the version of the full dependency tree of packages.
- It guarantees the generation of an identical dependency tree when the application is cloned by other developers.

**node_modules** folder

- Its contents are defined by the *package.json* file and it consists of all the packages required for running your application.

**public** folder

- Nothing inside this folder is processed by *Webpack*.
- It is used for keeping small files that are not required to be bundled.
- It can be used to contain images when there are thousands of them, and their paths need to be referenced dynamically.
- Any file inside this folder needs to be referenced at other places using the `%PUBLIC_URL%/ ` keyword, which gets replaced with the path of the public folder during the application's build process.

**index.html** file

- It is the starting point of the application.
- It should always remain with the name *index.html* and inside the *public* folder; otherwise, the code will fail to run.
- It can only reference files that are inside the *public*  folder.

**manifest.json** file

- It is a simple JSON file telling the browser about the web application and how the application should behave when it is installed on the user’s mobile device or computer.

**src** folder

- It consists of the real application code.
- It consists of all the files that are needed to get bundled by *Webpack*. 

**index.js** file

- It is the entry point for JavaScript.
- The filename should remain *index.js* and the location should be inside the *src* folder; otherwise, the code will not run.

**index.css** file

- It is the stylesheet for *index.html*.

**registerServiceWorker.js** file

- It is the web browser API that is used to cache assets and other files to work passively in the background. It helps offline users or the ones who are on the slow network to see results on the screen faster.
- It adds offline capabilities to the application.

**App.js** file

- It is the JavaScript file for the *App* component.

**App.css** file

- It is the stylesheet for the *App* component.

**App.test.js** file

- It is the test file for the *App* component.
- It contains unit tests for the application.
- It runs test cases for all the files that changed since the last commit of the application.

**logo.svg** file

- SVG is an acronym for Scalable Vector Graphics.
- An SVG file is an XML-based vector image format for 2D graphics with support for interactivity and animation.
- It is similar to raster-based image formats such as JPEG, PNG, BMP, GIF, etc.
- It offers a bandwidth-friendly way of rendering images; no matter how large a graphic gets, it transmits only the XML describing the graphic to the client.
- It helps to render resolution-independent and SEO-friendly images.
- It makes up the icon for your application and appears alongside the title in the browser tab.
- It gets saved along with the bookmark.

## Code Cleanup

We need to clean up some unnecessary code before we actually move on to building the application.

1. Inside the *src* folder, go to the *App.js* file.

   - Remove all the code written inside the *div*  of the return statement of *render*  method inside the *App*  class.

   - Remove the *className="App"*  from the outer *div*  while leaving the outer *div*  as it is. 

   - Remove the import statements at the top of the file for the *logo.svg* and *App.css* files. After doing this, the *App.js*  file looks like this:

      

     ![img](https://images.upgrad.com/c05f5458-76ac-4937-858e-fcbbdb7b6912-Code%20Cleanup%20App.js%20file.png)

2. Inside the *src*  folder, delete the *App.css*  file.

3. Inside the *src*  folder, delete the *logo.**svg*  file.

## JSX

Facebook created JSX by combining JS with their proprietary markup language called XHP, which itself is a combination of XML and PHP. JSX is HTML-looking syntax, but it is actually XML extension to ECMAScript specification. Thus instead of using pure JS for building DOM elements, one can use JSX, which offers familiar syntax, namely HTML.

This is how you write JSX inside `scripts/App.js`:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  // notice the comma in the end
  <input type="text" placeholder="Your Name" />,
  document.getElementById('root')
);
```

Differences between JSX and HTML:

1. Adjacent JSX elements must be wrapped in an enclosing tag

   We need to encompass all children elements within a parent element and then return this parent element. In React 16, one can return an array consisting of multiple elements existing at the same level. These elements are separated from each other using a comma.

   One can write the following in React 16:

   ```javascript
   return [
       <div> Phone Directory </div>,
       <button> Add </button>,
       <div>
       	<span> Name </span>
       	<span> Phone </span>
       </div>
   ]
   ```

   In `v16.2` React introduced `Fragment` which allows you to return multiple elements. We have to `import { Fragment } from 'react';` to reference `Fragment`.

   We can write:

   ```javascript
   return (
   	<Fragment>
           <div> 
       		Phone Directory 			</div>
           <button> Add </button>
           <div>
               <span> Name </span>
               <span> Phone </span>
           </div>
       </Fragment>
   )
   ```

2. Closing tag required

   We need to close both types of tags - opening-closing tags as well as self-closing tags. For example, we have to write `<br/>` instead of `<br>`.

3. JSX properties are not similar to HTML attributes

   We need to use `className` & `htmlFor` for `class` & `for` respectively. There are more. This is because JSX code gets converted to JS code at the end, and JS has its own reserved keywords, which might conflict with JSX properties. So use alternative keywords in JSX for those HTML attributes, which exist in JS language.

4. Case sensitiveness

   Since JS is case sensitive, JSX is case sensitive unlike HTML.

This is a valid JSX code:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  <div>    
      <label htmlFor="username">Username: </label> <br/>
      <input id="username" type="text" /> <br/> <br/>
      <label htmlFor="password">Password: </label><br/>
      <input id="password" type="password" /><br/><br/>
  </div>,
  document.getElementById('root')
);
```

## Injecting data using {}

Code Snippet:

```javascript
let moduleName="React";
<span>Learning {moduleName} is so much fun!</span>
```

Output:

```
Learning React is so much fun!
```

Whatever goes within curly braces `{}` is JS, in JSX.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const firstname = "Srishti";
const lastname = "Gupta";
const numberOfIceCreams = 5;
const iceCreamPrice = 20;

ReactDOM.render(
  <span>Hello {firstname + " " + lastname}! The total amount you need to pay for {numberOfIceCreams} ice-creams is Rs. {numberOfIceCreams * iceCreamPrice}.</span>,
  document.getElementById('root')
);
```

The above example is inside App.js file.

## React.createElement()

JSX is syntactic sugar for `React.createElement()` method. The syntax for `React.createElement()` method is

`React.createElement(element_name, element_properties, children);`

1. element_name (required)
2. element_properties (optional)
3. children (optional): Can pass infinite number of children elements, which will be nested inside the main element.

Example:

The below is JSX code:

```jsx
<div id="module">
	<p>ReactJS</p>
</div>
```

The equivalent code in JS is:

```javascript
React.createElement("div", {id: "modeule"},
                   React.createElement("p", null, "ReactJS")
                   );
```

When we write JSX code, Babel converts it into JS code.

That is why we need one parent container in JSX:

```jsx
class App extends Component {
    render() {
        return (
        	<h1>Welcome to React</h1>
			<div>Hi</div>
        );
    }
}
```

renders as

```javascript
class App extends Component {
    render() {
        return React.createElement("h1", null, "Welcome to React");
        return React.createElement("div", null, "Hi");
    }
}
```

We have 2 return statements inside render!

## Rendering elements into the DOM

One root node suffices in a small application, but one can have multiple root nodes depending upon the needs of the application.

Suppose we want to ship only some features in React in an application, not built using React. These features are spread across our entire application. We can choose selective pieces of our existing code to be shipped, convert them into React and then plug these new React code pieces back into different places inside our application. Having multiple root elements is needed here.

The syntax of `ReactDOM.render()` is `ReactDOM.render(argument_1, argument_2);` where `argument_1` tells what to render and `argument_2` tells where (location on the DOM) to render. We have been seeing this method for quite some time. `argument_1` can be a `Component` or `JSX`.

Look at our `index.js` file:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
```

Some good pep talk:

```
Geeks are the people who love something so much that all the details matter.
```

```
If you don’t succeed initially, call it version 1.0
```

```
There are 10 types of people in the world - those who understand binary and those who don’t!
```

```
Coding is a language of creativity!
```

```
Programming is a skill that is best acquired by practice rather than by reading books!
```

## Components

Components are JS way of writing independent, reusable & dynamic code.

Two types of components:

1. Functional components (stateless)
2. Class components (stateful)

A class component must have a `render()` function. This is because a class component extends from the Component base class. This is not the case with functional components.

Name of a component in JSX should always start with a capital letter. HTML elements must start with a lower case letter. This helps it distinguish between components & HTML elements.

You can pass props inside both types of components. But you can maintain state only inside a class component.

This is a functional component:

```javascript
import React from 'react';

const Header = function() {
    return (
        <div>
          Phone Directory
        </div>
    )
};

export default Header;
```

This is a class component:

```javascript
import React, {Component} from 'react';

class Header extends Component {
    render() {
        return (
            <div>
            Phone Directory
            </div>
        )
    }
}

export default Header;
```

A component must always return something. This returned value is the content that is actually rendered into the DOM; it replaces the name of the component.

If you do not wish to return anything, you can return *null* from the component, as written below:

```javascript
return null;
```

**In any case, the return statement needs to be mandatorily written, no matter whether you wish to return anything or not.**

In order to reference a component written in a separate file, you need to first export the component from the file where it has been defined (see `export default ComponentName;`) and then import the component in the required file where it needs to be used.

A component can have file extension `.js` or `.jsx`.

**In case of components where the file extension is .js or .jsx, the extension is not required to be explicitly mentioned while writing the import statement.**
For example, you can skip mentioning the file extension while writing the import statement when the Header file has the extension ‘.js’ or ‘.jsx’.

```javascript
import Header from './Header';
```

**However, for all other files, the extension should also be mentioned along with the file name while writing the import statement.** Let’s say there’s a logo file with `.svg` extension, then you would need to mention the file extension when importing the logo file, as written below:

```javascript
import logo from './logo.svg';
```

The below makes a page unresponsive, as it enters an infinite loop, but no warnings/errors thrown on the console:

```jsx
class App extends Component {
  render() {
    return (
      <div className="App">
        <p>Hello World!</p>
        <App/>
      </div>
    );
  }
}
```



## Styling

React offers styling in 2 ways - `inline` and `external`.

This is an example of inline styling:

```javascript
import React from 'react';

const Header = function() {
    const headerStyle = {
        textAlign: 'center',
        padding: 20,
        background: '#000',
        color: '#fff',
        textTransform: 'uppercase'
     };
     
     <div style={headerStyle}>
        Phone Directory
     </div>
};

export default Header;
```

External styling is same as using external CSS.

Internal Styling:

1. The property names must be written in camelCase. Unlike CSS, hyphens are not allowed in JSX because the JSX code gets converted to JavaScript code, and hyphens are not allowed in JavaScript identifiers.

   ```javascript
   <div style={{textTransform: 'uppercase'}}>
      Phone Directory
   </div>
   ```

   This is the reason why textTransform is written in camelCase in JSX unlike text-transform in CSS. In case you fail to follow this, you will get an error saying “*Uncaught SyntaxError: Inline Babel script: Unexpected token*”.
    

2. The property values look like CSS property values, but they are not exactly like them. These values can be considered the values corresponding to the keys (or properties) in a JavaScript object. Since all the values in JavaScript must be of a valid datatype, care must be taken regarding each value correctly mapping to a valid datatype in JavaScript.

   ```javascript
   <div style={{background: '#000'}}>
      Phone Directory
   </div>
   ```

   This is the reason why *'#000'* is written inside quotes, because it corresponds to a string value. In CSS, you must write it without quotes in order to make it work.
    

3. All property-value pairs are separated using the comma operator. The reason is that the *style*  property accepts a JavaScript object where a comma should be used in contrast to a CSS style, where a semicolon is used instead.

In external styling we use this:

```javascript
import React from 'react';
import "./Header.css"

const Header = function() {
     
    return (
        <div className="header">
            Phone Directory
        </div>
    )
};

export default Header;
```

where `Header.css` contains:

```css
.header {
    text-align: center;
    padding: 20px;
    background: #000;
    color: #fff;
    text-transform: uppercase;
}
```

## Rendering Content Dynamically

JavaScript’s `map()` method can be used to iterate over an array and inject data into the React components or elements dynamically. 

An example:

```javascript
import React, { Component } from 'react';
import Header from "./Header";
import "./App.css";

class App extends Component {
  render() {
    
    let subscribers = [
      {
        id: 1,
        name: "Saubhik Mukherjee",
        phone: "8888888888"
      },
      {
        id: 2,
        name: "Saswata Mukherjee",
        phone: "9999999999"
      },
      {
        id: 3,
        name: "Anula Mukherjee",
        phone: "7777777777"
      }
    ]
    return (
      <div>
        <Header />
        <div className="component-body-container">
          <button className="custom-btn add-btn"> Add </button>
          <div className="grid-container heading-container">
            <span className="grid-item name-heading"> Name </span>
            <span className="grid-item phone-heading"> Phone </span>
          </div>

          {
            subscribers.map(sub => {
              return (
                <div key={sub.id} className="grid-container">
                  <span className="grid-item"> {sub.name} </span>
                  <span className="grid-item"> {sub.phone} </span>
                </div>
              )
            })
          }

        </div>
      </div>
    );
  }
}

export default App;
```

The `key={sub.id}` is important.

## Key Points

Note that 

```javascript
React.createElement('div', {className: "main-container"}, "h1", "UpGrad", "p", "Building Careers of Tomorrow!");
```

is same as the following `JSX` code:

```jsx
<div className="main-container">
    h1UpGradpBuilding Careers of Tomorrow!
</div>
```

We need `React.createElement` before any element.

**input is a void element tag and must neither have `children` nor use `dangerouslySetInnerHTML`.**

In:

```react
React.createElement("div", {className: "container"}, // Line 1
  React.createElement("p", {style: "color: #aaa" }, "Welcome User!"), // Line 2
  React.createElement("hr"), // Line 3
  React.createElement("div"),
  React.createElement("input", {type: "text"}, "Please type your name here"), // Line 4
);
```

`Line 2` and `Line 4` contains errors. The correct way to write `style` is `React.createElement("p", {style:{color: "#aaa"}}, "Welcome User!"), `. 

`Line 4` throws an error saying, `input is a void element tag and must neither have 'children' nor use 'dangerouslySetInnerHTML`. `input` is a self-closing tag. No self-closing tag in React can contain any child element. However, for a tag that is not self-closing, it is optional to contain a child element. For example, the second `div` in the code, which is below `Line 3`, works perfectly. Although, this `div`  doesn't serve any purpose here, it is included just to make this point clear. 

```react
ReactDOM.render(
    <App></App>, 
    document.getElementById('root')
);
```

The above also works!

Also, a react component always starts with a capital letter!

```react
ReactDOM.render(
  <div>
     <CustomHeader></CustomHeader> // this is alright!
     <h3 class="heading">You should know how to "PROGRAM" a computer.</h3> // this is WRONG! Use className
     <p>It teaches you how to "THINK".</p>
     <customFooter/> // this is WRONG! Use CustomFooter
  </div>
)
```

It is strongly recommended that the custom components are written in `PascalCase`, whereas the pre-defined HTML elements should follow lowercase.

Even in case you have a component that starts with a lowercase letter, as you have *customFooter* here, you get a workaround. You can assign this component to a capitalised variable, like this:

```
const CustomFooter = customFooter;
```

And then, use this capitalised variable inside your JSX, like this:

```
<CustomFooter/>
```

This will, thus, allow you to use a  lowercase component (not recommended though) and get it rendered into the DOM while distinguishing it from well-known HTML elements using a PascalCase variable. Remember that despite this workaround existing, it is strongly recommended that the first letter of any component in React is capitalised.

***

