
class Component:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = float(price)

    def __str__(self):
        return f"{self.brand} {self.name} (${self.price:.2f})"

# FRAME
class Frame(Component):
    def __init__(self, brand, price, material, rear_travel):
        super().__init__("Frame", brand, price)
        self.material = material
        self.rear_travel = int(rear_travel)

    def __str__(self):
        return f"{self.brand} Frame - {self.material}, {self.rear_travel}mm rear travel (${self.price:.2f})"

# SUSPENSION
class Suspension(Component):
    def __init__(self, name, brand, price):
        super().__init__(name, brand, price)

class Fork(Suspension):
    def __init__(self, brand, price, travel_mm, stanchion_width):
        super().__init__("Fork", brand, price)
        self.travel_mm = int(travel_mm)
        self.stanchion_width = int(stanchion_width)

    def __str__(self):
        return f"{self.brand} Fork - {self.travel_mm}mm travel, {self.stanchion_width}mm stanchions (${self.price:.2f})"

class Shock(Suspension):
    def __init__(self, brand, price, shock_type):
        super().__init__("Shock", brand, price)
        self.shock_type = shock_type

    def __str__(self):
        return f"{self.brand} Shock - {self.shock_type} (${self.price:.2f})"

# DRIVETRAIN PARTS
class Chain(Component): pass
class Cranks(Component): pass
class Derailleur(Component): pass
class Cassette(Component): pass
class Shifter(Component): pass

# WHEELSET PARTS
class Rims(Component):
    def __init__(self, brand, price, front_size, rear_size):
        super().__init__("Rims", brand, price)
        self.front_size = front_size
        self.rear_size = rear_size

    def __str__(self):
        return f"{self.brand} Rims - Front: {self.front_size}, Rear: {self.rear_size} (${self.price:.2f})"

class Hubs(Component): pass
class Tyres(Component): pass

# BRAKES
class Brakes(Component): pass
class Rotors(Component): pass

# EXTRAS
class Extra(Component): pass



class MountainBike:
    def __init__(self, frame, fork, shock, chain, cranks, derailleur, cassette, shifter, rims, hubs, tyres, brakes, rotors, extras):
        self.frame = frame
        self.fork = fork
        self.shock = shock
        self.chain = chain
        self.cranks = cranks
        self.derailleur = derailleur
        self.cassette = cassette
        self.shifter = shifter
        self.rims = rims
        self.hubs = hubs
        self.tyres = tyres
        self.brakes = brakes
        self.rotors = rotors
        self.extras = extras

    def total_price(self):
        drivetrain_total = sum(comp.price for comp in [self.chain, self.cranks, self.derailleur, self.cassette, self.shifter])
        wheelset_total = sum(comp.price for comp in [self.rims, self.hubs, self.tyres])
        other_total = sum(comp.price for comp in [
            self.frame, self.fork, self.shock,
            self.brakes, self.rotors
        ] + self.extras)
        return drivetrain_total + wheelset_total + other_total

    def summary(self):
        print("\n====== Final MTB Build ======")
        print(f"Frame:      {self.frame}")
        print(f"Fork:       {self.fork}")
        print(f"Shock:      {self.shock}")
        print(f"Drivetrain: ${sum(comp.price for comp in [self.chain, self.cranks, self.derailleur, self.cassette, self.shifter]):.2f}")
        print(f"Wheelset:   ${sum(comp.price for comp in [self.rims, self.hubs, self.tyres]):.2f}")
        print(f"Brakes:     {self.brakes}")
        print(f"Rotors:     {self.rotors}")
        print("Extras:")
        for extra in self.extras:
            print(f"  - {extra}")
        print(f"\nTotal Price: ${self.total_price():,.2f}")
        print("=============================")



def input_number(prompt, allow_float=False):
    while True:
        try:
            value = input(prompt + ": ")
            return float(value) if allow_float else int(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_from_menu(title, options):
    print(f"\n{title}")
    for i, opt in enumerate(options, 1):
        print(f"{i}: {opt}")
    print(f"{len(options)+1}: Other")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            elif choice == len(options) + 1:
                return input("Enter custom value: ")
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")


def validate_component(component):
    return True

def backup_build(bike):
    print("\n[Stub] Simulated backup: Build not yet saved to file.")


def main():
    print("\nWelcome to the MTB Builder")

    frame = Frame(
        brand=input("Frame brand: "),
        price=input_number("Frame price", allow_float=True),
        material=choose_from_menu("Choose frame material", ["Carbon", "Aluminium", "Steel", "Titanium"]),
        rear_travel=input_number("Rear travel (mm)")
    )

    fork = Fork(
        brand=choose_from_menu("Choose fork brand", ["RockShox", "Fox", "\u00d6hlins", "Cane Creek"]),
        price=input_number("Fork price", allow_float=True),
        travel_mm=input_number("Fork travel (mm)"),
        stanchion_width=input_number("Stanchion width (mm)")
    )

    shock = Shock(
        brand=choose_from_menu("Choose shock brand", ["RockShox", "Fox", "\u00d6hlins", "Cane Creek"]),
        price=input_number("Shock price", allow_float=True),
        shock_type=choose_from_menu("Choose shock type", ["Coil", "Air"])
    )

    chain = Chain("Chain", choose_from_menu("Choose chain brand", ["Shimano", "SRAM"]), input_number("Chain price", True))
    cranks = Cranks("Cranks", choose_from_menu("Choose cranks brand", ["SRAM", "Shimano"]), input_number("Cranks price", True))
    derailleur = Derailleur("Derailleur", choose_from_menu("Choose derailleur brand", ["Shimano", "SRAM"]), input_number("Derailleur price", True))
    cassette = Cassette("Cassette", choose_from_menu("Choose cassette brand", ["Shimano", "SRAM"]), input_number("Cassette price", True))
    shifter = Shifter("Shifter", choose_from_menu("Choose shifter brand", ["Shimano", "SRAM"]), input_number("Shifter price", True))

    rims = Rims(
        brand=choose_from_menu("Choose rim brand", ["DT Swiss", "Spank", "Stans", "Industry Nine"]),
        price=input_number("Rim price", allow_float=True),
        front_size=choose_from_menu("Choose front wheel size", ["26\"", "27.5\"", "29\""]),
        rear_size=choose_from_menu("Choose rear wheel size", ["26\"", "27.5\"", "29\""])
    )

    hubs = Hubs("Hubs", choose_from_menu("Choose hub brand", ["Hope", "DT Swiss", "Industry Nine"]), input_number("Hub price", True))
    tyres = Tyres("Tyres", choose_from_menu("Choose tyre brand", ["Maxxis", "Schwalbe", "Michelin"]), input_number("Tyres price (front and rear)", True))

    brakes = Brakes("Brakes", choose_from_menu("Choose brake brand", ["Shimano", "SRAM", "Magura", "Hope"]), input_number("Brakes price (front and rear)", True))
    rotors = Rotors("Rotors", choose_from_menu("Choose rotor brand", ["Shimano", "SRAM", "Hope", "Galfer"]), input_number("Rotors price (front and rear)", True))

    extras = []
    print("\nAdd extras (e.g., handlebar, seat, stem, dropper post, grips). Type 'done' to finish.")
    while True:
        name = input("Extra name (or 'done'): ")
        if name.lower() == 'done':
            break
        brand = input(f"{name} brand: ")
        price = input_number(f"'{name}' price", allow_float=True)
        extras.append(Extra(name, brand, price))

    bike = MountainBike(frame, fork, shock, chain, cranks, derailleur, cassette, shifter, rims, hubs, tyres, brakes, rotors, extras)

    if all(validate_component(comp) for comp in [
        frame, fork, shock, chain, cranks, derailleur, cassette, shifter,
        rims, hubs, tyres, brakes, rotors
    ]):
        bike.summary()
        backup_build(bike)
    else:
        print("One or more components failed validation.")

if __name__ == "__main__":
    main()
