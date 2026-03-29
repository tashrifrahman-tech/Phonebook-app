# 📒 Phonebook App

A terminal-based phonebook application built with **Python** and **MySQL**. Supports full CRUD operations — add, search, update, and delete contacts — with a clean tabular display.

---

## Features

- Add contacts with multiple phone numbers, emails, and an address
- Search contacts by name, phone number, or email
- Update any field — name, phone, email, or address
- Delete contacts by name, phone, or email
- View all contacts in a formatted table with serial numbers
- Data persisted in a local MySQL database

---

## Requirements

- Python 3.x
- MySQL Server
- Python packages:
  ```
  mysql-connector-python
  tabulate
  ```

Install dependencies with:
```bash
pip install mysql-connector-python tabulate
```

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/phonebook-app.git
   cd phonebook-app
   ```

2. **Start your MySQL server** and make sure it's running on `localhost`

3. **Configure credentials** — open `phonebook.py` and update if needed:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password=""   # add your MySQL password here
   )
   ```

4. **Run the app**
   ```bash
   python phonebook.py
   ```

The database `phonebook_db` and the `contacts` table are created automatically on first run.

---

## Database Schema

| Column    | Type           | Description                        |
|-----------|----------------|------------------------------------|
| `id`      | INT (PK, AUTO) | Serial number, auto-incremented    |
| `name`    | VARCHAR(255)   | Contact name                       |
| `phone`   | TEXT           | Comma-separated phone numbers      |
| `email`   | TEXT           | Comma-separated email addresses    |
| `address` | TEXT           | Contact address                    |

---

## Usage

On launch you'll see the main menu:

```
Phonebook Main Menu:
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
```

Each option leads to a sub-menu where you can perform the relevant operation. All results are displayed in a grid table with serial numbers.

---

## Project Structure

```
phonebook-app/
│
├── phonebook.py   # Main application
└── README.md      # Project documentation
```

---

## Author

Made with Python 🐍 and MySQL 🐬
