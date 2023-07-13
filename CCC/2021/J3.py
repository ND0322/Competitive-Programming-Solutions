previous = ""
instruction = ""
direction = ""

while True:
    instruction = input()
    if instruction == "99999":
        break
    
    num = instruction[:2]
    sum = int(num[:1]) + int(num[1:])
    if sum == 0:
        direction = previous
    elif sum % 2 == 0:
        previous = "right"
        direction = "right"
    else:
        previous = "left"
        direction = "left"
    print(direction, instruction[2:])
