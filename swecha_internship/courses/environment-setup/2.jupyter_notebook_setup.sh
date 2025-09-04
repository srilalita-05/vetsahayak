#!/bin/bash

# Update package lists (adjust based on your distro)
if [ "$(command -v apt)" ]; then
  sudo apt update
elif [ "$(command -v yum)" ]; then
  sudo yum update
else
  echo "Warning: Could not identify package manager. Update may be required."
fi

# Install dependencies
sudo apt install -y python3 python3-pip  # Debian/Ubuntu
# Replace with sudo yum install -y python3 python3-pip for RedHat/CentOS

# Create a virtual environment (adjust name as needed)
python3 -m venv jupyter_env

# Activate the virtual environment
source jupyter_env/bin/activate

# Install Jupyter Notebook
pip install jupyter

# Deactivate the virtual environment (optional, recommended for clean management)
deactivate

echo "Jupyter Notebook installation complete! Run 'source jupyter_env/bin/activate' to activate the virtual environment and then 'jupyter notebook' to launch Jupyter Notebook."

