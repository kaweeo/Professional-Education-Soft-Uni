from collections import deque

parantheses_input = input()

parantheses_stack = deque()
balanced_parantheses = True

for element in parantheses_input:
    if element == "{" or element == "[" or element == "(":
        parantheses_stack.append(element)
    elif element == "}":
        if parantheses_stack:
            last_element = parantheses_stack.pop()
            if last_element != "{":
                parantheses_stack.append(last_element)
        else:
            balanced_parantheses = False
    elif element == "]":
        if parantheses_stack:
            last_element = parantheses_stack.pop()
            if last_element != "[":
                parantheses_stack.append(last_element)
        else:
            balanced_parantheses = False
    elif element == ")":
        if parantheses_stack:
            last_element = parantheses_stack.pop()
            if last_element != "(":
                parantheses_stack.append(last_element)
        else:
            balanced_parantheses = False

if parantheses_stack or balanced_parantheses == False:
    print("NO")
else:
    print("YES")