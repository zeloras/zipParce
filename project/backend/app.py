#!/usr/bin/env python3
import json
import os

import connexion
from logzero import loglevel
from ZipForce.ZipForce import ZipForce

SETTINGS = json.loads(open("settings.json").read())


def ping():
    """Send alive status."""
    return {'result': 'pong'}, 200


def upload_zip(file):
    return {'result': 'SomeGuid'}, 200


def result():
    filepath = f'{os.path.dirname(__file__)}/tmp/test.zip'
    force = ZipForce(filepath, "asd\n1112\n123\nsss")
    force = force.parse()
    return {'result': force, 'isFound': len(force) > 0}, 200


APP = connexion.App(__name__)
APP.add_api('protocol.yaml',
            strict_validation=SETTINGS["strict_validation"],
            validate_responses=SETTINGS["validate_responses"])

if __name__ == '__main__':
    loglevel(SETTINGS["loglevel"])
    APP.run(port=SETTINGS['port'])
