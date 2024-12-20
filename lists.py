import connection as c

def get_airp_name_list(airp_name: str):
    airp_name = airp_name.strip()

    if not airp_name:
        return []

    query_str = "SELECT name FROM airport;"
    c.cur.execute(query_str)
    results = c.cur.fetchall() 
    
    matching_names = []
    for (name,) in results: 
        if airp_name.lower() in name.lower():
            matching_names.append(name.replace("'", ""))

    return matching_names


def get_iata_list(iata: str):
    iata = iata.strip()

    if not iata:
        return []

    query_str = "SELECT IATACode FROM airport;"
    c.cur.execute(query_str)
    results = c.cur.fetchall()
    
    matching_names = []
    for (name,) in results:
        if iata.lower() in name.lower(): 
            matching_names.append(name)

    return matching_names


