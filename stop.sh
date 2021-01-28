#!/usr/bin/env bash

uwsgi --stop /tmp/vision.pid

sudo nginx -s quit


