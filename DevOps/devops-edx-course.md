# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

## Summary
  
  * [Chapter 1 - Concepts](#chapter-1-concepts)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-1-concepts)
  * [Chapter 2 - Understanding the Value Stream](#chapter-2-understanding-the-value-stream)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-2-understanding-the-value-stream)
  * [Chapter 3 - Getting Started with DevOps](#chapter-3-getting-started-with-devops)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-3-getting-started-with-devops)
  * [Chapter 4 - The First Way - Accelerate Flow](#chapter-4-the-first-way---accelerate-flow)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-4-the-first-way---accelerate-flow)

# Chapter 1 *Concepts*

### Japan's influence (Toyota Production Systems - Lean)

 - *Muda* (Waste): eliminate waste wherever possible.
 - *Mura* (Flow): It's about evenness. Getting the pipeline flow consistent.
 - *Muri* (Stress): reduce stress on the system.
 - *Kaizen* (Improvement): continuous improvement.
 - *Kata* (Form): repetitive actions become memory muscle. It's about integrate Muda, Mura, Muri and Kaizen to become a natural behavior.

--------------------------
> Faster and more reliable
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
 - They recover gaster: their MTTR (Mean Time to Recovery) is much lower
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
   - The time it takes one piece to move all the way through a process of the e stream from start to finish.
   - Lead time clock starts when the request is made and ends at delivery.
   - Lead time is what the customer sees.
 + Cycle Time
   - How often a part or product actually is completed by a process, as timed   bservation.
   - Cycle time clock starts when the work begins on the request and ends when the item is ready for delivery.
    
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

| | LEAD TIME | CYCLE TIME |
| ----- | ----- | ----- |
| Create an idea  | Design | |
| Add work to the backlog | Design | |
| Create a user story | Design | |
| Implement as code | Design | |
| Check into version control | Deployment | X |
| Deploy into production | Deployment  | X |
| Validate the customer experience | Deployment | X |

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
     + Splunk, ELK (Elastic Search, Logstash, Kibana), Loggly
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
> "A production line that never stopped was either extermely good or extremely bad." – Taiichi Ohno
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

 - The build phase
 - Typically triggered by a code commit
 - Typically builds are done from trunk
 - The process happens every time someone commits code
 - Code is compiled and libraries are built
 - Build trigger package, artifact and image creation

### 8 Principles of Continuous Delivery

 1. Create a repeatable, reliable process for releasing software
 2. Automate almost everything
 3. Keep everything in version control
 4. If it hurts, do it more frequently, and bring the pain forward
 5. Build quality in
 6. Done means released
 7. Everybody is responsible for the delivery process
 8. Continuous improvement

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
 - Git, Team Foundation Server, Perforce, **Github**, Bitbucket, GitLab

Build Console:
 - on-prem: **Jenkins**, Bamboo, Team City
 - SaaS-based: **Travis CI**, Circle CI, Shippable

Repository Managers:
 - Nexus, Artifactory, Docker Trusted Registry, Docker Hub, Google Container Registry

Operations Console:
 - **Rundeck**, Marathon, Asgard, Spinaker, Weave Scope

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

> You have to automate all that process of conversion and deal with the operational cost of the different platforms and potential inconsistencies

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

> Even if you have to use different infrastructure frameworks, at least have your operating system be the same

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

Pro's:
- Infrastructure primitives defined as DSL
  + The abstractions are well-defined
- Highly parameterized
- Desired state-based model
- Principles:
  + Modularity, Composability, Extensibility, Flexibility, Repeatability (DSL), Declaration, Abstraction, Idempotence, Convergence

Con's:


## Automated Testing

## Deployment Strategies (Zero Downtime Release)

By the end of this chapter, you should be able to:

 - Discuss the concept and goals of the First Way.
 - Explain the difference between shortening lead time and reducing bottlenecks.
 - Explain the difference between continuous integration, continuous delivery, and continuous deployments.
 - Discuss the eight principles of continuous delivery.
 - Explain the importance of everything being managed and controlled by source control.
 - Discuss the concepts of Infrastructure as Code and immutable infrastructure.
 - Discuss automated testing.
 - Explain the patterns for live deployments, otherwise called "zero downtime deployments".

