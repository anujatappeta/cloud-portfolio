# AWS Full Stack Cloud Deployment Project ☁️

## Role

Built and deployed a production-style full stack cloud application demonstrating practical implementation of cloud infrastructure using core AWS services.

---

# Goal

Design and deploy a real-world cloud-native web application architecture integrating frontend hosting, content delivery network, backend server deployment, and managed relational database services.

Primary focus:

- Real cloud infrastructure deployment
- Service integration across AWS ecosystem
- Scalable application architecture
- Production-style deployment workflow
- Practical hands-on cloud engineering implementation

---

# Cloud Stack Used

Infrastructure Services:

- AWS S3
- AWS CloudFront
- AWS EC2
- AWS RDS MySQL

Development Stack:

- HTML5
- CSS3
- JavaScript
- Python
- MySQL

Deployment Tools:

- Linux
- SSH
- Git
- GitHub

---

# Live Deployment Links

## CloudFront CDN Endpoint

https://d1eftdnww0jk7u.cloudfront.net

## Amazon S3 Website Endpoint

http://anuja-portfolio-cloud.s3-website.ap-south-1.amazonaws.com/

---

# Architecture Design

```text
User Browser
      │
      ▼
AWS CloudFront CDN
      │
      ▼
Amazon S3 Static Website Hosting
      │
      ▼
Frontend Sends API Request
      │
      ▼
Amazon EC2 Backend Server
      │
      ▼
Backend Connects To Database
      │
      ▼
Amazon RDS MySQL Database
```

---

# AWS Services Implementation

## Amazon S3

Implemented:

* Created S3 bucket
* Configured static website hosting
* Uploaded frontend portfolio files
* Configured bucket access policy
* Hosted public frontend application

Purpose:

Static frontend hosting without managing servers.

---

## Amazon CloudFront

Implemented:

* Created CloudFront distribution
* Connected S3 bucket as origin
* Configured CDN content delivery
* Enabled edge caching
* Improved website global performance

Purpose:

Deliver website through AWS global edge locations with reduced latency.

---

## Amazon EC2

Implemented:

* Launched Ubuntu EC2 instance
* Connected remotely using SSH terminal
* Installed Python environment
* Deployed backend server application
* Configured API handling for form submission
* Connected backend with AWS RDS

Purpose:

Backend compute layer for processing application requests.

---

## Amazon RDS MySQL

Implemented:

* Created managed MySQL database instance
* Configured database connection from EC2 backend
* Stored user submitted contact form information
* Managed relational structured data storage

Database Schema:

```sql
CREATE TABLE contacts (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) DEFAULT NULL,
    email VARCHAR(100) DEFAULT NULL,
    message TEXT,
    PRIMARY KEY (id)
);
```

Purpose:

Persistent managed cloud database for storing application data.

---

# Application Workflow

```text
Step 1

User opens portfolio website

↓

Step 2

CloudFront receives request

↓

Step 3

CloudFront fetches frontend content from S3

↓

Step 4

Portfolio website loads frontend files

↓

Step 5

User submits contact form

↓

Step 6

Frontend sends request to backend running on EC2

↓

Step 7

Backend validates request data

↓

Step 8

Backend connects with AWS RDS MySQL

↓

Step 9

Data inserted into database successfully
```

---

# Features Implemented

* Static website hosting using AWS S3
* Global CDN acceleration using CloudFront
* Backend deployment on AWS EC2
* Secure remote server access using SSH
* Contact form API processing
* MySQL database integration using AWS RDS
* Persistent cloud database storage
* End-to-end cloud infrastructure integration

---

# Technical Skills Demonstrated

Cloud Engineering:

* AWS Infrastructure Deployment
* Cloud Resource Provisioning
* CDN Configuration
* Server Deployment
* Database Connectivity
* Distributed Cloud Architecture
* Service Integration

Backend Engineering:

* Python API Development
* Request Processing
* Database Integration

DevOps Fundamentals:

* Linux Server Management
* SSH Remote Access
* Git Version Control
* GitHub Repository Management

---

# Learning Outcomes

Successfully gained practical understanding of:

* Cloud architecture design
* Production deployment workflow
* Service-to-service communication inside AWS
* Backend and database connectivity in cloud
* Cloud resource management
* Scalable web infrastructure deployment

---

# Author

Anuja Tappeta

Aspiring Cloud Engineer | AWS

© 2026 All Rights Reserved
