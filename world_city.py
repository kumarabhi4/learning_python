city = {"IND": {"MH":["Pune", "Mumbai", "Nagpur"],
                "GUJ":["Ahmadabad", "Gandhinagar", "Surat"],
                "UP":["Lucknow", "Kanpur", "Noida"],
                "KA":["Bangalore", "Maysuru"]},
         "US":{"CAL":["Los Angles", "San Fransisco", "Oakland"],
               "FL":["Miami", "Orlando", "Tampa"],
               "TX":["Houston", "Dallas", "Austin"]}
       }


for country in city:
    print("-"+country)
    for state in city[country]:
        print("\t-"+state)
        for wcity in city[country][state]:
            print("\t\t-"+wcity)
