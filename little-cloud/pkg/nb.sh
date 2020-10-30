#! /bin/bash -x

echo hello
echo hello
IFS=$'\n'
for file in $(find /opt -iname '*.ipynb*') ; do
	echo $file
	printf 'File found: %s\n' "$file";
	jupyter nbconvert "$file" --to python --output-dir . ;
done
