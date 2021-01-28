#!/bin/bash

args="$@"

args="$@ --host 0.0.0.0 --port 8080 --id nfInstanceId"

file=/db.json
if [ -f $file ]; then
    echo "Found db.json, trying to open"
    args="$args --watch /db.json"
fi

file=/routes.json
if [ -f $file ]; then
    echo "Found db.json, trying to open"
    args="$args --routes /routes.json"
fi

file=/file.js
if [ -f $file ]; then
    echo "Found file.js seed file, trying to open"
    args="$args /file.js"
fi

json-server $args
