my_var = input("Adauga un nr: ")
try:
    my_int = int(my_var)
#except ValueError:
#    print("Ai introdus un string in locul intregului")
except Exception as e:
    print("Exceptie generala", type(e).__name__)
except ValueError:
    print("Ai introdus un string in locul intregului")
else:
    print("A functionat")
finally:
    print("Se executa oricum")

print("Oricum")
