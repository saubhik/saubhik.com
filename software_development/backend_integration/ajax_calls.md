### Ajax Calls
We cover backend integration in this document. How to communicate with the backend server?

AJAX is used to retrieve data from servers or download a file, CSS or image.

We will use a special method in JS called `xhr`, stands for xml http request. This retains the name `xml` since it was used before `json` format came.

`Ajax` is a library written around `XHR` with an aim to provide better error checking and cross browser compatibility.

**Retrieving values from HTML**
How to get values from HTML elements? How to extract the text from forms and input boxes?

Don't put `submit` button inside a `form` element:

`<form>` attribute expects the data to be sent to an endpoint, and when the `Submit` button inside the <form> attribute is clicked on, it expects an endpoint to send the data to. As we haven’t provided any endpoint, the form refreshes the page.

Keeping the `Submit` button outside `<form>` helps you by adding a validation process between the submission and the sending of the data. Instead of providing a _reference_ to the Submit button and then expecting an endpoint on submission, the data can be manipulated to perform some checks if required and then be sent through an AJAX call.

Now after moving `Submit` outside `form` your UI might look broken, so put the `Submit` button and the `form` element inside a `div` with `class: "Container"` and then add the `form`'s CSS styles to the class `Container`. You can remove the `width` attribute from the `form`'s CSS since `form` will take the entire width of the `Container`.

You might have to give _reference_ to the `form` inside the `submit` button when it is outside the `form`: 

```html
<form id="form1">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
</form>
<button type="submit" form=“form1”  value="Submit">Submit</button>
```

We need `JSON.stringify` to convert JSON objects to text, since HTTP communicates over text.

```javascript
var jsonObject = {name: "Linus", job : "Engineer"};
var jsonString = JSON.stringify(jsonObject);

console.log(jsonString);

// Console log output
{"name": "Linus", "job" : "Engineer"}
```

**XMLHttpRequest**
`XMLHttpRequest.open(method, url, async, user, password)` initiates a new connection with the address provided as its parameter and also the method.
1. `method` is the HTTP request method used to talk with the server.
2. `url` is the url address of the resource trying to access
3. `async` is optional, with default value true. When the script sends a request to the server, it continues with the execution and doesn't wait for the response. Once the response is received the browser event is triggered and the script performs the associated actions.
4.`user` is optional, default is null. If the resource we are trying to access requires a username, input here.
5. `password` is optional, default is null. If the resource we are trying to access requires a password, input here.

`XMLHttpRequest.send(body)` connects to the server and forwards the request to the server. `body` is an optional parameter which can be in the form of a data or a file. If nothing is mentioned, its value is null. Primarily used for `PUT` or `POST`. `GET` request does not have a `body` parameter.

`XMLHttpRequest.onreadystatechange = callback;` listens for change in `XMLHttpRequest.readyState`, and on change it calls the `callback` function.

The `XMLHttpRequest.readyState` table is:
1. `UNSENT`, value `0`: request initiated, but call has not been opened yet.
2. `OPENED`, value `1`: `xhr.open()` has been called.
3. `HEADERS_RECEIVED`, value `2`: `xhr.send()` and headers have been called. Server acknowledged that it has been communicated with.
4. `LOADING`, value `3`: server is processing the request & is sending back the data, which is being stored in `xhr.responseText`.
5. `DONE`, value `4`: data has been received and communication with server is done.

We have to wait till `xhr.readyState == 4`. Then add another check for `xhr.state` which captures the HTTP response code sent by the server.

`200` and `201` response codes indicate that the request was a success.

**HTTP request methods**
An HTTP request method has a message head and a message body. The head contains the URL and headers, whereas the body contains the information to be sent. There are different HTTP request methods, but the major ones are as follows:

1. GET: request a particular resource from a server. Response can CSS file or a json object. This request does not have a message body; information is sent through the message header. It’s excellent for requests that are just supposed to send a small amount of information to a server and then receive some output.
The syntax of the GET request as sent by the browser is of the following form:
`Message Head: <URL>/endpoint.html?query1=query`
The XMLHttpRequest of a GET request would look like this:
```javascript
xhr.open(‘GET’, ‘<URL>/endpoint.html?query1=query’);
xhr.send();
```

2. POST: post data to a particular resource. Has a message body along with message head.
The information you send through a POST request is not stored in the browser; neither is the POST request cached. This makes it more desirable for sending sensitive information such as passwords or card information. The information is still sent after a proper encryption process.
 
The syntax of a POST request as sent by the browser is —
```
Message Head: <url>/api/test
Message Body: query1=query
```
The XMLHttpRequest of a POST request would look like this:
```javascript
xhr.open(‘POST’,’<url>/api/test’);
xhr.send(‘query1=query’)’;
```

3. PUT: They are idempotent (making multiple identical requests has the same effect as making a single request). PUT calls instruct the server to delete the existing resource and put the resource sent in the PUT request there, instead of modifying the resource in the URL mentioned. This is important in cases where you don’t want overlap of data. PUT calls are similar to the Update operation in a database. The syntax of a PUT request as sent by the browser is —
```
Message Head: <url>/api/test
Message Body: query1=query
```
The XMLHttpRequest of a PUT request would look like this:
```javascript
xhr.open(‘PUT’,’<url>/api/test’);
xhr.send(‘query1=query’)’;
```

4. DELETE: delete the particular resource. Does not contain any message body.
The syntax of a DELETE request as sent by the browser is of the following form:
```
Message Head: <URL>/endpoint.html
```
The XMLHttpRequest of a DELETE request would look like this:
```javascript
xhr.open(‘DELETE’, ‘<URL>/endpoint.html’);
xhr.send();
```

An example script is:
```javascript
function enterTheCode(country) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.openaq.org/v1/cities?country=" + country.value);
    xhr.send();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // we could also use xhr.response
            console.log(xhr.responseText);
        }
    };
}
```

**HTTP status codes**
First digit signifies one of the 5 predefined standard classes of response:
1. Informational - 1: server has received the request and is processing it
2. Success - 2: server has successfully processed the request
3. Redirection - 3: server has redirected the request
4. Client Error - 4: request made by the client has some error in it
5. Server Error - 5: error in server and can't process request

Some Common HTTP response headers are as follows:
 
100 - Continue
200 - OK
201 - Created
301 - Moved Permanently
400 - Bad Request
404 - Not Found
415 - Media Type Not Supported
500 - Internal Server Error
502 - Bad Gateway

Error 415 is code for “Media Type Not Supported”. When you transfer some data over any application, the data needs to be sent in a fixed format so that the receiver knows how to read and interpret the data. It’s like sending data to someone in a box so the data does not get changed, but then you also need to send the key of the box to open it and access the data. The definition of the encoding is the key so that the box can be opened.

**HTTP** headers are used by clients and servers to communicate with each other:
1. `General Headers`: used by clients & servers communicate information having no connection with the resource they have to transmit, eg "Date", "Cache-Control", "Connection" etc.
2. `Request Headers`: sent by client (browser) to the server, info about the client (browser, OS, data encoding type), or more info about the resource.
Some common request headers are as follows:
`host`: It tells who the host is that the request is being sent to.
`method`: It tells the server which HTTP request method is being used to send the request.
`accept`: It tells what methods are accepted by the browser.
3. `Response Headers`: sent by the server to the client, contain more info about the content being served to the client or the about the server.
Some common response headers are as follows:
`content-encoding`: This information is sent by the server telling the browser the encoding type of the content, so the browser knows how to decode it.
`expires`: This information is sent by the server telling the browser till when the server will sustain this particular API call.


This code is an example of sending a `POST` request:
```javascript
function sendPostRequest(userName, userJob) {
    var params = {
        name: userName.value,
        Job: userJob.value
    };
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://reqres.in/api/users");
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.send(JSON.stringify(params));
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 201) {
          console.log(xhr.response);
      }  
    };
}
```

`window.btoa` encryption encodes a string in base64. Use `window.atob` to decode it back.

`XMLHttpRequest.setHeader("Authorization",“Basic” + window.btoa(“Rahul:Rahul123”))` is used for basic authorisation. We use the `access-token` from the response headers after a successful login for validating all other API calls.

An access token is a way to tell the server that the API call that has been made to the server is by a user who’s already logged in. This is performed by the server creating a string that is unique to the user and sending the user that string after he/she logs in. This string is the access token, and for every API call after the login, this string is mandatory for the server so that it can validate the API call.
 
Access tokens are generated by the server using a secure algorithm, and then that token is stored against your credentials in a secure database by the server. Then, the token is transferred to you and that becomes your “pass” to use the APIs provided to you.

There is no standard practice of generating them. Each company generates them in their own random way, and the details of how they’re generated are very closely guarded.
Some companies use the user ID and subsequent information (e.g. the time stamp) to generate an access token after encoding them, whereas some others use totally random strings.

These methods have their own pros and cons. A totally random string as an access token is much more secure than an access token generated by encoding the user information because there is no inherent order in generating the string; hence, no data can be inferred from it.
 
On the other hand, retrieving data for a totally random string takes much more time than a string that has been generated by encoding a data sent by the user. This is because the database now has to traverse through all of the data to see if the string matches for a user.

Code to generate a token:
```javascript
function generateToken(userName,userPassword){
    if (userName.value.length == 0 || userPassword.value.length == 0){
        alert("Please Fill in the Complete Information")
    }
    else{
        var currDate = new Date().toLocaleTimeString();
        var stringToEncode = userName.value+userPassword.value+currDate;
        var accessToken = window.btoa(stringToEncode);
        console.log(accessToken);
    }
}
```

**Storage Type**	
1. Cookie
Memory: 4Kb
Persistence (Lifetime of data):	Unlimited unless explicitly deleted
Access: Can be accessed both by the server as well as the client, _can be programmed for only server access_
Preferred Usage: For storing sensitive data as they can be programmed to be only used by the server

2. Session Storage
Memory: At least 5Mb
Persistence (Lifetime of data): Stores the value till the tab or window remains open
Access: Can be accessed only by the client-side
Preferred Usage: For values that only need to persist for the duration of a tab eg: Score in a game

3. Local Storage
Memory: At least 5Mb
Persistence (Lifetime of data): Unlimited unless explicitly deleted
Access: Can be accessed only by the client-side
Preferred Usage: For values that require ongoing persistence eg: CSS files for web pages

**Session Storage**
Eg. items in Amazon cart, or the access token provided by the server. Local storage should not be used for such use cases because it need not stay in the memory for more than the time they are relevant (for eg. only till you do the payment in online shopping)  as storing such data would fill up the local storage very quickly.

We use `sessionStorage.setItem("user-detail", xhr.responseText)` and `sessionStorage.getItem("access-token", xhr.getResponseHeader("access-Token"))` in the callback `xhr.onreadystatechange` for storing these info in the session storage.

**window in JavaScript**
The browser provides JavaScript with some APIs so that JavaScript can interact with the browser, instructing it to perform some functions like opening a new tab, or changing the current URL. These APIs are known as **WebAPIs**. ‘window’ is one such WebAPI, which provides the browser access to the window (your system’s window) which contains the current DOM element. In short, it represents an open window in a browser.
 
window is a global variable WebAPI, and for a given page, every Javascript function associated with the page can access its properties. Similarly, any function or variable defined globally is said to be the part/property of window variable.
 
An example of this can be found in this code snippet.
```javascript
var carCompany = "maserati";
console.log(window.carCompany);
// this gets printed in console
maserati
```
`carCompany` is defined at a global level and hence is available as a variable in window.
 
Some common methods and properties provided by window variable are-
`window.innerHeight` - This property provides the inner height of the browser windows.
`window.open()` - This method opens a new window with the given URL.
`window.scrollTo()` - This method scrolls to a particular set of coordinates.
`window.location` - This property provides the current location/URL of window.
 
`window.location.href` is a common property used to redirect webpage to a new location in the same window or tab.

`window.location` method gives you the current URL, and as the link is a relative link, `window.location.href = www.google.com` appends the page address with `www.google.com`.

If you want to redirect the page to `www.google.com` using `window.location.href` method, you’ll have to give the complete address of the webpage i.e `https://www.google.com` instead of `www.google.com`. This is because `www.google.com` is a relative link, and `window.location.href` will append relative links at the end of the current page address.

Use `JSON.parse()` to parse string to JSON.

Code to get access token from the session storage: `var access = sessionStorage.getItem('access-token');`.

The session storage is being created by the window object, and as that is the global level variable, the session storage would be available to any webpage open through window variable in the context of current webpage. So it can be accessible from other tabs.


**forEach and map**
`.forEach()` works on the array, i.e it will affect the elements of the array you asked the function to work on. `.map()`, on the other hand, creates a new array as the result.
```javascript
var arr = [1 ,2 ,3];
const mapArr = arr.map(function(index) {
  return index*2;
});
console.log(mapArr);
```
The output of this function would be `[2,4,6]`. The actual `arr` would not change.
`.forEach` function, on the other hand, does not create any new array, nor does it return any value. `.forEach` is best used when you need to cycle through an array and perform functions like printing the value.
```javascript
var arr = [1 ,2 ,3];
arr.forEach(function(index){
  console.log(index*2);
});
```
The output would be
```
2
4
6
```
But no new value or array would be returned.


`readyState` would be 4 no matter there is error code or not.


Making all the API calls in a for loop is a bit problematic because of security reasons. The browser thinks of multiple API calls arising from the same source as an application trying to slow down its performance by inundating it with a lot of calls, which is quite similar to spamming a system. This is the reason that browser will block any such call.

`Event Driven API calls` form the backbone of modern JavaScript. Getting all the data for a particular webpage in a single API call causes the webpage to load slowly.
Imagine if Facebook loads all the data that’ll appear on your home screen in a single go. This means all the posts and all the comments on the post would be downloaded regardless of whether you want to read them or not.

`.toString()` method converts to string in JS.

`Event bubbling` arises when there are nested elements. The idea is that if one element is nested inside another like it was in our example, where `delete-btn` and `project-btn` are nested inside `div`, their events get linked.

Both the buttons, as well as div, have some `onClick` property attached to them. This causes a problem when the inner event is triggered, i.e the `onClick` button of the nested button (`delete-btn`) is clicked. This causes the `onClick` property of the `div` to be activated too. This happens because as the `div` is the parent container of the button, and in DOM, if you click the button, you’re clicking the div too. This bubbling of events, for eg. the `onClick` of child triggering the `onClick` of the parent is called as `event bubbling`. The solution to this bubbling is if there was a function that could limit the bubbling at the moment this function is defined.
There exist such a function known as `event.stopPropagation`. This function causes the triggering to stop the moment where this is defined. We define it in the `onClick` function for `delete-btn` to stop event bubbling.

Code for implementing `POST` request and saving the server response in `Session Storage`:
```javascript
function sendPostRequest(userName,userJob) {
    var params = {
        name: userName.value,
        job: userJob.value
    };
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://reqres.in/api/users");
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.send(JSON.stringify(params));
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            sessionStorage.setItem("user_ID", xhr.response);
        }
    };
}
```

This displays the response:

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.openaq.org/v1/countries");
xhr.send();
xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
        var response = JSON.parse(xhr.response);
        document.getElementById("country_data").innerHTML = "<p>Country Country Code</p>";
        response.results.forEach(function(value, index) {
            document.getElementById("country_data").innerHTML += "<p>" + value.name + " " + value.code + "</p>";
        });
    }
};
```

















