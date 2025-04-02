"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import json
import os

# Create an S3 bucket with website hosting enabled
bucket = aws.s3.BucketV2("pulumi-deploy-bucket")

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
bucket_policy = aws.s3.BucketPolicy(
    "bucketPolicy",
    bucket=bucket.id,
    policy=bucket.arn.apply(lambda arn: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"{arn}/*"
        }]
    }))
)

# Export bucket name and website URL
pulumi.export("bucket_name", bucket.id)
pulumi.export("website_url", website_config.website_endpoint)
