#!/bin/bash

get_size() {
	local path="$1"
	local size=$(du -hs "$path" | cut -f1)
	echo $size
}

for item in .* *; do
	if [[ $item == '..' ]]; then
		continue
	fi
	size=$(get_size "$item")
	echo -e "$size\t$item"
done | sort -hr -k1 | more -10


