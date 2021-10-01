from bson import json_util
import json

def parse_js(data):
    return json.loads(json_util.dumps(data))