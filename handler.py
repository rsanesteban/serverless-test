import json


def status(event, context):
    body = {
      "title": "Status OK",
      "text": "API is up and running",
    }
    return {"statusCode": 200, "body": json.dumps(body)}


def hello(event, context):

    name = json.loads(event.get('body', '{}')).get("name")

    message = f"Hello {name}!"

    body = { "message": message }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
