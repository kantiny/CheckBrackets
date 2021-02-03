check_str = input()
stack_brackets = []
result = True

for bracket in check_str:
    if bracket == '{':
        stack_brackets.append(1)
    elif bracket == '[':
        stack_brackets.append(2)
    elif bracket == '(':
        stack_brackets.append(3)
    elif bracket == "}":
        if stack_brackets[-1] == 1:
            stack_brackets.pop()
        else:
            result = False
            break
    elif bracket == "]":
        if stack_brackets[-1] == 2:
            stack_brackets.pop()
        else:
            result = False
            break
    elif bracket == ")":
        if stack_brackets[-1] == 3:
            stack_brackets.pop()
        else:
            result = False
            break

print(result)
