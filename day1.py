sum = 0
with open('day1_input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    singleLine = line.strip()
    curr = ""
    firstDigit = ""
    threeCheck = ""
    fourCheck = ""
    fiveCheck = ""
    for character in singleLine:
        if curr == "" and character.isdigit():
            firstDigit = str(character)
            curr = character
        elif character.isdigit():
            curr = character
        threeCheck += character
        fourCheck += character
        fiveCheck += character
        #print(threeCheck, fourCheck, fiveCheck)
        if len(threeCheck) == 3:  
            if(threeCheck == 'one' or threeCheck == 'two' or threeCheck == 'six'):
                if threeCheck == 'one':
                    curr1 = str(1)
                elif threeCheck == 'two':
                    curr1 = str(2)
                else:
                    curr1 = str(6)
                if curr == "":
                    firstDigit = curr1
                curr = curr1
            threeCheck = threeCheck[1:]
        if len(fourCheck) == 4:  
            if(fourCheck == 'four' or fourCheck == 'five' or fourCheck == 'nine'):
                if fourCheck == 'four':
                    curr1 = str(4)
                elif fourCheck == 'five':
                    curr1 = str(5)
                else:
                    curr1 = str(9)
                if curr == "":
                    firstDigit = curr1
                curr = curr1
            fourCheck = fourCheck[1:]
        if len(fiveCheck) == 5:  
            if(fiveCheck == 'three' or fiveCheck == 'seven' or fiveCheck == 'eight'):
                if fiveCheck == 'three':
                    curr1 = str(3)
                elif fiveCheck == 'seven':
                    curr1 = str(7)
                else:
                    curr1 = str(8)
                if curr == "":
                    firstDigit = curr1
                curr = curr1
                
            fiveCheck = fiveCheck[1:]
        #print(curr)
    #print(firstDigit, curr)            
    sum += int(firstDigit+curr)
  
print(sum)