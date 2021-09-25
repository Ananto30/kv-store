#!/bin/sh

gunicorn src.main:app --bind 0.0.0.0:8080
