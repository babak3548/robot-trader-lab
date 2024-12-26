# Machine Learning Lab for Stocks 

## Overview
This project is designed to enable seamless integration with new data providers and simplify testing machine learning (ML) and deep learning algorithms with minimal code changes. It is ideal for financial market analysis, including stocks, cryptocurrencies, and forex.

## Features
1. **Data Fetching**:
   - Supports fetching data from various financial markets, including stocks, cryptocurrencies, and forex.
   - Integrated with the **Twelve Data** API for data retrieval【41†source】.

2. **Extensible Data Providers**:
   - Includes a **Data Factory** class that allows adding new data providers easily【37†source】.
   - Provides partial implementation for fetching data from **MetaTrader**【39†source】, demonstrating extensibility for other sources.

3. **Data Preprocessing**:
   - The **PreprocessIndicators** class calculates various indicators for historical data, including:
     - **MA (Moving Average)**, **WMA (Weighted Moving Average)**, **MOM (Momentum)**
     - **K and D (Stochastic Oscillator)**
     - **RSI (Relative Strength Index)**
     - **MACD (Moving Average Convergence Divergence)**, **MACD Signal**, **MACD Histogram**
     - **LW (Larry Williams' %R)**, **AD (Accumulation/Distribution)**【40†source】.
   - Enables feature engineering to extract rich features before training ML algorithms.

4. **Data Storage**:
   - On the first run, the project fetches data from the data provider and saves it as a **CSV file**【39†source】.
   - Avoids repeated fetching of the same data during model training.

5. **Model Training**:
   - Includes models for training and testing various ML algorithms:
     - **Linear Regression with Polynomial Features**【42†source】
     - **Logistic Regression with Polynomial Features**【43†source】
     - **Logistic Regression**【44†source】.
   - Facilitates adding and testing new algorithms by organizing code into modular classes【45†source】.

## Goals
- Simplify integration with new data providers.
- Provide extensible design for adding and testing new machine learning algorithms.
- Facilitate feature engineering for better model performance.

## Requirements
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, talib, Scikit-learn, TensorFlow/PyTorch (optional)
- **Data Provider API**: Twelve Data API key

## Setup Instructions
1. Clone the repository.
2. Install required dependencies.
3. Configure API keys and data sources in the configuration file.
4. Run data fetching and preprocessing scripts.
5. Use the training module to test different ML algorithms.

## Contribution
Contributions are welcome! Please submit issues and pull requests to enhance functionality.

## License
This project is licensed under the **MIT License**. See the LICENSE file for details.

