"""
Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:

planets = [[‘Mercury’, ‘Venus’, ‘Earth’], [‘Mars’, ‘Jupiter’, ‘Saturn’], [‘Uranus’, ‘Neptune’, ‘Pluto’]]

Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]
"""
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
print(flatten_planets)
