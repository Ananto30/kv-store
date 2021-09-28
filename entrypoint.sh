#!/bin/sh

# worker must be one as we are initiating redis connection with api call, there will be inconsistency if more workers
gunicorn --bind 0.0.0.0:8080 --timeout 1000 --workers 1 --threads 2 src.main:app
