#!bin/bash

python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn _main:app --reload --port 4000
