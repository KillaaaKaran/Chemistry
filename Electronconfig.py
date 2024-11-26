# Dictionary with elements, their electron configuration, and number of electrons.
elements = {
    "H": ("1s¹", 1),
    "He": ("1s²", 2),
    "Li": ("1s² 2s¹", 3),
    "Be": ("1s² 2s²", 4),
    "B": ("1s² 2s² 2p¹", 5),
    "C": ("1s² 2s² 2p²", 6),
    "N": ("1s² 2s² 2p³", 7),
    "O": ("1s² 2s² 2p⁴", 8),
    "F": ("1s² 2s² 2p⁵", 9),
    "Ne": ("1s² 2s² 2p⁶", 10),
    "Na": ("1s² 2s² 2p⁶ 3s¹", 11),
    "Mg": ("1s² 2s² 2p⁶ 3s²", 12),
    "Al": ("1s² 2s² 2p⁶ 3s² 3p¹", 13),
    "Si": ("1s² 2s² 2p⁶ 3s² 3p²", 14),
    "P": ("1s² 2s² 2p⁶ 3s² 3p³", 15),
    "S": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16),
    "Cl": ("1s² 2s² 2p⁶ 3s² 3p⁵", 17),
    "Ar": ("1s² 2s² 2p⁶ 3s² 3p⁶", 18),
    "K": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 19),
    "Ca": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 20),
    "Sc": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹ 4s²", 21),
    "Ti": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d² 4s²", 22),
    "V": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d³ 4s²", 23),
    "Cr": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s¹", 24), #Anomoly
    "Mn": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s²", 25),
    "Fe": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", 26),
    "Co": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷ 4s²", 27),
    "Ni": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸ 4s²", 28),
    "Cu": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s¹", 29), # Anomoly
    "Zn": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 30),
    "Ga": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p¹", 31),
    "Ge": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p²", 32),
}

# Superscript map for electron configuration notation
superscript_map = {
    '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰'
}

def parse_charge(charge_input): ##the charge input to return the integer value idk how to do this so chatgpt did this bit
    if charge_input.startswith('+'):
        return int(charge_input[1:])
    elif charge_input.startswith('-'):
        return -int(charge_input[1:])
    return 0

def adjust_electron_count(base_electrons, charge):
    return base_electrons - charge

def to_superscript(number):#    Convert a number to its superscript representation.
    return ''.join(superscript_map[digit] for digit in str(number))

def fill_orbitals(adjusted_electrons):
    """Fill the orbitals with the adjusted number of electrons."""
    configuration = ""
    remaining_electrons = adjusted_electrons
    orbitals = {
        "1s": 2, "2s": 2, "2p": 6,
        "3s": 2, "3p": 6, "4s": 2,
        "3d": 10, "4p": 6, "5s": 2,
        "4d": 10, "5p": 6, "6s": 2,
        "4f": 14, "5d": 10, "6p": 6
    }

    for orbital, max_electrons in orbitals.items():
        if remaining_electrons <= 0:
            break
        if remaining_electrons >= max_electrons:
            configuration += f"{orbital}{to_superscript(max_electrons)} "
            remaining_electrons -= max_electrons
        else:
            configuration += f"{orbital}{to_superscript(remaining_electrons)} "
            remaining_electrons = 0

    return configuration.strip()

while True:
    user_input = input("Enter element symbol (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        break

    if user_input in elements:
        config, electron_count = elements[user_input]
        print(f"Original configuration of {user_input}: {config} ({electron_count} electrons)")
    else:
        print("Element not recognized.")
        continue

    charge_input = input("Enter oxidation state: (e.g., +2, -1, etc.): ")
    charge = parse_charge(charge_input)

    adjusted_electrons = adjust_electron_count(electron_count, charge)
    new_configuration = fill_orbitals(adjusted_electrons)

    print(f"New configuration of {user_input} with charge {charge_input}: {new_configuration} ({adjusted_electrons} electrons)")


if user_input.lower() == "quit":
        print("Thank you for using this. <3 By Karan")

if user_input.upper() == "QUIT":
        print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "Quit":
        print("Thank you for using this. <3 By Karan")