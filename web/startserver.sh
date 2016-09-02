#!/bin/sh
if [ $# -lt 2 ]; then
  echo "Syntax: replay.sh file"
  exit 1
fi

python -m SimpleHTTPServer $2