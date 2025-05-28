stack=[]
print(type(stack))
print(f"Initial stack: {stack}")

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(f"After pushing:{stack}")
popped=stack.pop()
print(f"Popped item:{popped}")
print(f"Stack after pop:{stack}")

if stack:
    print(f"Top of stack: {stack[-1]}")
else:
    print(f" Stack is empty")

    stack =[]
    print(f" Stack empty? {len(stack)== 0}")
    print(f" Stack contents(top to bottom):")
    for item in reversed(stack):
        print(f" {item}")



