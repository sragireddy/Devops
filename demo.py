import imaplib

# account credentials
username = "your_email_address"
password = "your_password"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")

# attempt to authenticate
try:
    imap.login(username, password)
    print("Login successful!")
except imaplib.IMAP4.error:
    print("Login failed.")

# close the mailbox and logout
imap.close()
imap.logout()
