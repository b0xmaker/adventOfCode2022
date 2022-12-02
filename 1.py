file_path = "/home/alex/Software/AoC-2022/1/input.txt"  # file location
elfNumber = 0       # number used to keep track of elves
elfSum = 0          # sum of individual elf
elfList = []        # blank list

# open the source file
with open(file_path, 'r') as file:
    
    # for each line in the file, 
    for line in file:
        
        # if there's a new line, add the value of the sum to the elf location
        # then zero the elf sum and increase the elf index. 
        if line == '\n':
            elfNumber += 1
            print(f'Elf Number is {elfNumber}')
            elfList.insert(elfNumber-1, elfSum )

            elfSum = 0
        # if there isn't a new line, add the number to the elf sum. 
        else:
            print(f'Sum for this elf {elfNumber} is {elfSum}')
            elfSum += int(line)
            
            
            
    # get top value, then second to top value, then third to top value.
    topValue = max(elfList)
    elfList.remove(max(elfList))
    
    secondValue = max(elfList)
    elfList.remove(max(elfList))
    
    thirdValue = max(elfList)
    
    # add and print top three values
    topThree = topValue + secondValue + thirdValue
    print(topThree)
    

