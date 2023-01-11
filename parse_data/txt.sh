#!/bin/bash

dirs=$(find . -maxdepth 4 -mindepth 4 -regex './opensubs/[^\.].*.align')

for dir in $dirs ; do
  python txt.py "$dir"
done
