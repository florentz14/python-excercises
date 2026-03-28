# -------------------------------------------------
# File Name: 26_phone_directory.py
# Created: 2026-03-08
# Description: Phone directory: create, consult, add, delete. File: phone_directory.txt
# -------------------------------------------------

PHONE_FILE = "phone_directory.txt"


def ensure_phone_file_exists() -> None:
    """Create phone_directory.txt if it does not exist."""
    try:
        open(PHONE_FILE, "r").close()
    except FileNotFoundError:
        with open(PHONE_FILE, "w", encoding="utf-8") as f:
            pass
        print(f"Created '{PHONE_FILE}'.")


def load_directory() -> dict:
    """Load name -> phone from phone_directory.txt."""
    ensure_phone_file_exists()
    d = {}
    with open(PHONE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "," in line:
                name, phone = line.split(",", 1)
                d[name.strip()] = phone.strip()
    return d


def save_directory(d: dict) -> None:
    """Save directory to phone_directory.txt."""
    with open(PHONE_FILE, "w", encoding="utf-8") as f:
        for name, phone in sorted(d.items()):
            f.write(f"{name},{phone}\n")


def consult_phone(name: str) -> str | None:
    """Return phone for name or None."""
    d = load_directory()
    return d.get(name)


def add_client(name: str, phone: str) -> None:
    """Add or update client."""
    d = load_directory()
    d[name] = phone
    save_directory(d)
    print(f"Added/updated: {name} -> {phone}")


def delete_client(name: str) -> bool:
    """Remove client. Returns True if found and deleted."""
    d = load_directory()
    if name not in d:
        return False
    del d[name]
    save_directory(d)
    return True


def menu() -> None:
    ensure_phone_file_exists()
    while True:
        print("\n1. Consult phone | 2. Add client | 3. Delete client | 4. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = consult_phone(name)
            print(phone if phone else "Not found")
        elif choice == "2":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                add_client(name, phone)
        elif choice == "3":
            name = input("Name: ").strip()
            if delete_client(name):
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == "4":
            break


if __name__ == "__main__":
    menu()
