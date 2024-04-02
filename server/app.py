#!/usr/bin/env python3
import os
#from werkzeug import Response,Request
from flask import Flask,request,current_app,g,make_response

app = Flask(__name__)
@app.before_request
def app_path():
    g.path=os.path.abspath((os.getcwd()))
    
@app.route("/")
def index():
    host=request.headers.get("host")
    appname=current_app.name
    response_body=f'''
      <h1>The host for this page is {host}
      <h1>The name for this application is {appname}
      <h1>The  path of this application on the user's device is {g.path}</h1>

'''
    status_code=200
    headers={}
    return make_response(response_body,status_code,headers)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
