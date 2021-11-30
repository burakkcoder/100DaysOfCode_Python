travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,visit,city):
  new_dict = {}
  new_dict["country"] = country
  new_dict["visits"] = visit
  new_dict["cities"] = city

  travel_log.append(new_dict)
  print(f"You've visited {country} {visit} times.")

  cities = " and ".join(city)
  print(f"You've been to {cities}.")

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])