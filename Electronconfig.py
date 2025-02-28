print("Welcome to Karan's electronic configuration calculator <3 leave a review on github if you want.")
# Dictionary with elements, their electron configuration, and number of electrons.
elements = {
    "hydrogen": ("1s¹", 1), "Hydrogen": ("1s¹", 1), "H": ("1s¹", 1),
    "helium": ("1s²", 2), "Helium": ("1s²", 2), "He": ("1s²", 2),
    "lithium": ("1s² 2s¹", 3), "Lithium": ("1s² 2s¹", 3), "Li": ("1s² 2s¹", 3),
    "beryllium": ("1s² 2s²", 4), "Beryllium": ("1s² 2s²", 4), "Be": ("1s² 2s²", 4),
    "boron": ("1s² 2s² 2p¹", 5), "Boron": ("1s² 2s² 2p¹", 5), "B": ("1s² 2s² 2p¹", 5),
    "carbon":  ("1s² 2s² 2p²", 6), "Carbon":  ("1s² 2s² 2p²", 6), "C": ("1s² 2s² 2p²", 6),
    "nitrogen": ("1s² 2s² 2p³", 7), "Nitrogen": ("1s² 2s² 2p³", 7), "N": ("1s² 2s² 2p³", 7),
    "oxygen": ("1s² 2s² 2p⁴", 8), "Oxygen": ("1s² 2s² 2p⁴", 8), "O": ("1s² 2s² 2p⁴", 8),
    "flourine": ("1s² 2s² 2p⁵", 9), "Flourine": ("1s² 2s² 2p⁵", 9), "F": ("1s² 2s² 2p⁵", 9),
    "neon": ("1s² 2s² 2p⁶", 10), "Neon": ("1s² 2s² 2p⁶", 10), "Ne": ("1s² 2s² 2p⁶", 10),
    "sodium": ("1s² 2s² 2p⁶ 3s¹", 11), "Sodium": ("1s² 2s² 2p⁶ 3s¹", 11), "Na": ("1s² 2s² 2p⁶ 3s¹", 11),
    "magnesium": ("1s² 2s² 2p⁶ 3s²", 12), "Magnesium": ("1s² 2s² 2p⁶ 3s²", 12), "Mg": ("1s² 2s² 2p⁶ 3s²", 12),
    "aluminium": ("1s² 2s² 2p⁶ 3s² 3p¹", 13), "Aluminium": ("1s² 2s² 2p⁶ 3s² 3p¹", 13), "Al": ("1s² 2s² 2p⁶ 3s² 3p¹", 13),
    "silicon": ("1s² 2s² 2p⁶ 3s² 3p²", 14), "Silicon": ("1s² 2s² 2p⁶ 3s² 3p²", 14), "Si": ("1s² 2s² 2p⁶ 3s² 3p²", 14),
    "phosphorous": ("1s² 2s² 2p⁶ 3s² 3p³", 15), "Phosphorous": ("1s² 2s² 2p⁶ 3s² 3p³", 15), "P": ("1s² 2s² 2p⁶ 3s² 3p³", 15),
    "sulfur": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16), "Sulfur": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16), "sulphur": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16), "Sulphur": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16), "S": ("1s² 2s² 2p⁶ 3s² 3p⁴", 16),
    "chlorine": ("1s² 2s² 2p⁶ 3s² 3p⁵", 17), "Chlorine": ("1s² 2s² 2p⁶ 3s² 3p⁵", 17), "Cl": ("1s² 2s² 2p⁶ 3s² 3p⁵", 17),
    "argon": ("1s² 2s² 2p⁶ 3s² 3p⁶", 18), "Argon": ("1s² 2s² 2p⁶ 3s² 3p⁶", 18), "Ar": ("1s² 2s² 2p⁶ 3s² 3p⁶", 18),
    "potassium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 19), "Potassium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 19), "K": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 19),
    "calcium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 20), "Calcium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 20), "Ca": ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 20),
    "scandium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹ 4s²", 21), "Scandium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹ 4s²", 21), "Sc": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹ 4s²", 21),
    "titanium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d² 4s²", 22), "Titanium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d² 4s²", 22), "Ti": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d² 4s²", 22),
    "vanadium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d³ 4s²", 23), "Vanadium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d³ 4s²", 23), "V": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d³ 4s²", 23),
    "chromium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s¹", 24), "Chromium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s¹", 24), "Cr": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s¹", 24), #Anomoly only shows when oxidation state is 0
    "magnanese": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s²", 25), "Magnanese": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s²", 25), "Mn": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s²", 25),
    "iron": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", 26), "Iron": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", 26), "Fe": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", 26),
    "cobalt": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷ 4s²", 27), "Cobalt": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷ 4s²", 27), "Co": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷ 4s²", 27),
    "nickel": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸ 4s²", 28), "Nickel": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸ 4s²", 28), "Ni": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸ 4s²", 28),
    "copper": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s¹", 29), "Copper": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s¹", 29), "Cu": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s¹", 29), # Anomoly only shows when oxidation state is 0
    "zinc": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 30), "Zinc": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 30), "Zn": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 30),
    "gallium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p¹", 31), "Gallium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p¹", 31), "Ga": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p¹", 31),
    "germanium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p²", 32), "Germanium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p²", 32), "Ge": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p²", 32),
    "arsenic": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p³", 33), "Arsenic": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p³", 33), "As": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p³", 33),
    "selenium":("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁴", 34), "Selenium":("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁴", 34), "Se": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁴", 34),
    "bromine": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁵", 35), "Bromine": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁵", 35), "Br": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁵", 35),
    "krypton": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶", 36), "Krypton": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶", 36), "Kr": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶", 36),
    "rubidium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s¹", 37), "Rubidium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s¹", 37), "Rb": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s¹", 37),
    "strontium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s²", 38), "Strontium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s²", 38), "Sr": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s²", 38),
    "yttrium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹ 5s²", 39), "Yttrium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹ 5s²", 39), "Y": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹ 5s²", 39),
    "zirconium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d² 5s²", 40), "Zirconium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d² 5s²", 40), "Zr": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d² 5s²", 40),
    "niobium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁴ 5s¹", 41), "Niobium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁴ 5s¹", 41), "Nb": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁴ 5s¹", 41),
    "molybdenum": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s¹", 42), "Molybdenum": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s¹", 42), "Mo": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s¹", 42),
    "technetium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s²", 43), "Technetium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s²", 43), "Tc": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁵ 5s²", 43),
    "ruthenium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁷ 5s¹", 44), "Ruthenium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁷ 5s¹", 44), "Ru": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁷ 5s¹", 44),
    "rhodium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁸ 5s¹", 45), "Rhodium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁸ 5s¹", 45), "Rh": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d⁸ 5s¹", 45),
    "palladium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰", 46), "Palladium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰", 46), "Pd": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰", 46),
    "silver": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s¹", 47), "Silver": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s¹", 47), "Ag": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s¹", 47),
    "cadmium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s²", 48), "Cadmium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s²", 48), "Cd": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s²", 48),
    "indium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p¹", 49), "Indium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p¹", 49), "In": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p¹", 49),
    "tin": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p²", 50), "Tin": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p²", 50), "Sn": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p²", 50),
    "antimony": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p³", 51), "Antimony": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p³", 51), "Sb": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p³", 51),
    "tellurium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁴", 52), "Tellurium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁴", 52), "Te": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁴", 52),
    "iodine": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁵", 53), "Iodine": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁵", 53), "I": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁵", 53),
    "xenon": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶", 54), "Xenon": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶", 54), "Xe": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶", 54),
    "caesium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s¹", 55), "Caesium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s¹", 55), "Cs": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s¹", 55),
    "barium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s²", 56), "Barium": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s²", 56), "Ba": ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 6s²", 56),
}

# Superscript map for electron configuration notation
superscript_map = {
    '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰'
}

def abs_charge(charge_input): ##the charge input to return the integer value idk how to do this so chatgpt did this bit
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
    user_input = input("Enter element (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        break

    if user_input in elements:
        config, electron_count = elements[user_input]
        print(f"Original configuration of {user_input}: {config} ({electron_count} electrons)")
    else:
        print("Element not recognized.")
        continue

    charge_input = input("Enter oxidation state: (e.g., +2, -1, etc.): ")
    charge = abs_charge(charge_input)

    adjusted_electrons = adjust_electron_count(electron_count, charge)
    new_configuration = fill_orbitals(adjusted_electrons)

    print(f"New configuration of {user_input} with charge {charge_input}: {new_configuration} ({adjusted_electrons} electrons)")


if user_input.lower() == "quit":
    print("Thank you for using this. <3 By Karan")

if user_input.upper() == "QUIT":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "Quit":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "Exit":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "exit":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "EXIT":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "Exit":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "exit":
    print("Thank you for using this. <3 By Karan")

if user_input.casefold() == "EXIT":
    print("Thank you for using this. <3 By Karan")
