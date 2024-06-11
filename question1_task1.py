# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

#Steps
#function that takes tuples as an argument
#Each tuple contains (traveler_name, origin, destination).
#should have a loop
#print a formatted string for each.

tuple1= [("Alice", "New York", "London"),("Bob", "Tokyo", "San Francisco")]

def tup_function(atuple):
    x = 1
    for name, departure, arrival in tuple1:
        print(f"Itinerary {x}: {name} - From {departure} to {arrival}")
        x += 1

tup_function(tuple1)
