"""
Phython scripts for Lambda to extract Parameter Store db_url (string) and db_password (secured string)
"""
import json
import boto3
import os

ssm = boto3.client('ssm', region_name="ap-southeast-1")
environment = os.environ['ENVIRONMENT'] 

def lambda_handler(event, context):
    db_url = ssm.get_parameters(Names=["/my-app/" + environment + "/db-url"])
    print(db_url)
    db_password = ssm.get_parameters(Names=["/my-app/" + environment + "/db-password"], WithDecryption=True)
    print(db_password)
    return "Successfull!"