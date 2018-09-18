#!/bin/bash

echo "Connecting to Jupyter Notebook through SSH..."

# Connect to SSH server and run jupyter notebook
ssh -t saubhik@122.166.170.151 'jupyter notebook --no-browser --port=5900 &'

# Connect to SSH for port forwarding
ssh -N -L localhost:8888:localhost:5900 saubhik@122.166.170.151 &

echo "Connected!"
