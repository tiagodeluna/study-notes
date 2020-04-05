# AZ-900 AZURE FUNDAMENTALS PREPARATION COURSE

# Cloud Computing

Cloud computing is renting resources on another company (a *cloudy provider*) in a "pay only for what you use" model.

Typically, the computing services offered by a cloud provider are:
* **Compute power** - such as Linux servers or web applications, usually in the form of a *virtual machine*, a *container* or as *serverless computing*. You can have a VM in minutes at less cost than a physical computer.
* **Storage** - such as files and databases. The advantage to using cloud-based data storage is you can scale to meet your needs.
* **Networking** - secure connections
* **Analytics** - visualizing telemetry and performance data.

## Benefits of Cloud Computing

* **It's cost effective**: Cloud computing provides a pay-as-you-go or consumption-based pricing model.
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
