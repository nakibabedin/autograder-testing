#!/usr/bin/env bash

REPO=git@github.com:REPO_URL
AUTOGRADER_BASE_DIR=/autograder/source/base/
BRANCH=prod # assumes you use this template

echo "Emoji"
cd /autograder/source/

ls -al
mkdir -p ~/.ssh
cp ssh_config ~/.ssh/config

# Make sure to include your private key here & chmod to 600 to allow 
# ssh agent to recognize it
cp deploy_key ~/.ssh/deploy_key
chmod 600 ~/.ssh/deploy_key

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/deploy_key

apt-get install -y python3 python3-pip python3-dev

pip3 install subprocess32 gradescope-utils>=0.3.1

# To prevent host key verification errors at runtime
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

ssh -T git@github.com
cat ~/.ssh/config

# Clone autograder files
git clone $REPO $AUTOGRADER_BASE_DIR -b $BRANCH