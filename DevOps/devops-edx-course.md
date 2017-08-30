# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

 ## Summary
  
  * [Chapter 1 - Concepts](#chapter-1-concepts)
    - [Resources](#resources-chapter-1)
  * [Chapter 2 - Understanding the Value Stream](#chapter-2-understanding-the-value-stream)
    - [Resources](#resources-chapter-2)

---
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

### Resources Chapter 1

#### Articles

  * [Knight Capital](https://en.wikipedia.org/wiki/Knight_Capital_Group)
  * [Knight Capital Accident](http://www.kitchensoap.com/2013/10/29/counterfactuals-knight-capital/)
  * [Continuous Delivery](https://continuousdelivery.com/)
  * [Lean software development](https://en.wikipedia.org/wiki/Lean_software_development)
  * [What Devops Means to Me (CAMS)](https://blog.chef.io/2010/07/16/what-devops-means-to-me/)
  * [IT Revolution - The Convergence of DevOps](http://itrevolution.com/the-convergence-of-devops/)
  * [IT Revolution - The And on Chord](http://itrevolution.com/kata/)
  * [The History Of DevOps](http://itrevolution.com/the-history-of-devops/)
  * [What is DevOps? (Wall of Confusion)](http://dev2ops.org/2010/02/what-is-devops/)

#### Books

  * The Machine that Changed The World
  * The Lean Startup
  * The Phoenix Project
  * Devops Handbook

#### Presentations

  * [DevOps Connect cdSummit: John Willis Kata Presentation](https://www.youtube.com/watch?v=0N0SBcp0mjY)
  * [Velocity 09: John Allspaw and Paul Hammond, "10+ Deploys Per Day"](https://www.youtube.com/watch?v=LdOe18KhtT4)
  * [The DevOps Transformation](https://www.youtube.com/watch?v=3KpPBnEtRj4)
  * [Netflix: Culture and Responsibility](http://www.slideshare.net/reed2001/culture-1798664/)
  * [Spotify engineering culture (part 1)](https://puppet.com/resources/white-paper/2015-state-of-devops-report)
  * [Leading A DevOps Transformation: Lessons Learned](http://www.slideshare.net/realgenekim/leading-a-devops-transformation-lessons-learned)

---
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
> "Culture eats strategy for breakfast" – Peter Drucker
> "I don't fear the man who has practiced 10,000 kicks. I fear the man who practiced one kick 10,00 times" – Bruce Lee
> "Learning is not compulsory... neither is survival" – W. Edwards Deming
------------------------

#### The Andon Cord

 - **Anybody** on the production line see the cord
 - If someone saw a **defect**, he could pull that cord and **stop the line**
 - Each pull on the cord is a **Opportunity to Learn**

### Resources Chapter 2

#### Articles

 * [The Satir Change Model](http://stevenmsmith.com/ar-satir-change-model/)
 * [Kanbans and DevOps: Resource Guide for “The Phoenix Project” (Part 2)](http://itrevolution.com/resource-guide-for-the-phoenix-project-kanbans-part-2)
 * [The Small Batches Principle](http://queue.acm.org/detail.cfm?id=2945077)
 * [Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)
 * [Resilience Engineering: Learning to Embrace Failure](http://queue.acm.org/detail.cfm?id=2371297)
 * [The Netflix Simian Army](http://techblog.netflix.com/2011/07/netflix-simian-army.html)
 * [FIT : Failure Injection Testing](http://techblog.netflix.com/2014/10/fit-failure-injection-testing.html)
 * [Fault Injection in Production - Making the case for resilience testing](http://queue.acm.org/detail.cfm?id=2353017)
 * [DevOps keeps it cool with ICE](http://radar.oreilly.com/2015/01/devops-keeps-it-cool-with-ice.html)
 * [Empathy: The Essence of DevOps][http://blog.ingineering.it/post/72964480807/empathy-the-essence-of-devops]
 * [Karōjisatsu (Burnout)](http://itrevolution.com/karojisatsu/)
 * [Feature flags, dark launches, and canary releases for all: LaunchDarkly first year in review](http://blog.launchdarkly.com/feature-flags-dark-launches-and-canary-releases-for-all-launchdarkly-first-year-in-review/)
 * [Feature flags and canary, dark, and A/B releases](http://www.pragmaticdevops.com/2014/05/continuous-delivery/feature-flags-and-canary-dark-and-ab-releases/)
 * [How does Etsy manage development and operations?](https://codeascraft.com/2011/02/04/how-does-etsy-manage-development-and-operations/)
 * [Introduction to the Improvement Kata](http://www.slideshare.net/mike734/introduction-to-the-improvement-kata)
 * [How Many Times Do You Pull the Andon Cord Each Day?](http://gembapantarei.com/2008/04/how_many_times_do_you_pull_the_andon_cord_each_day.html)
 * [The Three Ways: The Principles Underpinning DevOps](http://itrevolution.com/the-three-ways-principles-underpinning-devops/)
 * [Docker and the Three Ways of DevOps Part 1: The First Way – Systems Thinking](https://blog.docker.com/2015/05/docker-three-ways-devops/)
 [Improving Flow: Fix the Handoffs to Remove Your Worst Bottlenecks](http://dev2ops.org/2012/11/improving-flow-fix-the-handoffs-to-remove-your-worst-bottlenecks/)
 * [Use DevOps to Turn IT into a Strategic Weapon](http://dev2ops.org/2012/09/use-devops-to-turn-it-into-a-strategic-weapon/)

#### Books

* Learning to See - Mike Rother
* Personal Kanban - Jim Benson
* The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses - Eric Ries
* Lean Software Development: An Agile Toolkit by Mary Poppendieck (Author), Tom Poppendieck (Author)
* Beyond the Goal: Eliyahu Goldratt Speaks on the Theory of Constraints (Your Coach in a Box) Audio CD – Audiobook, CD, Unabridged by Eliyahu Goldratt
* The Art of Monitoring - James Turnbull
* Effective DevOps by Katherine Daniels, Jennifer Davis
* The Practice of Cloud System Administration: Designing and Operating Large Distributed Systems, Volume 2 1st Edition by Thomas A. Limoncelli
* Toyota Kata: Managing People for Improvement, Adaptiveness and Superior Results 1st Edition by Mike Rother
* The High-Velocity Edge: How Market Leaders Leverage Operational Excellence to Beat the Competition Hardcover – May 3, 2010 by Steven J. Spear

#### Presentations

 * [One Piece Flow vs. Mass Production: Envelope Stuffing Lean Thinking Simulation](https://www.youtube.com/watch?v=Dr67i5SdXiM)
* [How to initiate a DevOps Transformation (Video)](http://dev2ops.org/2013/12/how-to-initiate-a-devops-transformation-video/)
* [DevOps Kaizen: Practical Steps to Start & Sustain a Transformation](http://www.slideshare.net/dev2ops/devops-kaizen-practical-steps-to-start-sustain-a-transformation)
* [Support and Initiate a DevOps Transformation](http://www.slideshare.net/dev2ops/support-and-initiate-a-devops-transformation)
* [A Kanban System for Software Engineering](https://www.infoq.com/presentations/kanban-for-software)
* [DOES15 - Dominica DeGrandis - The Shape of Uncertainty](https://www.youtube.com/watch?v=Gp05i0d34gg)
* [GameDay: Creating Resiliency Through Destruction](https://www.youtube.com/watch?v=zoz0ZjfrQ9s)
* [Morgue: Helping Better Understand Events by Building a Post Mortem Tool - Bethany Macri](https://vimeo.com/77206751#t=27m40s)
