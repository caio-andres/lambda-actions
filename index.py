from log import log

def lambda_handler(event, context):
    # TODO implement
    log(msg=event)
    return {
        'statusCode': 200,
        'body': event
    }
