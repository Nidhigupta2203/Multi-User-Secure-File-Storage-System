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

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS  
- **Security:** Werkzeug  
- **Version Control:** Git & GitHub  

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

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Multi-User-Secure-File-Storage-System.git
cd Multi-User-Secure-File-Storage-System
```
### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the application
python3 server.py

## 🌐 Usage

- Open the application in your browser: http://127.0.0.1:5000/signup
- Create a new account
- Log in using your credentials
- Upload, download, or delete files securely

## 🔐 Security Highlights

- Passwords are hashed, never stored in plain text
- Sessions automatically expire after inactivity
- Secure filenames prevent directory traversal attacks
- Each user has an isolated upload directory

## 🧠 Learning Outcomes

- Implemented authentication and authorization in Flask
- Used SQLite for persistent user data storage
- Managed sessions securely
- Handled file uploads with validation
- Structured a Flask project professionally

## ⭐ Future Improvements

- Add role-based access (Admin/User)
- Deploy the application online
- Improve UI using Bootstrap or Tailwind CSS
- Add file size limits and logging
- Add email-based authentication

If you like this project, feel free to ⭐ the repository!
---
