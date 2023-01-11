#!/bin/bash
file=$1
# Remove ( ) tags
sed -e "s/[(][^)]*[)]//g" -i.backup $file
# Remove empty lines
awk 'NF' $file > temp && mv temp $file