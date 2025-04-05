# Pulumi Deploy Static

## License
Pulumi

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [File-structure](File-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license-1)
- [Contact](#contact)

---

## Overview
**Pulumi Deploy Static** is a project that utilizes Pulumi to provision and deploy a static website on AWS S3 while utilizing Cloudflare for domain management and CDN capabilities. 

This project demonstrates the process of building and deploying a static website using Pulumi to [AWS/Azure/Google Cloud], showcasing a seamless deployment experience with infrastructure as code and modern DevOps practices.

---

## Features
- **Infrastructure as Code**: Define your cloud resources using code with Pulumi.
- **Fast Delivery**: Serve your static content through Cloudflare’s global CDN.
- **Version Control**: Keep track of your infrastructure changes alongside your code.
- **Custom Domain**: Publish your site on a custom domain with SSL support provided by Cloudflare.

---

## Prerequisites
Before starting, ensure you have the following tools installed and set up:

- Node.js (v14.x or later)  
- Pulumi CLI (latest version)  
- AWS CLI (configured with your AWS credentials)  
- Cloudflare API Token with domain edit permissions  

---
## File-structure
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

## Installation

To get started with the project:

```bash
git clone https://github.com/onlyfave/Pulumi-deploy-static.git  
cd Pulumi-deploy-static
