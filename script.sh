#!/usr/bin/env bash

# Step-by-step script to set up and run the tictactoe workflow locally

set -e

# 1. Go to the profile directory (adjust path if needed)
# cd "$(dirname "$0")/profile"

# 2. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Ensure you have a .env file with your TinyURL API key
if [ ! -f .env ]; then
  echo "API_KEY=your_actual_tinyurl_api_key_here" > .env
  echo "Created a template .env file. Please edit it to add your TinyURL API key!"
  exit 1
fi

# 5. Run the tictactoe script
python tictactoe.py

# 6. Deactivate venv after run
deactivate

echo "Done! Check the output above for results."
