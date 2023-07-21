#!/bin/bash

##50 18 * * * ./deployment.sh
sh start_script.sh
# Step 1: Create a virtual environment and activate it
echo "Step 1: Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Virtual environment activated."

# Step 2: Install dependencies from requirements.txt
echo "Step 2: Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed successfully."

# Step 3: Run global_dict.py to initialize the global dictionary
echo "Step 3: Initializing global dictionary..."
python global_dict.py
echo "Global dictionary initialized."

# Step 4: Run prepare_data.py to preprocess the data
echo "Step 4: Preprocessing data..."
python prepare_data.py
echo "Data preprocessing completed."

# Step 5: Run train.py to train the model
echo "Step 5: Training the model..."
python train.py
echo "Model training completed."

# Step 6: Run app.py to start the monitoring dashboard
echo "Step 6: Starting the API ..."
python app.py
echo "API running."

echo "Step 7: Deleting older file ..."
sh delete.sh
echo "All older file  deleted"

echo "Script execution completed."



