#!/bin/bash


directory="/log/"

current_date=$(date +"%Y-%m-%d")

seven_days_ago=$(date -d "-7 days" +"%Y-%m-%d")

files_to_delete=$(find "$directory" -type f -name "????-??-??_app.log" -mtime +7)

if [ -n "$files_to_delete" ]; then
  echo "Deleting old files..."
  echo "$files_to_delete"
  rm -f $files_to_delete
else
  echo "No files to delete."
fi

model_directory="./models/"
find "$model_directory" -type f -name "????-??-??_*.pkl" -mtime +7 -delete

data_directory="./data/pre_processed_data"
find "$data_directory" -type f -name "????-??-??_*.csv" -mtime +7 -delete