# AWS Lambda S3 Word Counter

I completed this guided AWS lab to practice connecting Amazon S3, AWS Lambda, and Amazon SNS in an event-driven workflow. The repository contains the Python handler from the lab and sample inputs for repeating the exercise.

## How it works

1. An S3 object-created event invokes the Lambda function.
2. The handler reads the first event record, decodes the object key, and retrieves the uploaded file from S3.
3. It decodes the file as UTF-8 and counts words by splitting on whitespace.
4. It publishes the filename and count to an SNS topic with the subject `Word Count Result`.

## Reproduce the lab

1. Create an SNS topic and confirm an email subscription if you want to receive the results by email.
2. Deploy [`lambda_function.py`](lambda_function.py) to a Python Lambda function with the handler `lambda_function.lambda_handler`. Set the `SNS_TOPIC_ARN` environment variable to your topic ARN in Lambda.
3. Give the Lambda execution role permission to read the test objects (`s3:GetObject`), publish to the topic (`sns:Publish`), and write logs to CloudWatch.
4. Configure an S3 object-created trigger for the Lambda function. Upload the sample files one at a time and compare the SNS message or CloudWatch log with the expected results below.

## Sample inputs

| File | Expected words |
| --- | ---: |
| [simple.txt](tests/fixtures/simple.txt) | 5 |
| [multiline.txt](tests/fixtures/multiline.txt) | 6 |

These are expected counts for manual testing. The handler reads the entire object into memory and processes only the first record in each event. It treats punctuation as part of a word when there is no intervening whitespace.

## Screenshots

The [`screenshots/`](screenshots/) directory is reserved for lab screenshots to be added later.
