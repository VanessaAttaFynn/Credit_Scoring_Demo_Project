import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.figure_factory as ff
from prophet import Prophet
from prophet.plot import plot_plotly
from prophet.plot import plot_plotly, plot_components_plotly

#------------------NavigationBar--------------------------------------------
with st.sidebar:
	selected = option_menu(
		menu_title="Menu",
		options=["Home","Prediction","Report","Shop"],
		icons=["house","graph-up-arrow","file-earmark-bar-graph","shop"],
		menu_icon="cast",
		default_index=0,
	)
#------------------Home-------------------------------------------
if selected == "Home":
	st.title("Home")
	def load_lottieurl(url: str):
		r = requests.get(url)
		if r.status_code != 200:
			return None
		return r.json()
	cr_anime = "https://assets4.lottiefiles.com/packages/lf20_mwuczohj.json"
	cr_anime_json = load_lottieurl(cr_anime)
	st_lottie(cr_anime_json)
	






#------------------Predictions--------------------------------------------------------
if selected == "Prediction":
	st.title("Prediction")

	#-------------GIF from Lottie Animnations----------------------------------------
	def load_lottieurl(url: str):
		r = requests.get(url)
		if r.status_code != 200:
			return None
		return r.json()
	pred_anime = "https://assets4.lottiefiles.com/private_files/lf30_8exlgvzr.json"
	pred_anime_json = load_lottieurl(pred_anime)
	st_lottie(pred_anime_json)
	#---------------------------------------------------------------------------------


#------------------Crop Yield Prediction---------------------------------------------------------




#------------------Crop Import and Export--------------------------------------------------------

# time series plot function
layout2 = {'autosize': False, 'width': 750, 'height': 500, "xaxis": dict(titlefont=dict(size=15), visible=True),
            'yaxis': dict(titlefont=dict(size=15),), 'paper_bgcolor': 'rgba(0, 0, 0, 0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'title_x': 0.5,}

def line_graph_2(data, column):
    fig = px.line(data, x="Year", y='Total '+ column, title='Time Series of Data', color_discrete_sequence=px.colors.qualitative.D3)
    fig.update_xaxes(showgrid=False, rangeslider_visible=True)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(layout2)
    st.plotly_chart(fig)

# select data dto import
st.write('')
tasks = ['Imports', 'Exports']
selected_task = st.selectbox('Select dataset for prediction', tasks)

# function to load data
@st.cache
def load_data(ticker):
    if ticker == 'Imports':
        df = pd.read_csv('data/import.csv')
    elif ticker == 'Exports':
        df = pd.read_csv('data/export.csv')
    
    return df

data_load_state = st.text('Loading data.....')
data = load_data(selected_task)
data_load_state.text('Loading data...... Done!')


# view table and plot time series
st.write('')
st.write('')

st.subheader('Time Series Data')
st.write('')

if st.button('Display Data'):
    fig =  ff.create_table(data.head(10))
    st.write(fig)

st.write('')
st.write('')
st.subheader('Time Series Plot')
st.write('')

if st.button('Display Plot'):
    line_graph_2(data, selected_task)

def train_model(data):
    model = Prophet()
    model.fit(df_train)
    return model

df_train = data[['Year', 'Total '+ selected_task]]
df_train = df_train.rename(columns={'Year':'ds', 'Total '+selected_task: 'y'})
model = train_model(df_train)


# define missing dates

st.write('')
st.write('')
st.subheader('Forecasting')
st.write('')

try:
    years = ['2020', '2021', '2022', '2023']
    select_years = st.multiselect('Select years to forecast', years)

    st.write('')
    st.write('')
    st.write('Forecasted Output')
    forecast_years = pd.DataFrame(select_years)
    forecast_years.columns = ['ds']
    forecast = model.predict(forecast_years)

    figt =  ff.create_table(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
    st.write(figt)

    st.write('')
    st.write('')
    st.subheader('Visualize Forecast Output')
    st.write('')

    def visualize(moodel=model, forecast=forecast):
        fig1 = plot_plotly(model, forecast)
        fig1.update_layout(title='Forecast Time Series Plot', title_x=0.5, width=780, height=500)
        st.plotly_chart(fig1)

        fig2 = plot_components_plotly(model, forecast)
        fig2.update_layout(title='Forecast Time Series Components', title_x=0.5, width=780, height=500)
        st.plotly_chart(fig2)

    if st.button('Show Plots'):
        visualize()
except:
    st.write('Please select years to be forecasted!')

#------------------Credit Scoring/Rating--------------------------------------------------------











#------------------Report-------------------------------------------
if selected == "Report":
	st.title("Report")
	def load_lottieurl(url: str):
		r = requests.get(url)
		if r.status_code != 200:
			return None
		return r.json()

	rep_anime = "https://assets8.lottiefiles.com/packages/lf20_npjqm3yq.json"
	rep_anime_json = load_lottieurl(rep_anime)
	st_lottie(rep_anime_json)























#------------------Extra-------------------------------------------
if selected == "Shop":
	st.title("...Under Construction")
	def load_lottieurl(url: str):
		r = requests.get(url)
		if r.status_code != 200:
			return None
		return r.json()

	shop_anime = "https://assets3.lottiefiles.com/private_files/lf30_y9czxcb9.json"
	shop_anime_json = load_lottieurl(shop_anime)
	st_lottie(shop_anime_json)