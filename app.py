import streamlit as st
import requests
import pandas as pd
import numpy as np
#from pycaret.regression import *
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
	st.title("Credit Scoring Demo")
	
	st.write("Info about Project and SOlidaridad")
	st.write("How credit scoring works")
	st.write("Credit Score = Farmer info + Crop Yield Prediction + Crop Export Price + Crop Import Price")
	






#------------------Predictions--------------------------------------------------------
if selected == "Prediction":
	st.title("Crop Yield Prediction")

#Load dataset
	df = pd.read_csv('data/farm.csv')



	

#------------------Crop Yield Prediction---------------------------------------------------------

	st.write('')

#------------------Select Location/Area-------------------------------------------------
	loc = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Angola',
       'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
       'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belgium-Luxembourg', 'Belize',
       'Benin', 'Bermuda', 'Bhutan', 'Bolivia (Plurinational State of)',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands',
       'Central African Republic', 'Chad', 'Chile', 'China',
       'China, Hong Kong SAR', 'China, mainland',
       'China, Taiwan Province of', 'Colombia', 'Comoros', 'Congo',
       'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba',
       'Cyprus', 'Czechia', 'Czechoslovakia',
       "Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Ethiopia PDR', 'Faroe Islands', 'Fiji', 'Finland',
       'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guadeloupe',
       'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
       'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait',
       'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia',
       'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania',
       'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
       'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico',
       'Micronesia (Federated States of)', 'Mongolia', 'Montenegro',
       'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
       'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norway',
       'Occupied Palestinian Territory', 'Oman',
       'Pacific Islands Trust Territory', 'Pakistan', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
       'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea',
       'Republic of Moldova', 'Réunion', 'Romania', 'Russian Federation',
       'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
       'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
       'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
       'Sudan (former)', 'Suriname', 'Eswatini', 'Sweden', 'Switzerland',
       'Syrian Arab Republic', 'Tajikistan', 'Thailand',
       'The former Yugoslav Republic of Macedonia', 'Timor-Leste', 'Togo',
       'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
       'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'United Kingdom', 'United Republic of Tanzania',
       'United States of America', 'Uruguay', 'USSR', 'Uzbekistan',
       'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam',
       'Wallis and Futuna Islands', 'Yemen', 'Yugoslav SFR', 'Zambia',
       'Zimbabwe']

	selected_loc = st.selectbox('Select Area',loc)

	data = df[df['Area'] == selected_loc]

	st.subheader("Crop Yield Prediction for "+selected_loc)	
#--------------Select Location For Crop yeild prediction--------------------------------  
	crop = ['Maize', 'Potatoes', 'Rice, paddy', 'Wheat', 'Sorghum', 'Soybeans',
       'Cassava', 'Yams', 'Sweet potatoes', 'Plantains and others']

	selected_crop = st.selectbox('Select Crop', crop)

	

#--------------Select Years For Crop yeild prediction------------------------------------
	year = ['2017','2018','2019','2020']
	selected_year = st.multiselect('Select Year', year)


	if st.button('Display Data'):
		fig = ff.create_table(data.head())
		st.write(fig)


	crop_data = data[data['Item'] == selected_crop]

	if st.button('Display Crop'):
		fig2 = ff.create_table(crop_data.head())
		st.write(fig2)

	def train_model(crop_data):
		model = Prophet()
		model.fit(df_train)
		return model

	df_train = crop_data[['Year','Value']]
	df_train = df_train.rename(columns={'Year':'ds','Value':'y'})
	model = train_model(df_train)

	st.write('')
	st.subheader('Forecast')


	pred_year = pd.DataFrame(selected_year)
	pred_year.columns = ['ds']
	forecast = model.predict(pred_year)

	fig3 = ff.create_table(forecast[['ds','yhat','yhat_lower','yhat_upper']])
	st.write(fig3)

	st.write("Where:")
	st.write("ds - forecast date time")
	st.write("yhat - forecasted value")
	st.write("yhat_lower - forecasted value lower boundary")
	st.write("yhat_upper - forecast value upper boundary")




	#Encoding
	#data = pd.get_dummies(data=data, drop_first=True)
	#Train model
	#reg = setup(data=data, target='Value',feature_interaction=True, feature_selection=True, session_id=123,silent=True)
	#best_model = compare_models()
	#tuned_model = tune_model(best_model, optimize='R2')
	#final = finalize_model(tuned_model)

#------------------Crop Import and Export--------------------------------------------------------



#------------------Credit Scoring/Rating--------------------------------------------------------





#-------------GIF from Lottie Animnations----------------------------------------
	
#---------------------------------------------------------------------------------





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
