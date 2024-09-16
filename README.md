# Stock Prediction Web App

This is a web application for predicting stock prices using historical data. The app utilizes `Streamlit` for the user interface, `yfinance` for fetching stock data, `Prophet` for forecasting, and `Plotly` for visualizing the results.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
3. **Install the required libraries:**
   ```bash
   pip install streamlit yfinance prophet plotly
4. **Run the application:**
   ```bash
   streamlit run stock_prediction.py

## Libarries Used:
- streamlit: For creating the web application interface.
- yfinance: For downloading historical stock data.
- prophet: For forecasting stock prices.
- plotly: For interactive data visualization.

## Features:
- Stock Selection: Choose a stock from a predefined list (AAPL, GOOG, MSFT, NVDA, TSLA) for prediction.
- Prediction Horizon: Select a prediction horizon in years (1 to 4 years).
- Data Visualization: View raw stock data and interactive plots of stock prices over time.
- Forecasting: Forecast future stock prices and visualize the predictions with Prophet.

## Usage:
1. Choose a stock: From the dropdown menu, select the stock for which you want to make predictions.
2. Select prediction horizon: Use the slider to choose the number of years into the future you want to predict.
3. View Data: The app will display recent stock data and a plot of historical stock prices.
4. View Forecast: The app will show forecasted stock prices and a breakdown of forecast components.

## Code Overview:
- Date Range: The app uses data from January 1, 2015, to the current date.
- Data Fetching: Stock data is fetched using yfinance and cached for efficiency.
- Data Visualization: Historical stock prices are plotted using Plotly.
- Forecasting: Prophet is used to forecast future stock prices and visualize the predictions.
