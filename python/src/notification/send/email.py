import smtplib, os, json
from email.message import EmailMessage

def notification(message):
    """Notificating user via email that file is ready to be download."""
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        receiver_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"Hello! Mp3 with file_id *{mp3_fid}* is now ready to download!")
        msg["Subject"] = "MP3 Download"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        session = smtplib.SMTP("smtp.gmail.com", 587) #587 port for TLS
        session.starttls()
        session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, receiver_address)
        session.quit()
        print(f"Mail with file_id {mp3_fid} has been successfully send to {receiver_address}.")

    except Exception as err:
        print(err)
        return err
