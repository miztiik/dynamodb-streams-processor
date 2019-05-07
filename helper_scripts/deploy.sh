#!/bin/bash
set -ex

#----- Change these parameters to suit your environment -----#
AWS_PROFILE="default"
BUCKET_NAME="sam-templates-011" # bucket must exist in the SAME region the deployment is taking place
TEMPLATE_NAME="dynamodb-stream-processor.yaml"
STACK_NAME="dynamodb-stream-processor"
OUTPUT_DIR="./outputs/"
PACKAGED_OUTPUT_TEMPLATE="${OUTPUT_DIR}${STACK_NAME}-packaged-template.yaml"
SERVICE_NAME="dynamodb-stream-processor"
#----- End of user parameters  -----#


# You can also change these parameters but it's not required
enableDEBUGGER="true"

# Package the code
aws cloudformation package \
    --template-file "${TEMPLATE_NAME}" \
    --s3-bucket "${BUCKET_NAME}" \
    --output-template-file "${PACKAGED_OUTPUT_TEMPLATE}"


# Cleanup Output directory
rm -rf ./outpus/*

# Deploy the stack
aws cloudformation deploy \
    --profile "${AWS_PROFILE}" \
    --template-file "${PACKAGED_OUTPUT_TEMPLATE}" \
    --stack-name "${STACK_NAME}" \
    --parameter-overrides \
        enableDEBUGGER="${enableDEBUGGER}" \
    --tags Service="${SERVICE_NAME}" \
    --capabilities CAPABILITY_IAM
