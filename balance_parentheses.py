def check_balance(list_):
    
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
            
