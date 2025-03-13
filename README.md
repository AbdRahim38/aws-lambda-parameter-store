# aws-lambda-parameter-store
aws-lambda-parameter-store

## Step 1: AWS KMS
- Create Customer managed key

## Step 2: AWS Parameter Store
- Create 4 parameter using standard tier. Use Step #1 KMS key for the SecureString paramter
    - Name: /my-app/dev/db-url , Type: String
    - Name: /my-app/dev/db-password , Type: SecureString, KMS key
    - Name: /my-app/prod/db-url , Type: String
    - Name: /my-app/prod/db-password , Type: SecureString, KMS key

## Step 3: Lambda
- Create 1 Lambda function
- Used lambda_function.py code for the Lambda function
- Create a "Environment Variables" in the Lambda function
    - Key = ENVIRONMENT  ,  Value= dev/prod (to be toggle during testing)

## Step 4: IAM Role
- Log role will be default attached when creating a new Lambda Function.
- Create 2 IAM Role which will be attached to the Lambda Function. 

**Role 1: SSMAccessForApp**
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ssm:GetParametersByPath",
                "ssm:GetParameters"
            ],
            "Resource": "arn:aws:ssm:*:*:parameter/my-app/*"
        }
    ]
}
```

**Role 2: KMSDecryptKey**
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:*:*:key/[REPLACE-WITH-KMS-ID]"
        }
    ]
}
```