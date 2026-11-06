# Lab Evidence

These screenshots document the guided AWS word counter lab. Open any entry to view the full-size capture. Account and resource identifiers, subscription details, and log identifiers are masked where applicable.

| Step | Screenshot | What it shows |
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
