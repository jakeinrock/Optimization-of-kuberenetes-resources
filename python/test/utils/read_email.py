import imaplib
import email

def get_download_link(username: str, password: str) -> str:
    """Fetching file id from email.
    - if mail exists, returns *file_id* and deletes message,
    - if mail does not exist, return None.
    """
    imap_server = "smtp.gmail.com"
    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL(imap_server)
    # authenticate
    imap.login(username, password)

    _, messages = imap.select("INBOX")

    messages = messages[0].split(b' ')
    if messages == [b'0']:
        return None
    else:
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    body = msg.get_payload(decode=True).decode()
                    for i in body.split():
                        if i.startswith("*"):
                            file_id = i.replace("*", '')

            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")
            imap.expunge()
            imap.close()
            imap.logout()

            return file_id
