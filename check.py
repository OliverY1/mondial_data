import connection as c
import streamlit as st

def check_max_9_provinces(desert:str):
    query = """
    SELECT province
    FROM geo_desert
    WHERE desert = %s
    GROUP BY province;
    """
    try:
        c.cur.execute(query, (desert,))
        list = c.cur.fetchall()
    except:
        print("Invalid desert name! ")
        return False

    if len(list) <= 9:
        return True
    else:
        print("The provided desert name is in more than 9 provinces! Cant insert data")
        return False
    
def check_max_20_deserts(country:str):
    query = """
        SELECT DISTINCT geo_desert.desert
        FROM geo_desert
        JOIN country ON country.code = geo_desert.country
        WHERE country.name = %s;
        """
    try:
        c.cur.execute(query, (country,))
        list = c.cur.fetchall()
    except:
        st.write("Invalid country name! ")
        return False

    if len(list) <= 20:
        return True
    else:
        st.write("The provided country name is in more than 20 countries! Cant insert data")
        return False

def check_area(area:int, province:str):
    query = "SELECT area FROM province WHERE name = %s;"
    try:
        c.cur.execute(query,(province, ))
        list = c.cur.fetchall()
        province_area = int(list[0][0])
    except:
        st.write("Invalid data")
        return False
    
    if area <= province_area *30:
        return True
    else:
        st.write("The provided area is larger than 30 times the province area! Data not inserted ")
        return False
    