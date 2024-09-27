# PRODIGY_ML_01
# Bengaluru House Price Prediction

This project aims to predict house prices in Bengaluru using various regression techniques. The dataset is cleaned and processed to enhance the model's accuracy and effectiveness.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Modeling Techniques](#modeling-techniques)
- [Results](#results)
- [License](#license)

## Overview
The project involves the following main steps:
1. **Data Loading**: Load and unzip the dataset.
2. **Data Cleaning**: Handle missing values and remove unnecessary columns.
3. **Feature Engineering**: Convert the 'size' and 'total_sqft' columns into usable numerical formats and create a new feature for the number of bedrooms.
4. **Outlier Removal**: Identify and remove outliers based on price per square foot.
5. **Model Training**: Train multiple regression models (Linear Regression, Lasso, Ridge) on the cleaned data.
6. **Model Evaluation**: Evaluate models using R-squared metrics.

## Installation
To run this project, you will need to have Python 3.x installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install pandas numpy scikit-learn matplotlib
