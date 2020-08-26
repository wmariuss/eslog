import json
import pprint
from zipfile import ZipFile


def json_format(content):
    """Return text in JSON format"""
    return json.loads(content)


def pretty(data):
    """Nice print"""
    pp = pprint.PrettyPrinter(indent=2)
    return pp.pprint(data)


def archive(file):
    """Archive file"""
    with ZipFile("{}.zip".format(file), "w") as zipit:
        zipit.write(file)
