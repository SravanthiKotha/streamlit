import streamlit as st
import pandas as pd
import os
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import DataProfile

import pathlib
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir,"Data","Hotel_Reservations.csv")
df = pd.read_csv(data_file)
st.title("Hotel Reservation Data Profiling!!")
profile = ProfileReport(df,title="Hotel Reservation Data",
        dataset={
        "description": "The online hotel reservation channels have dramatically changed booking possibilities and customers’ behavior. A significant number of hotel reservations are called-off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with.Can you predict if the customer is going to honor the reservation or cancel it ?",
        "url": "https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset"},
        variables={
        "descriptions": {
            "Booking_ID": "unique identifier of each booking",
            "no_of_adults": "Number of adults",
            "no_of_children": "Number of Children",
            "no_of_weekend_nights": "Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel",
            "no_of_week_nights": "Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel",
            "type_of_meal_plan": "Type of meal plan booked by the customer",
            "required_car_parking_space": "Does the customer require a car parking space? (0 - No, 1- Yes)",
            "room_type_reserved": "Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.",
            "lead_time": "Number of days between the date of booking and the arrival date",
            "arrival_year": "Year of arrival date",
            "arrival_month": "Month of arrival date",
            "arrival_date": "Date of the month",
            "market_segment_type":"Market segment designation.",
            "repeated_guest": "Is the customer a repeated guest? (0 - No, 1- Yes)",
            "no_of_previous_cancellations": "Number of previous bookings that were canceled by the customer prior to the current booking",
            "no_of_previous_bookings_not_canceled": "Number of previous bookings not canceled by the customer prior to the current booking",
            "avg_price_per_room": "Average price per day of the reservation; prices of the rooms are dynamic. (in euros)",
            "no_of_special_requests": "Total number of special requests made by the customer (e.g. high floor, view from the room, etc)",
            "booking_status": "Flag indicating if the booking was canceled or not."}
                })

st_profile_report(profile)