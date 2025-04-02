"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# Create an S3 bucket
bucket = aws.s3.BucketV2("pulumi-deploy-bucket")

# Disable public access blocking
public_access_block = aws.s3.BucketPublicAccessBlock(
    "public-access-block",
    bucket=bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False
)

# Create an S3 Bucket Policy to allow CloudFront access
bucket_policy = aws.s3.BucketPolicy(
    "bucketPolicy",
    bucket=bucket.id,
    policy=pulumi.Output.all(bucket.id).apply(lambda bucket_name: f"""{{
      "Version": "2012-10-17",
      "Statement": [
        {{
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::{bucket_name}/*"
        }}
      ]
    }}"""),
    opts=pulumi.ResourceOptions(depends_on=[public_access_block])
)

# Create an AWS CloudFront Origin Access Control (OAC)
oac = aws.cloudfront.OriginAccessControl(
    "oac",
    name="PulumiCloudFrontOAC",
    description="OAC for S3 Bucket",
    origin_access_control_origin_type="s3",
    signing_behavior="always",
    signing_protocol="sigv4"
)

# Create a CloudFront distribution
cdn = aws.cloudfront.Distribution(
    "pulumi-cloudfront",
    origins=[{
        "domain_name": bucket.bucket_regional_domain_name,
        "origin_id": bucket.id,
        "origin_access_control_id": oac.id
    }],
    enabled=True,
    default_root_object="index.html",
    default_cache_behavior={
        "target_origin_id": bucket.id,
        "viewer_protocol_policy": "redirect-to-https",
        "allowed_methods": ["GET", "HEAD"],
        "cached_methods": ["GET", "HEAD"],
        "forwarded_values": {
            "query_string": False,
            "cookies": {"forward": "none"},
        },
        "default_ttl": 3600,
        "max_ttl": 86400,
        "min_ttl": 0,
    },
    viewer_certificate={
        "cloudfront_default_certificate": True
    },
    restrictions={
        "geo_restriction": {
            "restriction_type": "none",
        }
    }
)

# Export CloudFront URL
pulumi.export("bucket_name", bucket.id)
pulumi.export("cloudfront_url", cdn.domain_name)

