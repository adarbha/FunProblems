def check_balance(list_):
    '''Returns true if all the parentheses are True. Reurns true for empty list'''

    if len(list_) == 0:
        return True
    
    stack = []
    
    for temp in list_:
        if temp in "{[(":
            stack.append(temp)   
        elif temp == ')':
            if stack.pop() != '(':
                return False
        elif temp == '}':
            if stack.pop() != '{':
                return False
        elif temp == ']':
            if stack.pop() != '[':
                return False
        
    return True
            


