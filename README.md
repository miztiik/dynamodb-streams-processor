# AWS DynamoDB Stream Event Processor

Lets say, we have to do some action for every item added to DynamoDB. We can use _DynamoDB Streams_ along with Lambda to achieve the same.

![dynamodb-streams-processor](images/miztiik-dynamo-stream-processor.png)

#### Follow this article in [Youtube](https://youtube.com/c/valaxytechnologies)

0. ### Prerequisites

- AWS CLI pre-configured

1. ## Clone the repository

   ```sh
   git clone https://github.com/miztiik/dynamodb-streams-processor.git
   ```

1. ## Customize the deployment

    Edit the `./helper_scripts/deploy.sh` to update your environment variables.
  
    ```sh
    AWS_PROFILE="default"
    BUCKET_NAME="sam-templates-011" # bucket must exist in the SAME region the deployment is taking place
    SERVICE_NAME="dynamodb-stream-processor"
    TEMPLATE_NAME="${SERVICE_NAME}.yaml"
    STACK_NAME="${SERVICE_NAME}"
    OUTPUT_DIR="./outputs/"
    PACKAGED_OUTPUT_TEMPLATE="${OUTPUT_DIR}${STACK_NAME}-packaged-template.yaml"
    ```

1. ## Deployment

    We will use the `deploy.sh` in the `helper_scripts` directory to deploy our [AWS SAM](https://github.com/awslabs/serverless-application-model) template

    ```sh
    chmod +x ./helper_scripts/deploy.sh
    ./helper_scripts/deploy.sh
    ```
  
1. ## Test Stream Processor

    Insert a simple item to the table, either from the GUI/CLI

    ```json
    ddb_name="dynamodb-stream-processor-DynamoDBTable-N8Z22Q0GILUH"
    for i in {1..10}
     do
      val=${RANDOM}
      aws dynamodb put-item \
        --table-name "${ddb_name}" \
        --item '{ "Username": {"S":"User_'${i}'"},"Timestamp": {"S":"'$(date +"%d/%m/%Y-%H:%M:%S")'"},"Message":{"S":"Mystique_Msg_'${val}'"} }'
     done
    ```

### Contact Us

You can reach out to us to get more details through [here](https://youtube.com/c/valaxytechnologies/about).