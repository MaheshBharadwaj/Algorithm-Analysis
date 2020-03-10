'''
 S H A N T A 
+  M E E N A
------------
 G A N D H I
------------
'''
def isValid(_):
    if _['S'] == 0 or _['M'] == 0 or _['G'] == 0:
        return False
    return _['S'] * 100000 + _['H'] * 10000 + _['A'] * 1000 * _['N'] * 100 + _['T'] * 10 + _['A']\
            + _['M'] * 10000 + _['E'] * 1000 + _['E'] * 100 + _['N'] * 10 + _['A']\
            == _['G'] * 100000 + _['A'] * 10000 + _['N'] * 1000 + _['D'] * 100 + _['H'] * 10 + _['I']
            
variables = {'S':-1,'H':-1,'A':-1,'N':-1,'T':-1,'M':-1,'E':-1,'G':-1,'D':-1,'I':-1}

def generate_states(current_state):
    min_key = 'S'
    for key in current_state.keys():
        if current_state[key] < current_state[min_key]:
            min_key = key

    
    
    if current_state[min_key] == 9:
        yield None
        return

    temp = current_state[min_key]
    for i in range(9,temp,-1):
        current_state[min_key] = i
        #print('Yielding: ',current_state)
        yield current_state

def notFound(l,ele):
    for element in l:
        if element == ele:
            return False
    return True

def dfs(initial):
    stack = [initial]

    while len(stack):
        #print(stack.qsize())
        current_state = stack.pop()
        print(current_state)
        if(isValid(current_state)):
            print('Solution: ',current_state)
            continue
        
        for next_state in generate_states(current_state):
            if next_state is None:
                break
            else:
                if notFound(stack,next_state):
                    stack.append(dict(next_state))


dfs(variables)

# variables = {'S':8,'H':1,'A':-1,'N':-1,'T':-1,'M':-1,'E':-1,'G':-1,'D':-1,'I':-1}
# print(variables)
# l = []
# for i in generate_states(variables):
#     print(i)
#     l.append(dict(i))

# print()

# for i in l:
#     print(i)