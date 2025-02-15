import math 

#First: define the Planet class and its arguments

class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        self.name = name
        self.mass = mass  # in kilograms
        self.distance_from_sun = distance_from_sun  # in kilometers
        self.moons = moons 

    def __str__(self):
        moon_list = ', '.join(self.moons) if self.moons else 'This Planet has no moons'
        return (f"Name: {self.name}\n"
                f"Mass: {self.mass} kg\n"
                f"Distance from the Sun: {self.distance_from_sun} km\n"
                f"Moons: {moon_list}")

#Second: define the "solar system" class
class SolarSystem:
    def __init__(self):
        self.planets = {}

    def add_planet(self, planet):
        self.planets[planet.name.lower()] = planet

    def query_planet(self, name):
        planet = self.planets.get(name.lower())
        if planet:
            return str(planet)
        return f"Planet '{name}' not found."

    def planet_mass(self, name):
        planet = self.planets.get(name.lower())
        if planet:
            return f"The mass of {name} is {planet.mass} kg."
        return f"Planet '{name}' not found."

    def planet_moons_count(self, name):
        planet = self.planets.get(name.lower())
        if planet:
            return f"{name} has {len(planet.moons)} moon(s)."
        return f"Planet '{name}' not found."

    def is_planet_in_system(self, name):
        return name.lower() in self.planets

    def list_planets(self):
        return ', '.join(self.planets.keys())

solar_system = SolarSystem()
solar_system.add_planet(Planet("Mercury", 3.3011e23, 57910000, []))
solar_system.add_planet(Planet("Venus", 4.8675e24, 108200000, []))
solar_system.add_planet(Planet("Earth", 5.97237e24, 149600000, ["Moon"]))
solar_system.add_planet(Planet("Mars", 6.4171e23, 227900000, ["Phobos", "Deimos"]))
solar_system.add_planet(Planet("Jupiter", 1.8982e27, 778500000, ["Io", "Europa", "Ganymede", "Callisto"]))
solar_system.add_planet(Planet("Saturn", 5.6834e26, 1434000000, ["Titan", "Enceladus", "Mimas"]))
solar_system.add_planet(Planet("Uranus", 8.6810e25, 2871000000, ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]))
solar_system.add_planet(Planet("Neptune", 1.02413e26, 4495000000, ["Triton", "Nereid"]))

def main_menu():
    while True:
        print("\nSolar System Basic Info")
        print("1. List of planets")
        print("2. Query planet details")
        print("3. Check if a planet is in the system")
        print("4. Get planet mass")
        print("5. Get number of moons")
        print("6. Exit")

        choice = input("Choose an option:")
        if choice == "1":
            print(f"Planets: {solar_system.list_planets()}")
        elif choice == "2":
            name = input("Enter the planet name: ")
            print(solar_system.query_planet(name))
        elif choice == "3":
            name = input("Enter the planet name: ")
            print(f"{name} is in the system: {solar_system.is_planet_in_system(name)}")
        elif choice == "4":
            name = input("Enter the planet name: ")
            print(solar_system.planet_mass(name))
        elif choice == "5":
            name = input("Enter the planet name: ")
            print(solar_system.planet_moons_count(name))
        elif choice == "6":
            #implement a countdown? 
            print("Exiting Solar System Explorer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
