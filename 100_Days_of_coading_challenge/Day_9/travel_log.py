from typing import Dict, Any

country = input("Enter the name of the country you have been through-")
visit = input("Enter the number of visits to that country")
list_of_cities = input("Enter the list of countries you visited")

Travel_logs = [
    {
        "country": "India",
        "cities_visited": ["New Delhi", "Gujarat", "Telangana"],
        "Total_visits": 5
    },
    {
        "country": " France",
        "cities_visited": ["Paris", "little", "Puppy"],
        "Total_visits": 0
    }
]


def add_a_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visit"] = times_visited
    new_country["list_of_cities"] = cities_visited
    Travel_logs.append(new_country)


add_a_new_country(country, visit, list_of_cities)
print(f"I've been to {Travel_logs[2]["country"]} {Travel_logs[2]["visit"]} times")
print(f"My favourite city was {Travel_logs[2]}")