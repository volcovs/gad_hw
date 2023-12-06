my_dict = {
    "key_1": 1,
    "key_2": 2
}


print(type(my_dict))
print(my_dict)

# mesajul e un text reprezentativ care se returneaza default cand cheia nu exista in dictionar
print(my_dict.get('key_3', "Nu exista"))