import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

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