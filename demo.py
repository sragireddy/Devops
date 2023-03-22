


import imaplib
import email
from email.header import decode_header

# account credentials
username = "your_email_address"
password = "your_password"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")

# authenticate
imap.login(username, password)

# select the mailbox you want to read
# if you want to select the inbox, leave this line commented
# imap.select("INBOX")

# search for specific emails by subject
# you can also search by sender, date, or other criteria
# use ALL for all emails in the mailbox
status, messages = imap.search(None, 'SUBJECT "your_subject"')

# convert messages to a list of email IDs
messages = messages[0].split(b' ')

for msg_id in messages:
    # fetch the email message by ID
    res, msg = imap.fetch(msg_id, "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])

            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes type, decode to str
                subject = subject.decode()

            # print details for each message
            print("Subject:", subject)
            print("From:", msg["From"])
            print("To:", msg["To"])
            print("Date:", msg["Date"])
            print("="*100)

# close the mailbox and logout
imap.close()
imap.logout()