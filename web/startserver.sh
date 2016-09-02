#!/bin/sh
if [ $# -lt 2 ]; then
  echo "Syntax: replay.sh file"
  exit 1
fi

pushd $1; python -m SimpleHTTPServer $2; popd