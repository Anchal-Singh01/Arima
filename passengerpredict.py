
import streamlit as st
import pickle
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Load the pre-trained forecasting model
with open('arima.pkl', 'rb') as file:
    model = pickle.load(file)
    
# Create the web app
st.title('Passenger Prediction App')

# Input: Select a base date
base_date = st.date_input("Select the base date:", value=datetime.today())

# Input: Enter the number of months for prediction
month_delta = st.number_input('Number of months to predict:', min_value=1, max_value=120, value=1)

# Generate future dates based on the inputs
future_dates = [base_date + relativedelta(months=i) for i in range(1, month_delta + 1)]

# Prepare a DataFrame for prediction
future_data = pd.DataFrame({'Date': future_dates})
future_data['Month'] = future_data['Date'].dt.month  # Extract month if required
future_data['Year'] = future_data['Date'].dt.year   # Extract year if required

# Predict passengers
st.write("### Predicting Passenger Count...")
try:
    predictions = model.predict(start=len(future_dates), end=len(future_dates+ prediction")
Finallym>
    Finally.



