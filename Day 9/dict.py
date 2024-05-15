#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
print(capitals)

#Nesting a List in a dictionary
travel_log = {
    "france": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)

#Nesting a Dictionary in a dictionary
travel_log2 = {
    "france": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"Capital-visited": ["Berlin", "Hamburg", "Stuttgart"]},
}
print(travel_log2)

#Nesting Dictionary in a List
travel_log3 = [
    {
        "country": "france",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
print(travel_log3)