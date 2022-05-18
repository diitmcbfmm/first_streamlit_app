
import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast')
streamlit.text('Fucking Cerals')
streamlit.text('More fucking food')
streamlit.header('Breakfast Menu')
streamlit.text( '🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
                                      
# Picklist
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
                                        
# display table on page
streamlit.dataframe(my_fruit_list)
