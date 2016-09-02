#!/bin/sh

base_path=$1
fragments_path=$1/fragments

mkdir -p $base_path
mkdir -p $fragments_path

fswebcam -r 1280x720 --no-banner $fragments_path/goal.jpg -i 0