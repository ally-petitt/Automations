# one-liner to remove the top line of a file and then run a command with it
# replace "cat $FILENAME" with your own command to run with the modified file
export FILENAME="YOUR_FILE.TXT"; for i in {$(wc -l $FILENAME | cut -d ' ' -f 1)..1}; do echo "removing line $(head -n 1 $FILENAME)" && tail -n $(expr $i - 1) $FILENAME > $FILENAME.tmp && mv $FILENAME.tmp $FILENAME; cat $FILENAME; done
