# 🎓 Student Result Management System (CLI)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Stable-success)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/GitHub-dheanesh--dev-black?logo=github)

A **Python-based Command Line Interface (CLI) application** that manages student academic results using **role-based access control**.  
This project demonstrates backend logic, authentication, authorization, and clean modular design.

---

## 🚀 Features

### 👑 Admin
- Add student results  
- Update student results  
- Delete student results  
- View all student results  

### 🧑‍🏫 Teacher
- Add student results  
- Update student results  

### 👨‍🎓 Student
- Secure login  
- View **only their own** academic results  

---

## 🔐 Role-Based Access Control

The system enforces strict role permissions:

- **Admin** → Full access to all operations  
- **Teacher** → Limited result management  
- **Student** → Read-only access to personal results  

Each user can access **only what their role allows**.

---

## 📁 Project Structure

student-result-management-system/
│
├── main.py # Application entry point
├── auth.py # Authentication & registration logic
├── admin.py # Admin menu & operations
├── teacher.py # Teacher menu & operations
├── student.py # Student menu & operations
├── results.py # Result handling logic
├── data/
│ ├── users.json # Stores users & roles
│ └── results.json # Stores student results


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/dheanesh-dev/student-result-management-system.git
cd student-result-management-system
2️⃣ Run the application
python main.py
🛠 Technologies Used
Python 3

JSON (file-based storage)

CLI (Command Line Interface)

📌 Project Status
✅ Version 1.0 – Completed & Stable

🎯 Learning Outcomes
Python modular programming

Role-based authentication & authorization

File-based data persistence using JSON

Debugging real-world Python errors

Git & GitHub workflow (commit, push, versioning)

👤 Author
Dheaneswaran M
GitHub: https://github.com/dheanesh-dev

