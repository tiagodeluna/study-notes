# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

## Summary
  
  * [Chapter 1 - Concepts](#chapter-1-concepts)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-1-concepts)
  * [Chapter 2 - Understanding the Value Stream](#chapter-2-understanding-the-value-stream)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-2-understanding-the-value-stream)
  * [Chapter 3 - Getting Started with DevOps](#chapter-3-getting-started-with-devops)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-3-getting-started-with-devops)
  * [Chapter 4 - The First Way - Accelerate Flow](#chapter-4-the-first-way---accelerate-flow)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-4-the-first-way---accelerate-flow)
  * [Chapter 5 - The Second Way - Amplify Feedback Loops](#chapter-5-the-second-way---amplify-feedback-loops)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-5-the-second-way---amplify-feedback-loops)
  * [Chapter 6 - The Third Way - Accelerate Learning](#chapter-6-the-third-way---accelerate-learning)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources/README.md#chapter-6-the-third-way---accelerate-learning)

# Chapter 1 *Concepts*

### Japan's influence (Toyota Production Systems - Lean)

 - *Muda* (Waste): eliminate waste wherever possible
 - *Mura* (Flow): It's about evenness. Getting the pipeline flow consistent
 - *Muri* (Stress): reduce stress on the system
 - *Kaizen* (Improvement): continuous improvement
 - *Kata* (Form): repetitive actions become memory muscle. It's about integrate Muda, Mura, Muri and Kaizen to become a natural behavior

--------------------------
> Lean is about being faster and more reliable
--------------------------

### Continuous Delivery Principle

 - Full test coverage: build quality in.
 - Work in small branches
 - Automate repeatable tasks
 - Pursue continuous improvement: Plan-Do-Check-Act (Deming cycle)
 - Everyone is responsible: If you build it, you own it.

### Continuous Delivery Anti-Patterns

 - Incongruent testing and production environments
 - Testing takes too long
 - Manual regression and acceptance tests
 - Long lead times
 - High technical dept
 - Slow and hard to change
 - High MTTR (Mean Time to Recover)

### Continuous Delivery Patterns

 - Everything starts in source control (e.g, Github)
 - Peer reviews (pull requests)
 - Automate everything
 - Trunk based deployment
 - Done means released
 - Stop the line: if your code breaks the build, then it needs to get fixed right away.

### DevOps Values

--------------------------
> "A lot about DevOps is culture" - John Willis
--------------------------
> "DevOps is continuously looking for new ways to break down silos, eliminate inefficiencies, and remove the risks that prevent the **rapid and reliable** delivery of software-based services" - Damon Edwards
--------------------------

 - No rock star mentality
 - Shared contributions
 - Healthy attitudes towards failure
 - Failures are learning opportunities (the Deming cycle)
 - The problem is the enemy
 - No blame games / Shared blame
 - No victims
 - 5 Why's
 - Develop shared metrics
 - Focus on end goal
 - Alignment of purpose
 - Shared goals / Slay the dragon
 - Aim / Goal / Why

### High Performance Organizations

 - Deploy more frequently
 - Have shorter lead times
 - Less failures related to change
 - They recover faster: their MTTR (Mean Time to Recovery) is much lower
 - Make work visible
 - Manage WIP (work-in-progress) and Flow
 - Create high trust work environments
 - Learn and embrace failure
 - Use Continuous Delibery Principles

----------------------------
> The collaboration of humans is probably the most important aspect of DevOps
----------------------------

# Chapter 2 *Understanding the Value Stream*

---------------------------------------
> "If you can't describe what you're doing as a process, you don't know what you're doing." – Dr. W. Edwards Deming
---------------------------------------

### Definition

---------------
> The sequence of activities an organization undertakes to deliver upon a customer request.
> The sequence of activities required to design, produce, and deliver a service to a customer.
---------------

 + Workflow (Flow)
   - The waste (Muda) of the work
   - The evenness (Mura) of the work
 + Lead Time
   - The time it takes one piece to move all the way through a process of the value stream from start to finish.
   - Lead time clock starts when the request is made and ends at delivery.
   - Lead time is what the customer sees.
 + Cycle Time
   - How often a part or product actually is completed by a process, as timed   bservation.
   - Cycle time clock starts when the work begins on the request and ends when the item is ready for delivery.
   - Cycle time is a more mechanical measure of process capability
    
-------------------------
> **Lead Time** is the overall time and the **Cycle Time** is the time we actually start processing the request.
-------------------------

### The Two Lead Times

 + Design Lead Time
   - Design and Development
   - Measures how do we get the ideas
 + Deployment Lead Time
   - Test and Operations
   - Measures how good we are at our automation

### DevOps Value Stream

| STEPS | LEAD TIME | CYCLE TIME |
| ----- | ----- | ----- |
| Create an idea  | Design L.T. | |
| Add work to the backlog | Design L.T. | |
| Create a user story | Design L.T. | |
| Implement as code | Design L.T. | |
| Check into version control | Deployment L.T. | X |
| Deploy into production | Deployment L.T.  | X |
| Validate the customer experience | Deployment L.T. | X |

### Understanding The Value Stream

---------------------
> Watch the baton not the runner. (a metaphor about a 40 meter relay race team)
---------------------

 - The Value Stream of how things work (*runners*)
 - The Value Stream of the work (*baton*)

### How to Reduce Deployment Lead Time in the Workflow

 - Small batches
 - Recude work in process (WIP)
 - 1x1 Flow
 - Reduce Bottlenecks (TOC)
 - Optimize Globally

### The Three Ways of DevOps

 + The First Way: Accelerate Flow
   - Left to Right
   - System Thinking (global optimization over local optimization)
   - Increased Visibility
   - Just in Time
   - Shorten Lead Time
 + The Second Way: Amplify Feedback
   - Right to Left
   - Shorten Feedback Loops
   - Learn Faster
   - Fix Defects Faster
   - Embedding Knowledge
 + The Third Way: Continuous Learning
   - Full Cycle
   - Continual Experimentation (act like scientists / PDCA method)
   - Learning from Failure
   - Repetition and Practice
   - Increase Resilience

### The First Way - Flow

#### Make work visible

  + Using storyboards:
    - Use Scrum, Kanban, etc.
    - Putting WIP limits
  + With metrics and management reporting:
    - Use the board as a tool for measurement and metrics
    - Track the WIP, Lead Time, Throughput, Flow Efficiency and Failure Load

#### Reduce Batch Sizes

  - Faster Feedback
  - Faster Mean Time to detect and resolve
  - Reduces risk
  - Less overhead

#### Single Piece Flow (1x1)

  - No inventory reduces Cycle Time
  - Create smoother workflow
  - Catch errors earlier
  - Creates learning opportunities

#### Small Batch and Single Piece Flow in Software

  - Small piece of code (e.g. feature)
  - Checkin to source control
  - Merge into trunk
  - Testing
  - Deployment

#### Limiting WIP

  - In *Cognitive Work* (or knowledge work), Interruptions* and *Context Switching* are very expensive
  - *Multitasking* is not a good idea, because it degrades performance
  - We want to *Reduce Handoffs* whenever possible

#### Eliminating Waste

  - Lean Software Development Wastes:
    + Unnecessary code or functionality
    + Starting more than can be completed
    + Delay in the software development process
    + Unclear or constantly changing requirements
    + Bureaucracy
    + Slow or ineffective communication (e.g. email-based communication)
    + partially done work
    + Defects and quality issues
    + Task switching

#### Reducing Bottlenecks

---------------------------
> "In any value stream, there is always a direction of flow, and there is always one and only one constraint; any improvement not made at that constraint is an illusion." – Eliyahu Goldratt
---------------------------

  - Theory of Constraints - The 5 focusing steps:
    + Identify the system's constraint(s)
    + Decide how to exploit the system's constraint(s)
    + Subordinate everything else to the above decision(s)
    + Elevate the system's constraint(s)
    + Warning! If in the previous steps a constraint has been broken, go back to step 1

### The Second Way - Feedback

 - Telemetry
 - Fault Injection
 - Safety Culture
 - Fast Feedback

#### Telemetry

 - Monitoring
     + Legacy: HP Overview, IBM Tivoli, BMC Patrol
     + Open Source: Nagios, Sensu, Zenoss
     + SaaS: Datadog, NewRelic, SignalFX
 - Logging
     + Splunk, ELK (Elasticsearch, Logstash, Kibana), Loggly
 - Analytics
     + Graphite, Riemann, Hadoop/Spark

#### Fault Injection

-----------------------------
> This is the mindset of where we purposely create faults in production, in order to learn faster and become more resilient by understanding those failures.
-----------------------------

 - Motivations:
     + Reduce MTBF (Mean Time Between Failures)
     + Reduce MTTR (Mean Time To Resolve)
 - Exercises:
     + Game Day
     + Netflix Simian Army
     + Netflix FIT (Fault Injection Testing)

**Netflix Simian Army**
- Chaos Monkey (hosts)
  + Basically kills a host (a virtual instance running on Amazon)
- Chaos Gorilla (Data Center)
  + Takes down a whole data center
- Latency Monkey (Inject Latency)
- Comformity Monkey (Best Practice)
  + Anything that shows up on a system that doesn't have certain tags or hashes, it doesn't conform
- Security Monkey (Security Violations)
  + Anything that violates security practices

#### Safety Culture

 - ICE:
    + Inclusivity
    + Complexity
    + Empathy
- Diversity
- Collaboration

#### Fast Feedback

  - A/B Testing
  - Dark Deploys
  - Inject Deployment Metrics in Monitoring
  - Developers Wear Pagers
    + If something breaks in the code, make the developer be the person that gets the first notification
  - Pair Programming
  - Peer Reviews

### The Third Way - Culture of Continual Experimentation and Learning

-------------------------
> "We are what we repeatedly do. Excellence, then, is not an act, but a habit." – Aristotle
-------------------------
> "Toyota is not a story about techniques. It's an organization defined primarily by the unique behavior routines it continually teaches to all it's members." – Mike Rother
-------------------------

 - Ivisible (Memory muscle):
     + Culture
     + Behavior
     + Habit
     + Autonomic
 - Visible (Learning culture):
     + Scientific Method
     + Depersonalized
     + Non.Blameful
     + Non Deterministic

------------------------
> "94% of problems in business are systems driven and only 6% are people driven." – W. Edwards Deming
------------------------

#### Toyota Kata

 - Improvement
     + Single-Piece Flow
     + Small J's
     + PDCA Cycle
 - Coaching
     + Mentee Relationship / Mentoring

------------------------
> "A production line that never stopped was either extremely good or extremely bad." – Taiichi Ohno
------------------------
> "Culture eats strategy for breakfast" – Peter Drucker
------------------------
> "I don't fear the man who has practiced 10,000 kicks. I fear the man who practiced one kick 10,00 times" – Bruce Lee
------------------------
> "Learning is not compulsory... neither is survival" – W. Edwards Deming
------------------------

#### The Andon Cord

 - **Anybody** on the production line see the cord
 - If someone saw a **defect**, he could pull that cord and **stop the line**
 - Each pull on the cord is a **Opportunity to Learn**


# Chapter 3 *Getting Started with DevOps*

### Improvement Paradox (Balancing Risk/Reward)

 - Typically small enough in scope with a high probability of success and safe to fail
 - Large enough to have impact with possibility of future improvements while not appearing as a trivial experiment

### Value Stream Mapping

------------------
> Value Stream Mapping is the main tool used to map out Value Streams.
------------------

## Pick a Value Stream

There are basically three types of value stream:
 - Legacy
 - Greenfield
 - Brownfield

### Legacy

 - SOR and SOE
   + System of Record (Mode 1)
   + System of Engagement (Mode 2)
 - The 3 R's
   + Reward
   + Risk
   + Resistance

#### The 3 R's for Legacy

 - Leadership suppert is critical
 - Look for **Innovators** and **Early Adopters**
 - Prior knowledge of DevOps helps
 - System of Engagements is better then System of Records
 - Build on success

#### The ETTO Principle - Efficiency-Thoroughness Trade-Off (Erik Hollnagel)

 - Efficiency
     + Low investment
     + Sufficient to achieve the goal
 - Thoroughness
     + Achieve the objective without any unwanted side-effects
     + Outcomes will be the intended one

#### Focus Areas to Look For

 - Long wait times for work
 - Change approval bottlenecks
 - Rework is generated
 - Percentage of change and accurate (Backwash)

### Brownfield

------------------------
> Brownfield development is the process of develop new features in a legacy application, trying to treat it as a greenfield.
------------------------
> The strangler vine wraps itself around the host tree, kills it, and then becomes the host tree itself.
------------------------

 - Process:
     + Addind a new (greenfield like) featore to legacy
     + Altering functionality of a service
     + Upgrading a core service of a legacy application
 - "Strangler Application" pattern (Martin Fowler):
     + Event interception: You build an abstraction about any inbound-outbound events in order to break up the interface and implementation, so you are able to work on the inner part, because the outer boundaries are protected
     + Asset Capture: Similar to an event. but in this case you look at a particular asset and you basically encapsulate that asset
     + Legacy Test Automation

### Greenfield

------------------------
> A Greenfield project is the process of develop a system for a totally new environment, without concern for integrating with other systems. Such projects are deemed as higher risk, as they are often for new infrastructure, new customers, and even new owners.
------------------------

## Understanding Organizational Change

### Organizational Goals

 - The pipeline is everyone's responsibility
 - Focus on making more generalists: less focus on specialists
 - Fund services, not projects: projects tend to end. A service never ends, it just continues.
 - Encourage loose coupling
 - Smaller teams (and smaller services)
 - High trust and low blame
 - Make work visible

### Individual Level

Four areas arount the individual level:
 - I/T/E-Shaped Individuals
 - Mindsets
 - Motivation
 - Intent

### I/T/E-Shaped Individuals

#### I-Shaped

- Specialists (linear skilled)
- Deep expertise in one area
- Very few skills in other areas
- Can create bottlenecks
- Can create downstream waste

#### T-Shaped

 - Generalists (horizontally skilled)
 - Broad skills in many areas
 - Helps with bottlenecks
 - Can remove downstream waste

#### E-Shaped

- Deep in a few areas
- Typically an innovator
- General expertise in many areas
- High impact individual

### Mindsets

#### Fixed Mindset

- Fixed belief
- Outcome-based
- Belief that intelligence and talent are fixed traits

#### Growth Mindset
 - Alternative Belief
 - Effort-based
 - Belief that abilities can be developed through dedication and hard work
 
### Motivation

 - Intrinsic Motivation
   + Engaging in a behavior because it is personally rewarding.
   + Rewards: Autonomy, Sense of achievement, Passion
 - Extrinsic Motivation
   + Motivated behavior or engage in an activity to earn a reward or avoid punishment.
   + Rewards: Pay increase, Promotion, Bonuses
 - There is no good or bad here: The important thing is to understand what motivates people for change

#### Overjustification Effect

 - Extrinsic rewards can decrease an individuals intrinsic motivation
 - Individuals may pay more attention to the extrinsic rewards instead of their intrinsic motivations
 - Reinforce extrinsic motivation mindsets
 - Efforts over outcome based extrinsic rewards (effort-based rewards) are less influenced by the Overjustification Effect

#### Individuals Motivation

 - Use incentives approprietely
 - Challenge mindsets: A variation of the Growth Mindset. It's a very powerful tool, under-explored in our industry
 - Visualise the effort, not the success
 - Intent-based motivation (individual control)
 - Focus on the effort, not the outcome

### Technology Adoption Curve

#### Innovators

 - Typically risk takers
 - Have financial or social capital to take risks
 - They have higher failure tolerance
 - Tend to be good internal champions

-----------------
> In general, you wanna look for innovators when you are looking for transformation of new ideas. And DevOps would be one of those.
-----------------

#### Early Adopters

- Similtar characteristics of innovators
- Opinion leadership: they have higher credibility
- More discreet in adoption choices
- Tend to be more centralized than innovators

------------------
> They're a little more connected to the overall infrastructure of the company than innovators.
------------------

#### (Technology Adoption Curve) Strategies

 - Look for gate keepers: innovators of early adopters that might own a certain area
 - Identify champions: people that can be a internal advocate for change
 - Identify and manage resistors
 - Defuse cynicism

#### Leaders

 - Opinion leaders:
     + People that have high **Credibility**
 - Network leaders:
     + People with great **Influence** that are really good at spreading their ideas/opinions
 - Hierarchical leaders
     + People that **Control** a certain area to give you direct leadership **Support**

### Organizational Structures

-------------------
> Conway's Law: Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations
-------------------

#### Functional-Oriented

 - Optimized for cost
     + The classic organizational structures
 - Designed around expertise
 - Hierarchical in structure
 - Different teams for systems, networking, database and security
 - More handoffs and longer lead times
 - Leads to local optimization (instead of global optimization)
 - Leads to bottlenecks

#### Matrix-Oriented

 - Hybrid structure
     + Tries to bridge expertise and speed
 - Dotted line cross functional alignment
     + Have a functional hierarchical structure, but puts somebody in a dotted-line responsibility to another team
 - Complicated structures
 - Can lead to a lack of ownership
     + People are really not clear who has the authority or not

#### Market-Oriented

 - Optimized for speed
     + In general, it's what we find in high-performance organizations, DevOps-based organizations
 - Flat structure
 - Small teams
     + Microservices, bounded context...
 - Highly coordinated and collaborative
 - Tight coordination
 - Less handoffs and shorter lead times
 - Globally optimized
 - Cross functional with less bottlenecks

### How do you do transformation?

----------------
> "Don't fight stupid, make more awesome" - Jessie Robbins
----------------

 - Start small, build trust and safety
 - Create champions
 - Use metrics to gain confidence: build a narrative around your metrics
 - Celebrate successes
 - Exploit compelling events

----------------
> "Most of the time when people are saying no what they are really saying is they don't know how to say yes. Sometimes we have to hack the 'yes' out of people." - Jessie Robbins
----------------

## Enabling Transformation

### Best Practices

 - Alignment around the transformartion
     + Create an army around the transformation, starting small, growing, learning how to fight off the dissenters
 - Create a shared goal
 - Create non-functional buffers (20% time)
     + For just creative thought
 - Build generalist strategies
 - Build team with credibility and influence leaders
 - Create a physical workspace for the transformation team
     + The idea of getting the team away from the bureaucracy and inercia is a good idea
 - Give the transformation team some freedom
     + You do need to allow this team to break some rules

### Planning

 - Shorter planning cycles
 - Outcomes not budget related
 - Re-planning
 - MVP's (Minimal Viable Products) and pivots
 - Enforce learning as core objective
 - Quick start initiatives

### General Hacks

 - Self service
     + Allow teams to create fast implementations
 - Embed Ops
     + Embed ops into dev team or dev into ops team
 - Liaisons
     + Internal consultants (designated ops)
 - Retrospective and Standups
     + Invite all related

### Four Pillars of Effective DevOps

#### Collaboration

 - Micro-aggression and non-violent communication
     + These are ways that you communicate as part of the transformation team, of how you can say something
     + Avoid using "you" and "they" (blameless postmortem)
 - Asynchronous code reviews (*Pull Requests*)
 - Pair programming
 - Chatops
     + Chat tools like Slack, where teams can communicate, have war rooms, log error messages, do deployments, etc.
 - Standups

#### Affinity

 - Relationships
     + Embedded Ops, bootcamps, rotations, blameless postmortems
 - Empathy and trust
 - Inter-team relationships
 - Team culture and culture fit
 - Blamelessness
 - Respectful of individual differences and backgrounds
 - Team diversity

#### Tools

 - Use tools as an accelerator to enforce culture
 - Do the tools shorten lead time
 - Version control
 - Artifact management
 - Automation, monitoring, logging, alerting
 - Continuous integration and delivery (CI/CD)
 - Open source can help scale
 - In-House vs Open Source vs Commercial

#### Scaling

 - Grow and mature the transformation
 - Expand to other organizations and service groups
 - Managing zombie projects
     + Look out for projects that really just go nowhere and start eating resources
 - The service is never done

### John Kotter's 8-Step Change Model

 1. Establishing a Sense of Urgency
 2. Creating the Guiding Coalition
     + Find the right leaders
 3. Developing a Vision and Strategy
 4. Communicating the Change Vision
 5. Empowering Employees for Broad-Based Action
 6. Generating Short-Term Wins
    + Let the wins be known
 7. Consolidating Gains and Producting More Change
 8. Anchoring New Approaches in the Culture
    + You have to have a model for sustainability

# Chapter 4 *The First Way - Accelerate Flow*

## Continuous Delivery Patterns and Practices

-------------
> "There is nothing so useless as doing efficiently that which should not be done at all" - Peter Drucker
-------------

### First Way Principles

 - Create automated and repeatable environments at each stage of the pipeline
 - Apply automated testing at every stage of the pipeline
 - Increase flow and shorten lead times
 - Global optimization over local optimization

### Five Steps to Increase Value and Flow

 1. Define value precisely from the perspective of the end customer in terms of a specific product with specific capabilities offered at a specific price and time (**Separate business value from waste**)
 2. Identify the entire value stream for each product or product family and eliminate waste (**Value Stream Mapping**)
 3. Make the remaining value-creating steps flow (**Kaizen events, continuous improvement**)
 4. Design and provide what the customer wants only when the customer wants it (**the concept of pull model**)
 5. Pursue perfection (**the process is never done, it's virtuous cycle**)

### CI/CD

 - Continuous Integration
     + The process of integrating components of a feature, application or service
 - Continuous Delivery
     + Uses continuous integration to create installable artifacts (packages) that can be deployed
 - Continuous Deployment
     + The process of deploying a feature, application or service to production

### Continuous Integration

----------------
> In software engineering, Continuous Integration (CI) is the practice of merging all developer working copies to a shared mainline several times a day – Wikipedia
----------------

**The build Phase:**

 - Typically triggered by a code commit
 - Typically builds are done from trunk
 - The process happens every time someone commits code
 - Code is compiled and libraries are built
 - Build trigger package, artifact and image creation

### Continuous Delivery

-------------
> The Continuous Delivery means the code can be released. It is tested, it is reliable, and it has been through CI process.
-------------

- Code can be released
- Includes Continuous Integration (CI)
- After automated tests
- Changes are able to be deployed

**8 Principles of Continuous Delivery:**

 1. Create a repeatable, reliable process for releasing software
 2. Automate almost everything
 3. Keep everything in version control
 4. If it hurts, do it more frequently, and bring the pain forward
 5. Build quality in
 6. Done means released
 7. Everybody is responsible for the delivery process
 8. Continuous improvement

**Practices of Continuous Delivery:**

- Build binaries once
- Same process for deployment at every stage
- Smoke test your deployments
- If anything fails stop the line
- Peer reviews (pull requests)
- Code is committed to trunk

### Continuous Deployment

---------------
> Continuous Deployment means that every change is automatically deployed to production.
---------------

- Code is deployed
- Includes Continuous Integration
- Includes Continuous Delivery

**It considers that all these steps are automated:**

- Unit test
- Platform test
- Deliver to Staging
- Application Acceptance tests
- Deploy to production
- Post deploy tests


## The Deployment Pipeline

### Concepts

 - Visibility
   + All stages of the pipeline are visible to everyone responsible for the delivery of the service
 - Feedback
   + Each stage in the pipeline has designed "gates" created to eliminate downstream defects
 - Continually Deploy
   + The design of the pipeline is such that any patch, update or new feature can be automated for delivery, deploy and release

### The Deployment Pipeline (Service Delivery Platform Design Patterns)

 - Build Phase
   + Source Repository
   + Build Console
 - Package Repository
   + Build Artifacts
   + Store and retrieve
 - Deployment Phase
   + Pre-Production
   + Production

### Most Popular Tools

Source Control:
 - On premise: Git, Team Foundation Server, Perforce, SVN, CVS
 - SaaS-based: **Github**, Bitbucket, GitLab

Build Console:
 - on-prem: **Jenkins**, Bamboo, Team City
 - SaaS-based: **Travis CI**, Circle CI, Shippable

Repository Managers:
 - Nexus, Artifactory, Docker Trusted Registry, Docker Hub, Google Container Registry

Operations Console:
 - **Rundeck**, Marathon, Asgard (Netflix), Spinnaker (Netflix), Weave Scope

Automation:
 - CFEngine, Chef, Puppet, Ansible, Docker Compose, Cloud Formation, Terraform

Infrastructure Management:
 - VMWare
 - Cloud (AWS, GCE, Azure, Google Cloud)
 - Cloud (Openstack, Cloudstack)
 - Containers (Docker, LXC, Rocket)
 - Orchestration (Swarm, Mesos, Kubernetes)

### Vagrant

- Originally provided as a wrapper for Virtual Desktop
- Also wraps configuration management tools
- Very popular tool for developers
- Creates consistent environments

#### Vagrant Concepts

- Host and Guest
  + e.g. The Host environment is your laptop, and the Guest is the VM that gets provisioned
- Provider and Provisioner
- Boxes
  + It's an abstraction for the VM images
- Vagrantfile
  + The default source. A Ruby file that controls the provisioning and the provider
- Synced Folder
  + A nice interface for syncing folders between the host and the guests

#### Vagrant Commands

- up
  + Take a vagrantfile and fire up the VM, invoke any provisining scripts
- reload
- suspend
- resume
- destroy
- hakt
- ssh

### Git

Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for software development, but it can be used to keep track of changes in any files. As a distributed revision control system it is aimed at speed, data integrity and support for distributed, non-linear workflows.

- Everything is local
- Every local environment is a backup (clone)
- No network connectivity needed
- Works offline

### Build Phase

- Update your code from source control (if existing)
- Service is coded (if new)
- Run a local build in your dev environment
- Service code is commited to the source repository
- Service is built (binaries, libraries, artifacts...)
- Artifacts are tagged (version controlled) and packaged
- Packages are registered in a repository

#### Commit

- Files are uploaded to the source repository
- All source should be working code
- Code should have full coverage unit tests (TDD)
- Committed source should not break the build
- Pre-submit checks (bugs, lint, code styles)
- Automated trigger of the build stage

#### Build

- Compiling code
- Invokes build tools (ANT, Maven, Mercury, IVY, Make)
- Build time dependencies
- Creating and/or converting images
- Building container images
- Running functional/unit tests
- Automated trigger of integration and acceptance testing

#### Packages/Artifacts

- Compiled executables
- Components
- Libraries
- Container Images
- TAR'd and/or compressed binaries

#### Package/Artifact Repository

- Manages the distribution of packages and artifacts
- All packages/artifacts must be reproduccible from source
- Cryptographically hashed or digitally signed
- Manages security access management
- Invokes vulnerability scanning
- Provides usage reporting

#### Packages and Artifacts Repository Examples

All things that you can find in the artifact or package repository:
- JAR, WAR, and EAR packages (Java)
- Gems (Ruby)
- Python packages
- Perl modules
- DLLs (Windows)
- ZIP or TAR files
- Container images
- RPM or DEB packages (Linux)
- Metadata or Reports
- Documentation

### Deploy Phase

- Promotion: moving between the different stages of the pipeline / versioning the packages and artifacts in a deploy
- Provisioning
- Installation
- Configuration
- Orchestration: if you're doing cloud provisioning and/or containers

#### Promotion

- Candidate releases are selected
- Versions are selected and marked
- Tagging strategies
  + Marked "Production"
  + Marked "Latest"
  + Pinning: even if there's a newer version, we pin the most stable version to be the one used
- Multiple repositories strategies
  + Development
  + Testing
  + Production

#### Provisioning

- Bare metal provisioning (PXE)
- Virtual image provisioning (VMware ESX, XenServer, KVM...)
- Cloud provisioning (Amazon, Google, Azure, Digital Ocean...)
- Container provisioning

#### Installation

- Internally written installers
- Before and after scrips
- System level strategies (RPM/YUM, DEB/APT)

#### Configuration Management (Not Immutable)

- Install the service
- Infrastructure as Code
- Desired state configuration
- Convergence
- CFEngine, Chef, Puppet, Ansible

## Creating consistency in the pipeline

-------------------
> "A butterfly flaps its wings in the Amazonian jungle, and subsequently a storm ravages half of Europe" – Neil Gaiman and Terry Pratchett
-------------------

### Pets vs Cattle (concept)

- Servers as pets
  + You name them and when they get sick, you nurse them back to health
- Servers as cattle
  + You number them and when they get sick, you shoot them

-------------------
> Most high-performing organizations would describe their model as "service as cattle"
-------------------

### Consistent Environments in all Stages

- Goal is to create consistent environments
- All elements of the pipeline should be disposable and reproducible
- All environments should look like production
- Decrease variability between elements in the pipeline
- Repeatability increases speed rebuilding environments
- Reduced errors related to inconsistencies
- Increases security related to inconsistencies

### Version Control everything!

- Keeps a history of all changes
- Can easy check differences between versions
- Can restore and rebuild all elements
- Everything can be versioned and tagged
- All changes are visible and audited for everyone
- Changes can be automated

#### What should be in version control (everything)

- All application code
- All configuration scripts
- All configuration management DSL code
- All image build scripts (VM's, Containers)
- All meta definitions (JSON, YAML, TOML)
- All automated tests, test scripts and test DSL code
- All documentation, procedures, release notes
- All templates (Cloudformation, Terraform, Heat)
- All database schema abstractions, DNS, and Firewall definitions
- Network definitions (Switch configurations)
- Basically everything

### Why Order Matters

To avoid the following issues:
- Circular Dependancies
- Right Command Wrong Order
- Right Package Wrong Order

#### The Difference a Byte Makes

- Lean Enterprise story (from the Humble-Farley book):
  + A dependent library with only a couple of byte difference created a bug that could not be recreated in test
  + It is because there was just an out-of-sync
- Large Financial institution
  + Applied 5 seconds desired state configuration monitoring and saw 1 billion unplanned changes per day

### Consistent Infrastructure (Providers)

#### Provisioning: Bare Metal (BM)

- All BM scripts or DSL should also be kept in version control.
- BM scripts typically kick of configuration management processes when they complete.
- Some BM and CM (Configuration Management) tools "Devops" integrate together.

Tools:
- Kickstart, Cobbler, FAI (Fully Automatic Installation), Foreman, Razor, MAAS (Machine As A Service), Ironic, RackN - Digital Rebar (formerly Crowbar)

#### Provisioning: Virtualization (VM)

- VM image build scripts, meta and templates should be kept in version control
- All VM images should be reproductible from source (version control)
- Most configuration management tools can automate VM provisioning then kickoff the CM process
- Image strategies (Bake vs Fry)
  + The bake image is bigger, but is faster in deploy.
  + The fry image is smaller, but it takes longer to deploy, because you are literally installing, instead of having all the installed components in the backed image

Tools of Type 1 Hypervisors:
- VMWare ESX/vSphere, XEN, HyperV

Tools of Type 2 Hypervisors:
- KVM, VMWare Workstation, Oracle VirtualBox, Xhyve (Hyperkit - Docker)

#### Provisioning: Desktop Virtualization (VM)

Tools:
  + Vagrant, Docker Toolbox, Docker for Mac, Docker for Windows

#### Provisioning: Cloud (IaaS)

- Cloud image build scripts, meta and templates should be kept in version control
- All Cloud images should be reproductible from source (version control)
- Most configuration management tools can automate Cloud provisioning then kickoff the CM process
- Cloud-init/user-data/cloud-config file formats
- Image strategies (Bake vs Fry)

Public Cloud Tools (IaaS):
- Amazon (AWS), Google (GCE), Microsoft Azure, Rackspave, Digital Ocean

Public Cloud Tools (PaaS):
- Heroku, EngineYard, CloudFoundry (also private)

Private Cloud Tools (IaaS):
- OpenStack, CloudStack, VMWare vCloud, Microsoft Azure

#### Provisioning: Containers

- Container image build scripts, meta and templates should be kept in version control
- All container images should be reproducible from source (version control)
- Typically CM tools are not used inside of a running container
- Configuration files and meta are typically shared by the container host
- Containers work well with Immutable Delivery models

Tools:
- Docker, Rocket, LXD, LXC (Native Linux Containers), Amazon (ECS), Microsoft (ACS), Google (GCS)
  + Obs: Amazon ECS and Microsoft ACS are Docker implementations

### Infrastructure Image Portability

- Conversions between different infrastructures
- Conversions between different stages in the pipeline
- Directory structures and shared files

------
> You have to automate all that process of conversion and deal with the operational cost of the different platforms and potential inconsistencies
------

#### Example:

- Desktop
  + Vagrant BOX format
- Build
  + QCOW2
- QA (testing and quality assurance)
  + AMI
- Production
  + VMDK

### Consistent Operating System Environments

-----
> Even if you have to use different infrastructure frameworks, at least have your operating system be the same
-----

#### Consistent Operating System Environment Patterns

- Scripted environments
- Infrastructure as Code
- Immutable Infrastructure
- Immutable Delivery

#### Scripted Environments

Pro's:
- Easier to build
- Lower learning curve
  + Don't need to learn any complex language, like Chef and Puppet
- Language consistency (SHELL and bash)
- Easy to change

Con's:
- Environment abstractions are harder to code
- Typically lower reusability
- Harder to provide data driven models
- Could cause inconsistent environment builds
- Not really self documenting
- Could lead to local improvements and not global
- No real good testing interfaces

#### Infrastructure as Code

- Infrastructure primitives defined as DSL
- Highly parameterized
- Desired state-based model
- Principles:
  + Modularity, Composability, Extensibility, Flexibility, Repeatability (DSL), Declaration, Abstraction, Idempotence, Convergence
- Solutions:
  + CFEngine, Puppet, Chef, Ansible, Salt

Pro's:
- Abstraction DSL's are very powerful
- Self documenting
- High reusability code/modules
- Easy to provide data driven models
- Generally more consistent than scripted patterns
- Most major CM's have good testing abstractions

Con's:
- Abstractions DSL's have a higher learning curve
  + You need to learn the DSL language (Ruby for Chef, Puppet language for Puppet)
- Complex edge case scenarios/failures
- Script/Shell primitives are used often
- Point and time divergent
- Integration interfaces are more complex
- Infrastructure is built Just in Time (JIT)
- Slower to provision
- Builds are convergent not congruent

#### Immutable Infrastructure

**Configuration Management (Immutable):**
- Deploy the immutable image from an artifact repository
- Uses metadata layering tool to coverge a service or cluster

**Configuration Management (Netflix example):**
- Used Java, Scala and Groovy
- Created packages from artifacts
- Turned packages into immutable AMI's
- Used a meta layer for convergence

Pro's:
- Less variation than Infrastructure as Code
- Faster to provision then Infrastructure as Code
- Typically use Infrastructure as Code to build
- Built into the CI process

Con's:
- More variation than Immutable Delivery model
- Need a good model for image management
- Slower to provision than Immutable Delivery model
- Might still need Infrastructure as Code abstractions
- Not immutable from the developers perspective

#### Immutable Delivery

**The Four Vs**
- Variety *(raise)*
  + Determine your variety of offerings based on operational efficiency and market demand
- Velocity *(raise)*
  + Maintain a steady flor through all processes of the supply chain
- Variability *(reduce)*
  + Manage inconsistencies carefully to reduce cost and improve quality
- Visibility *(raise)*
  + Ensure the transparency of all processes to enable continuous learning and improvement

**No CRUD allowed for...**
- Packages
- Configuration files
- Application software
- Data (RUD)

**Configuration Management - Container Model:**
- Immutable Delivery model
- Use **orchestration** for provisioning
- Add meta layer similar to the Netflix model (however, much faster)

**Orchestration Tools for Containers:**
- Docker Swarm
- Mesos
- Kubernetes

Pro's:
- Least variation pattern
  + It's the most congruent
- Fastest provision model
  + You can provision thousand node clusters in seconds
- Fits well with Microservices architerctures
- Really no need for Infrastructure as Code
- Binary consistency from desktop to production
- Built into CI process

Con's:
- DSL abstraction not as mature as Infrastructure as Code
  + A Dockerfile is very scripty, it's not self-documenting as Chef and Puppet
- Small changes are harder to manage
  + Doesn't have a strong idempotent model
- Debugging is harder
- Need a good model for image management
- Not all delivery models fit well

#### Consistency Summary

- Infrastructure as Code is in general better than scripted environment builds
- Hybrid environments where immutability doesn't make sense still need Infrastructure as Code
- In environments where immutability makes sense Immutable Infrastructure and/or Immutable Delivery is the most consistent way to build a delivery pipeline

## Automated Testing

------------
> Continuous testing ensures continuous improvement
------------

### The 9 Principles of Testing (by Elisabeth Hendrickson)

1. Change the adversarial mindset to a collaboration mindset
2. Change the *dev then test* mindset to *test and dev* mindset (TDD)
3. Instead of having a *test team* you have an *everyone tests team*
4. Test early, test often and shorten the feedback loop
5. Tests should have reasonable expectations
6. Fix bugs when you find them
   - "Stop the line" (the andon cord)
7. Reduce test documentation, automate the expectation
8. *Done* means *released* (and tested)
9. Test implement vs Implement test

### Test-Driven Development (TDD)

#### Concept: Red, Green, Refactor (loop)

- Write a test based on the requirements. Make it fail
- Write a small piece of code to make it pass
- Refactor the code by improving it without changing the behavior and Repeat

#### Benefits

- Prevents scope creep
- Catches desings issues early
- Creates cleaner code
- Builds trust with other service owners
- Creates a consistent rhythm

### Acceptance Test-Driven Development (ATDD)

ATDD is very similar to TDD, but it has a business focus. Here is the ATDD loop:
- Discuss
  + With the business stakeholders to get a general idea of what are the intentions, and what makes a good acceptance
- Distill
  + Collaborate with the business stakeholders - define/refine *Done* in terms of the tests
- Develop
  + TDD
- Demonstrate
  + Show the new feature to the business stakeholders, get feedback

### Behavior-Driven Development (BDD)

- Tests whether the software fulfills the business need
- Instead of *how it works*, it tests *how it behaves*
- Based on Domain Driven Design (Eric Evans)
- Typically DSL-based
- Tests are typically conversational
  + Uses human-readable questions and answers

#### Example:

```
[Feature]: Hello World
As a service manager
I want our customers to be greeted when they visit our site
So that they have a better experience

[Scenario]: Customers sees the welcome message
When I go to the homepage
The I should see the welcome message
```

### Agile Testing Pyramid

- Developer Level (Basis):
  + Automated Unit Tests
- System Level (Middle):
  + Integration Tests
- UI (Top):
  + UI/UX tests (Manual tests)

### Automated Testing: Build Phase

- Unit tests
- Acceptance Tests
- Integration Tests
- User Acceptance Tests

#### Always Be Automating the tests

- Automated tests are always running
- Every commit
- Nightly functional testing
- Smoke testing
- Stability testing
- Performance testing
- Zero configuration

#### Unit Tests

- Testing the source code by class or function
- Typically done at commit or before commit
- Typically "mocks" are created for interface calls
- Typically created by the developer
- Develop intention checking
- Should be run on every change
- Unit tests should be fast
- Clear results
- TDD based

#### Acceptance Tests

 - Testing multiple classes or functions
 - Should verify a user story
 - Should be written vefore code
 - Checks for regressions
 - Tests what the customer expects
 - Specification is written in a domain-specific language
 - Run after the build and all unit tests have passed

#### Integration Tests

- Testing integratino with other applications and services
- All code and modules are tested as a group
- Tests are a system wide view of the service
- Tests real interfaces not "mocks"
- Integratino tests are typically more expensive (more time-consuming)
- Run after the build, all unit tests and acceptance tests

#### User Acceptance Tests (Manual)

- Testing done by customers
- Ensure the applicatinos or service meets the requirements
- Catch defects from a customer's perspective

### Automated Testing: Deploy Phase

- System Testing
- Performance Testing
- Load Testing
- Security Testing
- COnfiguration Management Testing

#### System Testing

- Precondition for release being turned on in production
- Testing of external interfaces (make a purchase, checking stock quote)
- Synthetic testing, emulation of user interactions
- Tests can be emulated from API's, consoles, web, devices, mobile and even from laser printers

#### Performance Testing

- Tests the speed and latency of a service
- Can test against customer SLA's (Service-Level Agreements)
- Performance regression tests (previous results)

#### Load Testing

- Tests how much load a service can handle
- Tests involve increasing traffic to find max load (the breakpoint)
- Performance regression load tests (previous results)

#### Security Testing

- SQL Injection
- Cross Site Scripting
- Unprotected Redirects
- Unsafe File Access
- Version-Specific Inssues (CVEs)
- Symbol Dos
- Remote Code Execution

--------------
> I recognize that my code will be attacked by talented and persistent adversaries who threaten our physical, economic, and national security – **The Rugged Manifesto**
--------------

**Security Testing process:**
- Create security related stories
- Add security unit tests
- Create a library of reusable test cases patterns
- Add vulnerability scans into the pipeline

### Tools

#### Unit Testing

- JUnit, JTest (Java)
- CUnit (C)
- RSpec (Ruby)
- Google Test
- Parasoft
- Visual Studio

#### Load and Performance Testing

- Apache Bench
- Apache JMeter
- LoadRunner, WinRunner (HP)
- Rational Performance Tester (IBM)
- Selenium
- Neoload
- SOASTA

#### BDD Testing

- Cucumber (Ruby-based)
- JBehave (Java)
- SpecFlow (.net)

#### Security Testing

- Brakeman
- Gauntlt
- Nmap
- OWASP

#### Configuration Management Testing

-------------
> The configuration management tools have, over the years, built up really robust automated testing themselves
------------

- Chef
  + ChefSpec (Unit)
  + Test Kitchen (Integration)
  + Cucumber-chef (BDD)
  + Food Critic (Lint)
- Puppet
  + rspec-puppet (Unit)
  + Test Kitchen (Integration)
  + Beaker (Integration)
  + Puppet-lint (Lint)

## Deployment Strategies (Zero Downtime Release)

-------------
> "Pushing code into production can be tricky because we are modifying a system while it is running. This is like changing the tires of a car while it is speeding down the highway at 90 km/h: you can do it, but it requires a lot of care and planning." - Thomas A. Limoncelli
-------------

### General Patterns and Constraints

- Changing **data or schemas** in the release can be more difficult
- Orchestrated release rollbacks can be difficult
- Best time to reply is during production (not at 3am)
- Log all deployment activities
- Don't delete old files
- Use warmup methodologies
  + Strategies that you can implement to let things run in a warm mode for a while, before you turn them on

### Upgrading Live Services

#### Rolling Upgrades

- Servers are removed from service and upgraded one at a time
- The process is complete when all the servers are updated
- During the upgrade there is a temporary reduction in capacity
- Server is first drained by removing from the load balancer

#### Canary

- Similar to rolling upgrade but to a subset of servers
- Apply smoke, performance and load test
  + To make sure that you are not having any bed regression reactions
- If no problems arise add more subsets
- Server is first drained by removing from the load balancer
- Can also be done by percentage of servers
- Canary'ing can be combined with other rollout strategies
  + e.g. Canary and A/B testing is a good combination
- Designed to find a defective release

#### Phased Roll-Outs

- Roll-outs partitioned by subsets based on users or groups
- Groups are categorized ny risk tolerance
  + You start off with a very low risk profile group, and then you increase by some risk categorization
- If no problems arise add more subsets
- Sometimes internal employees can be first roll-out group
- Power user or meta communities roll-outs

#### Proportional Shedding

- A new service is built on new machines
- The load balancers shed small percentages of traffic to the new service
- The percentage is increased if no issue are found
- The old service is turned off when all traffic is moved to the new service with no erros
- With bare metal this can be expensive. Cloud makes this more economical

#### Blue-Green Deployment

- Similar to proportional shedding except you duplicate the application not the servers
  + You have the new and the old applications running on the same server
- Green is the live service
- Blue is dormant and requires limited resources
- When the release goes live the two are swapped
- Rolling back is easier to do
- Very popular technique

#### Toggling Features

- Also known as feature flags
- Flags are set in the code that can turn on or off a feature
- Allows developers to continuously deploy new code decoupled from a release
- Distrusted key value stores like Zookeeper, Etcd and Consul can be used for feature toggling
- Features can be gradually introduced or be point and time released

#### A Case Study: Dark Launch at Facebook (Facebook Chat)

--------------------
> The secret for going from zero to seventy million users overnight is to avoid doing it all in one fell swoop. We chose to simulate the impact of many real users hitting many machines by means of a "dark launch" period in which Facebook pages would make connections to the chat servers, query for presence information and simulate message sends without a single UI element drawn on the page. With the "dark launch" bugs fixed, we hope that you enjoy Facebook Chat now that the UI lights have been turned on.
--------------------

- In the backend, they were actually invoking a Javascript that would invoke the new feature of chat, to do things like, make connections, query chat servers, and simulate message sends.
- It was a real production testing, but the users didn't know it was happening

# Chapter 5 *The Second Way - Amplify Feedback Loops*

## Creating a Service Reliability Culture

----------------
> "3% of the problems have figures, 97% of the problems do not." – Dr. Deming
----------------

### Second Way Principles (Goals)

- Right to Left flow
- Find and Fix Fast
- Shorten and Amplify Feedback

### Core Conflict "Dev vs Ops"

- Operations don't really know the code base
- The team that knows least about the code typically has the responsibility of it's launch

### Understanding Service Levels

#### Service Level Agreements (SLA)

- Between the business and the customer
- Typically a financial contract
- Can be MTTR or MTBF based
- Not all services have an explicit SLA

------------------
> An SLA is based between the business and the customer and an SLO is based between the internal service team and the system in which it operates.
------------------
> High-performing organizations don't set the SLAs. They tend to have their own SLA in the form of a SLO
------------------

#### Service Level Objectives (Targets)

- Typically the basis for SLA's
- Between the service and the system
- Typically target based
- All services should have an SLO
- Determine actions to take on missed SLO's
- SLO's should be tracked historically

**Picking Targets:**
- Try and keep them simple
- Don't over-design
- Let them evolve
- Will learn over time

#### Service Level Indicators

- Quantitative measure of a service
- Used as indicators for the SLO's
- Monitor SLI's and compare to SLO's

**Examples:**
- Latency
- Errors
- Availability
- Throughput

**Generalized Indicators:**
- Management By Objectives
- Key Performance Indicators
- Objective and Key Results

---------------
> "Management is about doing the things right; leadership is about doing the right things" – Peter F. Drucker
---------------

### Understanding Risk and Failure

------------------------
> "A production line that never stopped was either extremely good or extremely bad." – Taiichi Ohno
------------------------

- 100% reliability is a myth
- All systems go down
- Not all services are equal
- Manage risk and failure by service
- Managing reliability is about managing risk
- Managing risk is about cost

### Understanding the Cost of Reliability

- High availability systems
- Opportunity costs
- Is it a free service or a revenue-based service?

#### How Many 9's

The level of reliability/availability based on how many nines we want.

**Example:** A company that generates one million dollars per day in revenue...

| # 9's | % | Downtime | Lost Revenue |
| ----- | ----- | ----- | ----- |
| One | 90% | 36.5 days per year | $36.5M |
| Two | 99% | 3.65 days per year | $3.65M |
| Three | 99.9% | 8.76 hours per year | $365k |
| Four | 99.99% | 52.56 minutes per year | $36.5k |
| Five | 99.999% | 5.26 minutes per year | $3.65k |
| Six | 99.9999% | 31..5 seconds per year | $365 |

-------------
> The difference from two nines to three nines is significant, like three million dollars in savings. So, the cost might be worth it. But to go from three nines to four nines, and from four to five nines, the amount saved becomes less significant... so do you really have to be *five nines*?
-------------
> The cost to get an extra nine could be a hundred, and in some cases, 2-300x higher
-------------

#### Google Site Reliability Engineers (SRE)

SRE is a conceptual job title created by Google in 2003.

- No NOC
- A team that focuses on reliability
  + Focus on service
  + Focus on engineering
- To be a Google SRE you had to pass a coding test very similar to the coders's test

----------------
> "The number one feature for a product is that it works. The second most important feature for a product is that it works. The third most important feature for a product is that it works". - Benjamin Treynor Sloss from Google
---------------

#### Google Site Reliability Practices

- Hire only coders
- Have an SLA for your service
- Measure and report performance against the SLA
- Use Error Budgets and gate launches on them
- Have a common staffing pool for SRE and Developers
- Have excess Ops work overflow to the Dev team
- Cap SRE operational load at 50 percent
- Share 5 percent of Ops work with the Dev team
- Oncall teams should have at least eight people at one location, or six people at each of multiple locations
- Aim for a maximum of two events per oncall shift
- Do a postmortem for every event
- Postmortems are blameless and focus on process and technology, not people

#### Google SRE Case Study: Error Budget

- Theory is that 100% is the wrong reliability target for everything
- **Service objective minus 1 is the unavailability service's error budget**
- This resolves the Dev (*create new*) Ops (*protect the infrastructure*) conflict
- It's a math problem not an opinion or power
- Devs teams self police
- The service team gets to take SLA-1 feature/risk velocity

---------------
> Until you hit your **error budget**, you can do whatever you want... you can take risky deploys, you can keep experimenting.
---------------

SRE at Google don't:
- Access launches
- Avoid outages
- Set release policy

#### Google SRE Case Study: LRR/HRR

- Lauch Readiness Review
  + Sign-off before any service goes live at Google
  + Developer managed state
- Handoff Readiness Review
  + Signed-off for a service at higher acceptance
  + Operations managed state
- The Service Handback
  + Process to put a service back to developer managed status

#### Google and Operational Work (Types of Work)

- Software Engineering
  + Developing and designing code
- Systems Engineering
  + Configuration system (Sysadmin work)
- Toil
  + Manual not repeatable work
- Overhead
  + Administration, HR and training
  
#### Google and Operational Work (Goals)

- Creates good moral
- Creates positive career (growth)
- Creates clearer communication
- Creates velocity
- Unsets precedents
- Keeps good faith

### Anomaly Response

- Computers do not resolve outages...people do
- Trade-off's under pressure
- Cognition in the wild
- An outage is not a detective story
- With each step the story changes (it's the nature of a dynamic fault system)
- Need to see what's happening with incomplete information
- Tools don't always make thing better

#### Anomaly Response - Challenges

- Teamwork
- Communication
- Diagnosis
- Decision Making
- Coordination
- Improvisation
- Tooling

#### Dynamic Fault Management

- Cascading effects
- Tempo changes and time pressure
- Multiple interleaved tasks
- Multiple interacting goals
- Need to revise assessments as new evidence comes in

-----------
> In dynamic fault management, intervention precedes or is interwoven with diagnosis. – Woods (1994)
-----------

#### The *Thematic Vagabonding* Concept

-----------
> People in anomaly response tend to jump from one topic to the next, treating all superficially, in certain cases picking up topics dealt with earlier at a later time; they don't go beyond the surface with any topic and seldom finish with any. – Dietrich Dörner, 1980
-----------

#### Anomaly Response - Heuristic

------------
> An approach to problem solving, learning, or discovery that employs a practical methodology not guaranteed to be optimal or perfect, but sufficient for the immediate goals. Where finding an optimal solution is impossible or impractical, heuristic methods can be used to speed up the process of finding a satisfatory solution. Examples of heuristics are 'rules of thumb', educated guesses, and intuitive judgements. – John Allspaw
------------

**First Heuristic**
* Look for correlation between the behavior and any recent changes made in the software

**Second Heuristic**
* Widen the search to any potencial contributors imagined

**Third Heuristic**
* Validate hypothesis that most easily come to mind

**Fourth Heuristic**
* Rely on peer review of the changes more than automated testing

## Fast Feedback

------------
> "You built it, you run it" – Werner Vogels, CTO of Amazon
------------

### Design for Failure

- Software resiliency typically is better than hardware-based
  + More cost-effective
  + Easier to change (fix, upgrade, replace)
  + Faster to fix
  + Easier to experiment
- MTTR over MTBF
  + High-performing organizations adopt the assumption that all systems fail
  + They think about how to get a system up (fast) when something breaks
- Reduce MTBF and MTTR
  + Game Days
  + Chaos Monkey(s)
  + Fault Injection
- Fasten feedback
  + A/B testing
  + Dark Deploys
  + Inject Deployment Metrics in Monitoring

### Systems Thinking

- Looks at the system as a whole
- Global efficiency vs local efficiency
- Feedback loops vs cause-and-efect
- Trends not targets
- The system is greater than the sum of the parts

#### Feedback Originates from Systems Theory

- A system is made up of inputs and outputs
- The feedbacks are based on the output of a system being fed back into the input
- These are dynamic systems, systems that are constantly changing
- Delay in feedback:
  + Increases drift: the quicker you get feedback, the quicker you can accelerate
  + Limits options
  + Increases processing effort

**_Different feedback loops:_**
- Accelerating Loop
  + Amplifies behavior (negative or positive)
- Diminishing Loop
  + Supresses behavior (learned helplessness)
- Balancing Loop
  + Towards a stable goal (cooperation)
- Thrashing Loop
  + Oscillating between states

#### Developer Managed Services 

**_Designing Delivery:_**
- Design for failure
- Designing for service, not just software
- Minimizing latency and maximizing feedback
- Designing for failure and operating to learn
- Using operations as input to design
- Seeking empathy

**_Developers Wear Pagers:_**
- First on call is the dev rotation team
- Second call is the VP of Engineering
- Third call is CTO

**_Developers Operate the Service:_**
- Launch
- Monitor
- Guidance from operations

### Contingency

- Some releases need contingency reviews
  + Some types of services need to have some human factor in the delivery
- *Go/No Go* of major releases
- Universal agreement for the launch

#### Contingency - 10 Minutes Review

- When will it be launched
- Who is launching it
- Has it been in production yet
- Can it be dark, feature or percentage launched
- Is it new infrastructure (is it monitored)
- Has an on/off switch
- All parties available at launch time
- Contingency checklist

### Peer Reviews - Guidelines

- All changes are peer reviewed
- Everyone monitors the commit logs
- High risk changes should include an SME
- Break up larger changes into smaller ones

### Pairing

- Pair programming for everything
- Pair programming is slower but decreases bugs up to 70% to 80%
- Spreads knowledge
- Great for training
- Setup pair times
- Need a culture that values pair programming
  + It can'f be forced

### Embedded Engineers

The idea of taking Operations people and embedding them into the Development team (or vice versa).
- Operations in development
- Development in operations

### ChatOps

ChatOps is a collaboration model that connects people, tools, process, and automation into a transparent workflow. This flow connects the work needed, the work happening, and the work done in a persistent location staffed by the people, bots, and related tools.

#### Origins

- Originally based on chat bots
- Github's use of Hubot
  + A kind of an automated robot in chat rooms
- Jesse Newland - ChatOps at Github
  + *Putting tools in the middle of the conversation*

**_ChatOps Engines_**
- Hubot: Node-based, you can use *coffee-scripts* with it
- Lita: Ruby-based
- Err: Python-based

**_ChatOps Chat Tools_**
- Slack: Hubot on Slack is a very popular combination for ChatOps
- Campfile
- Hipchat

#### ChatOps Benefits

- It's like a multiuser terminal where everyone can see the conversation and the commands interwoven
- There is a historical record of the commands and the conversation
- Provide a great training tools - teaching by doing
  + People can watch in the channel and see what you're doing, see the results, interject a comment, etc.
- Great for tactical incident resolution - everyone gets to see the conversation and commands
  + It can be used for postmortems
- Dynamically manage the on call rotation
- Can manage all aspects of the "devops" practices from one central place
- Mobile operations tool for free

#### ChatOps Examples

- Run a command
- Deploy code
- Check logs
- Check status from Github or Jenkins
- Change the on call rotation
- Check Nagios alert
- Graph monitoring or alert data
- Take a system online or offline
- Kill a job or process

## Understanding Monitoring

--------------
> It's not the upfront capital that kills you, it's the operations and maintenance on the back end. – Gene Kim
--------------

### Culture Causality
Concept coined in The Visible Ops Handbook (Kim, Behr, Spafford).

- 80% of all outages are caused by a change
- 80% of restoration time is spent trying to figure out what changed
- High performance organizations look for the most recent change first

### Why monitor?

- Alerting: using email, page, ticket...
- Visualizing: using dashboard, graphs...
- Collecting: how we collect and use data, post-hoc diagnostics, retrospective...
- Trending: looking for direction, growing, shrinking
- Anomalies
- Learning

**Google's Four Golden Signals:**
- Latency
- Traffic
- Errors
- Saturation

### Looking at the Service Stack

- Business indicators
  + number of sales transactions, revenues, user sign ups, A/B testing results...
- Application indicators
  + transaction times, user response, application faults
- Infrastructure indicators
  + the database, networking, OS, CUP load, disk usage
- User based indicators
  + client side stuff, error and crash data...
- Deployment indicators
  + These are first-order metrics for high-performing organizations. e.g. deployment charts aligned with all the information above

**Other Examples:**
- Resolution times
- Abandoned shopping carts
- Churn rate
- Deployment promotions
- Lead time
- Forum posts

### Components of a monitoring system

- Sensing/Measuring
- Collecting
- Analysis/Computation
- Alerting
- Escalation
- Visualization

### Black Box vs White Box

- Black Box Monitoring
  + Symptom based
  + Active Problems
  + User's experience
  
- White Box Monitoring
  + Agent based
  + Log based
  + Instrumentation

### Types of Metrics

**Raw**
- Gauges
  + Basically numbers that measure speed, percentage or some data point
- Counters
  + Ever-increasing or resetting numbers, constantly going up until, at some point, resets to zero
- Timers
  + How long it took to do something (time-related)

**Derived**
- Delta
  + Variation of a number/variable/function
- Rates
  + A comparison between two values of different types. e.g. trasactions per minute
- Ratios
  + A comparison between two values of the same type

------------
> Even if you're working with summarized/derived data it's interesting to keep the raw data and always calculate the derived data *post hoc*, because if you don't have that calculation or that source data, you'll cannot be able to recalculate it
------------

### Analysis

- Real time (data)
- Correlation (data)
- Historical (data)
  + Hourly, daily, weekly, monthly
- Anomaly Detection
- Machine Learning

#### Statistical Analysis

- Mean
  + It's the average. The sum of all elements divided by number of elements
- Median
  + The value that is in the middle of the data set (after sorting)
- Percentiles
  + The value below which a given percentage of elements in a group of elements fall.
- (Sample) Standard Deviation
  + The standard deviation of a data set is the square root of its variance
  + Calculation: Take the mean of a vector with N elements, then take the sum of the squared differences of each element, divide it by N-1, and then take the root of it. It's kind of the average of the delta of the elements in the vector.
- Median Absolute Deviation
  + Takes the median, then takes the delta of the median (the difference between the median and each element), and then takes the median of that list.
  + It's a better representation of the variation between the elements

**_Example:_** Let's take the vector X below as our data. Note that there is an anomaly in it, which is 99. See the statistics results in this situation:
`Data: X = { 3 4 5 7 9 8 3 7 5 8 99 }`
- Mean(X): `14.36364`
- SD(X): `28.14702`
- Median(X): `7`
- MAD(X): `2.9652`

### Anomaly Detection

- Finding patterns in data that do not conform to expected behavior
- Can be used for noise reduction

#### Research Areas

- Statistics
- Machine Learning
- Information Theory
- Data Mining

#### Characteristics

- High Cardinality
- Minimizing False Positives
- Seasonality
- Non Normally Distributions

## Understanding Complexity

------------
> The meta goal here is to help you start thinking more like a physicist in terms of complexity in complex-adaptive systems.
------------

### Cynefin

- Defined by Dave Snowden
- Designed to describe the evolutionary nature of complex systems
- Draws on research from complex adaptive systems theory, cognitive science, ahthropology and psychology

**Obvious:**
- Known knowns
  + Sense: See what's coming in
  + Categorise: Make it fit predetermined categories
  + Respond: Decide what to do
- Good Practice

**Complicated:**
- Known unknowns
  + Sense: See what's coming in
  + Analyse: Investigate or analyse, using expert knowledge
  + Respond: Decide what to do
- Good Practice

**Complex:**
- Unknown unknowns
  + Probe: Experimental input (hypothesis-driven)
  + Sense: Failures or successes
  + Respond: Decide what to do, amplify or dampen
- Emergent Practice

**Chaotic:**
- Unknowable unknowns
  + Act: Attempt tp stabilise (cause and effect is undetermined)
  + Sense: Failures or successes
  + Respond: Decide what to do next
- Novel Practice

### Circuit Breaker Patterns (by Nygard)

- Wrap a protected function call in a circuit breaker object
- Monitors for failures
- When a threshold is met trip a circuit breaker
- Calls are then returned with an error

**Netflix Example:**
- In Nexflix aplication, when something goes wrong, instead of just breaking the whole system, you just can't get movie recommendations, or centain subsets of things that you'd want to do on Netflix might just get turned off.

**Netflix - Circuit Breaker - Hystrix project:**
A open source project built completely on Nygard's circuit breaker pattern.

- Give protection from and control over latency and failure from dependencies accessed
- Stop cascading failures in a complex distributed system
- Fail fast and rapidly recover
- Fallback and gracefully degrade when possible
- Enable near real-time monitoring, alerting, and operational control
- Isolates access points between services
- Can setup triggers (e.g. trip if 10 calls within 10 seconds take longer than 5 seconds)
- Provides fall back options (error, default value, null value, or special error)

### Promise Theory (by Mark Burgess)

- Is a model of voluntary cooperation between individual, autonomous actors or agents
- They publish their intentions to one another in the form of promises
- It is non-deterministic, but there is a relationship
- One of the strengths of this way of thinking is that it does not let you take things for granted
- Decomposing into agents and promises allows us to see how a system works
- Confronting detailed (atomic) expectation of behavior, not just the ones that we think are big and important
- The entire chain of responsibility begins to appear as we start thinking n these terms

#### Obligation vs Cooperation

- Failure:
  + O: It must not fail
  + C: It will fail
- Automation:
  + O: It must look like this
  + C: It should look like this
- Visualization:
  + O: Show me what it looks like
  + C: Show me what you think it looks like
  
#### Obligations vs Promises

- Obligation is not a promise
- Obligations are a problematic ideal
- Obligations oversimplify information
- Obligation allows you to take things granted
- Obligations can come from anywhere

#### Example

- Promise quality
  + "I will feed your cat"
- Promise quantity
  + "on Monday & Friday mornings"
Promisee
  + "My neighbor"
Promisor
  + "Me"

 # Chapter 6 *The Third Way - Accelerate Learning*

---------
> "You are either building a learning organization... or you will be losing to someone who is" – Andrew Shafer
---------

 ## Learning Organizations

 The scientific contributions of **Dr. W. Edwards Deming** have a great importance on what we call today DevOps. In continuous learning, particularly, everything starts with the Deming Cycle (Plan-Do-Check-Act) – that is essencially a scientific method –, the Deming's view on systems thinking, and the Deming's fourteen points, which is frequently called as the manifesto of DevOps.

 ### Demings's 14 Points (from **Out of the Crisis** book)

In general, it's the poster for DevOps. But most of them will apply to how a learning organization thinks.

**Point #1 - Create Constancy of Purpose**
- Deming called this the "AIM"
- Goldratt called it the "Goal"
- Simon Sinek calls it the "Why"
- Rother calls it "Vision"

**Point #2 - Adopt The New Philosophy**
- Lead not manage
- Replace top down management
- Replace command and control management
- Create cooperative leadership models

**Point #3 - Cease Dependence on Inspaction to Achieve Quality**
- Don't wait till it's done to test it
- Build quality from start to end (flow)
- Make sure the door fits before it's built (SPC)
- Core principles of Lean and DevOps

**Point #4 - End the Practice of Awarding Business on the Basis of a Price Tag**
- Top line ROI vs Bottom line ROI
- It's not how much it costs to make
- It's how much money you make once it's built
- Work towards a mission not a budget
- Lean Startup/MVP

**Point #5 - Improve Constantly and Forever the System of Production and Service**
- "The Second Way"
- Create feedback loops (PDCA)
- The Andon-Cord
- Devs wearing pagers
- Tests, TDD/BDD

**Point #6 - Institute Training on the Job**
- Create team and systems thinking
- Create a learning organization
- Peter Senge's (Fifth Discipline)
- Core principle of Mike Rother's "Coaching Kata"

**Point #7 - Help People, Machines and Gadgets do a Better Job**
- Modern complex systems are based on humans and machines interacting
  + Deming understood this 60 years ago
- Human/machine relationships need to be non-deterministic
  + Complex systems are autonomous actors
- Deming, Goldratt and Burgess all started out as physicists

**Point #8 - Drive Out Fear, so that Everyone May Work Effectively for the Company**
- Fail fast, fail often
- Learn from failing
- Chaos Monkey, FIT, Gameday
- Blameless Postmortem
- Mean Time to Resolve (MTTR) focus
- Embrace failure by normalizing fear

**Point #9 - Break Down Barriers Between Departments**
- Organization culture is the strongest predictor to IT performance - Devops Survey
- High trust environments
- Cross functional collaboration
- Shared responsibilities

**Point #10 - Stop Management by Slogans**
- Stop slogan saying "Zero defects/Never fail"
- Quotas are a form of local optimization
- 100% Availability myth

**Point #11 - Supervisors Must Change from Sheer Numbers to Quality**
- Workers must feel pride in what they do
- Need to intent, not demand-driven management
- Quantity focus creates volume but not quality
- Leader-Leader not Leader-Follower
- Effort over outcomes (growth mindset)

**Point #12 - Abolishment of the Annual or Merit Rating and MBO's**
- Deming hated MBO's (Management by objectives)
- He felt they created the wrong incentives
- Management should not be driven by determinism
- Another expression of management by intent

**Point #13 - Institute a Vigorous Program of Education and Self-Improvement**
- Kaizen (Self improvement)
- Kata (Vigorous Self Improvement)
  + Improvement Kata (Rother's book)
- Moving form improvement to an art form

**Point #14 - The Transformation is Everybody's Job**
- Back to the AIM/Goal/Why
- Transformation must be global
- If only one group is optimized it is called local optima
- Global optima eats local optima for breakfast

### The Fifth Discipline

-------------
> "Our prevailing system of management has destroyed our people. People are born with intrinsic motivation, self-respect, dignity, curiosity to learn, joy in learning. The forces of destruction begin with toddlers – a prize for the best halloween costume, grades in school, gold stars – and on up through the university. On the job, people, teams, and divisions are ranked, rewarded for the top, punished for the bottom. Management by Objectives, quotas, incentive pay, business plans, put together separately, division by division, cause further loss, unknown and unknowable." – Deming's response to a comment on the "Fifth Discipline"
-------------
> "A learning organization is a place where people are continually discovering how they create their reality" – Peter Senge
-------------

Five Disciplines that must be adopted in order to become a learning organization:
- Systems Thinking
- Personal Mastery
- Mental Models
- Shared Vision
- Team Learning

### Learning Organizations Building Blocks

- Psychological Safety
- Appreciation of Differences
- Openness to New Ideas
- Time for Reflection
- Systemic Knowledge Sharing
- Education and Experimentation
- Reinforced Learning

### Ladder of Inference (by Chris Argyris)

How you can make bad judgements and understand how to short circuit the process so that you don't wind up with wrong conclusions, and even worse, static beliefs systems that are ingrained as memory muscle.

- Action
  + I take Actions based on my Beliefs
- Beliefs
  + I adopt Beliefs about the world
- Conclusions
  + I draw Conclusions
- Assumptions
  + I make Assumptions based on the Meanings I added
- Meanings
  + I add Meanings (cultural and personal)
- Select
  + I Select "Data" from what I Observe
- Observe
  + Observable "data" and experiences

**Concepts:**
- I'm processing output. My actions become input for somebody else's ladder of inference. So we're constantly interacting through our ladders of inference.
- **The reflexive loop:** our beliefs attest what data we select next time.

**Problems:**
- Can create bad judgement
- Our assumptions can lead us to bad conclusions

**Solutions:**
- Question your assumptions and conclusions
- Seek contrary data
- Make your assumptions visible to others
- Invite others to test your assumptions and conclusions
- Inquire other people's assumptions and conclusions
- Move down the ladder instead of up

**Example:**
Imagine I'm giving a presentation to a small group od people in my company.

Path 1
- Observe: I notice people in the first row
- Select: Person in the front row keep looking at their phone
- Meaning: Not listening to my presentation
- Assumption: He is not interested
- Conclusion: Doesn't like my new ideas
- Beliefs: Their team always blocks new ideas
- Action: I send a nasty email to their boss

Path 2
- Observe: I notice people in the first row
- Select: Person in the front row keep looking at their phone
- Meaning: Not listening to my presentation
- Assumption: Try to engage with a question (safely)
  + Break the ladder: instead of making that first assumption, I say "You know, maybe I'm wrong..."
- Conclusion: Might find out that they are late for another meeting and they really don't want to miss this one... so they sent an email noticing the next meeting team that they will be late...
- Beliefs: Their are very excited about this new idea
- Action: Both teams setup another meeting to engage

### The Dimensions of Learning Organization Questionnaire (DLOQ)

- It's an approach created by Victoria J. Marsick and karen E. Watkins
- Uses surveys or questionnaires to measure important shifts in an organization's climate, culture, systems, and Structures that influence whether individuals learn.
- Two components (**People** in an organization and the **Structure** of the culture)

**Four Levels of a Learning Organization (DLOQ)**

The questions are grouped in four organizational levels:

1. Individual Level
   + Continuous learning, dialogue and inquiry questions
2. Team or Group Level
   + Team learning and collaboration
3. Organization Level
   + Organization learning and empowerment (leader-leader)
4. Global Level
   + Systems level and strategic level (leadership) questions

**Seven Dimensions of a Learning Organization (DLOQ)**

1. Create continuous learning opportunities
   + Learning is designed into work so that people can learn on the job; opportunities are provided for ongoing education and growth
2. Promote inquiry and dialogue
   + People gain productive reasoning skills to express their views and the capacity to listen and inquire into the views of others; the culture is changed to support questioning, feedback, and experimentation
3. Encourage collaboration and team learning
   + Work is designed to use groups to access different modes of thinking; groups are expected to learn together and work together; collaboration is valued by the culture and rewarded
4. Create systems to capture and share learning
   + Both high- and low-technology systems to share learning are created and integrated with work; access is provided; systems are maintained
5. Empower people toward a collective vision
   + People are involved in setting, owning, and implementing a joint vision; responsibility is distributed close to decision making so that people are motivated to learn toward what they are held accountable to do
6. Connect the organization to its environment
   + People are helped to see the effect of their work on the entire enterprise; people scan the environment and use information to adjust work practices; the organization is linked to its communities
7. Provide strategic leadership for learning
   + Leaders model, champion, and support learning; leadership uses learning strategically for business results

**Andrew Shafer asks:**

- What if we turned these into statements instead of questions?
- And we deliberately create incentives for these behaviors

### Netflix Nine Behaviors

----------------
> The actual company values, as opposed to the nice-sounding values, are shown by who gets rewarded, promoted, or let go
----------------

At Netflix, the managers decide who should be compensated, promoted, or let go, based on these values:

- Judgement
  + Think strategically, make hard decisions, rely on their judgement
- Communication
  + Be really good listeners, respectful
- Impact
  + Be reliable, do amazing impact on work
- Curiosity
  + Embrace learning, to be boundary spanners
- Innovation
  + Have new ideas, useful ideas, be innovative
- Courage
  + Make tough decisions, make really bold hypothesis at times
- Passion
  + inspire others, celebrate on the winds
- Honesty
  + directness, communicate honestly, know how to admit mistakes
- Selflessness
  + Eagerness, sharing openly, helping, being a mentor

### Netflix Freedom and Responsibility

- Self motivating
- Self aware
- Sel disciplined
- Self improving
- Acts like a leader
- Doesn't wait to be told what to do
- Picks up the trash lying on the floor

### Netflix Context vs Control

They look for the culture as a context-based versus control-based, and they tend to be a more of a context-based organization.

**Context-based:**
- Strategy
- Metrics
- Assumptions
- Objectives
- Clearly-defined roles
- Knowledge of the stakes
- Transparency around decision-making

**Control-based:**
- Top-down decision-making
- Management approval
- Committees
- Planning and process valued more than results

## Communication

------------
> "People fail to get along because they fear each other; they fear each other because they don't know each other; they don't know each other because they have not communicated with each other." – Martin Luther King Jr.
------------

### Communication Feedback

- Communication feedback is a system
- Understanding how to give negative/critical feedback is very important
- Positive feedback is also very important
- People are motivated more by progress then accomplishments
- Creating a cadence for feedback builds trust & safety
- Ad-hoc feedback doesn't work without a regularly understood process
- Feedback should be goal related
- The goals should be for: learning, improvement and creating higher trust
- Feedback should not be personal, it should be about behavior and be actionable

**Giving feedback - Anti-patterns:**

- "I'm right, you're wrong"
  + Or the senior versus junior approach
- Assigning blame
- Sarcasm
- Sugarcoating
  + Not being totally honest or making it sentimental
- Beating around the bush
  + Being indirect, avoiding get to the point
- Passive-aggression
  + Using a passive form of hostility, being falsely gentle
- One-way conversations
  + One person driving the whole conversation

**Giving feedback - Patterns:**

- Honesty
  + Being genuine
- Being straightforward
- Timely
  + Being opportune, without delay

**Receiving feedback:**

- Good listening
- Ask questions to understand
- **Always reply with thank you**

**Avoid:**

- Email
- Phone
- Chat
- Social media

-------------
> "Criticism may not be agreeable, but it is necessary. It fulfils the same function as pain in the human body. It calls attention to an unhealthy state of things." – Winston Churchill
-------------

### Feedback Techniques

There are three Types of Feedback identified by Dan North (that is one of the original authors of behavior-driven development and was part of the original continuous delivery pipeline):

- Porpoise Feedback
- Sandwich Feedback
- Atkins Feedback

**Porpoise Feedback (Used in Low Trust)**

- Only provide positive feedback
- Assume everything else will self-correct
- Everything else (magically) will self-correct

**Sandwich Feedback (Used in Medium Trust)**

- Offer positive feedback
- Give constructive feedback (critical/safe)
- Offer general positive summary

Obs: It has a positive-negative-positive structure and it's behavior-based. Some people need three-to-one positives and some people need like ten-to-one...

**Atkins Feedback (Used in High Trust)**

- ~~Offer positive feedback~~
- Give constructive feedback (critical/safe)
- ~~Offer general positive summary~~

### Frameworks for Feedback (by Rebecca Miller-Webster)

- Mirror, Validate, Empathy
- Start, Stop, Continue (SSC)
- Power Dynamics
- Microagressions
- Non-Violent Communication

**Mirror, Validate, Empathy:**

- Mirror
  + Repeat and confirm what was said
- Validate
  + Validate what makes sense or not
- Empathy
  + The receiver tries to assume what the sender is feeling (verbally)
  + Empathy is a skill and we can get better at it
  + You listen and summarize; recognize and point out your own emotions; shut off your inner narrator (day dreaming)

**Start, Stop, Continue (SSC):**

- Start
  + What should I start doing
- Stop
  + What should I stop doing
- Continue
  + What should I continue doing

**Power Dynamics:**

- Power dynamics exist whether we acknowledge them or not
- Power can be formal or informal
- Words from a person of power have exponential impact
- Consider the power dynamics when giving feedback

**Microaggressions:**

- A subtle but offensive comment or action directed at a minority or other non dominant group that is often unintentional or unconsciously reinforces a stereotype
  + Tone policing
  + Othering (not one of us)

**Non-Violent Communication:**

- Facts:
  + What happened without commentary
- Feelings:
  + Emotion it made you feel
- Needs:
  + Human need that wasn't met
- Requests:
  + What you would like the person to do in the future

## Blameless Culture

-------------
> A blameless culture believes that systems are NOT inherently safe and humans do the best they can to keep them running
-------------
> "Underneath every simple, obvious story about 'human error', there is a deeper, more complex story about the organization" – Sidney Dekker, The Field Guide to Understanding Human Error
-------------

### Views on Human Error

**The old view of human error (First Story)**

- Human error is cause of accidents
- To explain failure, you must seek failure
- You must find people's: inaccurate assessments, wrong decisions, bad judgements

**The new view of human error (Second Story)**

- Human error is a symptom of trouble deeper inside a system (systems thinking)
- To explain failure, do not try to find where people went wrong
- Instead, find how people's assessments and actions made sense at the time, given the circumstances that surrounded them

### Bad Apple Theory: Throw away the bad apples

- Complex systems are basically safe, they need to be protected from unreliable people (bad apples)
- Human errors cause accidents: humans are the dominant contributor to more than two-thirds of mishaps
- Errors occur because of human loss of situation awareness / complacency / negligence
- Errors are introduced to the system only through the inherent unreliability of people

### Taylorism in the root of all evil... four principles

1. Create efficiency models based on scientific method by studying work and specific tasks. Replace human instinct, behavior and rule of thumb
1. Match workers based on work at maximum efficiency
1. Control efficiency by monitoring and supervision
1. Managers plan and workers work

--------------
> "Murphy's Law is wrong. What can go wrong usually goes right, but then we draw wrong conclusion." – Dekker, The Field Guide of Human Error
--------------

### Just Culture concept (by Sidney Dekker)

- A culture of trust, learning and accountability. It's important to have when something goes wrong in your organization
- *Just culture* means that you're making effort to balance safety and accountability

**A retributive just culture asks:**

- Which rule is broken?
- Who did it?
- How bad was the breach, and what should the consequences be?
- Who gets to decide this?

**A retributive just culture - Shades of culpability:**

- Honest mistake, you can stay
  + "Don't let it happen again"
- Risk-taking, you get a warning
  + "You took a risk... Oh yeah, that's probably not a great idea"
- Negligence, you are get go
  + "You made that mistake thrww times, we're going to have to let you go"

**A restorative just culture asks:**

- Who is hurt?
- What do they need?
- Whose obligation is it to meet that need?
- How do you involve the community in this conversation?

**A restorative just culture - Shades of culpability:**

- Investigating mistakes that focuses on failure's mechanisms and decision-making processes
- Allow individuals to give detailed accounts without fear of punishment or retribution
  + People need to feel safe, to be able to explain a situation

### The Human Side of Postmortems

----------------
> You organization must continually affirm that individuals are **NEVER** the 'root causes' of outages – Dave Zwieback
----------------

**The 3 R's**

- Regret
  + An acknowledgment of the impact ot the outage and an apology
- Reason
  + A linear outage timeline, from initial incident detection to resolution, including the so-called "root causes"
- Remedy
  + A list of remediation items to ensure that this particular outage won't repeat

**Awesome Postmortems**

- In complex systems, there is no root clause, except...
- there are (multiple) conditions, some of which are unknowable, unfixable, outside our control
- poeple did what made sense at the time, given the information they had (no conterfactuals)
- failure and success are both normal (in complex systems)
- getting the full account* of what happened is more important than blame/punishment

**Understanding Cognitive Biases**

It's important to understand how those biases will play during an outage and an incident/anomaly resolution.

- Hindsight bias:
  + knew-it-all-along: It's the idea of seeing the event as having been predictable (*"Yes, we knew it all along"*)
- Outcome bias:
  + Evaluating the quality of a decision when the outcome of that decision is already known (*"Well, that happened because of XYZ... We've seen that before..."*)
  + The concept of **Normalization of Deviance** (by Diane Vaughan): you get used to making mistakes, and, because it doesn't really break when you make those mistakes, in the future you'll say *"Oh, don't worry about that, we do that all the time..."*
- Availability bias:
  + Preference by decision makers to information and events that are more recent
- Fundamental attribution bias:
  + Explain behavior in terms of internal disposition, such as personality traits, abilities, moties, etc. as opposed to external situational factors (*"Bill is aways sloppy with his code, so, surely, that's why the system went down"*)

### Just Culture at Etsy

- We encourage learning by having these **Blameless Postmortems** on outages and accidents
- We understand how an accident happen, in order to better equip ourselves from it happening in the future
- We gather details from multiple perspectives on failures, and we don't punish people for making mistakes
- We enable and encourage people who do make mistakes to be the experts on educating the rest of the organization how not to make them in the future
- We accept that there is always a discretionary space where humans can decide to make actions or not, and that the judgement of those decisions lie in hindsight
- We accept that the **Hindsight Bias** will continue to cloud our assessment of past events, and work hard to eliminate it
- We accept that the **Fundamental Attribution Error** is also difficult to escape, so we focus on the environment and circumstances people are working in when investigating accidents

### Postmortem Checklist (by Victor Ops)

- Document your timeline or log data
- Document conversations
- Leave room for notes
- Mean Time to Resolution / other time calculations
- Level of severity
- Archive it for historical retrieval
- Remediation - make it actionable

### The Awesome Postmortem Framework (by Mindweather LLC)

- Set the context
  + The purpose of a postmortem is to learn, no one will be blamed, shamed, or punished for providing account
  + Blame-free does not mean accountability-free, so you want to collect the full account (what happened)
- Build a timeline
  + Make sure you've got a good timeline by collecting data from different sources (e.g. chat logs, any correspondence, people's recent memory)
- Determine and prioritize the remediation items
- Publish the postmortem write-up as widely as possible
