#!/bin/bash
# Then I need to run alignment of the English file against all language files and print results to a text file
# Most probably I should also implement something which will rank the subtitles by alignment and select the best one.
# ^ potentially need to inspect the reason for wrong alignments.
#Pseudocode:
#generate trees
#for each file in english
#  find matching (sxey and show) file in other language
#  generate alignment to a file in the directory of that language


#On small sample:
# Try a couple of options, see which works best
# Migrate another language and see if that language has an improvement

declare -A languages
languages=( ["chi"]="zh" ["eng"]="en" ["zhe"]="zh")
dirs=$(find . -maxdepth 4 -mindepth 4 -regex './opensubs/[^\.].*.xml')

for dir1 in $dirs ; do
  lang1=$(echo "$dir1" | awk -F/ '{print $(NF - 1)}')
  if [[ $lang1 == "eng" ]] ; then
    show1=$(echo "$dir1" | awk -F/ '{print $(NF - 2)}')
    for dir2 in $dirs ; do
      lang2=$(echo "$dir2" | awk -F/ '{print $(NF - 1)}')
      show2=$(echo "$dir2" | awk -F/ '{print $(NF - 2)}')
      if [[ $lang2 != "eng" && $show1 == $show2 ]] ; then
      	echo -n "$dir1 : $dir2 : ">>corpus.align
        ./subalign/srtalign "$dir1" "$dir2" > "$dir2.align" 2>>corpus.align
        
      fi
    done
  fi
done
