#!/bin/bash
cd /opt/cier2019
source venv/bin/activate
cd /opt/cier2019/cier2019
gunicorn cier2019.wsgi -t 600 -b 127.0.0.1:8011 -w 6 --user=servidor --group=servidor --log-file=/opt/cier2019/gunicorn.log 2>>/opt/cier2019/gunicorn.log
