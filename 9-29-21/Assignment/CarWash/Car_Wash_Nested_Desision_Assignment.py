print("Car Wash Menu: ")
print("1 - Car")
print("2 - Pickup")
print("3 - Minivan")

vType = input("Select your vehicle type (1, 2, 3): ")

if vType != "1" and vType != "2" and vType != "3":
    print("Wrong Number Entered! I Haven't Learned While Loops, Just Restart The Program!")
else:
    wax = input("Do you want Wax? (Y/N): ")
    wheelShine = input("Do you want wheel shine? (Y?N): ")
    rustInhibitor = input("Do you want Rust Inhibitor? (Y/N): ")

    totalPrice = 0

    if vType == "1":
        print("-----------------------------")
        print("Vehicle Type:             Car")
        totalPrice += 6
        #Wax
        if wax == "Y":
            print("Wax:                   Seleted")
            totalPrice += 1
        else:
            print("Wax:             Not Selected")
        #Wheel Shine  
        if wheelShine == "Y":
            print("Wheel Shine:           Seleted")
            totalPrice += 2
        else:
            print("Wheel Shine:     Not Selected")
        #Rust Inhibitor  
        if rustInhibitor == "Y":
            print("Rust Inhibitor:        Seleted")
            totalPrice += 3
        else:
            print("Rust Inhibitor:  Not Selected")
    elif vType == "2":
        print("-----------------------------")
        print("Vehicle Type:          Pickup")
        totalPrice += 9
        #Wax
        if wax == "Y":
            print("Wax:                Seleted")
            totalPrice += 2
        else:
            print("Wax:            Not Selected")
        #Wheel Shine  
        if wheelShine == "Y":
            print("Wheel Shine:         Seleted")
            totalPrice += 4
        else:
            print("Wheel Shine:     Not Selected")
        #Rust Inhibitor  
        if rustInhibitor == "Y":
            print("Rust Inhibitor:       Seleted")
            totalPrice += 3
        else:
            print("Rust Inhibitor:   Not Selected")
    elif vType == "3":
        print("-----------------------------")
        print("Vehicle Type:         Minivan")
        totalPrice += 8
        #Wax
        if wax == "Y":
            print("Wax:                   Seleted")
            totalPrice += 2
        else:
            print("Wax:             Not Selected")
        #Wheel Shine  
        if wheelShine == "Y":
            print("Wheel Shine:            Seleted")
            totalPrice += 3
        else:
            print("Wheel Shine:     Not Selected")
        #Rust Inhibitor  
        if rustInhibitor == "Y":
            print("Rust Inhibitor:       Seleted")
            totalPrice += 3
        else:
            print("Rust Inhibitor:   Not Selected")

    print("-----------------------------")
    print("Total Cost:          $", totalPrice, ".00")
    print("-----------------------------")