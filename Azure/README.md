# AZ-900 AZURE FUNDAMENTALS PREPARATION COURSE

# Cloud Computing

Cloud computing is renting resources on another company (a *cloudy provider*) in a "pay only for what you use" model.

Typically, the computing services offered by a cloud provider are:
* **Compute power** - such as Linux servers or web applications, usually in the form of a *virtual machine*, a *container* or as *serverless computing*. You can have a VM in minutes at less cost than a physical computer.
* **Storage** - such as files and databases. The advantage to using cloud-based data storage is you can scale to meet your needs.
* **Networking** - secure connections
* **Analytics** - visualizing telemetry and performance data.

## Benefits of Cloud Computing

* **It's cost effective**: Cloud computing provides a **pay-as-you-go** or consumption-based pricing model.
* **It's scalable**: You can increase or decrease the resources and services used based on the demand or workload at any given time, doing both vertical and horizontal scaling.
    - *Vertical scaling*: adding resources to increase the power of an existing server (adding more CPUs or memory...).
    - *Horizontal scaling*: adding more servers that function together as one unit.
* **It's elastic**: As your workload changes due to a spike or drop in demand, a cloud computing system can compensate by automatically adding/removing resources.
* **It's current**: The cloud provider handles all software patches, hardware setup, upgrades, and other IT management tasks to ensure you're using the latest and greatest tools. The hardware is also maintained and upgraded by the cloud provider.
* **It's reliable**: Cloud computing providers offer data backup, disaster recovery, and data replication services to make sure your data is always safe. In addition, redundancy is often built into cloud services architecture so if one component fails, a backup component takes its place (aka *fault tolerance*)
* **It's global**: Cloud providers have fully redundant datacenters located in various regions all over the globe, giving you a local presence close to your customers to give them the best response time possible. You can replicate your services into multiple regions for *redundancy* and *locality*, or select a specific region to ensure you meet data-residency and compliance laws.
* **It's secure**: Cloud providers offer a broad set of policies, technologies, controls, and expert technical skills that can provide better security than most organizations can otherwise achieve.

## Compliance Terms and Requirements: Compliance Offerings

* **Criminal Justice Information Services (CJIS - US)**: Azure is the only major cloud provider that commits to conformance with FBI CJIS Security Policy.
* **Cloud Security Alliance (CSA) STAR Certification**: based on achieving ISO/IEC 27001 certification and meeting criteria specified in the Cloud Controls Matrix (CCM).
* **General Data Protection Regulation (GDPR)**
* **EU Model Clauses**
* **Health Insurance Portability and Accountability Act (HIPAA - US)**
* **International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) 27018**
* **Multi-Tier Cloud Security (MTCS - Singapore)**
* **Service Organization Controls (SOC) 1, 2, and 3**
* **National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF)**
* **UK Government G-Cloud**

## Economies of Scale

Economies of scale is the ability to do things more efficiently or at a lower-cost per unit when operating at a larger scale.

Cloud providers are large businesses leveraging the benefits of economies of scale, and can pass the savings on to their customers in a number of ways:
* Providing the ability to acquire hardware at a lower cost
* Making deals with local governments and utilities to get tax savings, lowering the price of power, cooling, and high-speed network connectivity
* Lowering prices for the services offered

## Capital expenditure (CapEx) versus operational expenditure (OpEx)

* **Capital Expenditure (CapEx)**: On-premise. The spending of money on physical infrastructure up front, and then deducting that expense from your tax bill over time. *CapEx is an upfront cost, which has a value that reduces over time.*
* **Operational Expenditure (OpEx)**: Cloud Computing. Spending money on services or products now and being billed for them now. You can deduct this expense from your tax bill in the same year. *There's no upfront cost. You pay for a service or product as you use it.*

### CapEx Computing Costs

* Server costs (servers, computers, power supplies and maintenance costs)
* Storage costs (hardware components and cost of supporting it)
* Network costs (cabling, switches, access points, routers and internet)
* Backup and archive costs
* Organization continuity and disaster recovery costs (fault tolerance and redundancy, data recovery site, backup generators...)
* Datacenter infrastructure costs (equipment, costs of renovation and upgrading, electricity, floor space, cooling, and building maintenance)
* Technical personnel (to install, deploy, and manage the systems)

```
 With cloud computing, many of the costs associated with an on-premises datacenter are shifted to the service provider.
```

```
 The Benefit of CapEx is that you can plan your expenses at the start of a project or budget period. Your costs are fixed.
```

### OpEx Cloud Computing Costs

* Leasing software and customized features (provisioned resources)
* Scaling charges based on usage/demand instead of fixed hardware or capacity (such as number of users, CPU usage time, allocated RAM, I/O operations per second (IOPS), and storage space)
* Billing at the user or organization level (scaling, customization, and  provisioning at organization or user level)

### Benefits of OpEx

* No need to invest in equipement if you want to try a new product or service
* Follows demand fluctuation (auto-scaling)
* Agile, due to its ability to rapidly change an IT infra to adapt to the evolving needs of the business
* You can manage your costs dynamically, optimizing spending as requirements change

## Cloud Deployment Models

**Public cloud**

Everything runs on your cloud provider's hardware.
* Advantages:
    - High scalability/agility
    - Pay-as-you-go pricing
    - You're not responsible for maintenance or hardware updates, so it also requires minimal technical knowledge to set up and use
* Disadvantages:
    - There may be specific security or legal requirements (overnment policies, industry standards...) that cannot be met
    - If you don't own the hardware/services and cannot manage them as you may want to
    - Unique business requirements, such as having to maintain a legacy application might be hard to meet

**Private cloud**

You create a cloud environment in your own datacenter and provide self-service access to compute resources to users in your organization.
* Advantages:
    - You can ensure the configuration can support any scenario or legacy application
    - You have control (and responsibility) over security
    - You can meet strict security, compliance, or legal requirements
* Disadvantages:
    - You have initial CapEx costs and must purchase the hardware for startup and maintenance
    - Limited agility: to scale you must buy, install, and setup new hardware
    - Private clouds require IT skills and expertise that's hard to come by

**Hybrid**

A combination of public and private clouds, allowing you to run your applications in the most appropriate location.
* Advantages:
    - You can keep any systems that use out-of-date hardware or OS running and accessible
    - You have flexibility with what you run locally versus in the cloud
    - You can take advantage of economies of scale from public cloud providers where it's cheaper, and then supplement with your own equipment when it's not
    - You can use your own equipment to meet security, compliance, or legacy scenarios where you need to completely control the environment
* Disadvantages:
    - It can be more expensive than selecting one deployment model (CapEx + OpEx)
    - It can be more complicated to set up and manage

## Types of Cloud Services

* **Infrastructure as a Service (IaaS)**: It's an instant computing infrastructure (hardware), provisioned and managed over the internet. IaaS is commonly used for: migrating workloads, test and development, storage, backup and recovery.
* **Platform as a Service (PaaS):** It's a complete development and deployment environment in the cloud. It helps you create an application quickly without managing the underlying infrastructure. PaaS is commonly used in the following scenarios: Development framework, Analytics or business intelligence.
* **Software as a Service (SaaS):** SaaS is software that is centrally hosted and managed for the end customer. Office 365, Skype, and Dynamics CRM Online are examples of SaaS software.

---

# Azure subscription

An Azure subscription is a logical container used to provision resources in Azure. It holds the details of all your resources like virtual machines (VMs), databases, and more.

It is possible to create additional subscriptions to separate: Environments (e.g development, testing, security), Organizational structures (e.g team, department, project), and Billing (e.g production workloads, development and testing workloads).

If you have multiple subscriptions, you can organize them into invoice sections. You can also set up multiple invoices within the same billing account, by creating additional billing profiles. Each billing profile has its own monthly invoice and payment method.

---

# Azure Services

The most commonly used categories are:

## Compute

A range of options for hosting applications and services, including:

* Azure Virtual Machines: Windows or Linux virtual machines (VMs)
* Azure Virtual Machine Scale Sets: Scaling for VMs hosted in Azure
* Azure Kubernetes Service: Management of a cluster of VMs that run containerized services
* Azure Service Fabric: Distributed systems platform
* Azure Batch: Managed service for parallel and high-performance computing applications
* Azure Container Instances: Run containerized apps on Azure without provisioning servers or VMs
Azure Functions: An event-driven, serverless compute service

## Networking

Includes a range of options to connect the outside world to services and features in the global Microsoft Azure datacenters.

* Azure Virtual Network: Connects VMs to incoming Virtual Private Network (VPN) connections
* Azure Load Balancer: Balances inbound and outbound connections to applications or service endpoints
* Azure Application Gateway: Optimizes app server farm delivery while increasing application security
* Azure VPN Gateway: Accesses Azure Virtual Networks through high-performance VPN gateways
* Azure DNS: Provides ultra-fast DNS responses and ultra-high domain availability
* Azure Content Delivery Network: Delivers high-bandwidth content to customers globally
* Azure DDoS Protection: Protects Azure-hosted applications from distributed denial of service (DDOS) attacks
* Azure Traffic Manager: Distributes network traffic across Azure regions worldwide
* Azure ExpressRoute: Connects to Azure over high-bandwidth dedicated secure connections
* Azure Network Watcher: Monitors and diagnoses network issues using scenario-based analysis
* Azure Firewall: Implements high-security, high-availability firewall with unlimited scalability
* Azure Virtual WAN: Creates a unified wide area network (WAN), connecting local and remote sites

## Storage

Azure provides four main types of storage services:

* Azure Blob storage: Storage service for very large objects, such as video files or bitmaps
* Azure File storage: File shares that you can access/manage like a file server
* Azure Queue storage: A data store for queuing and reliably delivering messages between applications
* Azure Table storage: A NoSQL store that hosts unstructured data independent of any schema

## Mobile

Azure enables developers to create mobile backend services for iOS, Android, and Windows apps quickly and easily. Features include: Corporate sign-in, Offline data synchronization, Connectivity to on-premises data, Broadcasting push notifications, Autoscaling.

## Databases

Azure provides multiple database services to store a wide variety of data types and volumes:

* Azure Cosmos DB: Globally distributed database that supports NoSQL options
* Azure SQL Database: Fully managed relational database with auto-scale, integral intelligence, and robust security
* Azure Database for MySQL: Fully managed and scalable MySQL relational database with high availability and security
* Azure Database for PostgreSQL
* SQL Server on VMs
* Azure SQL Data Warehouse
* Azure Database Migration Service: Migrates your databases to the cloud with no application code changes
* Azure Cache for Redis: Caches frequently used and static data to reduce data and application latency
* Azure Database for MariaDB

## Web

First-class support to build and host web apps and HTTP-based web services.

* Azure App Service: Quickly create powerful cloud web-based apps
* Azure Notification Hubs: Send push notifications to any platform from any back end.
* Azure API Management: Publish APIs to developers, partners, and employees.
* Azure Cognitive Search: Fully managed search as a service.
* Web Apps feature of Azure App Service: Create and deploy mission-critical web apps at scale.
* Azure SignalR Service: Add real-time web functionalities easily.

## Internet of Things

There are a number of services that can assist and drive end-to-end solutions for IoT on Azure:

* IoT Central: Fully-managed global IoT SaaS solution that makes it easy to connect, monitor, and manage your IoT assets at scale
* Azure IoT Hub: Messaging hub that provides secure communications between and monitoring of millions of IoT devices
* IoT Edge: Push your data analysis models directly onto your IoT devices, allowing them to react quickly to state changes without needing to consult cloud-based AI models.

## Big Data

Microsoft Azure supports a broad range of technologies and services to provide big data and analytic solutions:

* Azure SQL Data Warehouse: Run analytics at a massive scale using a cloud-based Enterprise Data Warehouse (EDW) that leverages massive parallel processing (MPP) to run complex queries quickly across petabytes of data
* Azure HDInsight: Process massive amounts of data with managed clusters of Hadoop clusters in the cloud
* Azure Databricks: Collaborative Apache Spark–based analytics service that can be integrated with other Big Data services in Azure.

## Artificial Intelligence

Some of the most common Artificial Intelligence and Machine Learning service types in Azure are listed below, along with cognitive services (pre-built APIs that solve complex problems):

* Azure Machine Learning Service: Cloud-based environment you can use to develop, train, test, deploy, manage, and track machine learning models. It can auto-generate a model and auto-tune it for you
* Azure Machine Learning Studio: Collaborative, drag-and-drop visual workspace where you can build, test, and deploy machine learning solutions using pre-built machine learning algorithms and data-handling modules
* Vision: Image-processing algorithms to smartly identify, caption, index, and moderate your pictures and videos
* Speech: Convert spoken audio into text, use voice for verification, or add speaker recognition to your app
* Knowledge mapping: Map complex information and data in order to solve tasks such as intelligent recommendations and semantic search
* Bing Search: Add Bing Search APIs to your apps and harness the ability to comb billions of webpages, images, videos, and news with a single API call
* Natural Language processing: Allow your apps to process natural language with pre-built scripts, evaluate sentiment and learn how to recognize what users want.

## DevOps

Azure DevOps Services allows you to create build and release pipelines that provide continuous integration, delivery, and deployment for your applications.

* Azure DevOps: Azure DevOps Services provides development collaboration tools including high-performance pipelines, free private Git repositories, configurable Kanban boards, and automated and cloud-based load testing
* Azure DevTest Labs: Quickly create on-demand Windows and Linux environments to test or demo applications directly from your deployment pipelines

---

# Basic concepts for creating websites hosted in Azure

Let's review some basic terms required if you want to have a website up and running in Azure:

## What is an App Service?

Azure App Service is an HTTP-based service that enables you to build and host many types of web-based solutions (web apps, mobile backends, and RESTful APIs...) without managing infrastructure. Applications developed in .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python can run in and scale with ease on both Windows and Linux-based environments.

## App Service Plans

When you create an application using App Service or want to *scale up* an existing application, you have to select an App Service plan. There are three categories for different types of workload (plan):

* **Dev/Test:** for less demanding workloads. Focused on providing shared infrastructure. This category has additional features that become available to the App Service application. e.g. Custom domains/SSL and manual scale.
* **Production:** for more demanding workloads. There are added features such as staging slots, daily backups, and a traffic manager.
* **Isolated**: for workloads that require advanced networking and fine-grained scaling.

Within each category, there are pricing tiers that will allow you to scale the resources available and give you access to additional features.

## Microsoft Azure Marketplace

The Microsoft Azure Marketplace is an online store that hosts applications that are certified and optimized to run in Azure.

## Resource Groups in Azure

Typically, the first step for hosting a web application in Azure is to create a resource group to hold all the things needed. The resource group allows us to administer all the services, disks, network interfaces, and other elements that potentially make up our solution as a unit. Resource groups can be created and managed via Azure portal or via command line using the *Azure CLI*.

```
Tip: Unused resources left running still can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
```

## Azure Cloud Shell, CLI, and PowerShell 

**Azure Cloud Shell**: A *browser-based command-line console* for managing and developing Azure resources. Cloud Shell provides two experiences to choose from, Bash and PowerShell. Both include access to the Azure command-line interface called *Azure CLI* and to *Azure PowerShell*.

**Azure PowerShell**: A *module that you can install* for Windows PowerShell or PowerShell Core, which is a cross-platform version of PowerShell that runs on Windows, Linux, or macOS. It enables you to connect to your Azure subscription and manage resources. You can create administration scripts and use automation tools to automate repetitive tasks and optimize your workflow.

    New-AzVM ` -ResourceGroupName "MyResourceGroup" ` -Name "TestVm" ` -Image "UbuntuLTS" `

**Azure CLI**: A cross-platform *command-line program* (Bash) that connects to Azure and executes administrative commands on Azure resources. Cross-platform means that it can be run on Windows, Linux, or macOS.

    az vm create --resource-group MyResourceGroup --name TestVm --image UbuntuLTS --generate-ssh-keys

---

# Datacenters and Regions in Azure

## What is a region?

Microsoft Azure is made up of datacenters located around the globe. The specific datacenters aren't exposed to end users directly; instead, Azure organizes them into *regions*.

A region is a geographical area on the planet containing at least one, but potentially multiple datacenters that are nearby and networked together with a low-latency network. When you deploy a resource in Azure, you will often need to choose the region where you want your resource deployed.

Regions are important to give you flexibility to bring applications closer to your users, and also to provide better scalability, redundancy, and ensure data residency for your services.

## Geographies

Azure divides the world into *geographies* (typically containing two or more regions) that are defined by geopolitical boundaries or country borders. This division has several benefits:
* Ensure that data residency, sovereignty, compliance, and resiliency requirements are honored within geographical boundaries.
* Geographies are fault-tolerant to withstand complete region failure through their connection to dedicated high-capacity networking infrastructure.

Geographies are broken up into the following areas:
* Americas
* Europe
* Asia Pacific
* Middle East and Africa

## Availability Zones

Azure ensures high availability and redundancy through Availability Zones, which are physically separate datacenters within an Azure region. Each AZ is made up of one or more datacenters equipped with independent power, cooling, and networking. They are isolation boundaries connected through high-speed, private fiber-optic networks.

Obs: Not every region has support for Availability Zones.

### Using Availability Zones in your apps

You can use AZs to run mission-critical (highly-available) applications by co-locating your compute, storage, networking, and data resources within a zone and replicating in other zones. There could be a cost to duplicating your services and transferring data between zones.

Azure services that support AZs fall into two categories:
* **Zonal services** – you pin the resource to a specific zone (e.g. VMs, managed disks, IP addresses)
* **Zone-redundant services** – platform replicates automatically across zones (zone-redundant storage, SQL Database).

## Region Pairs

Each Azure region is always paired with another region within the same geography (such as US, Europe, or Asia) at least 300 miles away. This approach allows for the replication of resources across a geography that helps reduce the likelihood of interruptions due to events such as natural disasters, civil unrest, power outages, or physical network outages affecting both regions at once. If a region in a pair was affected by a natural disaster, for instance, services would automatically fail over to the other region in its region pair.

## Service-Level Agreements (SLA)

SLAs are formal documents that capture the specific terms (operational policies, standards, and practices) that define the performance standards that apply to Azure services. SLAs also specify what happens if a service or product fails to perform to a governing SLA's specification.

There are three key characteristics of SLAs for Azure products and services:

1. Performance Targets - usually expressed as uptime guarantees or connectivity rates.
2. Uptime and Connectivity Guarantees - for example, the SLA for Azure Cosmos DB offers **99.999%** uptime, which includes low-latency commitments of less than 10 milliseconds on DB read and write operations.
3. Service credits - customers may have a discount applied to their Azure bill, as compensation for an under-performing Azure service (for example, 10 service credit percentage for a monthly uptime percentage below 99.9).

### Composite SLAs

The resulting composite SLA can provide higher or lower uptime values, depending on your application architecture. For instance, consider an App Service (99.95%) web app that writes to Azure SQL Database (99.99%). If either service fails the whole application will fail. The composite SLA value for this application is:

`99.95% × 99.99% = 99.94%`

This means the combined probability of failure is higher than the individual SLA values.

---

# Azure Compute

Azure compute is an on-demand computing service for running cloud-based applications. There are four common techniques for performing compute in Azure:

## Virtual machines

Software emulations of physical computers, where you're able to install and run software. You can run single VMs for testing, development, or minor tasks; or you can group VMs together to provide high availability, scalability, and redundancy. Azure has several features such that:

### Availability sets

A logical grouping of two or more VMs that help keep your application available during planned or unplanned maintenance.

A *planned maintenance event* is when the underlying Azure fabric that hosts VMs is updated by Microsoft. When the VMs are part of an availability set, they're put into different *update domains*, which indicate groups of VMs and underlying physical hardware that can be rebooted at the same time.

*Unplanned maintenance events* involve a hardware failure in the data center, such as a power outage or disk failure. The group of VMs that share common hardware are in the same *fault domain*, which is essentially a rack of servers, with power, cooling, and network hardware. In the event the hardware that supports a server rack becomes unavailable, only that rack of servers is affected by the outage.

### Virtual Machine Scale Sets

Virtual Machine Scale Sets let you create and manage a group of identical, load balanced VMs. They allow you to centrally manage, configure, and update a large number of VMs in minutes to provide highly available applications. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule.

### Azure Batch

Azure Batch enables large-scale job scheduling and compute management with the ability to scale to tens, hundreds, or thousands of VMs.

## Containers

Virtualization environment for running applications. Unlike VMs, containers don't include an OS. Instead, they bundle the libraries and components needed to run the application and use the existing host OS. Azure supports Docker containers, and there are several ways to manage containers in Azure:

### Azure Container Instances (ACI)

It offers the fastest and simplest way to run a container in Azure. You don't have to manage any VMs or configure any additional services. It is a PaaS offering that allows you to upload your containers and execute them directly with automatic elastic scale.

### Azure Kubernetes Service (AKS)

The task of automating, managing, and interacting with a large number of containers is known as *orchestration*. AKS is a complete orchestration service for containers with distributed architectures with multiple containers.

## Azure App Service

A platform-as-a-service (PaaS) offering designed to host enterprise web-oriented applications without need of managing infrastructure. It offers automatic scaling and high availability. App Service supports both Windows and Linux, and enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.

## Serverless computing

A cloud-hosted execution environment that runs your code but completely abstracts the underlying hosting environment. Serverless computing encompasses three ideas: the abstraction of servers, an event-driven scale, and micro-billing.

*Micro-billing*: with serverless computing, you pay only for the time your code runs. If no active function executions occur, they're not charged. For example, if the code runs once a day for two minutes, they're charged for one execution and two minutes of computing time.

Azure has two implementations of serverless compute:
* **Azure Functions**, which can execute code in almost any modern language. They're commonly used when you need to perform work in response to an event, often via a REST request, timer, or message from another Azure service and when that work can be completed quickly, within seconds or less. They can be either stateless (the default) or stateful (called *Durable Functions*), where a context is passed through the function to track prior activity.
* **Azure Logic Apps**, which are designed in a web-based designer and can execute logic triggered by Azure services without writing any code. Where Functions execute code, Logic Apps execute workflows designed to automate business scenarios from predefined logic blocks.

---

# Azure Data Storage

## Benefits

* **Automated backup and recovery**
* **Replication across the globe**: copies your data to protect it against any planned or unplanned events (scheduled maintenance, hardware failures, etc)
* **Support for data analytics**: supports performing analytics on your data consumption.
* **Encryption capabilities**
* **Multiple data types**: Azure can store video files, text files, and even large binary files like virtual hard disks. It also has many options for your relational and NoSQL data.
* **Data storage in virtual disks**: Azure also has the capability of storing up to 32 TB of data in its virtual disks.
* **Storage tiers**: storage tiers to prioritize access to data based on frequently used versus rarely used information.

## Types of data

1. **Structured data**. Structured data is data that adheres to a schema, can be stored in a database table with rows and columns, and relies on keys to indicate identity and relationship (relational data)
2. **Semi-structured data**. Semi-structured data (also referred to as non-relational or NoSQL data) doesn't fit neatly into tables, rows, and columns. Instead, it uses tags or keys that organize and provide a hierarchy for the data.
3. **Unstructured data**. Unstructured data encompasses data that has no designated structure to it. There are no restrictions on the kinds of data it can hold. For example, a blob can hold a PDF document, a JPG image, a JSON file, video content, etc.

## Azure Data Storage options

**Azure SQL Database**
A relational database as a service (DaaS) based on the latest stable version of the Microsoft SQL Server database engine.

**Azure Cosmos DB**
A globally distributed database service. It supports schema-less data that lets you build highly responsive and **Always On** applications to support constantly changing data.

**Azure Blob storage**
Azure Blob Storage is unstructured, meaning that there are no restrictions on the kinds of data it can hold. Blobs are highly scalable and apps work with blobs in much the same way as they would work with files on a disk.

**Azure Data Lake Storage**
The Data Lake feature allows you to perform analytics on your data usage and prepare reports. Data Lake is a large repository that stores both structured and unstructured data. It combines the scalability and cost benefits of object storage with the reliability and performance of the Big Data file systems.

**Azure Files**
It offers fully managed file shares in the cloud that are accessible via the industry standard Server Message Block (SMB) protocol.

**Azure Queue**
Azure Queue storage is a service for storing large numbers of messages that can be accessed from anywhere in the world. It provides asynchronous message queueing for communication between application components, whether they are running in the cloud, on the desktop, on-premises, or on mobile devices.


**Disk Storage**
It provides disks for virtual machines, applications, and other services to access and use as they need.

**Storage tiers**
Azure offers three storage tiers for blob object storage:
1. **Hot storage tier**: optimized for storing data that is accessed frequently.
2. **Cool storage tier**: optimized for data that are infrequently accessed and stored for at least 30 days.
3. **Archive storage tier**: for data that are rarely accessed and stored for at least 180 days with flexible latency requirements.

**Encryption**
1. **Azure Storage Service Encryption (SSE)** for data at rest encrypts the data before storing it and decrypts the data before retrieving it. The encryption and decryption are transparent to the user.
2. **Client-side encryption** is where the data is already encrypted by the client libraries. Azure stores the data in the encrypted state at rest, which is then decrypted during retrieval.

**Replication**
Azure provides regional and geographic replications to protect your data, which is set up when you create a storage account. The replication feature ensures that your data is durable and always available.

# Azure Networking

## Using a Loosely Coupled Architecture (N-tier)

**N-tier** is an architectural pattern that can be used to build loosely coupled systems. It divides an application into two or more logical tiers. Architecturally, a higher tier can access services from a lower tier, but a lower tier should never access a higher tier.

Tiers help separate concerns and are ideally designed to be reusable. Using a tiered architecture also simplifies maintenance. Tiers can be updated or replaced independently, and new tiers can be inserted if needed.

## Virtual Network

A virtual network is a logically isolated network on Azure. It allows Azure resources to securely communicate with each other, the internet, and on-premises networks. A virtual network is scoped to a single region; however, multiple virtual networks from different regions can be connected together using virtual network peering.

Virtual networks can be segmented into one or more *subnets*. Subnets help you organize and secure your resources in discrete sections. For example, in a three-tier solution using VMs, the Web, App, and Data tiers/VMs are in the same virtual network but are in separate subnets.

Users interact with the Web tier directly, so that VM has a *public IP address* along with a *private IP address*. Users don't interact with the App or Data tiers, so these VMs each have a private IP address only.

## Network Security Group

A network security group, or NSG, allows or denies inbound network traffic to your Azure resources. Think of a network security group as a cloud-level firewall for your network.

For example, notice that the VM in the web tier allows inbound traffic on ports 22 (SSH) and 80 (HTTP). This VM's network security group allows inbound traffic over these ports from all sources. You can configure a network security group to accept traffic only from known sources, such as IP addresses that you trust.

## Azure Load Balancer

A *load balancer* distributes traffic evenly among each system in a pool. It can help you achieve both *high availability* (ability to stay up and running for a long period of time) and *resiliency* (ability to stay operational during abnormal conditions).

Azure Load Balancer supports inbound and outbound scenarios, provides low latency and high throughput, and scales up to millions of flows for all Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) applications. You can use Load Balancer with incoming internet traffic, internal traffic across Azure services, port forwarding for specific traffic, or outbound connectivity for VMs in your virtual network.

Also, there's no infrastructure or software for you to maintain. You define the forwarding rules based on the source IP and port to a set of destination IP/ports.

## Azure Application Gateway

If all your traffic is HTTP, a potentially better option is to use Azure Application Gateway, which is a load balancer designed for web applications. It uses Azure Load Balancer at the transport level (TCP) and applies sophisticated URL-based routing rules to support several advanced scenarios.

Some of the benefits of using Azure Application Gateway over a simple load balancer are: cookie affinity, SSL termination (SSL certificates management and encryption), Web application firewall (WAF), URL rule-based routes, and rewrite HTTP headers.

## Azure DNS

DNS, or Domain Name System, is a way to map user-friendly names to their IP addresses. You can think of DNS as the phonebook of the internet. You can bring your own DNS server or use Azure DNS, a hosting service for DNS domains that runs on Azure infrastructure.

## Azure Traffic Manager

Factors such as the type of connection you use and how your application is designed can affect *latency*. But perhaps the biggest factor is distance (between the application server and the client's physical location).

```
Latency refers to the time it takes for data to travel over the network and reach its destination. Bandwidth refers to the amount of data that can fit on the connection.
```

One way to reduce latency is to provide exact copies of your service in more than one region, but in this case each region will have a different DNS name. *Azure Traffic Manager*, instead, uses the DNS server that's closest to the user to direct user traffic to a globally distributed endpoint, including both Azure and on-premise deployments.

/*
# Azure Portal

## Azure Portal dashboards

A dashboard is a customizable collection of UI tiles displayed in the Azure portal. You add, remove, and position tiles to create the exact view you want, and then save that view as a dashboard. Dashboards are stored as JSON files, which you can download, edit manually and upload. You can create dashboards for specific roles within the organization, and then use role-based access control (RBAC) to control who can access that dashboard.
*/

---