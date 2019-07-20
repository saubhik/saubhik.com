---
layout: post
title:  "Full Stack Development"
date:   2019-07-06
tags: targets
---

I decide to spend the next few weeks learning the MEAN development stack, from
an udemy [course](https://www.udemy.com/mern-stack-front-to-back/). It is always
fun to hack something new.

The technology stack I want to learn is MFRN (Mongo DB, Fastify JS, React and
Node.js).

## To Do
I am just jotting down some topics I need to know:

* MongoDB:
	* Wired Tiger Storage Engine
	* Replica Sets
	* Sharding
	* Clusters
	* Indexing
* FastifyJS
* React:
	* Redux
	* react-router 4
	* semantic UI
* Node.js:
	* streams
	* I/O
	* web frameworks:
		* Express
		* Loopback
		* Fastify
* Javascript:
	* closure
	* prototypes
	* design patterns
* AWS:
	* EC2
	* ELB
	* Cloudfront
	* S3
* HTTP layer:
	* sockets
	* WebRTC
	* security

I know a bit of JS and React, a bit of S3, some DB concepts. Time to fix the
missing pieces.

## Action Plan
My plan of action is:
* Step 1: Understand the MEAN stack by working through the course.
* Step 2: Go for advanced course, or figure out MFRN stack by myself.
* Step 3: Build a better app. Re-iterate.

## Some Googling-based research
Some googling & fooling around yielded me some useful information:
* [Mean-Blog](https://github.com/DimiMikadze/Mean-Blog) : Blog using Nodejs,
	Expressjs, Angularjs and Mongodb. MEAN Javascript Fullstack application.
* [MERN Stack Course](https://www.udemy.com/mern-stack-front-to-back/) : MERN
	Stack Front to Back: Full Stack React, Redux & Node.js. The course helps in
	building and deploying a social network with Node.js, Express, React, Redux &
	MongoDB.
* [tuts756](https://thepiratebay.org/user/tuts756/) : Blessed be this guy's
	life.
* [Vimming JS](https://freshman.tech/vim-javascript/) : Make VIM sing in
	JavaScript.

Going through the course seems like the best thing that I can do right now.
Once, I make a web-application using MERN stack, I can go ahead and tinker
stuff, or move on to further.

## Coursework

### Introduction
Technologies covered: ES6+, async/await, react hooks, redux with DevTools, JWT
(JSON Web Tokens), Postman HTTP Client, Mongoose/MongoDB/Atlas, Bcrypt Password
Hashing, Heroku & Git Deployment.

Course will be of 2 halves:
1. Backend (using postman, mongoose for DB interactions, node, express)
2. Frontend (React, Redux for state management)

Initial steps:
* Install NodeJS.
* I will not use VS Text. Go to hell.
* I already have git.
* Install Postman for all the API requests. Cool. Done.
* Add ReactDevTools, & ReduxDevTools chrome extensions.

### Express & MongoDB setup
Lets use MongoDB Atlas.
MongoDB is a NoSQL DB, no relations, tables - document-oriented database program.

### Installing dependencies
```
npm install express express-validator bcryptjs config gravatar jsonwebtoken mongoose request
```

`express` is our main web framework for our backend.

`express-validator` for data validation - when we make a POST request to our
API if there are are fields that need to be there that aren't there, it will
raise an error.

`bcryptjs` is used for password encryption, before storing in DB.

`config` is used for global variables.

`gravatar` for profile avatars - if a user signs up they can use an email that
is associated with a gravatar account and it will automatically show their
profile image.

`jsonwebtoken` for using JWT to pass along a token for validation.

`mongoose` is a layer that sits on top of the database so we can interact with
it.

`request` is just a small module that will allow us to make HTTP request to
another API. We want our profiles to be able to have GitHub repositories listed
on them. So we're going to make that request from our backend so that we can
hide our API key and stuff like that.

These are our regular dependencies.

Now we will install couple dev dependencies.

`npm install -D nodemon concurrently`

`nodemon` will constantly watch our server so that we do not have to refresh it
every time we make a change.

`concurrently` will allow us to run our backend express server and our frontend
react dev server at the same time with one single command.

### Progress Checking
I have the following topics left:

* User API Routes & JWT Authentication:
	* 6 lectures, ~ 2 days
* Profile API Routes:
	* 9 lectures, ~ 2 days
* Post API Routes:
	* 5 lectures, ~ 2 days

I think I might be able to finish the backend part by next weekend.
