import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Google ne vous permet pas de vous connecter via smtplib car il a marqué ce type de connexion comme moins sécurisé, donc ce que vous avez à faire est d'aller sur ce lien pendant que vous êtes connecté à votre compte Google, et permettre l'accès: https://myaccount.google.com/lesssecureapps")
subject = "Candidature pour votre offre emploi."
body = input("Entrez un message d'envoie: ")+"\n'est un mail envoyé par script de Python, mais en dur "
sender_email = "yuyuanenzo@gmail.com" # pour l'instant un gmail
receiver_email = input("Entrez le mail d'envoie: ")
password = "Evecs870329"



filename = input("Entrez le fichier joint: ") # In same directory as script

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    print("Votre mail est envoyé avec succès.")