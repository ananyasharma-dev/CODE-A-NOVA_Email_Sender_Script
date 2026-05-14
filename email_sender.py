# email_sender.py
# Main file - run this to start the app

from emailcore import send_email
from file_handler import save_log, load_log

print("=" * 45)
print("      CODE A NOVA - Email Sender")
print("=" * 45)

def show_menu():
    print("\n1. Send Email to One Person")
    print("2. Send Email to Multiple People")
    print("3. View Sent Email Log")
    print("4. Exit")

while True:
    show_menu()
    choice = input("\nEnter choice (1-4): ").strip()

    if choice == "1":
        print("\n--- Send Single Email ---")
        sender    = input("Your Gmail address : ")
        password  = input("Your App Password  : ")
        recipient = input("Recipient email    : ")
        subject   = input("Subject            : ")
        body      = input("Message            : ")

        result = send_email(sender, password, [recipient], subject, body)
        if result:
            save_log(sender, [recipient], subject)
            print("\n Email sent successfully!")
        else:
            print("\n Failed to send. Check your credentials.")

    elif choice == "2":
        print("\n--- Send to Multiple People ---")
        sender   = input("Your Gmail address : ")
        password = input("Your App Password  : ")
        emails   = input("Enter emails separated by commas: ")
        recipients = [e.strip() for e in emails.split(",")]
        subject  = input("Subject : ")
        body     = input("Message : ")

        result = send_email(sender, password, recipients, subject, body)
        if result:
            save_log(sender, recipients, subject)
            print(f"\n Email sent to {len(recipients)} people!")
        else:
            print("\n Failed to send. Check your credentials.")

    elif choice == "3":
        logs = load_log()
        if not logs:
            print("\n📭 No emails sent yet.")
        else:
            print("\n--- Sent Email Log ---")
            for i, log in enumerate(logs, 1):
                print(f"\n{i}. From    : {log['from']}")
                print(f"   To      : {', '.join(log['to'])}")
                print(f"   Subject : {log['subject']}")
                print(f"   Time    : {log['time']}")

    elif choice == "4":
        print("\n Goodbye!\n")
        break

    else:
        print("  Invalid choice. Enter 1 to 4.")
