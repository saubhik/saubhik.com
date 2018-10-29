# DevOps

The principles of DevOps is shortened as CALMS:

- **Culture:** It gives the preference order of people over process over the tool. It aims to maintain a good culture within a company.
- **Automation:** Instead of doing work manually and in a “hands-on” fashion, automation is preferred, not only in one part but throughout the DevOps process.
- **Lean:** It focuses on creating a smooth end-to-end flow, from the idea to the cash flow.
- **Measurement**: Considering the importance of data, not only the application but also the user’s activities are to be monitored
- **Sharing**: The interests of all the teams should be aligned so that they are always on the same page. To this end, continuous sharing of information is important.

***

Rollbacks is an important DevOps practice. The application once developed is updated constantly according to the present needs of the users. Now, if any application update breaks, it does not shut down the whole application. So, users are not able to find it out because the update is rolled back and the previous version is loaded till the update gets fixed. 

The different stages in the workflow are:

1. Coding = Initial code + static analysis + unit tests
2. Testing = Integration test + quality assurance
3. Testing = Staging server + acceptance testing (automated build & testing on real data)
4. Deployment =  Production server

***

**The practices involved in the implementation of software development are as follows:**

- **Source control management:** It allows you to keep track of all the changes made in the source code, making it easier to identify any buggy code and recover the code that was running fine.
- **Continuous integration:** It is a practice where automatic builds and basic tests are executed, and the feedback is sent to the developer whenever the code is checked into the source control management tool.
- **Continuous testing:** It is a practice that allows developers to perform automated testing on the software development pipeline, and then provide automated feedback regarding the tests to them so that they can spot gaps, errors, etc.
- **Continuous delivery:** It is a practice where all the code changes are automatically built and tested, and the code is made ready for deployment. Here, the testing is of a different kind; the focus is more on test cases specific to the end user’s use, and less from a unit or functional perspective.
- **Continuous deployment:** It is a practice that allows the automatic deployment of a delivered product in the production server, which may be on the cloud or stored locally. It also allows automatic recovery and rollbacks, in case of failures.
- **Continuous monitoring:**  It is a practice where the performance, availability, and other important metrics of the application are continuously monitored in real time. It allows tracking of metrics and monitoring of log files and resources used for the deployment of the application.
- **Configuration management:** It is a solution that automatically creates a self-serving environment — one that configures and manages resources, operating systems, and application stacks automatically.

***

Eight stages of a software development life cycle are:

1. Plan: To create a proper plan for the development of the whole application
2. Code: To write the actual code for the individual features of the application
3. Build: To build the code written to check whether it can be compiled and executed successfully or not
4. Test: To test the code that is written, based on its quality and the initial requirements provided
5. Deploy: To launch the application on the production server, but still keeping it invisible from real users
6. Release: To make the final application available to users
7. Operate: To continuously manage the deployment process
8. Monitor: To monitor the application with all its resources after its deployment

***

##Continuous Integration

While dealing with microservices, it is important to make sure that each microservice is interacting with the others because at the end, they will be part of a single application. So, integration bugs are the errors that come when the cohesiveness of two different services is checked. Integration testing also tells whether the services are well integrated with the databases or not. If not, integration bugs are found.

- Developers commit code changes to the source control server.
- The CI server is always looking for new commits in the source control server; as soon as it recognizes a new commit, it fetches the changes.
- The fetched code enters the cycle/pipeline in which it is built.
- If there is a problem at any point in the pipeline, for example, if the code fails to compile, appropriate feedback is sent to the developers.
- After the successful build, there is a testing stage in which unit tests are done on the build code.
- The notification of the success or failure of the tests is sent to the developers.
- This cycle runs for each module of the application code, one by one.

 

**The primary benefits of continuous integration are as follows:**

- It detects integration bugs early on. They can be tracked down easily due to small commits.
- Automated feedback helps developers rectify the errors as soon as they are encountered.
- Since the small commits are already tested and built here, the developers don’t have to worry about their code being able to merge with the final code or introducing bugs into the overall software.
- The use of incremental commit is always a good practice since it makes the code modular.

 

**The major tools available for continuous integration are as follows:**

- Jenkins
- Travis CI
- Bamboo

Build automation is a process that automatically compiles the code and creates a build artifact to deploy. Continuous integration, on the other hand, is a process that includes build automation and the testing of that build. So, build automation can be seen as part of continuous integration.

**The tools used for build automation are as follows:**

- Java: Maven, Gradle
- JavaScript: NPM, Webpack, Grunt, Gulp

Any code written by a developer is in a high-level language, which is in a human-readable format. However, a computer does not understand this language. So, it has to be converted into machine-level language so that it can be understood and executed by computers. This is done through the build process.

The inbuilt process in build automation are as follows:

1. Fetching the code from the source control
2. Compiling the code
3. Performing dependency check on the code
4. Linking the libraries with the code
5. Creating an artifact of the code in a binary or executable format once the build is successful
6. Creating a build log and archiving it
7. Sending notifications of success or failure to the developers

***

Alpha testing is a kind of acceptance testing done before deployment. It mainly involves simulation of the tasks performed by real users, while beta testing is done by the actual users on the prototype of the final application. Based on the use of this prototype, users provide their feedback, addressing features they like or the issues they face while using the application.

As you can see, unit testing is at the base, while beta testing is at the top. The bottom five tests are technology related, and the top two are business related.

The major tools for testing are as follows:

1. JUnit for writing back-end unit tests
2. Mocha and Chai for writing front-end unit tests

![img](https://images.upgrad.com/9294e0ae-9ba1-4e0d-af17-e7d1cc17c846-V13_PL33_OG (0-00-01-00).png)



***

##Continuous Delivery & Continuous Deployment

Continuous delivery is the process that ensures that the application is always in a deployable state, but needs to be manually triggered.

Continuous deployment is the process that ensures that application is deployed automatically without any manual intervention.

**Continuous delivery refers to the process of keeping the code in a deployable state.**  Specifically, it follows continuous integration and automates the entire DevOps process, up to pushing the application to the production server. For example, the code is deployed in the staging server, where acceptance testing is conducted on the application, to make sure that it performs well if deployed in the production server.

The primary goal of continuous delivery is to make sure that the software is packaged in such a way that it can be readily deployed to a production-like environment.

**Continuous deployment refers to automatically deploying the code in small increments, frequently, to production.** So, it allows automatic recovery and rollbacks in case of failures.

**Four standard processes in deployment are as follows:**

1. Use the same server configuration throughout the SDLC, building, testing, QA, and production.
2. Automate the different stages of software development through continuous integration, continuous delivery, and continuous deployment, and also automate the transition between the different stages.
3. Deliver incremental changes.
4. Release the software to the production server only when it has passed all the required tests.

You also saw that both continuous delivery and deployment are quite similar, and they differ mostly by the end of the pipeline.

​                 ![img](https://images.upgrad.com/8ddf69f0-097c-416d-8342-0ca9d31e6a7f-7.3.2%20image%20recreation%20(1).png)

 

As mentioned earlier, in continuous delivery, the application is always in a deployable state but needs to be manually triggered. In the case of continuous deployment, the application is deployed automatically, without any manual work from the software developer, tester, or QA team.

Both continuous delivery and deployment are important because they automate the deployment process. If any problem arises during delivery or deployment, the software can be easily rolled back to the previously working version. Thus, they create an environment that is more reliable, fast, transparent, and easy to use.

**The major tools involved in continuous deployment are as follows:**

- AWS CodeDeploy
- Elasticbox
- Jenkins

***

DevOps has always been aiming at automating the software development process. Infrastructure as code lets you write codes to manage configurations and automate infrastructure provisioning. So, the code has to be written only once, based on which the infrastructure can be provisioned as many times as required for all the different environments.

## Configuration Management

**The major benefits of configuration management are as follows:**

- **Maintains the consistency of software and systems:** It helps developers write scripts to make sure that systems, servers, or a set of servers follow the prescribed steps during their configuration, ensuring consistency.
- **Saves time:** It saves time in replicating environments. As the infrastructure is already configured, you can replicate it simply with a few lines of code or the push of a few buttons.
- **Provides scalability:** It makes the application scalable with the help of resources that can be replicated at will, without altering the configuration. For example, if a DevOps person at Google has to configure tens of thousands of servers, it will be time-consuming for him to do it manually and also prone to errors. This is where configuration management comes to the rescue.
- **Allows more control:** It provides more control of entire servers or environments; with only a few changes, all the servers can be configured simultaneously.

It provides these benefits by embedding the infrastructure into the code itself. Here, **infrastructure as code (IaC)** is the process of writing a code to manage and provision computing infrastructure (processes, bare-metal servers, virtual servers, etc.) and update the server configurations.

The infrastructure as code approach has become increasingly widespread with the adoption of cloud computing and infrastructure as a service (IaaS). This is because it helps in managing infrastructure, such as server setup, network security, virtual machines, etc., in a descriptive model.

**The tools used for configuration management are as follows:**

- Chef
- Ansible
- Puppet

## Continous Monitoring

Validated learning promotes the concept of ‘learning by doing’. So, if you have any theory, try to implement it. If you fail, you can rethink your theory, but if you pass, your theory will have some validation too.

**The different types of monitoring are as follows:**

- Resource monitoring
- Network and security monitoring
- CPU and disk usage monitoring
- latency
- Memory monitoring
- Uptime

**These kinds of monitoring can be provided as dashboards — in the form of graphs, charts, etc. — and can prove to be beneficial, as it gives you real-time analysis.**

One vital goal of monitoring is to ensure high availability by minimising the **time to detect and mitigate (TTD, TTM)**. After mitigation, the teams work on remediating problems at the root cause, so that they do not recur. The time is measured as **TTR (time to repair).**

The second goal of monitoring is to enable “**validated learning**” by tracking usage.

It can also help analyse user data to gain a business perspective.

**The tools available for monitoring are as follows:**

- AWS CloudWatch
- Nagios
- Zabbix

You learnt that continuous monitoring helps you monitor the performance of the infrastructure, service, etc. on the technical front. It can also help you from the business perspective by providing user-relevant data.

## Containerisation

The code created by developers has to run on different systems, such as the tester’s system, the system administrator’s machine, etc. Therefore, the codes created by developers are not always independent; they have underlying dependencies on OS, libraries, and other things. If these dependencies don’t match the developer's system, this might create some problem. Here, containers give you a way out by packaging all the dependencies into a single image file.

You must have got a complete understanding of what containers are and how they can be helpful. A container lets you standardise the whole environment on which your application is based. It sets you free from underlying connections, such as operating systems, hardware, and software, thus making your software independent of your system.

**A container allows you to package everything — your application binary files, configuration files, libraries, and other parts of your application stack — into a single container**. You can think of a container as an image file that lets you run the container in any environment, irrespective of its hardware and software specifications.

So, overall containerisation allows you to package everything required to run your application in a single file and deliver it for deployment. This makes your application independent of systems, easy to use, and anybody with that container can run your application.

**A container is similar to a virtual machine but trumps VM since it contains the bare minimum resources required to run a software.** VM, on the other hand, contains the entire OS and a virtual version of all the hardware required for the application to run.

**The major containerisation tools are as follows:**

- Docker
- Kubernetes
- Mesos

You can orchestrate the containers based on your requirements. Orchestration helps in automating processes and workflows. So, you don’t have to micromanage here; you just have to provide commands on a higher level. This is heavily used by companies such as Netflix. **This helps your application by making it:**

- **Scalable**, as the resources can be requisitioned or dropped on demand
- **Time-saving**, since the process is mostly automated, thereby reducing the time consumption
- **Stable**, as orchestration tool, automate most things, reducing the chances of errors; and even if they occur, they get fixed automatically

Container orchestration refers to managing containers in different dynamic environments. **Different tasks can be automated using container orchestration, such as:**

- Provisioning and deploying containers
- Scaling and removing containers on demand
- Monitoring containers

**Docker is a tool used for containerisation.** It also facilitates the orchestration of those containers, making it a container orchestration tool.

An image is essentially a template that can be turned into a container, which basically means they are used to create containers. Once the image file is built, it creates a container. So, a running instance of an image is a container, while a docker image only contains the application and all its dependencies.

## Software Development Pipeline

There are eight major stages involved in the pipeline:

​                   ![img](https://images.upgrad.com/4e005b49-5436-4d44-aec1-f821c355b21f-V19_PL61_OG%20(0-04-54-10).png)

 



1. **Stage 1:** In this stage, the developers write the application code, and then do static analysis and code review on it.
2. **Stage 2:** Developers write the unit tests, which the code has to pass to move forward.
3. **Stage 3:** Once the code passes the unit tests, it should be able to build and create an executable.
4. **Stage 4:**  Since the application is a culmination of several different software components (e.g. application layer, service layer, database layer), you need to do integration testing on the various components to ensure that each of them is working well with the others.
5. **Stage 5:** If the integration test passes, the code is deployed to the staging server.
6. **Stage 6**: On the staging server, acceptance testing is done on the application to check how well it performs in a real environment with real data.
7. **Stage 7:** Once the application has passed the acceptance test, the final code is sent for deployment on the production server.
8. **Stage 8:** Once the code is deployed and a release is produced, it is continuously monitored along with the resources hosting the application.

If there is a problem at any point in this pipeline, proper feedback is sent to the developers and the other parties involved. This completes your software development pipeline. An important thing to note here is that this pipeline is generic and can be customised based on the requirements of the application.

​      ![img](https://images.upgrad.com/a0b6537b-5532-488a-b1a8-66dfabf4114d-V20_PL63_OG%20(0-03-50-04).png)

As you can see DevOps sits at the top and combines the two teams, development and operations. All the practices that make DevOps are then fit inside this architecture.

***

