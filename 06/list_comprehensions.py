var = 'comprehension'

#list_forloop = []
#for i in var:
 #   list_forloop.append(i)

# print(list_forloop)
# sau print(list(var))

# list_forloop = [i for i in var]
# print(list_forloop)

#list_forloop = []
#for x in range(30):
 #   if x % 2 == 0:
 #       list_forloop.append(x)

# list_forloop = [x for x in range(30) if x % 2 == 0]
# print(list_forloop)

list_forloop = [x if x % 2 == 0 else 0 for x in range(30)]
print(list_forloop)
