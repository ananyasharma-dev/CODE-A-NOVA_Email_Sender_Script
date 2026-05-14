#  Email Sender Script

A professional Python-based Email Sender application that allows users to send emails to single or multiple recipients using Gmail SMTP.  
The project also maintains a local email log system for tracking previously sent emails.

---

##  Features

- ✅ Send emails to a single recipient
- ✅ Send emails to multiple recipients
- ✅ Secure Email logging system
- ✅ Error handling and validation
- ✅ Modular project structure
- ✅ Beginner-friendly implementation

---

#  Project Structure

```bash
Email-Sender-Script/
│
├── email_sender.py      # Main application file
├── emailcore.py         # SMTP email sending logic
├── file_handler.py      # Email log handling
├── email_log.json       # Auto-generated email logs
└── README.md            # Project documentation
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| smtplib | Sending emails using SMTP |
| email.mime | Formatting email content |
| JSON | Storing email logs |
| TLS Encryption | Secure email transmission |


# ▶️ Application Menu

When the program starts, the following menu appears:

```bash
=============================================
     📧 CODE A NOVA - Email Sender
=============================================

1. Send Email to One Person
2. Send Email to Multiple People
3. View Sent Email Log
4. Exit
```

---

# 📂 Module Explanation

---

## 1️⃣ email_sender.py

Main application file responsible for:

- Displaying menu options
- Taking user input
- Calling email sending functions
- Saving logs

---

## 2️⃣ emailcore.py

Handles SMTP operations:

- Creates email messages
- Connects to Gmail SMTP server
- Starts TLS encryption
- Logs into Gmail
- Sends emails securely

---

## 3️⃣ file_handler.py

Responsible for:

- Saving sent email history
- Loading previous logs
- Managing JSON files

---
## Steps to Generate App Password

1. Open your Google Account
2. Enable **2-Step Verification**
3. Go to **Security**
4. Open **App Passwords**
5. Generate a password for Mail
6. Copy and use it inside the project

# 📸 Example Usage

```bash
Your Gmail address : example@gmail.com
Your App Password  : ********
Recipient email    : user@gmail.com
Subject            : Test Email
Message            : Hello from Python!

## Made by
Ananya Sharma — CODE A NOVA Internship
