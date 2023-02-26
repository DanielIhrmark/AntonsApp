"""
Description
Anton's vocabulary trainer, based on the 1500 most common nouns


"""
# Core Pkgs
import streamlit as st
import os
import pandas as pd


# Set tabs up
tab1, tab2, tab3 = st.tabs(["Vocabulary Trainer", "Words", "Other Exercises"])

df ('./vocab_data.csv')
df = df.drop('class', axis=1)
colNames = list(df.columns.values)
for column in colNames:
	df[column] = df[column].str.lower()

@st.cache_data
def vocablist(number):
	newnumber = int(number)
	newdf = df.sample(n=newnumber)
	return newdf

def main():
	""" web interface """

	# Title
	st.sidebar.title("Anton's Vocabulary Trainer")
	st.sidebar.subheader("Learn new words quickly and easily!")

	# Vocabulary trainer
	with tab1:
		with st.form('vocab_form'):
			st.subheader("Translate the word!")
			userNumber = st.number_input("Number of words", 10)

			submitted = st.form_submit_button("Generate vocabulary list")
			if submitted:
				vocabulary = vocablist(userNumber)
				vocabulary.insert(0,"Answer", " ")
				maindf = vocabulary
				st.experimental_data_editor(maindf.drop('english', axis=1))
				
				with st.expander("Answers"):
					st.dataframe(vocabulary.drop('Answer', axis=1))


			

	# Registry of words
	with tab2:
		st.subheader("Current register of words")
		st.dataframe(df)

		userWord = st.text_input("Search for a word", "")
		langChoice = st.selectbox('Select language:', colNames)
		if st.button("Search"):
			st.dataframe(df.loc[df[langChoice]==userWord], use_container_width=True)
		

	#Other exercises
	#with tab3:


	st.sidebar.subheader("About the App")
	st.sidebar.info("This is a training app using frequent words in English to build vocabulary. The word choices are based on the B level of CEFR, and is intended for use in Swedish upper-secondary schools. The translation was done using the Google Translate API, so be aware that some words might have been translated incorrectly.")
	st.sidebar.subheader("Contact and Complaints")
	st.sidebar.text("Daniel Ihrmark")
	st.sidebar.text("(daniel.o.sundberg@lnu.se)")




if __name__ == '__main__':
	main()
