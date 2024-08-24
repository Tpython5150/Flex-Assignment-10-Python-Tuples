'''
1. Tuple Mastery in Python

Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

Intnerary 1: Alice - Form New York to London
Itinerary 2: Bob - From Tokyo to san Francisco

'''

def formatted_intineraries(intneraries):
  result = []
  for i, (traveler_name, origin, destination) in enumerate(intineraries, start = 1):
      result.append(f"Iitinerary {i}: {traveler_name} - From {origin} to {destination}")
  return "\n".join(result)
  
intineraries = [
  ("Bruce", "Chicago", "Albuquerque"),
  ("Jason", "London", "Miami")
  ]

formatted_intineraries_str = formatted_intineraries(intineraries)
print(formatted_intineraries_str)