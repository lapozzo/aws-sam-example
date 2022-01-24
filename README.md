# Introduction

Simple AWS Serverless Application Model example with Layer and a SQS destination

## Requirements
* aws-cli/2.0.56 
* Python/3.7.3
* aws sam cli 1.15.0

### calculation-layer

AWS Lambda Layer with a simple sum function in the calculation module

### sum-app

AWS Lambda Function that references the calculation-layer and SQS destination that receives a message in case of failures (event with a simulate_error property)


## Start Environment


### 1 Deploy the layer:

```bash
cd calculation-layer
sam deploy --guided
```

### 2 Deploy the lambda with destination configuration and SQS:

```bash
cd sum-app
sam deploy --guided
```

### 3 Test

3.1. Unit Test (pytest)
```bash
cd sum-app
make test
```

3.2. Local Test with SAM

```bash
cd sum-app
make invoke
```

3.2. AWS Test with AWS Cli

```bash
aws lambda invoke --cli-binary-format raw-in-base64-out --function-name sum-app-SumAppFunction-xxxxxxxxxxxxx --invocation-type Event --payload '{"n1":1,"n2":3}' response.json
```
