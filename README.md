# Overview

This is a skeletal example of one way to run a Tornado application in
production.  It currently covers running the application under
[Supervisor](http://supervisord.org).  Future additions may include
automating initial setup and deploying new code (e.g. with
[Fabric](http://fabfile.org)) and running multiple processes behind a proxy
(e.g. [nginx](http://nginx.org)).


## `basic-project` directory

This is our application;

## `production` directory

This directory contains scripts used for Supervisor and other production
services.


# Run Main Project

* Create a virtualenv environment
* Install packages

    `pip install -r requirements.txt`

* Then you are good to go!

# Try if it works:

    $ cd ares-api
    python server.py
    curl -d "title=title_from_curl&text=text_from_curl" localhost:2358/test_model

You should see from_curl in the list.

