Operations = {'+', '-', '*', '/', '(', ')', '^'}
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}


def Conversion_function(The_function_to_be_converted): 

    Stack = [] 
    
    Final_equation = '' 
    
    for Character in The_function_to_be_converted:
    
        if Character not in Operations:
        
            Final_equation += Character
        
        elif Character == '(': 
        
            Stack.append('(')
        
        elif Character == ')':
        
            while Stack and Stack[-1] != '(':
            
                Final_equation += Stack.pop()  
     
            Stack.pop()
        
        else:
            
            while Stack and Stack[-1] != '(' and  Priority[Character] <=   Priority[Stack[-1]]:
                            
                Final_equation += Stack.pop()
                
            Stack.append(Character)
        
    while Stack:
        
        Final_equation += Stack.pop()
    
    return Final_equation
    
The_function_to_be_converted = input('\nEnter the Infix expression: ')

print('\n The Postfix expression is:', Conversion_function(The_function_to_be_converted), "\n")
