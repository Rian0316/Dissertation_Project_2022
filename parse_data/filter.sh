#!/bin/bash
# Remove files that aren't in sub.paths (omit English files)

# Testing
dirs=$(cat sub.paths)
for dir in $dirs; do
	if echo $dir | grep -q -v "/eng/"; then
		echo "This wouldn't be deleted: $dir"
	else
		echo "This would be deleted: $dir"
	fi
done

dirs=$(find . -maxdepth 4 -mindepth 4 -regex './opensubs/[^\.].*')
for dir in $dirs; do
	# -v is reverse matching
	if echo $dir | grep -q -v "/eng/"; then
		if ! grep -q "$dir" sub.paths; then
        		echo "Deleting: $dir"
	        rm "$dir"
		fi
	fi
done
