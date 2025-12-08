from log import log
import boto3

client = boto3.client("s3")


def lambda_handler(event, context):
    record = event["Records"][0]

    Bucket = record["s3"]["bucket"]["name"]
    Key = record["s3"]["object"]["key"]

    object_result = client.get_object(Bucket, Key)

    mega_byte = 1024 * 1024

    if object_result["ContentLength"] > 1 * mega_byte:
        log("Object much big.")
        return "Object much big."

    return "Object's size is OK."
