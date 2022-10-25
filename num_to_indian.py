def num_to_indian_sys(number_):
    number_ = str(number_)
    
    #To check whether there is "." in the string to know whether the amount has paisa or not
    if len(number_.split('.')) == 1:
        rupees = number_
    else:
        rupees,paisa = number_.split('.')
    
    #To check whether the length of the money is less than 3 or not
    if len(rupees)<3:
        print(rupees)
    
    #To check whether the length of the money is greater than 3 or not
    if len(rupees)>3:
        money = ''.join(rupees[-3:])
        for x in range(-3,-len(rupees),-2):
        
            money = rupees[x-2:x] + ","+money
    
    #If there is no paisa in the money
    if len(number_.split('.')) == 1:
        final_money = money
    
    #If the money has paisa in it
    else:
        final_money = money+ '.'+paisa
        
    return final_money
