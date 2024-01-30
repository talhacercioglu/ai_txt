# Real Estate Price Prediction

This Python script is designed to predict real estate prices based on various input parameters using a pre-trained machine learning model.

## Overview

The script takes input data from a file (`input_verileri.txt`), including information about the location (province, district, neighborhood), property type, floor information, and features like square footage, number of rooms, and more. It then uses a pre-trained gradient boosting model to predict the property price.

## Getting Started

### Prerequisites

- Python 3.12
- Required Python packages can be installed using `pip install -r requirements.txt`.

### Usage

1. Make sure to have the necessary input files (`il_avg_label.txt`, `il_id_label.json`, etc.) in the same directory as the script.
2. Run the script by executing `python real_estate_prediction.py`.
3. The script continuously checks for new input data in the `input_verileri.txt` file and provides predictions when new data is available.

### Input Data Format

- The input data should be formatted as a dictionary in the `input_verileri.txt` file.
- Provide details such as province, district, neighborhood, property type, floor information, square footage, number of rooms, etc.

### Output

- The predicted property price is displayed on the console.
- The result is also written to a file named `predicted_price.txt`.

## File Descriptions

- `real_estate_prediction.py`: The main Python script.
- `gradient_boosting_model_2.pkl`: Pre-trained machine learning model (gradient boosting).
- `il_avg_label.txt`, `il_id_label.json`, etc.: Data files containing information about provinces, districts, neighborhoods, etc.

## Notes

- The script utilizes the `joblib` library to load the pre-trained model.
- Continuous monitoring for new input data is implemented with a loop.
- The user can stop the loop by entering '0' when prompted.

## Author

Talha Çerçioğlu
