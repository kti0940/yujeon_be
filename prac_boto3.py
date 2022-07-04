# import boto3

# def control_s3(image):
#     s3 = boto3.client('s3')
#     s3.put_object(
#         ACL="public-read",
#         Bucket="migdracios",
#         Body=image,
#         Key=image.filename,
#         ContentType=image.content_type
#         )
#     print(s3)
#     return ""

# control_s3("result.jpeg")

import datetime

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d_%H%M%S'))