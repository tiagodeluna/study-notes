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

**API Gateway**

Amazon API Gateway is a fully-managed service that allows you to create and maintain your own APIs for your application. It acts as a "front-door" for your application, allowing access to data/logic/functionality from your back-end services.

API Gateway uses Stages, that are snapshots of your API (e.g. dev, prod, beta...) containing specific settings - it stores configuration for deployments.

There are also Gateway Methods that are associated with an API Gateway Resource. They include the allowed HTTP methods (DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT) and the AWS-provided ANY method as a catch-all. API Gateway methods can be configured to respond to requests to AWS Lambda functions, integrated with other AWS Services, and to existing HTTP endpoints.

**Aurora**

Amazon Aurora is a MySQL database engine that combine the speed and availability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. It offers aproximately 5 times the performance of MySQL. You use Amazon Aurora by selecting it when creating a RDS instance. 

**Auto Scaling**

The Auto Scaling Service allows you to automatically create and delete instances as needed to optimize resource usage, following predetermined scaling policies.

**CodeDeploy**

CodeDeploy is a deployment service that enables developers to perform *Blue Green Deployments* automatically, implementing the *Immutable servers* concept. Check the [documentation](https://aws.amazon.com/pt/documentation/codedeploy/) for more details.

**CloudFormation**

CloudFormation is the pure embodiment of infrastructure as code, because you can describe your application's architecture in a CloudFormation template as either JSON or YAML. It makes possible to, for example, version control your infrastructure, and reuse the same template to deploy copies of that architecture to other AWS regions or accounts.

A Cloudformation Stack is a group of AWS resources that you can manage together, as they are treated as one single unit. If the creation of one resource fails, the default behavior is a *RollBack* in the whole Stack.

CloudFormation provides built-in *Intrinsic Functions* that can be used in the template to assign values to different properties that are only available at or after runtime (e.g Fn::GetAtt, Fn::Join, Ref...). You can also use API calls to interact with CloudFormation to retrieve information, e.g. *ListStackResources* (to list all resources that belong to a Stack) and *DescribeStacks* (that returns descriptions of a list of all current Stacks), as well as AWS CLI commands, such as `aws cloudformation describe-stacks`.

**CloudWatch**

Amazon CloudWatch is a tool used to monitor AWS services, such as EC2, ELB and S3. It lets you collect and track metrics, monitor log files, and set other alert types. For example, we may be notified when the CPU is too busy for a certain time, writing or reading is slow, disk space is running out, among many other possibilities. CloudWatch also allows you to create **Billing Alarms** to avoid spending unexpected values while using your AWS account. Check the [documentation](https://aws.amazon.com/pt/documentation/cloudwatch/) for more details.

**DynamoDB**

Amazon DynamoDB provides **NoSQL** database **tables** as a service, with unlimited number of items per table, low-latency queries and scalable read/write throughput. Amazon DynamoDB is a good fit for structured data from the Web, Mobile and Internet of Things Apps, as well as Ad Tech and Gaming.

DynamoDB stores data in partitions. Partitions are SSD allocations of storage for the table and automatically replicated accross multiple AZs. 

Primary key:

Primary key attributes must have the data type of string, number, or binary. There are two types of primary key:
* Simple PK: partition key only. In this model, no two items can have the same partition key.
* Composite PK: partition key + sort key. Items must have a unique combination of partition key and sort key.

Partition keys:

Every DynamoDB table requires a partition key -- also known as **hash attribute**. DynamoDB uses partition keys in an internal hash function to determine where the partition data will be stored.

Sort keys:

After DynamoDB uses the partition key to determine the partition data will be stored in, the sort key -- or **range attribute** -- is used to sort the data inside of that partition.

Indexes:

DynamoDB has two types of indexes:
* *Local secondary indexes* must have the same partition key and the same hash key as the table. They also must be created at the same time as the table itself. The point is that it has a different range key. Every partition of the index is scoped to a table partition with the same hash key.
* A *Global secondary index* is an index with: a hash and range key. The hash and range key can be different from what's on the table. It is thought of as "global" because queries on the index can span all of the table data across partitions.

Queries:

In DynamoDB, a query efficiently searches using the partition key and an optional sort key. You have to supply a partition key when creating a query in DynamoDB. A query returns only the items matching the primary key. By default, a query is an *eventually consistent read* only. You have to explicitly request it to be a *strongly consistent read*.

As the read (and write) throughput in DynamoDB is scalable and charged accordingly, it is important to determine beforehand how much read capacity throughput you should provision to your table. It can be done by using the formula: `( N x (S/K))`, where `N` is the number of items you want to read per second, `S` is the item size (in KB) and `K` is the throughput capacity size per read capacity unit (RCU), which is 4KB. For *eventually consistent reads*, which require half the throughput necessary for *strongly consistent reads*, divide the result by 2.

Other important facts about DynamoDB:
* The limit of tables an AWS account can have per region is 256. You can increase DynamoDB table limit by contacting AWS and requesting a limit increase.
* You can define up to 5 *local secondary indexes* and 20 *global secondary indexes* per table (by default), i.e 25 in total.
* One *read capacity unit* (RCU) represents one strongly consistent read per second, or two eventually consistent reads per second, for an item up to 4 KB in size.
* One *write capacity unit* (WCU) represents one write per second for an item up to 1 KB in size.

**Elastic Beanstalk**

Elastic Beanstalk is designed to make it easy to deploy and scale less complex (single-tier) applications. It takes advantage of core services such as EC2, Auto Scaling, ELB, RDS, SQL and CloudFront, to help reduce the management required for provisioning applications.

When using Elastic Beanstalk you will have to pay for only the costs of resources deployed by Elastic Beanstalk. The following platforms are supported: Docker, Packer, Java, Windows .NET, Node.js, PHP, Python, Ruby and Go.

You can deploy your web applications by configuring a git repository with Elastic Beanstalk – so that changes will be detected and your application will be updated –, or uploading code files to the Elastic Beanstalk service.

**EBS**

Elastic Block Device is where instances save their data (like an HD). It is a feature that guarantees high availability because it automatically replicates your instance data within the same Availability Zone.

We can associate an EBS volume from an instance to another (but only an instance at a time), or create a new EBS volume separately and associate with an instance later.

**EC2**

The Amazon Elastic Cloud Computer is a service that allows you to create instances of machines from predefined images, the AMIs (Amazon Machine Images). These machines can be configured to be flexible, with resources allocated (and deallocated) on demand. The costs are proportional to the quantity of the resources allocated on the machine.
Each instance type has its own characteristics and purposes. See the [Documentation](https://aws.amazon.com/pt/ec2/instance-types/) for more details.

EC2 instances are launched from Amazon Machine Images (AMIs). Public AMIs can only be used to launch EC2 instances in the same AWS region as the AMI is stored.

Regarding data storage, there are two types of EC2 images:

* Amazon EBS-backed: instances of this type of image can be stopped and restarted without losing data.
* instance-store backed: images use "ephemeral" storage (temporary). The storage is only available during the life of an instance. Rebooting an instance will allow ephemeral data stay persistent. However, stopping and starting an instance will remove all ephemeral storage.

**ECS**

Elastic Container Service is a container management service that supports Docker. It allows you to easily create and manage a fleet of Docker containers on a cluster of EC2 instances. It uses **Fargate**, an AWS service that allows you to use containers as the fundamental building blocks of your application while AWS manages the EC2 instances for you.

The containers can be created from images stored in a container registry located on AWS via the ECR service (Elastic Container Registry), a 3rd-party repository like DockerHub or a self-hosted registry.

**ElastiCache**

ElastiCache is a fully managed, in-memory cache engine used to improve database performance by caching results of queries that are made to a database. It is great for large, high-performance or high-taxing queries - and can store them inside of a cache cluster that can be accessed later.

Available engines to power ElastiCache are **Memcached** and **Redis**. Some of the caching strategies that can be used in ElastiCache are:
* *Lazy Loading*: you write data to the cache only when a cache miss occurs.
* *Write Through*: the cache is updated whenever a new write or update is made to the underlying database.
* *Adding Time To Live (TTL)*: a TTL is the length of time before a key expires. It can be used together with Lazy Loading or Write Through techniques to avoid its drawbacks.

**IAM**

Identity and Access Management is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

**Load Balancer**

A Load Balancer divides traffic between network interfaces on a network socket basis, improving the distribution of workloads across multiple computing resources.

The Amazon *Elastic Load Balancing* is a solution that aims to optimize resource use, maximize throughput, minimize response time, and avoid overload of any single resource. It supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers.

**RDS**

The Amazon RDS (Relational Database Service) is a SaaS-based service that provides an EC2 instance with a relational database ready to use and available on the cloud with minimum configuration.

RDS provides *read replicas* that allows you to creates elasticity by adding/removing replicas based on demand, and improves performance of the primary database by taking workload from it.

The DB Engines currently supported by RDS are: MySQL, Amazon Aurora, MS SQL Server, PostgreSQL, MariaDB and Oracle DB.

**Redshift**

Amazon Redshift is a fast fully-managed petabyte-scale data warehousing service, generally used for BigData analytics. It is compatible with the tools we already know and use, supporting standard SQL, JDBC and ODBC connectors and business inteligence tools (e.g Jaspersoft, Microstrategy, Cognos...).

**S3**

The Amazon S3 (Simple Cloud Storage Service) is a highly-scalable cloud object storage that provides a way to store and retrieve data on the web. To upload your data (photos, videos, documents etc.), you create a *bucket* in one of the AWS Regions that will serve as a container to your objects.

Objects stay within an AWS region and are synced across all AZ's for extremely high availability and durability.

With Amazon S3, you can store virtually unlimited number of objects with a rich security control, and access them any time, from anywhere. Common use cases of S3 include: Storing application assets, static web hosting, backup & disaster recovery, staging area for Big Data, and many more...

**SNS**

Simple Notification Service is a Pub/Sub service for messaging and mobile notifications. SNS allows you to fan-out messages to a large number of subscribers and makes it easier to send push notifications and SMS to a variety of devices.

The two main benefits of using SNS are that it's scalable and highly reliable, and it's usable through the AWS Console, APIs, CLI and multiple SDKs.

SNS has Access Control Policies that grant access to your SNS topics to other AWS accounts and to some AWS services. You can use IAM Policies and Access Control Policies at the same time.

The three main components when working with SNS are:
* Topic: the group of subscriptions that you send a message to.
* Subscription: an endpoint that a message is sent to, which may include: HTTP, HTTPS, Email, Email-JSON, SQS, mobile apps (IOS/Android/Amazon/Microsoft), Lambda and SMS
* Publisher: the "entity" that triggers the sending of a message. Examples include: AWS CLI, SDKs (e.g. boto3) and services (e.g S3 events, Cloudwatch alarms, code in Lambda).

**SQS**

Simple Queue Service provides the ability to have hosted/highly available queues that can be used to send and receive messages between producers and consumers, allowing for the creation of distributed/decoupled components. Messages between servers are retrieved through *polling*.

There are two types of polling:
* Long polling (1-20 seconds): Reduces API requests by allowing the SQS service to wait until a message is available in a queue before sending a response.
* Short polling: queries a subset of the SQS servers to determine if there are messages available for a response -- not necessarily sending all possible messages in a poll. It increases API requestes, which increases costs.

Other important SQS facts:
* Each SQL Message can contain up to 256KB of text (in any format).
* In order to send more than 256KB, a possible solution is to store the data in S3 or DynamoDB and attach message instructions to the message for the worker to retrieve the data.
* Amazon SQS offer two different types of queues:
    - Standard Queues: message order can be indeterminate and messages can be delivered one or more times.
    - FIFO Queues: messages will be delivered exactly once and in First in, First out order.

**SSM Parameter Store**

The Parameter Store – available inside the Systems Manager (SSM) section – allows you to centralize your operational data and automate tasks in AWS, providing secure storage for configuration and secrets such as passwords, database strings, API keys, and license codes.

You can make use of API Actions – through AWS Console, AWS SDKs, or the AWS CLI – to access and manipulate the parameter store. Some como API actions:
* PutParameter: adds a parameter to Parameter Store, either a String, StringList or SecureString (KMS-encrypted).
* GetParameter: returns a parameter from SSM either encrypted or decrypted.
* DeleteParameter: deletes a parameter from SSM.

**Step Functions**

AWS Step Functions lets you coordinate multiple AWS services into serverless workflows. Using Step Functions, you can design and run visual workflows that stitch together services such as AWS Lambda and Amazon ECS into feature-rich applications.

Workflows are made up of a series of steps defined via JSON, with the output of one step acting as input into the next. It translates your workflow into a state machine diagram that is easy to understand, easy to explain to others, and easy to change.

**Trusted Advisor**

Trusted Advisor provides best practices and checks if all services in your account are in accordance to that practices. It checks the best practices in four categories: Cost Optimization, Performance, Security and Fault Tolerance.

**VPC**

Virtual Private Cloud (VPC) enables you to launch AWS resources into a virtual network that you've defined. A VPC is designed to resemble private on-premise data centers or private corporate networks, with the benefits of using the scalable infrastructure of AWS.

A VPC is housed within a chosen AWS region, and spans multiple availability zones within a region. AWS provides a DNS server for your VPC so each instance has a hostname. It's possible to configure and attach a Internet Gateway to allow communication between instances in your VPC and the internet.

The security of VPC is performed by two services:
* Network Access Control Lists (ACLs): operate at the network/subnet level. Defines a list of rules to allow/deny traffic. These rules are applied in number order and are **stateless**: so return traffic must be allowed through an outbound rule.
* Security Groups: operate at the instance level. They support only "allow" rules and are **stateful**: so return traffic requests are allowed regardless of rules.


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

### Dealing with Session State

When dealing with session state in EC2-based applications using Elastic Load Balancers, the best practice for managing user sessions is:
1. Having the ELB distribute traffic to all EC2 instances and then...
2. Having the instance check a caching solution like ElastiCache running Redis or Memcached for session information.

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
    + Operates at the request level, with focus on HTTP/HTTPS connections.
    + Indicated when you need a flexible feature set for your web applications with HTTP and HTTPS traffic
- Network Load Balancers:
    + Operates at the connection level, it is focused on TCP connections.
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

To solve this problem in AWS, we use a strategy called **Sticky Session** (also known as **Session Affinity**), in which the load balancer itself creates an additional cookie on the first access and causes the browser to always make requests for the same instance.

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

When you stop an instance generated by the Auto Scaling service, and it reaches the minimum size configured, another instance is automatically created. To effectivelly turn off the Auto Scaling feature without deleting all configuration, you can just set the minimum, maximum and desired number of machines to **0**.

## AWS CLI

### Configuring CLI Access

**Creating IAM User:**

To use the AWS CLI console, you must be authenticated with an access key and an access secret (similar to a login and password).

To do so, navigate to AWS IAM service, click "Users" link in the "IAM Resources" section, then click "Add User" button:
- **Details:** define a name and check the access type "Programmatic access"
- **Permissions:** click "Attach existing policies directly" option, then select the policy "AmazonEC2FullAccess"

**Configuring CLI:**

At the console on your machine, type the `aws configure` command and set properties as follows:
- **AWS Access Key ID and AWS Secret Access Key:** from your configured IAM user.
- **Default region name:** your selected region (e.g. "us-east-1")
- **Default output format:** json

### Creating EC2 Instances

Run `aws ec2 run-instances` command, providing the AMI image ID, the number of instances, the instance type, the .pem filename and the security groups. The command should look like:

`aws ec2 run-instances --image-id ami-2c076c56 --count 1 --instance-type t2.micro --key-name "luna-application.pem" --security-groups launch-wizard-1`

### Creating and Configuring Load Balancers

Run `aws elb create-load-balancer` command to create a new load balancer. The command should look like:

`aws elb create-load-balancer --load-balancer-name "aws-cli-lb" --listeners "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=8080" --availability-zones us-east-1a us-east-1b`

After executed, the command returns the DNS name for the load balancer. Now you need to configure the load balancer to manage your instances. You can do this with command:

`aws elb register-instances-with-load-balancer --load-balancer-name "aws-cli-lb" --instances i-04ff5990be5b83773 i-00c6924238d4053b5`

**Applying Sticky Session resource to a load balancer:**

As we saw earlier it is necessary to use some strategy to keep the user session active when using a load balancer. Configuring a load balancer to use Sticky Session through CLI is quite simple. The first step is to create a *cookie stickiness* policy:

`aws elb create-lb-cookie-stickiness-policy --load-balancer-name "aws-cli-lb" --policy-name "aws-cli-csp" --cookie-expiration-period 60`

Now associate this policy to the balancer with:

`aws elb set-load-balancer-policies-of-listener --load-balancer-name "aws-cli-lb" --load-balancer-port 80 --policy-names "aws-cli-csp"`

## AWS S3

### Access granting

Both ACLs and Bucket Policies can be used to grant access to S3 buckets. Bucket Policies are written in JSON and are only attached to S3 buckets. ACLs are written in XML and ACLs can be attached to S3 objects or S3 Buckets

Example of a Bucket Policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::[bucket name]",
                "arn:aws:s3:::[bucket name]/*"
            ]
        }
    ]
}
```

### Multipart Upload API

In S3, to upload large objects (bigger than that), it is necessary to use the Multipart Upload API. The Multipart upload API enables you to upload new large objects or make a copy of an existing object in parts. [Read more...](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html)

### Reading Performance

When you have significantly high numbers of GET requests there are two measures to improve S3 performance: 
* Setup CloudFront for S3 objects
* Introduce random prefixes to S3 objects: The first few characters of S3 objects are used to determine the allocation of object keys behind the scenes to S3 partitions.

### Versioning and Lifecycle policies

Use versioning to keep multiple versions of an object in one bucket. You can enable versioning either when you create a new bucket or edit an existing bucket. But once enabled, you cannot disable this feature, just suspend it.

Everytime you upload a new version of a file, a new version ID is created. Files uploaded before versioning is enabled have a null version ID. When you DELETE an object, all versions remain in the bucket and Amazon S3 inserts a delete marker, that becomes the current version of the object. So you still can GET a noncurrent version of a "deleted" object by specifying its version ID. [Read more...](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectVersioning.html)


## Useful Commands

### Server Admin

| Command | Description |
| ----- | ----- |
| `ssh -i <.pem file> <instance user>@<instance public DNS>` | Starts the SSH client program that enables secure connection to the SSH server on a remote machine |
| `scp -i <.pem file> <file to copy> <instance user>@<instance public DNS>:~` | Secure Copy. Connects to the server using the SSH private key file (.pem) and copies the file which name is provided |
| `mysql -u <db user> -p<db password> -h <db public DNS (without port)>` | Mysql command to connect with a remote database |
| `sudo tcpdump 'dst port 8080 and tcp[32:4] = 0x47455420'` | Listen to the requests made to an instance |
| `sudo systemctl enable tomcat8` | Enable tomcat8 service to start automatically when the machine is initialized |

### AWS CLI

| Command | Description |
| ----- | ----- |
| `aws configure` | Define AWS CLI configuration |
| `aws ec2 run-instances --image-id <image id> --count <number of instances> --instance-type <type> --key-name <.pem filename> --security-groups <security group>` | Generate new EC2 instances |
| `aws elb create-load-balancer --load-balancer-name <name> --listeners "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=8080" --availability-zones <at least two zones>` | Create a Elastic Load Balancer |
| `aws elb register-instances-with-load-balancer --load-balancer-name <name> --instances <instances ids>` | Register instances to be managed by a laod balancer |
| `aws elb create-lb-cookie-stickiness-policy --load-balancer-name <lb name> --policy-name <policy name> --cookie-expiration-period <seconds>` | Create a cookie stickiness policy |
| `aws elb set-load-balancer-policies-of-listener --load-balancer-name "aws-cli-lb" --load-balancer-port 80 --policy-names "aws-cli-csp"` | Apply a cookie stickiness policy to a load balancer |
| `aws s3 sync [local folder] s3://[bucket name]` | Upload files from a local folder to a specified S3 bucket. You can use this command as your deploy script in a React project, for example, to send the output source to the cloud |

## Structure Reminder

| Item | Path | Note |
| ----- | ----- | ----- |
| Tomcat8 Environment configuration | `/usr/share/tomcat8/bin/` | Create/Edit the setenv.sh file to set a environment variable |
| Tomcat8 Logs folder | `/var/lib/tomcat8/logs` | |


