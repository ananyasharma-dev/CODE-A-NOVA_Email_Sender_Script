# emailcore.py
# Connects to Gmail and sends the email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, recipients, subject, body):
    try:
        # Build the email
        msg = MIMEMultipart()
        msg["From"]    = sender
        msg["To"]      = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()                    # secure the connection
        server.login(sender, password)       # log in
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        return True

    except smtplib.SMTPAuthenticationError:
        print("⚠️  Wrong email or App Password.")
        return False
    except Exception as e:
        print(f"⚠️  Error: {e}")
        return False
        
