print("Welcome! Please use this calculator if your thin-film coating is under 1 micron thick and/or only has one material used in the thin film.")
#Young's modulus (in MPa)
E_FS = 73000
E_Si = 130000
E_CaF2 = 75800
E_SiC = 410000
E_HK9L = 79200
E_Sapphire = 345000
E_NBK7 = 82000
E_TIH6 = 93100
E_ZnS = 70300
E_Zerodur = 90300
E_ZnSe = 67200
E_ULE = 67600

#Poisson ratio
nu_FS = 0.17
nu_Si = 0.28
nu_CaF2 = 0.26
nu_SiC = 0.19 
nu_HK9L = 0.211
nu_Sapphire = 0.29
nu_NBK7 = 0.206
nu_TIH6 = 0.261
nu_ZnS = 0.28
nu_Zerodur = 0.24
nu_ZnSe = 0.28
nu_ULE = 0.17

#Substrate loop 
#We get user input and we select the saved data. If it is not found, we prompt the user to try again. 
while True:
    substrate_type = input("What is the glass type: ")
    if substrate_type == "Fused Silica" :
        E_sub = E_FS
        nu_sub = nu_FS
        break
    elif substrate_type == "Silicon":
        E_sub = E_Si
        nu_sub = nu_Si
        break
    elif substrate_type == "CaF2":
        E_sub = E_CaF2
        nu_sub = nu_CaF2
        break
    elif substrate_type == "SiC":
        E_sub = E_SiC
        nu_sub = nu_SiC
        break
    elif substrate_type == "H-K9L":
        E_sub = E_HK9L
        nu_sub = nu_HK9L
        break
    elif substrate_type == "Sapphire":
        E_sub = E_Sapphire
        nu_Sapphire
        break
    elif substrate_type == "NBK7":
        E_sub = E_NBK7
        nu_sub = nu_NBK7
        break
    elif substrate_type == "TIH6":
        E_sub = E_TIH6
        nu_sub = nu_TIH6
        break
    elif substrate_type == "ZnS":
        E_sub = E_ZnS
        nu_sub = nu_ZnS
        break
    elif substrate_type == "Zerodur":
        E_sub = E_Zerodur
        nu_sub = nu_Zerodur
        break
    elif substrate_type == "ZnSe":
        E_sub = E_ZnSe
        nu_sub = nu_ZnSe
        break
    elif substrate_type == "ULE":
        E_sub = E_ULE
        nu_sub = nu_ULE
        break
    else:
        print("Not a recognized glass type. Please try again.")


#Thickness of substrate. We make it a loop to see if the user input is a number or not
while True:
    try:
        t_sub = float(input("What is the thickness of the substrate(in mm): " ))
        break
    except ValueError:
        print("Not a number. Please try again.")
#here we convert the user input of th substrate thickness from mm to m by dividing by 1000
t_sub = t_sub/1000
#Film thickness loop. We make it a loop to see if the user input is a number or not
while True:
    try:
        t_film = float(input("What is the thickness of the film (in um): "))
        break
    except ValueError:
        print("Not a number. Please try again.")
#Here we convert the user input from the film thickness in um to m by dividing by 1000000
t_film = t_film/1000000
#we add a note to prompt the user to look and see if a stress wafer was used for maximum accuracy
if t_film <= float(5/1000000):
    print("Please make sure that a stress wafer was used.")
#radius of curvature loop. We make it a loop to see if the user input is a number
while True:
    try:
        radius_curvature = float(input("What is the radius of curvature: "))
        break
    except ValueError:
        print("Not a number. Please try again.")
#Finally we get to Stoney's Equation
stress = (E_sub * t_sub**2)/(6*(1.0-nu_sub)*radius_curvature*t_film)

print("The Stress is: ", stress, "MPa.\n")
print("Please note that a negative result means the stress is compressive and a positive result means the stress is tensile.")
