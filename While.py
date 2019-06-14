alder = 10
num = 0

while num < alder:
    if num == 0:
        num += 1
        continue # starter på toppen av while igjen

    if num % 2 == 0:
        print(num)
    
    if num > 5:
        break # hopper ut av while
    num += 1

