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
def add_new_country(country, visits, places):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = places
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
add_new_country("India", 4, ["Mumbai", "Delhi"])
print(travel_log)
