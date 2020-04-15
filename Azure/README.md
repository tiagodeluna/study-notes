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

# Azure subscription

An Azure subscription is a logical container used to provision resources in Azure. It holds the details of all your resources like virtual machines (VMs), databases, and more.

It is possible to create additional subscriptions to separate: Environments (e.g development, testing, security), Organizational structures (e.g team, department, project), and Billing (e.g production workloads, development and testing workloads).

If you have multiple subscriptions, you can organize them into invoice sections. You can also set up multiple invoices within the same billing account, by creating additional billing profiles. Each billing profile has its own monthly invoice and payment method.

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

# Basic concepts for creating websites hosted in Azure

Let's review some basic terms required if you want to have a website up and running in Azure:

## What is an App Service?

Azure App Service is an HTTP-based service that enables you to build and host many types of web-based solutions (including web apps, mobile back ends, and RESTful APIs) without managing infrastructure. Applications developed in .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python can run in and scale with ease on both Windows and Linux-based environments.

## App Service Plans

When you create an application using App Service or want to *scale up* an existing application, you have to select an App Service plan. There are three categories to make it easier to decide the type of workload (plan) you need:

* **Dev/Test:** ideal for less demanding workloads and focused on providing shared infrastructure. In this category, you have additional features that become available to the App Service application. e.g. Custom domains/SSL and manual scale.
* **Production:** ideal for more demanding workloads. In this category there are added features such as staging slots, daily backups, and a traffic manager.
* **Isolated**: ideal for workloads that require advanced networking and fine-grained scaling.

Within each category, there are pricing tiers that will allow you to scale the resources available and give you access to additional features.

## What is the Microsoft Azure Marketplace?

The Microsoft Azure Marketplace is an online store that hosts applications that are certified and optimized to run in Azure.

## Resource Groups in Azure

Typically, the first for hosting a web application in Azure is to create a resource group to hold all the things needed. The resource group allows us to administer all the services, disks, network interfaces, and other elements that potentially make up our solution as a unit. Resource groups can be created and managed via Azure portal or via command line using the *Azure CLI*.

Unused resources left running still can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.

## What is Azure Cloud Shell?

A browser-based command-line console for managing and developing Azure resources. Cloud Shell provides two experiences to choose from, Bash and PowerShell. Both include access to the Azure command-line interface called *Azure CLI* and to *Azure PowerShell*.

In this exercise, you'll use the Cloud Shell window shown side by side with the exercise instructions. When normally accessing the Cloud Shell from within the Azure portal, you'll click the Cloud Shell icon from the top navigation bar. This icon is sometimes within the ellipsis (...) menu icon next to your profile.



