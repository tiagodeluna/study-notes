# DevOps

Notes about **Introduction to DevOps: Transforming and Improving Operations** edX course, by John Willis, *The Linux Foundation*

## Concepts:

### Japan's influence (Toyota Production Systems - Lean)

 - Muda (Waste): eliminate waste wherever possible.
 - Mura (Flow): It's about evenness. Getting the pipeline flow consistent.
 - Muri (Stress): reduce stress on the system.
 - Kaizen (Improvement): continuous improvement.
 - Kata (Form): repetitive actions become memory muscle. It's about integrate Muda, Mura, Muri and Kaizen to become a natural behavior.

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

## Understanding the Value Stream

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

 - Create an idea *Design Lead Time*
 - Add work to the backlog *Design Lead Time*
 - Create a user story *Design Lead Time*
 - Implement as code *Design Lead Time*
 - Check into version control *Deployment Lead Time* *Cycle Time*
 - Deploy into production *Deployment Lead Time* *Cycle Time*
 - Validate the customer experience *Deployment Lead Time* *Cycle Time*

### Understanding The Value Stream

---------------------
> Watch the baton not the runner. (a metaphor about a 40 meter relay race team)
---------------------

 - The Value Stream of how things work (runners)
 - The Value Stream of the work (baton)

### How to Reduce Deployment Lead Time in the Workflow

- Small batches
- Recude work in process (WIP)
- 1x1 Flow
- Reduce Bottlenecks (TOC)
- Optimize Globally











