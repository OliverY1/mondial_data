import streamlit as st

st.set_page_config(page_title="lab4", page_icon="💡", initial_sidebar_state="auto")

#import connection as c
import country_gpd
import airport
import search_language
from streamlit_option_menu import option_menu as op


st.title("Explore the mondial database!")
st.subheader("Made by Oliver Youness")
selected = op(
    menu_title=None,
    options=["Airports", "Countries", "Compare GDP"],
    icons=["airplane", "translate", "database"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal")


if __name__ == "__main__":

    if selected == "Airports":
        st.subheader("Search for airport by name and/or IATA")
        airport.search_airports()
    
    if selected == "Countries":
        st.subheader("Search for countries by language")
        search_language.countries_and_languages()
    
    if selected == "Compare GDP":
        st.subheader("Compare gdp to neighbouring countries")
        country_gpd.compare_gdp()
    

