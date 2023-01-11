#!/bin/bash
# Fix encoding of subtitles
# Use enca for Polish subtitles - because it works for sure - and iconv for the rest.
dirs=$(find . -maxdepth 4 -mindepth 4 -regex './opensubs/[^\.].*.srt')
for dir in $dirs ; do
  lang=$(echo "$dir" | awk -F/ '{print $(NF - 1)}')
  if [[ $lang == "pol" ]]
  then
    enconv -L polish -x utf-8 "$dir"
  else
    IFS=' '
    x=$(chardetect "$dir")
    array=( $x )
    enc=${array[1]}
    if [[ $enc != "utf-8" && $enc != "UTF-8-SIG" ]]
    then
      if [[ $enc == "Windows-1254" ]]
      then
        enc="ISO-8859-1"
      fi
      iconv -f $enc -t utf-8 "$dir" > temp && mv temp "$dir"
    fi
  fi
done


# WHEN YOU COME BACK: RUN THIS ON THE FILES, THEN DELETE "FONT" LINES, THEN CONVERT TO XML

