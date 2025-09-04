#!/bin/bash

# Update package lists
sudo apt update  # For Debian/Ubuntu based systems
# Replace with yum update for RedHat/CentOS based systems

# Install basic developer tools
sudo apt install -y git build-essential curl unzip wget zsh tmux

# Install Node.js (consider using a version manager for flexibility)
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Python3 and development libraries
sudo apt install -y python3 python3-pip

# Additional tools (uncomment to install)
#sudo apt install -y code  # Visual Studio Code

# Optional: ZSH configuration (change .zshrc path if needed)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
cp ~/.oh-my-zsh/templates/zshrc ~/.zshrc
echo "source ~/.zshrc" >> ~/.zshrc  # Add source command to your main shell config

echo "Developer environment setup complete!"

