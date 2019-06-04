import sys
import jwt
from flask import Flask, request

app = Flask(import_name=__name__)

is_member = jwt.encode({'profyle_member': True},
                       'secret', algorithm='HS256')
isnt_member = jwt.encode({'profyle_member': False},
                         'secret', algorithm='HS256')

member_list = ['babs0001', 'uppe0001']

@app.route("/claim_source/<subject>")
def echo(subject):
    for key in request.args:
        print('args[', key, '] = ', request.args[key])
    print('subject: ', subject)
    print(request.method, file=sys.stderr)
    print(request.get_json(), file=sys.stderr)
    token = is_member if subject in member_list else isnt_member
    return token, 200, {"Content-Type": "application/jwt"}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
