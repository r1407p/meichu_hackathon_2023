import smtplib
import auto_mail_template_data as used_data
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_server_str = "smtp.gmail.com"
port = 465  # email port to use SSL
sender_email = "mchackathon@gmail.com"
password = input("Enter your email password:")


with smtplib.SMTP_SSL(smtp_server_str, port) as smtp_server:
    smtp_server.login(sender_email, password)
    for mes in used_data.test_receiver:
        msg = MIMEMultipart()
        msg["Subject"] = "Email test"
        msg["From"] = sender_email
        receiver_email = "mes[1]"  # index 1 gives your the receiver email
        msg["To"] = receiver_email  
        txt = "Here is the artical"
        body = MIMEText(txt, "plain")
        msg.attach(body)

        smtp_server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )
