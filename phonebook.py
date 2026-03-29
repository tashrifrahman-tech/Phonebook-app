import mysql.connector
from tabulate import tabulate

# Step 1: Connect MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= #Add your MySQLPassword
)
cursor = conn.cursor()

# Step 2: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS phonebook_db")
conn.database = "phonebook_db"

# Step 3: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
)
""")

# Add address column if it doesn't exist (for existing databases)
try:
    cursor.execute("ALTER TABLE contacts ADD COLUMN address TEXT")
    conn.commit()
except mysql.connector.errors.DatabaseError:
    pass  # Column already exists
conn.commit()


# ── Menus ──────────────────────────────────────────────────────────────────────

def display_main_menu():
    print("\nPhonebook Main Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

def display_search_menu():
    print("\nSearch Menu:")
    print("1. Search by Name")
    print("2. Search by Phone Number")
    print("3. Search by Email Address")
    print("4. Go Back to Main Menu")

def display_update_menu():
    print("\nUpdate Menu:")
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Email")
    print("4. Update Address")
    print("5. Go Back to Main Menu")

def display_delete_menu():
    print("\nDelete Menu:")
    print("1. Delete by Name")
    print("2. Delete by Phone Number")
    print("3. Delete by Email Address")
    print("4. Go Back to Main Menu")


# ── Add Contact ────────────────────────────────────────────────────────────────

def add_contact():
    name = input("Enter contact name: ").strip().title()
    phone_numbers = []
    emails = []

    while True:
        # FIX: removed erroneous int() wrapping the prompt string
        phone = input("Enter phone number (or press Enter to finish): ").strip()
        if not phone:
            break
        phone_numbers.append(phone)

    while True:
        email = input("Enter email address (or press Enter to finish): ").strip()
        if not email:
            break
        # FIX: was `email.append(email)` — should be `emails.append(email)`
        emails.append(email)

    if not phone_numbers and not emails:
        print("Cannot add contact without phone number or email.")
        return

    address = input("Enter address (or press Enter to skip): ").strip()
    phone_combined = ",".join(phone_numbers)
    email_combined = ",".join(emails)

    cursor.execute(
        "INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)",
        (name, phone_combined, email_combined, address)
    )
    conn.commit()
    print(f"Contact '{name}' added successfully.")


# ── Search Functions ───────────────────────────────────────────────────────────

def search_by_name():
    name = input("Enter name to search: ").strip().title()
    cursor.execute(
        "SELECT id, name, phone, email, address FROM contacts WHERE name LIKE %s",
        (f"%{name}%",)
    )
    results = cursor.fetchall()
    if results:
        print(tabulate(results, headers=["S.No", "Name", "Phone(s)", "Email(s)", "Address"], tablefmt="grid"))
    else:
        print("No contact found with that name.")

def search_by_number():
    number = input("Enter phone number to search: ").strip()
    cursor.execute(
        "SELECT id, name, phone, email, address FROM contacts WHERE phone LIKE %s",
        (f"%{number}%",)
    )
    results = cursor.fetchall()
    if results:
        print(tabulate(results, headers=["S.No", "Name", "Phone(s)", "Email(s)", "Address"], tablefmt="grid"))
    else:
        print("No contact found with that phone number.")

def search_by_email():
    email = input("Enter email address to search: ").strip()
    cursor.execute(
        "SELECT id, name, phone, email, address FROM contacts WHERE email LIKE %s",
        (f"%{email}%",)
    )
    results = cursor.fetchall()
    if results:
        print(tabulate(results, headers=["S.No", "Name", "Phone(s)", "Email(s)", "Address"], tablefmt="grid"))
    else:
        print("No contact found with that email.")


# ── Update Functions ───────────────────────────────────────────────────────────

def update_name():
    old_name = input("Enter the current name of the contact: ").strip().title()
    new_name = input("Enter the new name: ").strip().title()
    cursor.execute("UPDATE contacts SET name = %s WHERE name LIKE %s", (new_name, f"%{old_name}%"))
    conn.commit()
    if cursor.rowcount:
        print(f"Name updated to '{new_name}'.")
    else:
        print("No contact found with that name.")

def update_phone():
    name = input("Enter the name of the contact to update phone: ").strip().title()
    new_phone = input("Enter the new phone number(s), comma-separated: ").strip()
    cursor.execute("UPDATE contacts SET phone = %s WHERE name LIKE %s", (new_phone, f"%{name}%"))
    conn.commit()
    if cursor.rowcount:
        print("Phone number updated.")
    else:
        print("No contact found with that name.")

def update_email():
    name = input("Enter the name of the contact to update email: ").strip().title()
    new_email = input("Enter the new email(s), comma-separated: ").strip()
    cursor.execute("UPDATE contacts SET email = %s WHERE name LIKE %s", (new_email, f"%{name}%"))
    conn.commit()
    if cursor.rowcount:
        print("Email updated.")
    else:
        print("No contact found with that name.")

def update_address():
    name = input("Enter the name of the contact to update address: ").strip().title()
    new_address = input("Enter the new address: ").strip()
    cursor.execute("UPDATE contacts SET address = %s WHERE name LIKE %s", (new_address, f"%{name}%"))
    conn.commit()
    if cursor.rowcount:
        print("Address updated.")
    else:
        print("No contact found with that name.")


# ── Delete Functions ───────────────────────────────────────────────────────────

def delete_by_name():
    name = input("Enter the name of the contact to delete: ").strip().title()
    cursor.execute("DELETE FROM contacts WHERE name LIKE %s", (f"%{name}%",))
    conn.commit()
    if cursor.rowcount:
        print(f"Contact '{name}' deleted.")
    else:
        print("No contact found with that name.")

def delete_by_phone():
    number = input("Enter the phone number of the contact to delete: ").strip()
    cursor.execute("DELETE FROM contacts WHERE phone LIKE %s", (f"%{number}%",))
    conn.commit()
    if cursor.rowcount:
        print("Contact deleted.")
    else:
        print("No contact found with that phone number.")

def delete_by_email():
    email = input("Enter the email address of the contact to delete: ").strip()
    cursor.execute("DELETE FROM contacts WHERE email LIKE %s", (f"%{email}%",))
    conn.commit()
    if cursor.rowcount:
        print("Contact deleted.")
    else:
        print("No contact found with that email.")


# ── View All Contacts ──────────────────────────────────────────────────────────

def view_all_contacts():
    cursor.execute("SELECT id, name, phone, email, address FROM contacts ORDER BY name")
    results = cursor.fetchall()
    if results:
        print(tabulate(results, headers=["S.No", "Name", "Phone(s)", "Email(s)", "Address"], tablefmt="grid"))
    else:
        print("No contacts found.")


# ── Sub-menu Handlers ──────────────────────────────────────────────────────────

def handle_search_menu():
    while True:
        display_search_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_by_number()
        elif choice == "3":
            search_by_email()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

def handle_update_menu():
    while True:
        display_update_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            update_name()
        elif choice == "2":
            update_phone()
        elif choice == "3":
            update_email()
        elif choice == "4":
            update_address()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

def handle_delete_menu():
    while True:
        display_delete_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            delete_by_name()
        elif choice == "2":
            delete_by_phone()
        elif choice == "3":
            delete_by_email()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")


# ── Main Loop ──────────────────────────────────────────────────────────────────

def main():
    print("Welcome to the Phonebook Application!")
    while True:
        display_main_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            handle_search_menu()
        elif choice == "3":
            handle_update_menu()
        elif choice == "4":
            handle_delete_menu()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
