#!/bin/bash
cd /opt/cier2019
source venv/bin/activate
cd /opt/cier2019/cier2019
python manage.py process_tasks
