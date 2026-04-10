# Menu CRUD: importa modulos por operacion (mismo patron READ/MODIFY/WRITE en storage).

from create_student import run_create
from delete_student import run_delete
from read_students import list_all, view_by_sid
from update_student import run_update


def menu():
    print("\n=== Student CSV CRUD (sequential demo) ===")
    print("1) List all students")
    print("2) View student by SID")
    print("3) Create student")
    print("4) Update student by SID")
    print("5) Delete student by SID")
    print("6) Exit")
    return input("Option: ").strip()


def main():
    while True:
        choice = menu()
        if choice == "6":
            print("Bye.")
            break
        if choice == "1":
            list_all()
        elif choice == "2":
            view_by_sid()
        elif choice == "3":
            run_create()
        elif choice == "4":
            run_update()
        elif choice == "5":
            run_delete()
        else:
            print("Invalid option.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
