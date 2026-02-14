div align="center">

# 🎓 Secure Student Result Management System  
### Python CLI • Backend Project • Role-Based Access

A clean and modular **Python backend CLI application** focused on  
authentication, role separation, and structured data handling.

</div>

---

## ✨ Overview

This project demonstrates how a **real-world backend system** can be designed using:
- Modular Python files
- Role-based logic (Admin / Student)
- Persistent storage (JSON)
- Clear separation of responsibilities

Built step-by-step as a learning project and structured for GitHub.

---

## 🚀 Key Features

### 🔐 Authentication
- User registration
- User login
- Role assignment (admin / student)

### 👨‍💼 Admin Capabilities
- Add student results
- Update student results
- Delete student results
- View all stored results

### 👨‍🎓 Student Capabilities
- Secure login  
- *(Result access under development)*

---

## 🗂️ Project Structure

```text
auth-system/
│
├── main.py          → Application entry point
├── auth.py          → Authentication logic
├── admin.py         → Admin operations
├── student.py       → Student operations
│
├── data/
│   ├── users.json   → Registered users
│   └── results.json → Student results
│
├── .gitignore
└── README.md
⚙️ Requirements
Python 3.10+

No external dependencies

Runs entirely in the terminal (CLI)

▶️ How to Run
python main.py
⚠️ Ensure both JSON files contain:

[]
🧪 How to Test
Register a new user

Choose role: admin or student

Login using credentials

Admin can manage student results

🎯 What This Project Demonstrates
Backend thinking without frameworks

Clean modular Python design

Role-based access control

JSON-based persistence

Git & GitHub best practices

🔮 Future Enhancements
Student-specific result access

Password hashing

Database integration (SQLite)

REST API using Flask / FastAPI

Frontend integration

👤 Author
Dheaneswaran M

