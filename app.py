import streamlit as st
import pickle
import pandas as pd 

pipe = pickle.load(open('model.pkl', 'rb'))

teams = [
    'Australia',
    'India',
    'South Africa',
    'Pakistan',
    'West Indies',
    'England',
    'Sri Lanka',
    'New Zealand',
    'Bangladesh',
    'Afghanistan',
    'Ireland',
    'Zimbabwe'
]

cities = [
    'Auckland', 
    'Southampton', 
    'Sydney', 
    'Durban', 
    'Delhi',
    'Melbourne', 
    'Lauderhill', 
    'Wellington', 
    'Adelaide', 
    'Dubai',
    'Hambantota', 
    'Pallekele', 
    'Barbados', 
    'Colombo', 
    'London',
    'Mirpur', 
    'St Lucia', 
    'Nottingham', 
    'Manchester', 
    'Harare',
    'Johannesburg', 
    'Kolkata', 
    'Centurion', 
    'Sharjah', 
    'Trinidad',
    'Chittagong', 
    'Bangalore', 
    'Dhaka', 
    'Abu Dhabi', 
    'Cape Town',
    'Mount Maunganui', 
    'Guyana', 
    'Christchurch', 
    'Hamilton',
    'Chandigarh', 
    'Greater Noida', 
    'Cardiff', 
    'Lahore', 
    'St Kitts',
    'Nagpur', 
    'Mumbai'
]


st.title("T20 Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done(>5 overs)')
with col5:
    wickets = st.number_input('Wickets Out')

last_five = st.number_input('Runs Scored in Last 5 Overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 
        'current_score': [current_score], 'balls_left': [balls_left], 'wickets_left': [wickets],
        'crr': [crr], 'last_five': [last_five]})
    
    result = pipe.predict(input_df)

    st.header("Predicted Score is - " + str(int(result[0])))

