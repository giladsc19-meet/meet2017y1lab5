def add_numbers(start,end):
    c=0
    for number in range(start,end+1):
        print(number)
        c = c + number
    return(c)


answer=add_numbers(1000,5000)
print(answer)
