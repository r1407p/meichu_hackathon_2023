
#encoding:utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import decline_data  

smtp_server_str = "smtp.gmail.com"
port = 465  # email port to use SSL
sender_email = "mchackathon2023@gmail.com"
password = input("Enter your email password:")

with smtplib.SMTP_SSL(smtp_server_str, port) as smtp_server:
    smtp_server.login(sender_email, password)
    for person in decline_data.receiver:
        if person[1] in decline_data.not_receiver:
            continue
        print(person[1])
        msg = MIMEMultipart()
        msg["Subject"] = "【2023 梅竹黑客松】錄取結果通知信件"
        msg["From"] = sender_email
        receiver_email = person[0]  # index 1 gives your the receiver email
        msg["To"] = receiver_email  
       
        txt = f"""
        <font size="4">{person[1]}同學 您好，

我們是 2023 梅竹黑客松籌備團隊，
非常感謝您關注梅竹黑客松，並撥出寶貴的時間參加我們的徵才面試！

在此很遺憾的通知您，您並未錄取今年的部員徵才。

對於本年度無緣錄取，我們感到十分遺憾。但請您謹記，此次結果並非是因為您的能力、經驗不足或面試表現的不理想，只是團隊內的名額有限，我們必須在此狀況下進行多方面考量並做出決定。因此請您持續保有信心，持續尋覓與爭取各方面機會，豐富自己的大學生活！

當然，未來也歡迎您繼續以任何形式參與梅竹黑客松的活動，和我們一起寫下精彩的故事！

| 電子信箱   mchackathon2023@gmail.com
| 梅竹黑客松 FB 粉專 https://www.facebook.com/HackMeiChu/
| 梅竹黑客松 IG 粉專 https://www.instagram.com/mc_hackathon/
2023 梅竹黑客松籌備團隊 敬上"""
        txt = txt.replace('\n','<br>')
        print(txt)

        body = MIMEText(txt, "html")
        msg.attach(body)

        smtp_server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        