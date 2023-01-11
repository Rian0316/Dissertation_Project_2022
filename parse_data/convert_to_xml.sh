#!/bin/bash
# In this file I need to use srt2xml to convert all subtitle files to xml
declare -A languages
languages=( ["chi"]="zh" ["eng"]="en" ["zhe"]="zh" ["zht"]="zh")
dirs=$(find . -maxdepth 4 -mindepth 4 -regex './opensubs/[^\.].*')
for dir in $dirs ; do
  awk '!/font/' "$dir" > temp && mv temp "$dir"
  lang=$(echo "$dir" | awk -F/ '{print $(NF - 1)}')
  ./subalign/srt2xml -l "${languages[$lang]}" "$dir" > "${dir%.*}.xml"
done


