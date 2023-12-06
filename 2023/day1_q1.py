sum = 0
with open('./day1_input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    singleLine = line.strip()
    curr = ""
    for character in singleLine:
        if curr == "" and character.isdigit():
            firstDigit = str(character)
            curr = character
        elif character.isdigit():
            curr = character      
    sum += int(firstDigit+curr)
  
print(sum)