import streamlit as st
import streamlit.components.v1 as stc

from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage Diabetes Risk Data App </h1>
		</div>
		"""

desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- ML Section: ML Predictor App
				- EDA Section: Exploratory Data Analysis of Data
				

			"""

def main():
	# st.title("Main App")
	stc.html(html_temp)

	menu = ["ML", "EDA","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "ML":
		st.subheader("Machine Learning Predictor App")
		# st.write(desc_temp)
		st.markdown(desc_temp, unsafe_allow_html=True)
		run_ml_app()

	elif choice == "EDA":
		run_eda_app()

	else:
		st.subheader("About")

if __name__ == '__main__':
	main()