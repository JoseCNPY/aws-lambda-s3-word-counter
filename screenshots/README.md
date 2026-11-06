# AWS Word Counter Lab Walkthrough

This walkthrough documents a guided AWS lab. Follow the steps in order, then use the [screenshot gallery](#screenshot-gallery) to review the setup and the recorded result.

**Workflow:** Upload a `.txt` file to S3 → S3 invokes Lambda → Lambda counts the words → Lambda publishes the result to SNS. CloudWatch records the invocation and the word count.

## 1. Set up SNS notifications

In **Amazon SNS → Topics → Create topic**, select **Standard** and create a topic. Open the topic, choose **Create subscription**, select **Email**, and enter your email address. Open the confirmation message and verify that the subscription shows **Confirmed** in the SNS console.

## 2. Deploy and configure Lambda

In **AWS Lambda → Functions**, create a Python function. Add [`lambda_function.py`](../lambda_function.py), set the handler to `lambda_function.lambda_handler`, and deploy the code. In **Configuration → Environment variables**, add `SNS_TOPIC_ARN` with the ARN of your topic.

The execution role needs permission to read the input objects (`s3:GetObject`), publish to the topic (`sns:Publish`), and write logs to CloudWatch.

## 3. Connect the S3 trigger

In the Lambda function overview, choose **Add trigger → S3**. Select an input bucket in the same AWS Region as the function, choose **All object create events**, and set the suffix filter to `.txt`.

## 4. Upload a test file and check the result

Upload a sample from [`tests/fixtures/`](../tests/fixtures/) to the input bucket. In **Lambda → Monitor → View CloudWatch logs**, open the latest log stream and compare the result with the [expected counts](../README.md#sample-inputs). If you confirmed an email subscription, check for an SNS message with the subject **Word Count Result**.

In the recorded lab run, CloudWatch shows that Lambda processed `sample3.txt` and logged a count of **10 words**.

---

## Screenshot gallery

Open any link to view the capture at full size. Sensitive details are masked where applicable.

| # | Screenshot | What it shows |
| --- | --- | --- |
| 1 | [SNS topic setup](01-sns-topic-setup.png) | The Standard topic option selected in the SNS console. |
| 2 | [SNS confirmation email](02-sns-confirmation-email.png) | The email requesting confirmation of the topic subscription. |
| 3 | [Confirmed SNS subscription](03-sns-confirmed-subscription.png) | The SNS console showing the email subscription as confirmed. |
| 4 | [Lambda code deployment](04-lambda-code-deployment.png) | The Python handler in the Lambda console and the successful update message. |
| 5 | [Lambda configuration](05-lambda-configuration.png) | The S3 connection and the `SNS_TOPIC_ARN` environment variable. |
| 6 | [S3 trigger setup](06-s3-trigger.png) | Object-created events filtered to keys ending in `.txt`. |
| 7 | [CloudWatch log streams](07-cloudwatch-log-streams.png) | Log streams available for inspecting Lambda executions. |
| 8 | [CloudWatch word-count result](08-cloudwatch-word-count.png) | A Lambda invocation logged **10 words** for `sample3.txt`. |

[Back to the project README](../README.md)
