import json
import logging
from calculation import sum

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    statusCode = 200
    result = 0

    if 'simulate_error' in event:
        raise Exception('Simulating Error!')

    if event and 'n1' in event and 'n2' in event:
        n1 = event['n1']
        n2 = event['n2']
        result = sum(n1, n2)
        msg = "sum result:"+str(result)
        logger.info("status={0}, msg={1}".format(statusCode, msg))
    else:
        statusCode=400
        msg = "invalid numbers n1 and n2"
        logger.error("status={0}, msg={1}".format(statusCode, msg))

    return {
        "statusCode": statusCode,
        "body": json.dumps({
            "message": msg,
            "result": result
        }),
    }
