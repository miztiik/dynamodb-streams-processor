# AWS Serverless CloudWatch Logs Retention Policy Enforcer

This lambda function adds a retention policy to CloudWatch log group[s] that does *not* have an retention policy. You can use the override feature to set new values on existing policies, Say for example you have decided to retain logs longer now, from 14 to 21 days.

![AWS Serverless CloudWatch Logs Retention Policy Enforcer](images/miztiik-serverless-cloudwatch-log-retention-policy.png)

#### Follow this article in [Youtube](https://youtube.com/c/valaxytechnologies)


0. # Prerequisites

- AWS CLI pre-configured
- Log Retention Days: Defaults to 14 days

1. ## Clone the repository

   ```sh
   git clone https://github.com/miztiik/serverless-cloudwatch-log-retention.git
   ```

1. ## Customize the deployment

    Edit the `./helper_scripts/deploy.sh` to update your environment variables.
  
    ```sh
    AWS_PROFILE="default"
    BUCKET_NAME="sam-templates-010" # bucket must exist in the SAME region the deployment is taking place
    TEMPLATE_NAME="serverless-cloudwatch-log-retention-policy.yaml"
    STACK_NAME="set-cloudwatch-logs-retention"
    OUTPUT_DIR="./outputs/"
    PACKAGED_OUTPUT_TEMPLATE="${OUTPUT_DIR}${STACK_NAME}-packaged-template.yaml"
    ```

    For the `RETENTION_IN_DAYS`, you can customize this in the code in `./src/cw-log-retention.py` or post deployment in the Lambda environment variable.

1. ## Deployment

    We will use the `deploy.sh` in the `helper_scripts` directory to deploy our [AWS SAM](https://github.com/awslabs/serverless-application-model) template

    ```sh
    chmod +x ./helper_scripts/deploy.sh
    ./helper_scripts/deploy.sh
    ```
  
1. ## Usage

    The function will automatically trigger once every 24 hours via a CloudWatch Event. Here is an example of the output from the Lambda function,

    ```json
    {
      "status": true,
      "logs_metadata": [
        {
          "logGroupName": "/aws/lambda/set-cloudwatch-logs-reten-CloudWatchLogRetentionFu-1SABSGG9H6XV1",
          "retentionInDays": 5,
          "region": "us-east-1"
        }
      ],
      "total_policies_set": 1
    }
    ```

### Contact Us

You can reach out to us to get more details through [here](https://youtube.com/c/valaxytechnologies/about).