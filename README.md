# dreamingplaces_bed
Python Script to Contol the Dreaming Places Bed, built for Raspberry Pi

## Setup
Take a fresh raspbain SD card (tested with jessie) 
As the pi user run
sudo pip install pexpect

Then edit the ~/.bashrc file and add the following 2 lines to the end

xset -d :0 s blank
xset -d :0 s 1

Finally add your videos to the ~/Videos folder

