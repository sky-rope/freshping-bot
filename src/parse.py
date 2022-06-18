import json


def validate_json(data):
    try:
        json.loads(data)
    except ValueError as err:
        raise err
    return True


def parse_webhook(data):
    message = ""
    json_payload = json.loads(data)
    for k, v in json_payload.items():
        message += str(k) + ": " + str(v) + "\n"
    return message
