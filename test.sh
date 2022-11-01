#!/bin/bash
"""
./a file should exist

test_* directories should be in the same level with the current working directory
"""

shopt -s nullglob
for dir in test*/ ; do
	cat "${dir}output2.txt" > my_out
	# ./a < "${dir}input.txt" > my_out
	diff -w my_out "${dir}output.txt"
	if [[ $? -ne 0 ]]; then
		echo -e "\n=== True output":
		cat my_out
		echo -e "\n\n=== My output:"
		cat "${dir}output.txt"
	fi
	rm my_out
done;