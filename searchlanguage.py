import connection as c
import streamlit as st
import pandas as pd

pd.set_option('display.max_rows', None)


def countries_and_languages():
    language = str(st.text_input("Enter a language: ")).lower().capitalize()
    
    if language:
        query = """
        SELECT Country.Name, Spoken.Language, COALESCE(ROUND(SUM(Country.Population * spoken.Percentage / 100)),0) AS Speakers
        FROM Country
        JOIN Spoken on Country.Code = Spoken.Country
        WHERE Spoken.Language = %s
        GROUP BY Spoken.Language, Country.Name
        HAVING COALESCE(ROUND(SUM(Country.Population * spoken.Percentage / 100)),0) > 0
        ORDER BY Speakers DESC;
        """

        try:
            c.cur.execute(query, (language,))
            rows = c.cur.fetchall()
            print("\n")
            st.dataframe(pd.DataFrame(rows, columns=["Country", "Language", "Speakers"]), use_container_width=True)
        
        except:
            st.write("No countries found!")
