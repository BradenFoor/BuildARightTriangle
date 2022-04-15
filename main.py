def r1(textInput): #Write the line
    print(textInput)
    pass
def br(): #Breaks the line
    print("\n")

def x(xInput):
    sizeX = "_";
    sizeXnum = 1;
    countedX = 0;
    for x in range(xInput):
        sizeXnum = sizeXnum + 1
        sizeX = sizeX + "_"
        countedX = countedX + 1
        if (sizeXnum % 2) == 0:
            #print("Even")
            sizeX = sizeX + "_"
            sizeXnum = sizeXnum + 1
        else:
            #print("Odd")
            sizeX = sizeX
        if countedX >= xInput:
            print(sizeX)


#Head (Head of text)
r1("Right Triangle V1-0 By: Braden Foor")
br()
r1("Last updated: 4/15/2022!")
xStart = 1
loopAmt = input("How big do you want the right triangle? ")
for do in range(int(loopAmt)):
    num = xStart
    x(num)
    xStart = xStart + 1
