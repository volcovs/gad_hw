import csv

def creare_categorii():
    categorii = {'curs', 'cumparaturi', 'munca', 'cadouri'}

    with open('categorii.txt', 'w') as file:
        for c in categorii:
            file.write(c + "\n")

def adauga_task():
    end = False
    existent = False
    with open('categorii.txt', 'r') as file:
        categorii_citite = file.readlines()
        categorii_citite = [x.strip() for x in categorii_citite]

    while not end:
        nume = input("Introdu task-ul:\n")
        with open("taskuri.txt", 'r') as f:
            taskuri_citite = f.readlines()
            for t in taskuri_citite:
                task_data = t.split(",")
                if nume in task_data[0]:
                    print("Task deja existent!")
                    existent = True
                    break

        if existent:
            continue
        dl = input("Introdu deadline-ul:\n")
        persoana = input("Introdu omul responsabil:\n")

        while True:
            categorie = input("Introduceti categoria task-ului:\n")
            if categorie in categorii_citite:
                with open("taskuri.txt", "a") as tasks:
                    tasks.write(f'{nume},{dl},{persoana},{categorie}\n')
                break
            else:
                print("Categoria nu exista")

        while True:
            raspuns = input("Doriti sa continuati? Da/Nu: ")
            if raspuns.lower() == "nu":
                end = True
                break
            elif raspuns.lower() == "da":
                end = False
                break
            else:
                print("Raspunsul nu este valid")
                continue

def listare_pe_categorii():
    with open('categorii.txt', 'r') as file, open('taskuri.txt', 'r') as file2:
        categorii_citite = file.readlines()
        categorii_citite = [x.strip() for x in categorii_citite]

        taskuri = file2.readlines()

        for categorie in categorii_citite:
            print(f'Task-uri din categoria {categorie}: ')
            for task in taskuri:
                att_list = task.split(",")
                if att_list[3] == categorie:
                    print(att_list[0])


def sortare_ascendenta_dupa_categorie():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[3])
        for task in lista_taskuri:
            print(task)


def sortare_descendenta_dupa_categorie():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[3], reverse=True)
        for task in lista_taskuri:
            print(task)


def sortare_ascendenta_dupa_persoana():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[2])
        for task in lista_taskuri:
            print(task)


def sortare_descendenta_dupa_persoana():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[2], reverse=True)
        for task in lista_taskuri:
            print(task)


def sortare_ascendenta_dupa_nume():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[0])
        for task in lista_taskuri:
            print(task)


def sortare_descendenta_dupa_nume():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[0], reverse=True)
        for task in lista_taskuri:
            print(task)


def sortare_ascendenta_dupa_deadline():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[1])
        for task in lista_taskuri:
            print(task)


def sortare_descendenta_dupa_deadline():
    with open("taskuri.txt", "r") as f:
        lista_taskuri = []
        for line in f.readlines():
            lista_taskuri.append(line.strip().split(","))
        lista_taskuri.sort(key=lambda x: x[1], reverse=True)
        for task in lista_taskuri:
            print(task)

# TO-DO:
def filtrare():
    while True:
        criteriu = input("Introdu criteriul de filtrare:\n")
        if criteriu == "task":
            task_de_gasit = input("Introdu numele task-ului:\n")

        elif criteriu == "data":
            pass
        elif criteriu == "persoana":
            pass
        elif criteriu == "categorie":
            pass
        else:
            print("Criteriul nu este valabil")
            # va reveni la solicitarea unui input valid
            continue


def delete_line_by_task():
    task_to_delete = input("Introdu task-ul de sters:\n")

    with open('taskuri.txt', 'r') as file:
        lines = file.readlines()

    # Verificam daca este gasit task ul
    task_gasit = False
    updated_lines = []
    for line in lines:
        if line.strip().split(',')[0] == task_to_delete:
            task_gasit = True
        else:
            updated_lines.append(line)

    # Scriem lista modificata
    with open('taskuri.txt', 'w') as file:
        file.writelines(updated_lines)

    if task_gasit:
        print(f'Task-ul "{task_to_delete}" a fost sters.')
    else:
        print(f'Task-ul "{task_to_delete}" nu a fost gasit.')


creare_categorii()
while True:
   adauga_task()
   while True:
       print("Meniu: ")
       print("1. Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.")
       print("2. Sortare: se alege o opțiune din cele 8 de mai jos:")
       print("3. Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură. criteriile de filtrare sunt:")
       print("4. Adăugare task: se adaugă un nou task.")
       print("5.  Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât să se știe ce informație urmează să editeze utilizatorul)")
       print("6. Ștergerea unui task din lista inițială.")
       print("7. Ieșire")
       optiune = input("Introduceti optiunea: ")

       if optiune == "1":
           listare_pe_categorii()
           continue

       elif optiune == "2":
           print("Meniu sortare: ")
           print("1. sortare ascendentă task")
           print("2. sortare descendentă task")
           print("3. sortare ascendentă deadline")
           print("4. sortare descendentă deadline")
           print("5. sortare ascendentă persoană responsabilă")
           print("6. sortare descendentă persoană responsabilă")
           print("7. sortare ascendentă categorie")
           print("8. sortare descendentă categorie")
           print("9. revenire la meniul principal")
           while True:
               optiune_sortare = input("Introduceti optiunea:\n")
               if optiune_sortare == "1":
                   sortare_ascendenta_dupa_nume()
                   break
               elif optiune_sortare == "2":
                   sortare_descendenta_dupa_nume()
                   break
               elif optiune_sortare == "3":
                   sortare_ascendenta_dupa_deadline()
                   break
               elif optiune_sortare == "4":
                   sortare_descendenta_dupa_deadline()
                   break
               elif optiune_sortare == "5":
                   sortare_ascendenta_dupa_persoana()
                   break
               elif optiune_sortare == "6":
                   sortare_descendenta_dupa_persoana()
                   break
               elif optiune_sortare == "7":
                   sortare_ascendenta_dupa_categorie()
                   break
               elif optiune_sortare == "8":
                   sortare_descendenta_dupa_categorie()
                   break
               elif optiune_sortare == "9":
                   break
               else:
                   print("Optiune invalida\n")
                   continue

       elif optiune == "3":
           # filtrare
           continue

       elif optiune == "4":
           ## Adaugare task nou
           continue

       elif optiune == "5":
           # Editare task
           continue

       elif optiune == "6":
           # Stergere task
           delete_line_by_task()
           continue
       elif optiune == "7":
           # iesire
           break
       else:
           print("Optiune invalida\n")
           continue
