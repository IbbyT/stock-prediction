#stock prediction web app
#to run use streamlit run stocl_prediction.py
#add libaries
import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go

#date range
START_DATE = "2015-01-01"
CURRENT_DATE = date.today().strftime("%Y-%m-%d")

st.title("Stock Forecasting Application")

#stocks variable declaration
available_stocks = ("AAPL", "GOOG", "MSFT", "NVDA", "TSLA")
chosen_stock = st.selectbox("Choose a stock for prediction", available_stocks)

years_to_predict = st.slider("Select prediction horizon (years):", 1, 4)
days_to_predict = years_to_predict * 365

#load data with cache
@st.cache_data
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, START_DATE, CURRENT_DATE)
    stock_data.reset_index(inplace=True)
    return stock_data

#display raw data
st.text("Loading data...")
stock_data = fetch_stock_data(chosen_stock)
st.text("Data loaded successfully!")

st.subheader("Recent Data")
st.write(stock_data.tail())

#plot raw data
def display_raw_data():
    plot = go.Figure()
    plot.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Open'], name='Opening Price'))
    plot.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name='Closing Price'))
    plot.layout.update(title="Stock Price Over Time", xaxis_rangeslider_visible=True)
    st.plotly_chart(plot)

display_raw_data()

#data forecasting
training_data = stock_data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"})

model = Prophet()
model.fit(training_data)
future_dates = model.make_future_dataframe(periods=days_to_predict)
forecast = model.predict(future_dates)

#display
st.subheader("Prediction Results")
st.write(forecast.tail())

#plot data
st.write("Forecasted Stock Prices")
forecast_plot = plot_plotly(model, forecast)
st.plotly_chart(forecast_plot)

#display components
st.write("Forecast Breakdown")
forecast_components = model.plot_components(forecast)
st.write(forecast_components)