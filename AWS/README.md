# AWS

## Introduction

There are different ways of make your application available:
- Private Server
    + Buying and maintaining a server requires a high cost
    + The server may not meet the demand for access required on your system after some time
- Hosting Service
    + Hiring a server also requires considerable costs and a contract
    + If there is a problem with your hosting provider's infrastructure, your application will be offline
- Cloud Computing
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

**AWS CLI**

The AWS CLI (Command Line Interface) is a tool for managing your AWS services using command line. It allows you, for example, to automatize the creation and configuration of your EC2 instances via scripts. Check the [documentation](https://aws.amazon.com/pt/cli/) for more details.

**Auto Scaling**

The Auto Scaling Service allows you to automatically create and delete instances as needed to optimize resource usage, following predetermined scaling policies.

**CodeDeploy**

CodeDeploy is a deployment service that enables developers to perform *Blue Green Deployments* automatically, implementing the *Immutable servers* concept. Check the [documentation](https://aws.amazon.com/pt/documentation/codedeploy/) for more details.

**CloudWatch**

A tool that allows you to create **Billing Alarms** to avoid spending unexpected values while using your AWS account. CloudWatch also lets you collect and track metrics, monitor log files, and set other alert types. For example, we may be notified when the CPU is too busy for a certain time, writing or reading is slow, disk space is running out, among many other possibilities. Check the [documentation](https://aws.amazon.com/pt/documentation/cloudwatch/) for more details.

**EBS**

Elastic Block Device is where instances save their data (like an HD). It is a feature that guarantees high availability because it automatically replicates your instance data within the same Availability Zone.

We can associate an EBS volume from an instance to another (but only an instance at a time), or create a new EBS volume separately and associate with an instance later.

**EC2**

The Amazon Elastic Cloud Computer is a service that allows you to create instances of machines from predefined images, the AMIs (Amazon Machine Images). These machines can be configured to be flexible, with resources allocated (and deallocated) on demand. The costs are proportional to the quantity of the resources allocated on the machine.
Each instance type has its own characteristics and purposes. See the [Documentation](https://aws.amazon.com/pt/ec2/instance-types/) for more details.

**Load Balancer**

A Load Balancer divides traffic between network interfaces on a network socket basis, improving the distribution of workloads across multiple computing resources.

The Amazon *Elastic Load Balancing* is a solution that aims to optimize resource use, maximize throughput, minimize response time, and avoid overload of any single resource. It supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers.

**RDS**

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

### Creating and Using AMIs

An AMI is a *server template* that has information about the operating system (and other software), permissions (associated account), and the *block device* mapping. The block device is like an HD that is available for an instance.

To create an AMI from an instance that is already configured, you just need to right-click the chosen instance and select *Image > Create Image*. When creating a new EC2 instance, select the image you've created on the left side menu item "My AMIs". Choose the same .pem file for the new instance.

To avoid managing multiple Security Groups for equal instances, you can set the same Security Group to the new one. Right-click your instance and select *Networking > Change Security Groups*.

## Amazon RDS

### Creation Steps

When creating a RDS instance, you can choose:
- **Engine type and version**: Amazon Aurora, MySQL, Postgresql, etc.
- **DB instance class**: the EC2 instance type.
- **Multi-AZ deployment**: creates replicas in a different Availability Zone to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups. Read the [documentation](https://aws.amazon.com/pt/rds/details/multi-az/) for more details.
- **Storage type**:
    + General Purpose: default. Suitable for a broad range of database workloads.
    + Provisioned IOPS: suitable for I/O-intensive database workloads.
- **Virtual Private Cloud (VPC)**: defines the virtual networking environment for the DB instance.
- **Allocated storage (in GB), Subnet, Backups, Maintenance, etc**.

### Making it Available

After the RDS instance be available, you'll need to configure its default Security Group to enable access to the machines that will connect with it (modifying the *Inbound* rule).

### Using a new Elastic Block Device

- Create a new EBS volume: go to the menu Elastic Block Store -> Volumes and press the button *Create Volume*.
- Attach it to an instance: Right-click on the volume and "Attach Volume".
- Format and mount the new volume:
    + Discover the real name on the kernel, typing command `sudo fdisk -l`. It'll be something like "/dev/xvdf".
    + Format volume: `sudo mkfs -t ext3 <volume name>`
    + Create a directory to mount the volume: `sudo mkdir /dev/ebs`
    + Mount volume using `sudo mount <volume name> <directory>`. e.g. `sudo mount /dev/xvdf /dev/ebs/`
    + Check if is listed within the available disks: `df -h`

## Elastic Load Balancing

The Amazon *Elastic Load Balancing* supports three types of load balancers:

- Application Load Balancers:
    + Operates at the request level
    + Indicated when you need a flexible feature set for your web applications with HTTP and HTTPS traffic
- Network Load Balancers:
    + Operates at the connection level
    + Indicated when you need ultra-high performance and static IP addresses for your application
- Classic Load Balancers:
    + Indicated when you have an existing application running in the EC2-Classic network

### Classic Load Balancer

This is the most basic implementation of a load balancer. The CLB just delegates to an instance requests received from a specific port and protocol. It has some limitations. For example, it's not possible to manage different versions of an application using different paths.

**Creation steps:**

- **Define Load Balancer:**
    + Define a listener from load balancer protocol/port `HTTP/80` to the instance's `HTTP/8080`
    + Enable advanced VPC (Virtual Private Cloud) configuration: to provide higher availability by selecting multiple subnets for your Availability Zones
    + Select Subnets according to your instances' Availability Zones
- **Assign Security Groups:** Create a new Security Group to your load balancer (or use an existent if you already have) enabling access to port `80` from `Anywhere`.
- **Configure Health Check:** Choose a path where your load balancer can perform a request to check availability. e.g. `Ping Protocol: HTTP | Ping Port: 8080 | Ping Path: /index.html`
- **Add EC2 Instances**

### Application Load Balancer

This implementation works on the application layer, so it provides more resources at HTTP level. The ALB can perform routing based on the application path.

**Creation steps:**

The creation steps are quite similar to Classic Load Balancer's, excepting the Configure Routing and Register Targets steps.

- **Configure Routing:**
    + Target group: `Protocol: HTTP | Port: 8080 | Target type: instance`
    + Health check: `Protocol: HTTP | Path: /index.html` (or other available path)
    + Advanced health check settings - Success codes: The HTTP codes to use when checking for a successful response from a target.
- **Register Targets:** select the instances that will be part of the default target group configured on the previous step. Other target groups can be defined later through the `LOAD BALANCING > Target Groups` menu.

**How to configure different paths:**

In order to manage different versions of an application or different paths, it's necessary to create specific listener rules:
- Select load balancer, go to Listener tab and click the "View/Edit rule" link in the default rule.
- Click "Add Rules" (+) button and then "Insert rule"
- Define a rule by Host (or sub-domain) or Path. For example: `IF path-pattern: <path> | THEN forward: <target group>`
    + Usually include an "*" at the end of the path to consider all pages within that path

### See Load Balancer in action

To check if your load balancer is working, access your instances and listen to the external requests, using the following command:
`sudo tcpdump 'dst port 8080 and tcp[32:4] = 0x47455420'`

### Authentication with Load Balancer

In an application with a newly configured load balancer, the login does not work. This is because as the load balancer redirects the request to different machines, the application understands that it is always a new request and then it deletes the cookie and generates a new session ID.

To solve this problem in AWS, we use a strategy called **Stick Session** (also known as **Session Affinity**), in which the load balancer itself creates an additional cookie on the first access and causes the browser to always make requests for the same instance.

To active this resource in AWS in each Target Group:
- Go to Description tab and click the "Edit Attributes" button
- Change value of property "Stickiness" to "Enable load balancer generated cookie stickiness"
    + Set stickiness duration: Provide a cookie expiration interval. Default value is `1 day`

## Auto Scaling

### Creation steps

To use the Auto Scaling service, select "Auto Scaling Groups" in the left menu, then click "Create Auto Scaling Group" button and follow the creation steps:
- **Create lauch configuration:** The steps are quite similar to the EC2 instance creation steps. The launch configuration serves as a template for the instances managed by the Auto Scaling Group.
- **Configure Auto Scaling Group:**
    + Subnets: Select at least two subnets
    + Load Balancing: check "Receive traffic from one or more load balancers"
    + Target Groups: select target group(s) to scale
- **Configure scaling policies:** choose one of the two options...
    + *Keep this group at its initial size:* to maintain a fixed number of active instances
    + *Use scaling policies to adjust the capacity of this group:* to scale between a minimum and a maximum size, according to the policies defined. You'll need to setup alarms to increase and decrease the group size.
    
### Turning off Auto Scaling

When you stop an instance generated by the Auto Scaling service, and it reaches the minimum size configured, another instance is automatically created. To effectivelly turn off the Auto Scaling feature without deleting all the configuration, you can just set the minimum, maximum and desired number of machines to **0**.

## Useful Commands

| Command | Description |
| ----- | ----- |
| ssh -i `.pem file` `<instance user>@<instance public DNS>` | Starts the SSH client program that enables secure connection to the SSH server on a remote machine |
| scp -i `.pem file` `file to copy` `<instance user>@<instance public DNS>`:~ | Secure Copy. Connects to the server using the SSH private key file (.pem) and copies the file which name is provided |
| mysql -u `<db user>` -p`<db password>` -h `<db public DNS (without port>` | Mysql command to connect with a remote database |
| `sudo tcpdump 'dst port 8080 and tcp[32:4] = 0x47455420'` | Listen to the requests made to an instance |

## Structure Reminder

| Item | Path | Note |
| ----- | ----- | ----- |
| Tomcat8 Environment configuration | `/usr/share/tomcat8/bin/` | Create/Edit the setenv.sh file to set a environment variable |
| Tomcat8 Logs folder | `/var/lib/tomcat8/logs` | |

