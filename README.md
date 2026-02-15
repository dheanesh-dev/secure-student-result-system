# 🎓 Student Result Management System (CLI)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Stable-success)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A **Python-based Command Line application** that manages student academic results using **role-based access control**.  
Designed to demonstrate backend logic, authentication, and clean project structure.

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
- View **only their own** academic result  

---

## 🔐 Role-Based Access Control

This system enforces strict role permissions:
- **Admin** → full access  
- **Teacher** → limited result management  
- **Student** → read-only access (own data only)

Unauthorized access is prevented by design.

---

## 📁 Project Structure

student-result-management-system/
│
├── main.py # Application entry point
├── auth.py # Login & registration logic
├── admin.py # Admin menu & actions
├── teacher.py # Teacher menu & actions
├── student.py # Student menu & actions
├── results.py # Result management logic
├── data/
│ ├── users.json # User credentials & roles
│ └── results.json # Student results data


---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/student-result-management-system.git
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

Role-based authentication

File-based data persistence

Real-world debugging & Git workflow

Clean backend project structuring

👤 Author
Dheaneswaran M
GitHub: https://github.com/your-username