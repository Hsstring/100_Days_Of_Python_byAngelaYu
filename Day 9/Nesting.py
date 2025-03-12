#Nesting
"This is a list nested in a dictionary  and the dictionary nested in another dictionary"
travel_log1 = {
    "France": { "cities_visited": ["paris", "lille","Dijon"],"total_visits":12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5}

}

"This is a dictionary nested in a list"
travel_log2 = [
    {
        "country":"France",
        "cities_visited": ["paris", "lille","Dijon"],
        "total_visits":12
    }
    ,
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    }

]