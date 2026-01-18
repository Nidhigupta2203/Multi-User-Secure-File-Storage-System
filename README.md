# Multi-User-Secure-File-Storage-System

A secure, multi-user file management web application built using **Flask** and **SQLite**.  
Users can sign up, log in, and manage their own files with proper authentication and security.

This project focuses on secure authentication, session handling, and user-isolated file storage.

---

## 🚀 Features

- User Signup and Login
- Password hashing using Werkzeug
- Session-based authentication with auto logout
- Secure file upload, download, and delete
- User-specific file storage (each user has a private folder)
- File type validation
- Protection against unsafe filenames

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS  
- **Security:** Werkzeug  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```text
Multi-User-Secure-File-Storage-System/
│
├── server.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│ ├── login.html
│ ├── signup.html
│ └── index.html
│
└── uploads/ # Auto-created

```


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Multi-User-Secure-File-Storage-System.git
cd Multi-User-Secure-File-Storage-System

```
