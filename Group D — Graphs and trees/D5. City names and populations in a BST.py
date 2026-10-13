cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Nashik": 1500000
}

# Add a city
cities["Nagpur"] = 3000000

# Update population
cities["Pune"] = 7200000

# Delete a city
del cities["Nashik"]

# Display in ascending and descending city order
print("Ascending:")
for city in sorted(cities):
    print(city, cities[city])

print("Descending:")
for city in sorted(cities, reverse=True):
    print(city, cities[city])

# Count comparisons needed to find a city in the sorted list
names = sorted(cities)
wanted = "Pune"
comparisons = 0

for city in names:
    comparisons += 1
    if city == wanted:
        break

print("Comparisons to find Pune:", comparisons)