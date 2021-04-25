badInput = True

while (badInput):
    badInput = True
    prompt = input("please enter a year: ")
    year = 0

    if (prompt.isdigit()):
        year = int(prompt)
        badInput = False
    
    else:
        print ("not a valid input")


if (year % 4) == 0:
        if (year % 100) == 0:
                if (year % 400) == 0:
                        print (year, "is a leap year")
                else:
                        print (year, "is not a leap year")
        else:
                print (year, "is a leap year")
else:
        print (year, "is not a leap year")

