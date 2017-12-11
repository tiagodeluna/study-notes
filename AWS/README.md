# AWS

## Introduction

There are different Ways of make your application available:
- Private Server
    + Buying and maintaining a server requires a high cost
    + The server may not meet the demand for access required on your system after some time
- Hosting Service
    + Hiring a server also requires considerable costs and a contract
    + If there is a problem with your hosting provider's infrastructure, your application will be offline
- Make it available using Cloud Computing
    + Allows you to balance costs
    + Offers high availability and flexibility

### Cloud Computing

----------------
> "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models." (NIST - National Institute of Standards and Technology)
----------------

- Infrastructure as a Service (IaaS)
    + The provider allows allocating machines on demand, without concern with maintenance of these machines
    + The administrator needs to perform the installations/configurations (install servers, databases, configure firewall, etc.)
    + e.g. Amazon Elastic Cloud Computer (EC2), Digital Ocean
- Platform as a Service (PaaS)
    + The provider itself allocate machines, install server, configure ports, firewall and even scale.
    + e.g. Heroku, Openshift, AWS Beanstalk
- Software as a Service (SaaS)
    + Software delivered through the Cloud
    + e.g. Google Docs, Dropbox, Spotify, Relational Databases (Amazon)

### How to deal with the increase in access

- Vertical Scalability
    + Improving the CPU, HD or RAM to be able to serve more customers
    + In AWS EC2, you can change the instance to another with more processing power, but it will increase the cost per hour
    + We continue with the availability problem, because if the instance drops, the entire application goes offline
- Horizontal Scalability
    + Increase the number of machines running the application
    + It's interesting to create an instance only for the database in order to separate it from the application and then instanciate new instances running the application in parallel

## AWS Services Overview

**CloudWatch**
A tool that allows you to create **Billing Alarms** to avoid spending unexpected values while using your AWS account. CloudWatch also lets you collect and track metrics, monitor log files, and set other alert types. For example, we may be notified when the CPU is too busy for a certain time, writing or reading is slow, disk space is running out, among many other possibilities. Check the [Official Documentation](https://aws.amazon.com/pt/documentation/cloudwatch/) for more details.

**EC2**
The Amazon Elastic Cloud Computer is a service that allows you to create instances of machines from predefined images, the AMIs (Amazon Machine Images). These machines can be configured to be flexible, with resources allocated (and deallocated) on demand. The costs are proportional to the quantity of the resources allocated on the machine.
Each instance type has its own characteristics and purposes. See the [Documentation](https://aws.amazon.com/pt/ec2/instance-types/) for more details.

**Amazon RDS**

The Amazon RDS (Relational Database Service) is a SaaS-based service that provides an EC2 instance with a relational database ready to use and available on the cloud with minimum configuration.

## Amazon EC2

### Instance Creation Steps

- Choose AMI
    + There are several images from different OS/distributions: Windows, Ubuntu, Red Hat, etc.
- Choose instance type
    + The instance types are optimized to fit different use cases. They have varying combinations of CPU, memory, storage, and networking capacity.
    + The _t2.*_ instances have variable ECUs (Elastic Computer Units), while the _m2.*_ instances have fixed ECUs.
- Configure Instance
- Add storage
- Add tags
- Configure Security Group
- Review and confirm

### Managing Security Groups

When we create an instance on EC2, by default the firewall that is natively configured on it blocks all ports, as a matter of security.
The Security Groups section allows you to define specific security rules to the server. Some rules are preconfigured when the instance is created (e.g. *launch-wizard-1* contains a rule to enable access to the server via SSH using port 22).
- Inbound: in this tab, we define rules to allow traffic receipt
- Outbound: in this guide, we define rules to allow server access to external connections

## Amazon RDS

### Creation Steps

When creating a RDS instance, you can choose:
- **Engine type and version**: Amazon Aurora, MySQL, Postgresql, etc.
- **DB instance class**: the EC2 instance type.
- **Multi-AZ deployment**: creates replicas in a different Availability Zone to provide data redundancy, eliminate I/O freezez, and minimize latency spikes during system backups. Read the [documentation](https://aws.amazon.com/pt/rds/details/multi-az/) for more details.
- **Storage type**:
    + General Purpose: default. Suitable for a broad range of database workloads.
    + Provisioned IOPS: suitable for I/O-intensive database workloads.
- **Virtual Private Cloud (VPC)**: defines the virtual networking environment for the DB instance.
- **Allocated storage (in GB), Subnet, Backups, Maintenance, etc**.

### Making it Available

After the RDS instance be available, you'll need to configure its default Security Group to enable access to the machines that will connect with it (modifying the *Inbound* rule).

### Useful Commands

| Command | Description |
| ----- | ----- |
| ssh -i `.pem file` `<instance user>@<instance public DNS>` | Starts the SSH client program that enables secure connection to the SSH server on a remote machine |
| scp -i `.pem file` `file to copy` `<instance user>@<instance public DNS>`:~ | Secure Copy. Connects to the server using the SSH private key file (.pem) and copies the file which name is provided |
| mysql -u `<db user>` -p`<db password>` -h `<db public DNS (without port>` | Mysql command to connect with a remote database |