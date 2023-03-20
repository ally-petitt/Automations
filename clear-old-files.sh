#!/bin/bash
# Description: Bash script to delete files that have not been accessed in $2 number of days.
# Author: Ally Petitt

FILE_PATH=$1
AGE=$2

if [ "$#" -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "This script deletes all files that have not been accessed in X days"
    echo "Usage: ./clear-old-files.sh <FILE_PATH_TO_DELETE_FROM> <MIN_NUM_DAYS>"
    exit 2
fi

if ! [ -x "$(command -v tmpreaper)" ]; then
	echo "tmpreaper not found. Installing the package"
	sudo apt update
	sudo apt install tmpreaper
fi

echo "START: $FILE_PATH has $(ls -A $FILE_PATH | wc -l) files"
tmpreaper ${AGE}d $1
echo "END: $FILE_PATH has $(ls -A $FILE_PATH | wc -l) files"
