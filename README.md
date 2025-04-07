# Pulumi Deploy Static
![Website](https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=https%3A%2F%2Fone-million.tech)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [File-structure](File-structure)
- [Installation-Guide](#installation-Guide)
- [Configuration](#Configuration)
- [Useful-Resources](#Useful-Resources)
- [Contributing](#contributing)
- [License](#license-1)
- [Contact](#contact)

---

## 🌐Overview
**Pulumi Deploy Static** is a project that utilizes Pulumi to provision and deploy a static website on AWS S3 while utilizing Cloudflare for domain management and CDN capabilities. 

This project demonstrates the process of building and deploying a static website using Pulumi to [AWS/Azure/Google Cloud], showcasing a seamless deployment experience with infrastructure as code and modern DevOps practices.

---

## 🧪Features
- **Hosting**: Deploy a public [AWS](https://aws.amazon.com) S3 Bucket to host a static site.
- **Infrastructure as Code**: Define your cloud resources using code with [Pulumi](https://pulumi.com).
- **Fast Delivery**: Serve your static content through Cloudflare’s global CDN.
- **Version Control**: Keep track of your infrastructure changes alongside your code with [GitHub](http://github.com).
- **Custom Domain**: Publish your site on a custom domain with SSL support provided by [Cloudflare](https://cloudflare.com).

---

## 🧰Prerequisites
Before starting, ensure you have the following tools installed and set up:
  
- ✅ Pulumi CLI installed ([Install Guide](https://www.pulumi.com/docs/get-started/install/))
- ✅ Python 3.7+
- ✅ AWS CLI configured with credentials (`aws configure`)  
- ✅ A [Cloudflare](https://cloudflare.com) account
- ✅ A simple static website (e.g., `index.html`)
- ✅ Git & GitHub account 

---

## 📁File-structure
```bash
.
├── __main__.py          # Pulumi program (Python)
├── Pulumi.yaml          # Project metadata
├── Pulumi.dev.yaml      # Stack configuration (region, bucket name, etc.)
├── static/              # Folder containing website files (HTML, CSS, JS)
│   ├── index.html
│   └── styles.css
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
```

## 🌍Configuration

This project uses **Pulumi (Python)** for Infrastructure as Code (IaC) to deploy a static website to **AWS S3** with **Cloudflare** handling DNS and HTTPS.

- An AWS account with programmatic access (Access Key ID and Secret Access Key)
- A Cloudflare account with a configured zone (domain)
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/) installed
- [Python 3.7+](https://www.python.org/downloads/)
- A Pulumi account (or self-managed backend)

### Environment Setup

1. **Install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
2. **Configure AWS credentials**

Set your AWS credentials using environment variables or your preferred method.

  ```bash
  export AWS_ACCESS_KEY_ID=your-access-key-id
  export AWS_SECRET_ACCESS_KEY=your-secret-access-key
  ```
3. **Configure Pulumi**

Log in to Pulumi:

  ```bash
  pulumi login
  ```
4. **Creat a new stack (if not already created)**
 ```bash
 pulumi stack init dev
```
5. **Set Pulumi configuration values**
```bash
pulumi config set aws:region us-east-1  # or your preferred AWS region
pulumi config set cloudflare:apiToken your-cloudflare-api-token --secret
pulumi config set cloudflare:zoneId your-cloudflare-zone-id
pulumi config set siteDomain yourdomain.com
```
6. **Deployment**
Once configured, deploy the infrastructure with:
```bash
pulumi up
```
---

## 🚀Installation-Guide

To get started with the project:
### 1. Clone the repository

```bash
git clone https://github.com/onlyfave/Pulumi-deploy-static.git  
cd Pulumi-deploy-static
```

### 2. Install Python Requirements
Create a requirements.txt:
```bash
pulumi
pulumi_aws
pulumi_cloudflare
```
### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```
### 4. Pulumi stack code(__main.py__)
````
"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import json

# Create an S3 bucket
bucket = aws.s3.BucketV2("one-million.tech")


# Disable Block Public Access to allow the policy update
block_public_access = aws.s3.BucketPublicAccessBlock(
    "blockPublicAccess",
    bucket=bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False
)
# Enable static website configuration
website_config = aws.s3.BucketWebsiteConfigurationV2(
    "websiteConfig",
    bucket=bucket.id,
    index_document={"suffix": "index.html"},
    error_document={"key": "error.html"}
)

# Upload a sample index.html file
index_html = aws.s3.BucketObject(
    "index.html",
    bucket=bucket.id,
    source=pulumi.FileAsset("index.html"),  # Ensure this file exists in your project
    content_type="text/html"
)

# Public access policy (uncomment to make it publicly accessible)
bucket_policy = aws.s3.BucketPolicy("bucket-policy",
    bucket=bucket.id,
    policy=bucket.id.apply(lambda bucket_id: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_id}/*"],
        }]
    }))
)


# Export bucket name and website URL
pulumi.export("bucket_name", bucket.id)
pulumi.export("website_url", website_config.website_endpoint)
````
### 5. Add Your Website Files
Create a directory called static/ and include   your website content:

```bash
mkdir static
/index.html

```
5. Deploy to the Cloud
```bash
pulumi up
```
  
## 📚Useful Resources
🚀 Pulumi Documentation

- [Pulumi Official Docs](https://www.pulumi.com/docs/)– Learn how to build, deploy, and manage cloud infrastructure using Pulumi.
- [Pulumi AWS Provider](https://www.pulumi.com/registry/packages/aws/api-docs/provider/) – Reference for using AWS resources with Pulumi.
- [Pulumi Cloudflare Provider](https://www.pulumi.com/registry/packages/cloudflare/) – Reference for managing Cloudflare resources using Pulumi.

☁️ AWS Resources

- Hosting a Static Website on [Amazon S3](https://aws.amazon.com/pm/serv-s3/?trk=c8974be7-bc21-436d-8108-722e8ab912e1&sc_channel=ps&ef_id=CjwKCAjwzMi_BhACEiwAX4YZUNYVvpQW0NH25CwfxUp5gLAblA2GjLsuw_uxw3UZGg9uw3121I5JxxoCS2EQAvD_BwE:G:s&s_kwcid=AL!4422!3!645125274431!e!!g!!amazon%20s3!19574556914!145779857032&gclid=CjwKCAjwzMi_BhACEiwAX4YZUNYVvpQW0NH25CwfxUp5gLAblA2GjLsuw_uxw3UZGg9uw3121I5JxxoCS2EQAvD_BwE)


🌐 Cloudflare Resources

- [Cloudflare Docs](https://developers.cloudflare.com/)
- [Using Cloudflare with S3](https://developers.cloudflare.com/workers/demos/) – Guide for serving static sites with Cloudflare and S3.

---

## 🤝Contributing

Contributions are welcome and appreciated! 🙌
 
Please review the [Code of Conduct](./CODE_OF_CONDUCT.md) and follow the [Pull Request Guidelines](.github/PULL_REQUEST_TEMPLATE.md).


If you have suggestions, bug reports, improvements, or new features you'd like to add, here's how to contribute:

1. **Fork the repository**
2. **Create a new branch**
 ```bash
 git checkout -b your-feature-name
```
3. **Make your changes**
4. **Commit your changes**
5. **Push to the forked repository**
 ```bash
 git push origin your-feature-name
```
6. **Open a Pull Request**
--- 

## 📌License
MIT License. Free to use and modify.

---

## 📬Contact
[![X](https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/only_fave)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/favour-onyeneke-2b2881297/)
[![Dev.to](https://img.shields.io/badge/Dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/onlyfave)
[![Hashnode](https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://hashnode.com/@onlyfave)


python

---

> *🏆 This project was built as part of the Pulumi Static Website Challenge — powered by Pulumi, AWS, and Cloudflare.*
