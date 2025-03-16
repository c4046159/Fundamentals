import json
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
    def __init__(self, filename: str = "planets_data.json"):
        self.planets: Dict[str, Planet] = {}
        self.filename = filename
        self.load_data()

    def load_data(self):
        # Data sourced from Wikipedia (https://en.wikipedia.org/wiki/Planet)
        default_data = {
            "Mercury": {"mass": 0.330, "distance": 57.9, "moons": []},
            "Venus": {"mass": 4.87, "distance": 108.2, "moons": []},
            "Earth": {"mass": 5.97, "distance": 149.6, "moons": ["Moon"]},
            "Mars": {"mass": 0.642, "distance": 227.9, "moons": ["Phobos", "Deimos"]},
            "Jupiter": {"mass": 1898, "distance": 778.6, "moons": ["Io", "Europa", "Ganymede", "Callisto"]},
            "Saturn": {"mass": 568, "distance": 1433.5, "moons": ["Titan", "Enceladus", "Mimas"]},
            "Uranus": {"mass": 86.8, "distance": 2872.5, "moons": ["Titania", "Oberon", "Umbriel"]},
            "Neptune": {"mass": 102, "distance": 4495.1, "moons": ["Triton", "Nereid"]}
        }
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = default_data
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
        
        for name, info in data.items():
            self.planets[name.lower()] = Planet(name, info["mass"], info["distance"], info["moons"])

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
