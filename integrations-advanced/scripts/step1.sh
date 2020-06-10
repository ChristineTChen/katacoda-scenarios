#!/usr/bin/env bash

echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config

apt update && apt install -y python3.8-dev

echo "Creating workspaces..." | wall -n

mkdir /workspace && cd /workspace

echo "Cloning the integrations-extras repository..." | wall -n
git clone -q https://github.com/DataDog/integrations-extras.git /workspace/integration-extras

echo "Setup a python3 virtual environment..." | wall -n
cd /workspace/integration-extras
virtualenv -p python3.8 venv
source venv/bin/activate

echo "Install and configure the datadog-check-dev cli..." | wall -n
echo "Running \"pip install \"datadog-checks-dev[cli]\"\"" | wall -n
pip install "datadog-checks-dev[cli]"
echo "Running \"ddev config set extras \"/workspace/integrations-extras\"\"" | wall -n
ddev config set extras "/workspace/integrations-extras"
echo "Running \"ddev config set repo extras\"" | wall -n
ddev config set repo extras

echo "Your workspace setup is done! Enjoy the workshop :) " | wall -n



