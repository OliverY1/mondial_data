import connection as c
import pandas as pd
import streamlit as st

def compare_gpd():
    
    country = st.text_input("Enter a country").capitalize()
    
    if country:
        query= """
        WITH nations_with_borders AS (
            SELECT Country1, Country2
            FROM
                (SELECT Country1, Country2 
                FROM borders
                UNION
                SELECT Country2, Country1 
                FROM borders) AS all_borders
            GROUP BY Country1, Country2
        ),


        gdp_for_country1 AS (
            SELECT Country.Name as country, Economy.Country AS Country1, Economy.GDP AS gdp1
            FROM Economy
            JOIN Country on Country.Code = Economy.Country
        ), 

        gdp_for_country2 AS (
            SELECT Country.Name as Border_country, Economy.Country AS Country2, Economy.GDP AS gdp2
            FROM Economy
            JOIN Country on Country.Code = Economy.Country
        )

        SELECT gdp_for_country1.country AS Country, gdp_for_country1.gdp1, gdp_for_country2.Border_country,
        gdp_for_country2.gdp2, COALESCE(gdp_for_country1.gdp1 / gdp_for_country2.gdp2 ,0) AS ratio
        FROM nations_with_borders
        JOIN gdp_for_country1 ON gdp_for_country1.Country1 = nations_with_borders.Country1
        JOIN gdp_for_country2 ON gdp_for_country2.Country2 = nations_with_borders.Country2
        where gdp_for_country1.country = %s
        ORDER BY ratio DESC;
        """

        try:
            c.cur.execute(query, (country,))
            rows = c.cur.fetchall()
            columns = [desc[0] for desc in c.cur.description]

            df = pd.DataFrame(rows, columns=columns)

            st.dataframe(df, use_container_width=True)

        except Exception:
            st.write("Data not found!")
        


