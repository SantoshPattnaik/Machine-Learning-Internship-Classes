import streamlit as st
import pandas as pd

st.title('Hello Santosh')
st.subheader('This is a simple streamlit app')
st.text('You can use this app for your streamlit setup')
st.write('This is a write command ion streamlit')

hero=st.selectbox('Choose Your Superhero: ',['Ironman', 'Captain America','Thor','Hulk'])
st.write(f'You Selected: {hero}')
st.success('This is a success message')
st.warning('This is a warning message')
st.info('This is a info message')
st.error('This is a error message')


st.title('Chaimaker Application')
if st.button('Make Chai'):
    st.success('Chai is ready')
add_masala=st.checkbox('Add Masala')
if add_masala:
    st.write('Masala added to your chai')
tea_type=st.radio('Select Tea Type: ',['Black Tea','Green Tea','Herbal Tea'])
st.write(f'You Selected: {tea_type}')
flavour=st.selectbox('Select Flavour: ',['Cardamom','Ginger','Mint'])
st.write(f'You Selected: {flavour}')
sugar=st.slider('Select Sugar Level: ',0,5,2)
st.write(f'You selected sugar level: {sugar}')
cups=st.number_input('Enter number of cups: ',min_value=1,max_value=10,value=1)
st.write(f'You selected number of cups: {cups}')

col1,col2=st.columns(2)
with col1:
    st.header('Masala Chai')
    vote1=st.button('Vote for masala chai')
with col2:
    st.header('Black Tea')
    vote2=st.button('Vote for Black Tea')

if vote1:
    st.success('You voted for masala chai')
elif vote2:
    st.success('You voted for black tea')

name=st.text_input('Enter Your name:')
tea=st.sidebar.selectbox('Select Your tea: ',['Masala Chai','Black Tea','Green Tea'])
st.write(f'Hello {name if name else 'Anonymous'}, you selected {tea} from the sidebar')    

with st.expander('Show chai making instructions:'):
    st.write("""
             1. Boil water in a pot.
             2. Add tea leaves and let it steep.
             3. Add milk and sugar to taste.
             4. Strain the tea into cups.
             5. Enjoy your chai!
             """)
    
st.title('File Uploader')
file=st.file_uploader('Upload a CSV file:',type=['csv','xlsx'])
if file:
    df=pd.read_csv(file)
    st.subheader('Data')
    st.dataframe(df)
    
    
import requests
st.title('Currency Converter')

amount = st.number_input("Enter amount in INR", min_value=0.0)
target_currency = st.selectbox("Convert to:", ["usd", "eur", "gbp", "jpy"])

if st.button('Convert'):
    url="https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/inr.json"
    response=requests.get(url)
    
    if response.status_code == 200:
        data=response.json()
        try:
            conversion_rate=data['inr'][target_currency.lower()]
            converted_amount = amount * conversion_rate
            st.success(f"{amount} INR = {converted_amount:.2f} {target_currency.upper()}")
        except KeyError:
            st.error(f"Conversion rate for '{target_currency}' not found.")
    else:
        st.error(f"Failed to fetch currency data. Status code: {response.status_code}")
