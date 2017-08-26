# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

 ## Summary
  
  * [Chapter 1 - Concepts](#chapter-1-concepts)
    - [Resources](#resources-chapter-1)
  * [Chapter 2 - Understanding the Value Stream](#chapter-2-understanding-the-value-stream)
    - [Resources](#resources-chapter-2)

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

### A Value Stream Example

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

### The First Way

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

### Resources Chapter 2

#### Presentations

  * [One Piece Flow vs. Mass Production: Envelope Stuffing Lean Thinking Simulation](https://www.youtube.com/watch?v=Dr67i5SdXiM)
  * 