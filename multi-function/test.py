
unit_list = [] 

number = 10 

while number > 0 :
    unit = number % 10 
    unit_list.insert(0,unit) 
    number = int(number/10) 

print(f"units = {unit_list}")