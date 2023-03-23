import win32com.client

# connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 refers to the inbox folder

# get the latest email
messages = inbox.Items
message = messages.GetLast()

# print the subject and sender
print("Subject:", message.Subject)
print("Sender:", message.SenderEmailAddress)
