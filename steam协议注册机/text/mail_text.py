import imaplib, email
from bs4 import BeautifulSoup
imap = imaplib.IMAP4_SSL("outlook.office365.com")
imap.login("Dwiymz135253@outlook.com", "Syyewa770886")
imap.select("inbox")
subject = "New Steam Account Email Verification"
subject_unicode = subject.encode('utf-8')
status, messages = imap.search(
    None, 'SEEN')
print(status)
print(messages)
if status == "OK":
    messages = messages[0].split()
    print(messages)
emails = []
for message in messages:
    status, data = imap.fetch(message, "(RFC822)")
    if status == "OK":
        emails.sort(key=lambda x: x["Date"], reverse=True)
        emails.append(email.message_from_bytes(data[0][1]))
        for part in emails[0].walk():
            if part.get_content_type() == "text/html":
                html = part.get_payload(decode=True)
                with open("../resources/steam.html", "wb") as file:
                    file.write(html)
                link = BeautifulSoup(html, "html.parser").find("a", class_="link c-grey4")
                print(link)

