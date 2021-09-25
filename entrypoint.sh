#!/bin/sh

gunicorn --bind 0.0.0.0:8080 --timeout 1000 --workers 2 --threads 4 src.main:app
