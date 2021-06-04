computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

another_list = computer_parts
print(computer_parts)
print(another_list)
print(id(computer_parts))
print(id(another_list))

computer_parts += ["Speaker"]

print(computer_parts)
print(another_list)
print(id(computer_parts))
print(id(another_list))