import boto3
import urllib.parse
import os

# Initialize AWS service clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# SNS topic ARN from environment variable
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']


def lambda_handler(event, context):
    try:
        # Read S3 event details
        record = event['Records'][0]
        bucket_name = record['s3']['bucket']['name']

        # Decode the S3 object key
        file_name = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        print(f"Processing file: {file_name}")

        # Read the uploaded file from S3
        response = s3.get_object(
            Bucket=bucket_name,
            Key=file_name
        )

        # Read file content
        content = response['Body'].read().decode('utf-8')

        # Count words
        word_count = len(content.split())

        # Prepare SNS message
        message = (
            f"The word count in the {file_name} "
            f"file is {word_count}."
        )

        print(message)

        # Publish message to SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Word Count Result",
            Message=message
        )

        return {
            'statusCode': 200,
            'body': message
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise
