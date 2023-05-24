#!/bin/bash
# Description: Collection of various enumeration tools to aggregate a list of subdomains for a given target ($1).
#              Quick and dirty script that can be optimized, but gets the job done
# Author: Ally Petitt

amass enum --passive -d $1 -o domains_$1
assetfinder $1 | tee -a domains_$1
subfinder -d $1 | tee -a domains_$1
anubis -t $1 -ip | tee -a domains_$1
sd-goo.sh $1 | tee -a domains_$1


sort domains_$1 | uniq > tmp
mv tmp domains_$1
