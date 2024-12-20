import connection as c
import lists
import pandas as pd
import streamlit as st

pd.set_option('display.max_rows', None)

def search_airports():
    name = str(st.text_input("Enter an airport name: "))
    iata = str(st.text_input("Enter iata or dont: "))

    airp_name = lists.get_airp_name_list(name)
    iata_name = lists.get_iata_list(iata)

    select = "SELECT airport.IATACode AS IATA, airport.Name, Country.Name AS country FROM airport JOIN Country ON Country.Code = airport.Country"
    query = ""

    if airp_name != [] and iata_name == []:

        airp_list = ', '.join(f"'{name}'" for name in airp_name)
        query = query = f"{select} WHERE airport.Name IN ({airp_list});"

    if iata_name != [] and airp_name == []:
        iata_list = ', '.join(f"'{name1}'" for name1 in iata_name)
        query = f"{select} WHERE airport.IATACode IN ({iata_list});"

    if airp_name != [] and iata_name != []:
        airp_list = ', '.join(f"'{name}'" for name in airp_name)
        iata_list = ', '.join(f"'{name1}'" for name1 in iata_name)
        query = f"{select} WHERE airport.IATACode IN ({iata_list}) AND airport.Name IN ({airp_list});"

    if name or iata:
        try:
            c.cur.execute(query)
            rows = c.cur.fetchall()
            columns = [desc[0] for desc in c.cur.description]

            df = pd.DataFrame(rows, columns=columns)

            st.dataframe(df, use_container_width=True)
        
        except:
            st.write("No data found!")
