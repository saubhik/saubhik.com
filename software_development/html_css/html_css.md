## html and css

HTML is hypertext markup language. Hypertext is text that links to other information. A markup language distinguish between its elements & normal content. It defines a way of formatting content.

An **HTML element** consists of an opening tag and a closing tag. Anything inside the opening & closing tags is a **content** of the element.

`<!DOCTYPE html>` is used to tell the browser the version of html. For html5 we use `<!DOCTYPE html>`. It's not mandatory but if you don't write it the browser will assume some html version by itself. 

`<html>...</html>` encompasses all other html elements and is considered a root element for an html page. A root element is the highest level parent element that has other elements as its children. It can be considered to have 2 children elelements,
* `<head>...</head>` which is the parent element of `<title>...</title>`
* `<body>...</body>` which is the parent element of `<p>...</p>`

Character sets can be defined on a `<meta>...</meta>` tag. Also used to define the responsiveness of a web page.

Inside head tag we can have:
* title tags
* meta tags
* script tags to include javascript files into our web page
* style tags to style elements to our web page

Inside body tag we can have:
* paragraphs `<p>...</p>`
* headings `<h1>...</h1>`. There are 6 different variations, h1 to h6, with h1 being the largest with thickest bold effect
* hyperlinks `<a href="">...</a>`
* aside `<aside>...</aside>`
* sections `<section>...</section>`
* image tag `<img>`
* video tag `<video>...</video>`
* audio tag `<audio>...</audio>`, in html5

The aside and section tags are used to format the paragraphs.

2 different types of tags:
* Tags having a closing tag
* Tags not having a closing tag or self-closing tags - example, `<img>`, `<br>`, `<meta>`  does not have a closing tag.

Some tags are **block** and some are **inline**.
* `inline` elements take up only the space they require. There are no line breaks before or after them. Examples: a, br, button, img, input, script, select, span, textarea.
* `block` elements have a line break before and after them such that they take up the entire horizontal width of a row. Examples: aside, div, form, h1 to h6, header, li, ol, p, section, ul.

#### More Tags
**Attributes**
They provide additional information about a tag. It is a property of a tag. The `<a>...</a>` is called the anchor tag, used to create hyperlinks. `href` is an attribute of the anchor tag. Image tag `img` has attributes `src` and `alt`. The latter one can help vision-impaired users who use screen reader software.

`<a href="https://www.google.com/" target="_blank">Here to google</a>`, opens the google site in a new tab, due to the attribute `target="_blank"`.

Remember that `span` is inline whereas `div` is a block element.

`ul` is unordered list, `ol` is ordered list, `li` is a list item.

For example:
```html
<body>
	<ul>
		<li>This is unordered list item</li>
		<li>This is unordered list item</li>
	</ul>
	<ol>
		<li>This is ordered list item</li>
		<li>This is ordered list item</li>
	</ol>
</body>
```

Section tags are inline elements.

**Grouping in HTML**
To group individual elements in HTML we use the `div` and the `span` tags. This is done to apply similar CSS properties (style, colour, height) to a group of elements so that I don't have to apply them individually. It also gives structure to our HTML code.

We will make a small project management app which has:
* sign-up page
* login page
* boards page
* tasks page

Today, we will focus on sign-up page & login page.

`input` elements are known as **form** elements. In order to send data gathered by input elements to a server, we wrap it in `<form>...</form>` tags.

The `<form>...</form>` element helps in collecting data from all the input fields and sends it to the server when the user clicks "submit". It has the following attributes:
* action - specifies the URL where the data is sent when user clicks on 'submit'
* method - which HTTP method to be used, GET or POST
* target - specifies where to display the response received after submitting the form. It can have `_blank`, `_self`, `_parent`, `_top` values.


```html
<!DOCTYPE html>
<html>
	<head>
		<title>My Page</title>
	</head>
	<body>
		<form>
			<input type="text" placeholder="Your name">
			<button>Submit</button>
		</form>
	</body>
</html>
```

Remember that img tag is an inline tag.


## CSS
CSS stands for Cascading Style Sheets.

```css
Selector {
	Property: value;
}
```

**Selectors** identify the element that is to be styled, from all other HTML elements. Within the opening & closing braces succeeding the selector, we can use any CSS property and give a value to that property. Add a `;` after the Property-value.

Use [this](https://www.w3schools.com/cssref/) for CSS reeference.

*Read about the `position` property (static, relative, fixed, absolute). And also about `width` property (which can be defined in px or %).*

Styles in CSS that have the highest priority tend to override all the other properties. That's why it is called "Cascading".


Types of selectors (used for style sheets to access the HTML elements):
1. ID (unique)
2. Class (multiple HTML tags can have the same class)
3. Tag (applies style directly to a HTML tag)


We can do this, but this makes our HTML cluttered:
```html
<body>
	<form>
		<h1 style="text-align: center;">Signup page</h1>
	</form>
</body>
```html


So we can do this:
```html
<head>
	<title>Signup Page</title>
	<style>
		h1 {
			text-align: center;
		}
	</style>
</head>
```

Whenever there is a `h1` tag, it becomes center-aligned. This is called `tag` selector.

ID > Class > Tag, in terms of priority, and hence the name CSS.


We can also do this:
```html
<style>
	h1 {
		text-align: center;
	}
	label {
		color: green;
	}
	#password {
		color: red;
	}
	.labelText {
		color: blue;
	}
</style>
```

Here, all the labels become colored green, with the exception of the label with id password, `<label id="password">Password</label>`, and the labels which have the class "labelText", `<label class="labelText">First name</label>`. Unlike ids, a class can be applied to many tags.


**Box Model**
* Content - you put content like text, images, videos, audio etc
* Padding - area between content & border
* Border - wraps the padding & content
* Margin - blank space wrapping the border from the outside


This is inline CSS:
```html
<!DOCTYPE html>
<html>
<head></head>
<body>
	<h3 style="color: red; text-align: center;">Hi, I am a heading</h3>
</body>
</html>
```

In rgba(red, green, blue, alpha), the alpha defines the opacity as a number between 0.0 (fully transparent) and 1.0 (fully opaque).


To declutter the html, we can keep the CSS in a different file called `index.css` and write this:
```html
<head>
	<title>Signup Page</title>
	<link rel="stylesheet" type="text/css" href="./index.css">
</head>
```

So we can add styles in 3 ways:
* inline, within html tags
* internal, within `style` tags
* external, in a separate file

The order of priorities is inline > internal > external.

We can even do this:
```html
<div class=”container”>
    <h1> Heading 1 </h1>
    <h2> Heading 2 </h2>
    <p> Paragraph </p>
</div>
```

and inside css:
```css
.container{
    background-color: black;
}
.container h1{
    background-color: white;
}
.container h2{
    background-color: blue;
}
.container p{
    background-color:green;
}
```


Remember that you select IDs by hashtags `#`, and classes by dots `.`.

**Flexbox**
A container, an area in which content is contained, can be made flexible by setting the display property to `flex`. The resultant container is called `flexbox`, and the elements inside this flexbox are known as `flex` items.

Properties of Flexbox:
* flex-direction: with values column, row
* justify-content: with values flex-start, flex-end, center
* align-items: (alignment of items inside flexible container on the vertical axis), using values flex-start, flex-end, center

So `justify-content` positions elements on the horizontal axis and `align-items` positions elements on the vertical axis.


**Viewport** is the area of the webpage that is visible to the users. It is different for each device and varies from a computer screen to a tablet to a mobile device.

Different types of values we can give to margin, padding & width:
1. em
2. pt or points
3. px
4. %

In order to set a margin of 10px to an element the best way to do it would be to use `margin : 10px;`

This will set a margin of 10px on all the sides. So instead of setting the left-margin, right-margin etc and increasing the lines of code you can use this one line of code. Also instead of writing - `margin: 10px 10px 10px 10px;` for each side you can reduce your effort even more and just write - `margin : 10px;`

Writing CSS for specific devices is called **Responsive CSS**.

The meta tag takes the following attribute, values and properties:
`name = viewport`. To handle the available area on the viewport:
`content =”width=device-width , initial-scale=1.0”`.

`width=device-width` is to tell the browser that whichever device it is, set the width to the width of the device. `initial-scale=1.0` is to set the zoom level of the page. Here 1.0 means do not zoom into the page.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Media queries are conditional properties that can update the CSS of the HTML elements if the webpage width dimensions satisfy the conditions defined in the media queries. Example:

```css
@media (max-width: 500px) {
	form {
		width: 80%;
	}
	label {
		color: green;
	}
}

@media (min-width: 500px) and (max-width: 1000px) {
	form {
		width: 80%;
	}
	label {
		color: red;
	}
}
```

We can accomplish the following using media queries:
1. we can add multiple breakpoints on the page for different screen sizes
2. we can change the layout of a page depending on the orientation of the page, portrait or landscape
3. we can hide certain HTML elements on different screens


When you zoom out you're increasing the viewport size. When media queries refer to "screen", they are talking about the browser's viewport width, not your physical screen's width. Also, when you are zooming in, you are decreasing the viewport size.



