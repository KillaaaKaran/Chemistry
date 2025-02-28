elements_atomic_number = {
    "Hydrogen": 1, "H": 1,
    "Helium": 2, "He": 2,
    "Lithium": 3, "Li": 3,
    "Beryllium": 4, "Be": 4,
    "Boron": 5, "B": 5,
    "Carbon": 6, "C": 6,
    "Nitrogen": 7, "N": 7,
    "Oxygen": 8, "O": 8,
    "Fluorine": 9, "F": 9,
    "Neon": 10, "Ne": 10,
    "Sodium": 11, "Na": 11,
    "Magnesium": 12, "Mg": 12,
    "Aluminum": 13, "Al": 13,
    "Silicon": 14, "Si": 14,
    "Phosphorus": 15, "P": 15,
    "Sulfur": 16, "S": 16,
    "Chlorine": 17, "Cl": 17,
    "Argon": 18, "Ar": 18,
    "Potassium": 19, "K": 19,
    "Calcium": 20, "Ca": 20,
    "Scandium": 21, "Sc": 21,
    "Titanium": 22, "Ti": 22,
    "Vanadium": 23, "V": 23,
    "Chromium": 24, "Cr": 24,
    "Manganese": 25, "Mn": 25,
    "Iron": 26, "Fe": 26,
    "Cobalt": 27, "Co": 27,
    "Nickel": 28, "Ni": 28,
    "Copper": 29, "Cu": 29,
    "Zinc": 30, "Zn": 30,
    "Gallium": 31, "Ga": 31,
    "Germanium": 32, "Ge": 32,
    "Arsenic": 33, "As": 33,
    "Selenium": 34, "Se": 34,
    "Bromine": 35, "Br": 35,
    "Krypton": 36, "Kr": 36,
    "Rubidium": 37, "Rb": 37,
    "Strontium": 38, "Sr": 38,
    "Yttrium": 39, "Y": 39,
    "Zirconium": 40, "Zr": 40,
    "Niobium": 41, "Nb": 41,
    "Molybdenum": 42, "Mo": 42,
    "Technetium": 43, "Tc": 43,
    "Ruthenium": 44, "Ru": 44,
    "Rhodium": 45, "Rh": 45,
    "Palladium": 46, "Pd": 46,
    "Silver": 47, "Ag": 47,
    "Cadmium": 48, "Cd": 48,
    "Indium": 49, "In": 49,
    "Tin": 50, "Sn": 50,
    "Antimony": 51, "Sb": 51,
    "Tellurium": 52, "Te": 52,
    "Iodine": 53, "I": 53,
    "Xenon": 54, "Xe": 54,
    "Cesium": 55, "Cs": 55
}

# Function to parse the charge input
def parse_charge(charge_input):
    """Parse the charge input to return the integer value."""
    if charge_input.startswith('+'):
        return int(charge_input[1:])
    elif charge_input.startswith('-'):
        return -int(charge_input[1:])
    else:
        # Handle cases where the charge might just be a number with no sign (like '3')
        return int(charge_input)

while True:
    user_input = input("Enter element (or type 'quit' to exit): ")
    
    if user_input.lower() == "quit":
        break
    
    if user_input in elements_atomic_number:
        atomic_number = elements_atomic_number[user_input]
        print(f"{user_input} has atomic number {atomic_number}")

        charge_input = input("Enter charge (e.g., +2, -1, 3+, etc.): ")
        try:
            charge = parse_charge(charge_input)
            print(f"The charge is: {charge}")

            # Calculate number of electrons based on atomic number and charge
            number_of_electrons = atomic_number - charge
            
            # Print the final number of electrons
            print(f"Number of electrons = {number_of_electrons}")
        
        except ValueError:
            print("Invalid charge input. Please enter a valid charge (e.g., +2, -1, etc.).")
    else:
        print("Element not recognized. Please try again.")
