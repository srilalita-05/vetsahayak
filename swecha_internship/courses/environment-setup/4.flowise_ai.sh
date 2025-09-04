#!/bin/bash

# Install Flowise
bun add -g flowise

# Install dos2unix if not already installed
sudo apt install dos2unix -y

# Find the Flowise executable and fix line ending error
dos2unix $(realpath $(which flowise))

bun add -g sqlite3
