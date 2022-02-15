unitConverted = input("Unit You Want To Convert: ")
unitConvertedTo = input("Enter The Unit You Want To Convert To: ")

# fl --> ml | l
FLtoML = 29.57353193
FLtoL = FLtoML / 1000
# gal --> ml | l
GALtoML = 3785.41
GALtoL = GALtoML / 1000
# lb --> g | kg
LBtoG = 453.592
LBtoKG = LBtoG / 1000
# in --> mm | cm | m
INtoMM = 25.4
INtoCM = INtoMM / 10
INtoM = INtoMM / 1000
# ft --> mm | cm | m
FTtoMM = 25.4 * 12
FTtoCM = FTtoMM / 10
FTtoM = FTtoMM / 1000
# mi --> mm | cm | m
MItoMM = (25.4 * 12) * 5280
MItoCM = MItoMM / 10
MItoM = MItoMM / 1000

if unitConverted == "floz":
    if unitConvertedTo == "ml" or "l":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "ml":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*FLtoML, unitConvertedTo)
        elif unitConvertedTo == "l":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*FLtoL, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)
elif unitConverted == "gal":
    if unitConvertedTo == "ml" or "l":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "ml":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*GALtoML, unitConvertedTo)
        elif unitConvertedTo == "l":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*GALtoL, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)
elif unitConverted == "lb":
    if unitConvertedTo == "g" or "kg":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "g":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*LBtoG, unitConvertedTo)
        elif unitConvertedTo == "kg":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*LBtoKG, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)
elif unitConverted == "in":
    if unitConvertedTo == "mm" or "cm" or "m":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "mm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*INtoMM, unitConvertedTo)
        elif unitConvertedTo == "cm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*INtoCM, unitConvertedTo)
        elif unitConvertedTo == "m":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*INtoM, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)
elif unitConverted == "ft":
    if unitConvertedTo == "mm" or "cm" or "m":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "mm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*FTtoMM, unitConvertedTo)
        elif unitConvertedTo == "cm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*FTtoCM, unitConvertedTo)
        elif unitConvertedTo == "m":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*FTtoM, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)
elif unitConverted == "mi":
    if unitConvertedTo == "mm" or "cm" or "m":
        value = eval(input("What Is The Value Of The Unit You Want To Convert: "))
        if unitConvertedTo == "mm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*MItoMM, unitConvertedTo)
        elif unitConvertedTo == "cm":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*MItoCM, unitConvertedTo)
        elif unitConvertedTo == "m":
            print(value, unitConverted, "in", unitConvertedTo, "is", value*MItoM, unitConvertedTo)
    else:
        print("You cannot convert", unitConverted, "To", unitConvertedTo)