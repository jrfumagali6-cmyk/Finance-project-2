import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page setup
st.set_page_config(
    page_title='Project 2', 
    page_icon='📉', 
    layout='wide'
)

# Descrição do projeto # Project Description
st.header('Project 2')
st.markdown('**Dynamic adjustment and plotting of a technical analysis indicator.**')

# Period selection
period_options = {
    'Last 90 days': 90, 
    'Last 180 days': 180,
    'Last 360 days': 360, 
    'Last 760 days': 760
}
period = st.sidebar.selectbox('Select the period', list(period_options.keys()))

# Gets the number of selected days
days = period_options[period]

 #Candles selection interval
interval_options = {
    'Daily': '1d',
    'Weekly': '1wk',
    'Hour by hour': '1h'
}
interval = st.sidebar.selectbox('Select the interval', list(interval_options.keys()))

# Gets the selected interval
interval_value = interval_options[interval]

# Função para calcular médias móveis
def calculate_moving_averages(data, short_window, long_window, third_window):
    data['MA_Fast'] = data['Close'].ewm(span=short_window).mean()
    data['MA_Slow'] = data['Close'].rolling(window=long_window).mean()
    data['MA_Ultra Slow'] = data['Close'].rolling(window=third_window).mean()
    return data

 # Side Bar setup
st.sidebar.header('Options Menu')

# Ticker box text (Put the name of ticker)
selected_stock = st.sidebar.text_input(
    'Inform the ticker name', value='VALE3.SA'
)

# Slider setting for the number of periods of the fast moving average
short_window = st.sidebar.slider(
    'Fast Moving Average periods', 
    min_value=1, 
    max_value=50, 
    value=5
)

# Slider setting for the number of periods of the Slow moving average
long_window = st.sidebar.slider(
    'Slow Moving Average periods', 
    min_value=5, 
    max_value=50, 
    value=15
)

# Slider setting for the number of periods of the Ultra Slow moving average
third_window = st.sidebar.slider(
    'Ultra Slow Moving Average periods', 
    min_value=5, 
    max_value=200, 
    value=25
)

# End data is today date and start date is the number of days ago
end_date = datetime.today().date()
start_date = end_date - timedelta(days=days)

 # Download tickers data selected
data = yf.Ticker(selected_stock).history(start=start_date, end=end_date, interval=interval_value)

if not data.empty:
     # Calculate the Moving Average
    data = calculate_moving_averages(data, short_window, long_window, third_window)

     # Create the candles chart
    fig = go.Figure()

     # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    ))

     # Fast Moving Average chart
    fig.add_trace(go.Scatter(
        x=data.index, 
        y=data['MA_Fast'], 
        mode='lines', 
        name=f'Fast Moving Average ({short_window} periods)',
        line=dict(color='blue', width=2)
    ))

     # Slow Movinge Average chart
    fig.add_trace(go.Scatter(
        x=data.index, 
        y=data['MA_Slow'], 
        mode='lines', 
        name=f'Slow Moving Average ({long_window} periods)',
        line=dict(color='orange', width=2)
    ))
    
     # Ultra Slow chart
    fig.add_trace(go.Scatter(
        x=data.index, 
        y=data['MA_Ultra Slow'], 
        mode='lines', 
        name=f'Moving Average Ultra Slow ({third_window} periods)',
        line=dict(color='green', width=2)
    ))

     # Layout chart setup
    fig.update_layout(
        title={
            'text': f'Candlestick chart and Moving Average to {selected_stock}',
            'x': 0.5, 
            'xanchor': 'center',  
        },
        yaxis_title='Price',
        xaxis_title='Date',
        height=600,
        legend=dict(
            orientation="h",  
            yanchor="bottom",  
            y=1.02,  
            xanchor="center",  
            x=0.5  
        ),
        xaxis=dict(rangeslider_visible=False)  
    )

    # Show the streamlit chart
    st.plotly_chart(fig)
else:
    st.error(f"No found data for the ticker {selected_stock}.")

st.sidebar.markdown('''
    <p style="margin-top: 30px; text-align: center">
        Second project in Python for the Financial Market.<br>
        
    </p>
''', unsafe_allow_html=True)
