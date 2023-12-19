from apiflask import APIBlueprint
from flask_httpauth import HTTPBasicAuth

router = APIBlueprint("user", __name__)
auth = HTTPBasicAuth()
