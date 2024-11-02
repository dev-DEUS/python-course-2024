# Defining a basic class with a constructor
class Laptop:
    # Constructor method (__init__) initializes the instance of the class
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable for brand
        self.model = model  # Instance variable for model

    # A simple method that prints a statement
    def start_vs_code(self):
        print("Starting VS Code")

    # A method that returns a formatted string with the brand and model
    def get_specs(self):
        return f"Laptop Brand: {self.brand}, Model: {self.model}"

    # A method that accepts unlimited arguments
    def install_apps(self, *apps):
        print("Installing the following apps:")
        for app in apps:
            print(f"- {app}")

    # A method with keyword arguments (key-value pairs)
    def update_settings(self, **settings):
        print("Updating settings:")
        for key, value in settings.items():
            print(f"{key}: {value}")

# Creating an object of the Laptop class
my_laptop = Laptop("Dell", "XPS 15")

# Using the start_vs_code method
my_laptop.start_vs_code()

# Getting the laptop specifications
print(my_laptop.get_specs())

# Installing multiple applications using the method with unlimited arguments
my_laptop.install_apps("Python", "VS Code", "Git")

# Updating settings using the method with keyword arguments
my_laptop.update_settings(theme="Dark Mode", resolution="1920x1080")

# Example of another class showcasing inheritance
class GamingLaptop(Laptop):
    # Constructor that extends the base class
    def __init__(self, brand, model, gpu):
        super().__init__(brand, model)  # Calls the constructor of the parent class
        self.gpu = gpu  # Adds a new instance variable for the GPU

    # Method to print gaming-specific features
    def display_gaming_specs(self):
        print(f"{self.get_specs()}, GPU: {self.gpu}")

# Creating an object of the GamingLaptop class
my_gaming_laptop = GamingLaptop("Asus", "ROG Zephyrus", "NVIDIA RTX 3080")

# Displaying gaming specifications
my_gaming_laptop.display_gaming_specs()