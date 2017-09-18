# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

## Summary
  
  * [Chapter 1 - Concepts](#chapter-1-concepts)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-1-concepts)
  * [Chapter 2 - Understanding the Value Stream](#chapter-2-understanding-the-value-stream)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-2-understanding-the-value-stream)
  * [Chapter 3 - Getting Started with DevOps](#chapter-3-getting-started-with-devops)
    - [Resources](https://github.com/tiagodeluna/study-notes/blob/master/DevOps/devops-edx-course-resources.md#chapter-3-getting-started-with-devops)

## Chapter 1 *Concepts*

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


## Chapter 2 *Understanding the Value Stream*

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


## Chapter 3 *Getting Started with DevOps*

### Improvement Paradox (Balancing Risk/Reward)

 - Typically small enough in scope with a high probability of success and safe to fail
 - Large enough to have impact with possibility of future improvements while not appearing as a trivial experiment

### Pick a Value Stream

 - Legacy
 - Greenfield
 - Brownfield

#### Legacy

 - SOR and SOE
   + System of Record (Mode 1)
   + System of Engagement (Mode 2)
 - The 3 R's
   + Reward
   + Risk
   + Resistance

##### The 3 R's for Legacy

 - Leadership suppert is critical
 - Look for innovators and early adopters
 - Prior knowledge of DevOps helps
 - System of Engagements is better then System of Records
 - Build on success

##### The ETTO Principle - Efficiency-Thoroughness Trade-Off (Erik Hollnagel)

 - Efficiency
     + Low investment
     + Sufficient to achieve the goal
 - Thoroughness
     + Achieve the objective without any unwanted side-effects
     + Outcomes will be the intended one

##### Focus Areas to Look For

 - Long wait times for work
 - Change approval bottlenecks
 - Rework is generated
 - Percentage of change and accurate (Backwash)

#### Brownfield

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

#### Greenfield

------------------------
> A Greenfield project is the process of develop a system for a totally new environment, without concern for integrating with other systems. Such projects are deemed as higher risk, as they are often for new infrastructure, new customers, and even new owners.
------------------------

### Understanding Organizational Change

#### Organizational Goals

 - The pipeline is everyone's responsibility
 - Focus on making more generalists: less focus on specialists
 - Fund services, not projects: projects tend to end. A service never ends, it just continues.
 - Encourage loose coupling
 - Smaller teams (and smaller services)
 - High trust and low blame
 - Make work visible

#### Individual Level

Four areas arount the individual level:
 - I/T/E-Shaped Individuals
 - Mindsets
 - Motivation
 - Intent

#### I/T/E-Shaped Individuals

##### I-Shaped

- Specialists (linear skilled)
- Deep expertise in one area
- Very few skills in other areas
- Can create bottlenecks
- Can create downstream waste

##### T-Shaped

 - Generalists (horizontally skilled)
 - Broad skills in many areas
 - Helps with bottlenecks
 - Can remove downstream waste

##### E-Shaped

- Deep in a few areas
- Typically an innovator
- General expertise in many areas
- High impact individual

#### Mindsets

##### Fixed Mindset

- Fixed belief
- Outcome-based
- Belief that intelligence and talent are fixed traits

##### Growth Mindset
 - Alternative Belief
 - Effort-based
 - Belief that abilities can be developed through dedication and hard work
 
#### Motivation

 - Intrinsic Motivation
   + Engaging in a behavior because it is personally rewarding.
   + Rewards: Autonomy, Sense of achievement, Passion
 - Extrinsic Motivation
   + Motivated behavior or engage in an activity to earn a reward or avoid punishment.
   + Rewards: Pay increase, Promotion, Bonuses
 - There is no good or bad here: The important thing is to understand what motivates people for change

##### Overjustification Effect

 - Extrinsic rewards can decrease an individuals intrinsic motivation
 - Individuals may pay more attention to the extrinsic rewards instead of their intrinsic motivations
 - Reinforce extrinsic motivation mindsets
 - Efforts over outcome based extrinsic rewards (effort-based rewards) are less influenced by the Overjustification Effect

##### Individuals Motivation

 - Use incentives approprietely
 - Challenge mindsets: A variation of the Growth Mindset. It's a very powerful tool, under-explored in our industry
 - Visualise the effort, not the success
 - Intent-based motivation (individual control)
 - Focus on the effort, not the outcome
