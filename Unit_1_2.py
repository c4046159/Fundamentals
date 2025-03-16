from typing import List, Dict

class Planet:
    def __init__(self, name: str, mass: float, distance: float, moons: List[str]):
        self.name = name
        self.mass = mass  # in 10^24 kg
        self.distance = distance  # in million km
        self.moons = moons

    def get_info(self) -> str:
        return (f"Planet: {self.name}\n"
                f"Mass: {self.mass} x 10^24 kg\n"
                f"Distance from Sun: {self.distance} million km\n"
                f"Moons: {', '.join(self.moons) if self.moons else 'None'}")

class PlanetDatabase:
    def __init__(self):
        # Hardcoded data from Wikipedia (https://en.wikipedia.org/wiki/Planet)
        self.planets: Dict[str, Planet] = {
            "mercury": Planet("Mercury", 0.330, 57.9, []),
            "venus": Planet("Venus", 4.87, 108.2, []),
            "earth": Planet("Earth", 5.97, 149.6, ["Moon"]),
            "mars": Planet("Mars", 0.642, 227.9, ["Phobos", "Deimos"]),
            "jupiter": Planet("Jupiter", 1898, 778.6, ["Io", "Europa", "Ganymede", "Callisto"]),
            "saturn": Planet("Saturn", 568, 1433.5, ["Titan", "Enceladus", "Mimas"]),
            "uranus": Planet("Uranus", 86.8, 2872.5, ["Titania", "Oberon", "Umbriel"]),
            "neptune": Planet("Neptune", 102, 4495.1, ["Triton", "Nereid"])
        }

    def get_all_info(self, planet_name: str) -> str:
        planet_name = planet_name.lower()
        if planet_name in self.planets:
            return self.planets[planet_name].get_info()
        return f"{planet_name.capitalize()} is not in the database."

    def get_mass(self, planet_name: str) -> str:
        planet_name = planet_name.lower()
        if planet_name in self.planets:
            return f"{planet_name.capitalize()} has a mass of {self.planets[planet_name].mass} x 10^24 kg"
        return f"{planet_name.capitalize()} is not in the database."

    def is_in_list(self, planet_name: str) -> str:
        planet_name = planet_name.lower()
        return f"Yes, {planet_name.capitalize()} is in the list." if planet_name in self.planets else f"No, {planet_name.capitalize()} is not in the list."

    def get_moon_count(self, planet_name: str) -> str:
        planet_name = planet_name.lower()
        if planet_name in self.planets:
            count = len(self.planets[planet_name].moons)
            return f"{planet_name.capitalize()} has {count} moon{'s' if count != 1 else ''}"
        return f"{planet_name.capitalize()} is not in the database."

def validate_input(user_input: str) -> bool:
    # Basic validation: non-empty and contains only letters and spaces
    return bool(user_input.strip() and all(c.isalpha() or c.isspace() for c in user_input))

def main():
    db = PlanetDatabase()
    
    while True:
        print("\nPlanet Information System")
        print("1. Get all info about a planet")
        print("2. Get planet mass")
        print("3. Check if planet is in list")
        print("4. Get number of moons")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4']:
            query = input("Enter planet name: ").strip()
            if not validate_input(query):
                print("Invalid input. Please use letters only.")
                continue
                
            if choice == '1':
                print(db.get_all_info(query))
            elif choice == '2':
                print(db.get_mass(query))
            elif choice == '3':
                print(db.is_in_list(query))
            elif choice == '4':
                print(db.get_moon_count(query))
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
