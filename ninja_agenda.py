def mostrar_menu():
    print("=== Agenda Ninja ===")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Salir")

def user_selection(user_option,users):
    user_name = ""
    user_phonenumber = 0
    if user_option == 4:
        print("Adios, guerrero")
        exit()
    elif user_option == 1:
        print("===Agregar contacto===")
        user_name = input("Nombre del usuario: ")
        user_phonenumber = input("Telefono del usuario: ")
        users.append({user_name:user_phonenumber})
    elif user_option == 2:
        print("===Ver contactos===")
        for i in range(0,len(users)):
            print(f"{i + 1} - {users[i]}")

    elif user_option == 3:
        flag = False
        print("===Buscar contacto===")
        user_search = input("Nombre a buscar: ")
        for i in range(0,len(users)):
            for name,phone in users[i].items():
                if user_search == name:
                    print(users[i])
                    flag = True
        if flag == False:
            print("Usuario no encontrado")


def Main():
    users = []
    user_option = 0

    while user_option != 4:
        print("\n")
        mostrar_menu()
        user_option = int(input("Escoge una opcion: "))
        print("\n")
        user_selection(user_option,users)

if __name__ == "__main__":
    Main()