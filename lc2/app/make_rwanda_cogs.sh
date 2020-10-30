#! /bin/bash -x

find /mnt/rwanda/ -name "*_sr_ban*.tif">/tmp/cog_dance_card.txt

for f in `cat /tmp/cog_dance_card.txt`; do python3 cogify.py $f; done
