print("Welcome. Please use this calculator if your thin-film coating is over 1 micron thick and uses two different materials.")
#Material Young's Modulus (in MPa)
Y_Al2O3 = 60000
Y_HfO2 = 120000
Y_Ta2O5 = 136000
Y_Nb2O5 = 130000
Y_SiO2 = 87000
Y_Nb = 105000
Y_Y2O3 =205000
Y_Ag = 74000
Y_Ge = 103000
Y_Hf = 140000
Y_MgF2 = 138000
y_Al2O3 = 60000
y_HfO2 = 120000
y_Ta2O5 = 136000
y_Nb2O5 = 130000
y_SiO2 = 87000
y_Nb = 105000
y_Y2O3 = 205000
y_Ag = 74000
y_Ge = 103000
y_Hf = 140000
y_MgF2 = 138000

#Poisson Ratio of Material (lower case is for higher index; upper case is for lower index)
p_Al2O3 = float(0.36)
p_HfO2 = float(0.22)
p_Ta2O5 = float(0.27)
p_Nb2O5 = float(0.22)
p_SiO2 = float(0.11)
p_Nb = float (0.40)
p_Y2O3 = float(0.31)
p_Ag = float(0.365)
p_Ge = float(0.27)
p_Hf = float(0.26)
p_MgF2 = float(0.276)
P_Al2O3 = float(0.36)
P_HfO2 = float(0.22)
P_Ta2O5 = float(0.27)
P_Nb2O5 = float(0.22)
P_SiO2 = float(0.11)
P_Nb = float(0.40)
P_Y2O3 = float(0.31)
P_Ag = float (0.365)
P_Ge = float(0.27)
P_Hf = float(0.26)
P_MgF2 = float(0.276)

#Young's modulus (in MPa)
E_FS = 73000
E_Si = 130000
E_CaF2 = 75800
E_SiC = 410000
E_HK9L = 79200
E_Sapphire = 345000
E_NBK7 = 82000
E_TIH6 = 93100
E_ZnS = 74500
E_Zerodur = 90300
E_ZnSe = 67200
E_ULE = 67600

#Poisson ratio
nu_FS = float(0.17)
nu_Si = float(0.28)
nu_CaF2 = float(0.26)
nu_SiC = float(0.19) 
nu_HK9L = float(0.211)
nu_Sapphire = float(0.29)
nu_NBK7 = float(0.206)
nu_TIH6 = float(0.261)
nu_ZnS = float(0.27)
nu_Zerodur = float(0.24)
nu_ZnSe = float(0.28)
nu_ULE = float(0.17)

#Our first loop is to get the first material type
while True:
    material_type1 = input("What is the material with the higher index of refraction: ")
    if material_type1 == "Al2O3":
        Y_sub = Y_Al2O3
        p_sub = p_Al2O3
        break
    elif material_type1 == "HfO2":
        Y_sub = Y_HfO2
        p_sub = p_Al2O3
        break
    elif material_type1 == "Ta2O5":
        Y_sub = Y_Ta2O5
        p_sub = p_Ta2O5
        break
    elif material_type1 == "Nb2O5":
        Y_sub = Y_Nb2O5
        p_sub = p_Nb2O5
        break
    elif material_type1 == "SiO2":
        Y_sub = Y_SiO2
        p_sub = p_SiO2
        break
    elif material_type1 == "Nb":
        Y_sub = Y_Nb
        p_sub = p_Nb
        break
    elif material_type1 == "Y2O3":
        Y_sub = Y_Y2O3
        p_sub = p_Y2O3
        break
    elif material_type1 == "Ag":
        Y_sub = Y_Ag
        p_sub = p_Ag
        break
    elif material_type1 == "Ge":
        Y_sub = Y_Ge
        p_sub = p_Ge
        break
    elif material_type1 == "Hf":
        Y_sub = Y_Hf
        p_sub = p_Hf
        break
    elif material_type1 == "MgF2":
        Y_sub = Y_MgF2
        p_sub = p_MgF2
        break
    else:
        print("Not a recognized material. Please try again.")
#We now get the second material information
while True:
    material_type2 = input("What is the material with the lower index of refraction: ")
    if material_type2 == "Al2O3":
        y_sub = y_Al2O3
        P_sub = P_Al2O3
        break
    elif material_type2 == "HfO2":
        y_sub = y_HfO2
        P_sub = P_HfO2
        break
    elif material_type2 == "Ta2O5":
        y_sub = y_Ta2O5
        P_sub = P_Ta2O5
        break
    elif material_type2 == "Nb2O5":
        y_sub = y_Nb2O5
        P_sub = P_Nb2O5
        break
    elif material_type2 == "SiO2":
        y_sub = y_SiO2
        p_sub = p_SiO2
        break
    elif material_type2 == "Nb":
        y_sub = y_Nb
        P_psub = P_Nb
        break
    elif material_type2 == "Ag":
        y_sub = y_Ag
        P_sub = P_Ag
        break
    elif material_type2 == "Ge":
        y_sub = y_Ge
        P_sub = P_Ge
        break
    elif material_type2 == "Hf":
        y_sub = y_Hf
        P_sub = P_Hf
        break
    elif material_type2 == "MgF2":
        y_sub = y_MgF2
        P_sub = P_MgF2
        break
    else:
        print("Not a recognized material. Please try again.")
#Thickness ratio loop
while True:
    try:
        thickness_ratio = float(input("What is the thickness ratio: "))
        break
    except ValueError:
        print("Not a number. Please try again.")
high_index_percent = float(thickness_ratio/ (thickness_ratio + 1))
low_index_percent = float(1 / (thickness_ratio + 1))

#Film Young Modulus and film Poisson ratio
film_young = float((high_index_percent * Y_sub) + (low_index_percent * y_sub))
film_poisson = float((high_index_percent * p_sub) + (low_index_percent * p_sub))


#Substrate input and selection loop
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

#M ratio
mf = float(film_young / ((1-film_poisson)))
ms = float(E_sub /((1-nu_sub)))
  
#Thickness of substrate and film [mm] selection
while True:
    try:        
        t_sub = float(input("What is the thickness of the substrate(in mm): " ))
        break
    except ValueError:
        print("Not a number. Please try again.")
t_sub = t_sub/1000
while True:
    try:
        t_film = float(input("What is the thickness of the film (in um): "))
        break
    except ValueError:
        print("Not a number. Please try again.")
t_film = float(t_film/1000000)
if t_film <= float(5/1000000):
    print("Please make sure that a stress wafer was used.")
#radius of curvature loop
while True:
    try:    
        radius_curvature = float(input("What is the radius of curvature: "))
        break
    except ValueError:
        print("Not a number. Please try again.")
#stress calculation
stress = (ms * (t_sub**2) * (1 + (4 * (t_film / t_sub) * (mf/ms)) + (6*(t_film / t_sub)**2) * (mf/ms) + (4 * (t_film / t_sub)**3 * (mf/ms)) + ((t_film / t_sub)**4 * (mf/ms)**2)))/(6*(1.0+ (t_film / t_sub))*radius_curvature *t_film)

print("The Stress is: ", stress, "MPa.\n")
print("Please note that a negative result means the stress is compressive and a positive result means the stress is tensile.")
