import sys
import os
import requests
import jwt
from flask import Flask, request

app = Flask(import_name=__name__)

IS_MEMBER = jwt.encode({'profyle_member': True},
                       'secret', algorithm='HS256')
ISNT_MEMBER = jwt.encode({'profyle_member': False},
                         'secret', algorithm='HS256')

REMS_HOST = os.getenv("REMS_PROXY_HOST", "http://elixir_rems_proxy")
REMS_KEY = os.getenv("REMS_PROXY_KEY", "secret")
REMS_PORT = os.getenv("REMS_PROXY_PORT", "8080")

PROFYLE_URN = "urn:nbn:fi:lb-201403262"

def lookup(subject):
    url = REMS_HOST + ":" + REMS_PORT + "/user/" + subject
    print("Lookup at "+url, file=sys.stderr)
    response = requests.get(
        url,
        headers={'elixir-api-key': REMS_KEY,
                 'Accept': 'application/json'}
    )
    if not response.status_code == 200:
        print('Lookup failed', file=sys.stderr)
        return False

    result = response.json()
    print('Lookup result '+str(result), file=sys.stderr)
    for permission in result['permissions']:
        if PROFYLE_URN in permission['datasets']:
            return True

    return False


@app.route("/claim_source/<subject>")
def echo(subject):
    for key in request.args:
        print('args[', key, '] = ', request.args[key])
    print('subject: ', subject)
    member = lookup(subject)
    token = IS_MEMBER if member else ISNT_MEMBER
    return token, 200, {"Content-Type": "application/jwt"}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
