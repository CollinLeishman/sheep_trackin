#!/bin/bash

# create virtualenvironment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

# Create required_environment_variables file
if [ ! -f required_environment_variables ]; then
  virtual_environment_path=$(pwd)/venv
  if [ ! -f sqlite.db ]; then
    sqlite_path=$(pwd)/sqlite.db
  fi
  touch required_environment_variables
  echo "PYTHON_VENV_PATH=$virtual_environment_path" >> required_environment_variables
  echo "DATABASE_URL=$sqlite_path" >> required_environment_variables
fi

echo "Be sure to source the virtualenvironment with 'source venv/bin/activate' now."