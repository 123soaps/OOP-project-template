Describe and explain how you used a range of OOP principles in your project. For each principle, include a very small code snippet that highlights the principle.

- Classes
I created many individual classes to represent all important mountain bike components. For example, Fork, Shock, Frame, Chain, and    MountainBike were all structured as separate classes, which helped break the project into logical parts and made the code easier to manage and expand.

class Suspension(Component):
    def __init__(self, name, brand, price):
        super().__init__(name, brand, price)


- Constructors
Each class uses a constructor (__init__) to initialise attributes like brand, price, or travel_mm when a component is created. This allowed user input to be directly assigned to object properties when constructing the virtual bike.

def __init__(self, brand, price, travel_mm, stanchion_width):
    super().__init__("Fork", brand, price)
    self.travel_mm = int(travel_mm)
    self.stanchion_width = int(stanchion_width)

  
- Methods
I used methods like total_price() and summary() in the MountainBike class to calculate and display the build summary. These methods help encapsulate functionality and reduce repetition.

def total_price(self):
    drivetrain_total = sum(comp.price for comp in [self.chain, self.cranks, ...])
    return drivetrain_total + ...


- Objects
Throughout the build process, I created and worked with objects of each component class. These objects were passed into the MountainBike class to assemble the full build.

shock = Shock("Fox", 450, "Coil")


- Inheritance
I used inheritance to avoid repeating code. For example, Fork and Shock both inherit from Suspension, which itself inherits from Component, allowing them to automatically have attributes like brand and price without redefining them. The component class also has all of the atributes that classes like Chain need meaning they do not need any extra lines of code at all. 

class Chain(Component): pass


- Polymorphism
I used polymorphism when handling different types of components (like extras) in the same way. All components share the __str__ method from Component, so I could loop through them and display details consistently.

for extra in self.extras:
    print(f"  - {extra}")


- Generalisation
I generalised all bike components under a single base class called Component. This reduced redundancy and allowed me to apply common functionality across forks, shocks, rims, cranks, and other parts.

class Component:
  def __init__(self, name, brand, price):
      self.name = name
      self.brand = brand
      self.price = float(price)

  def __str__(self):
      return f"{self.brand} {self.name} (${self.price:.2f})"

class Suspension(Component):
  def __init__(self, name, brand, price):
      super().__init__(name, brand, price)
