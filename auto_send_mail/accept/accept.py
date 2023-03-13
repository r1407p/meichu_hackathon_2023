
#encoding:utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import accept_data  

smtp_server_str = "smtp.gmail.com"
port = 465  # email port to use SSL
sender_email = "mchackathon2023@gmail.com"
password = input("Enter your email password:")

with smtplib.SMTP_SSL(smtp_server_str, port) as smtp_server:
    smtp_server.login(sender_email, password)
    for person in accept_data.test:
        msg = MIMEMultipart()
        msg["Subject"] = "| 第一波錄取結果通知信件 |"
        msg["From"] = sender_email
        receiver_email = person[1]  # index 1 gives your the receiver email
        msg["To"] = receiver_email  
       
        txt = f"""
        <font size="4">{person[0]}同學 您好，

我們是 2023 梅竹黑客松籌備團隊，非常感謝您關注梅竹黑客松，並撥出寶貴的時間參加我們的徵才面試！

在此我們要向您說聲恭喜——

經過一階與二階面試，以及團隊內的密集討論，由於您在面試時展現出的積極與熱忱，和與部內所需相符的特質，


<b>您已被選為「2023 梅竹黑客松籌備團隊」 <font color="#AE0000">{person[2]}</font> 的一員！</b>


在正式加入團隊之前，要請您完成以下的幾個事項。

同時，我們預計將於 <b>3/20（一）21:00~23:00</b> 於交大交映樓 702 舉辦第一次全員會，屆時將備有餐點與茶水，邀請您一同來參與！

請於 <b><font color="#AE0000">3/12（日）20:00 </font></b>以前完成以下事項：
1. 填寫<a href="https://docs.google.com/forms/d/1zY8l5VQlq2FSWgUQc07lbAht-_RFtwgmdGnm4AVS0gA/viewform?edit_requested=true">全員會表單</a>

2. 註冊 Discord 帳號，並由連結加入討論。
<blockquote>Discord 為梅竹黑客松團隊共用的通訊軟體，進行所有公共事物的討論 。
以下為申請步驟：
(1)下載 <a href="https://discord.com/">Discord</a>
(2)申請帳號，並將您的暱稱更改為 部門/ 中文全名，e.g. 行政/賴睿麒
(3)點選<a href="https://discord.gg/KWA4kdT8">邀請連結</a>，加入共同工作空間</blockquote>
3. 加自己部長 FB 好友：
<blockquote>行政部：<a href="https://www.facebook.com/rcltw/">賴睿麒</a>
公關部：<a href="https://www.facebook.com/amanda00601">解心妤</a>、<a href="https://www.facebook.com/profile.php?id=100016265235054">林庭伃</a>、<a href="https://www.facebook.com/profile.php?id=100011087057588">楊晨鍾</a>
行銷部：<a href="https://www.facebook.com/profile.php?id=100004462725190">宋少瑜</a>、<a href="https://www.facebook.com/people/%E8%B6%99%E4%BA%8E%E7%91%84/100009964414812/">趙于瑄</a>
活動部：<a href="https://www.facebook.com/people/%E8%B6%99%E4%BA%8E%E7%91%84/100009964414812/">蔡欣儒</a>、<a href="https://www.facebook.com/tiffany1015">范禎宸</a>、<a href="https://www.facebook.com/popkcal">林麒安</a>
財務部：<a href="https://www.facebook.com/people/%E9%99%B3%E9%83%81%E5%AE%89/100006131026595/">陳郁安</a>、<a href="https://www.facebook.com/melody.yi.9">翼瑄卉</a>
開發部：<a href="https://www.facebook.com/mudamongpeoele">徐瑞澤</a>、<a href="https://www.facebook.com/people/%E6%9B%BE%E5%AE%B6%E7%A5%90/100011337532579/">曾家祐</a>
設計部：<a href="https://www.facebook.com/people/%E9%99%B3%E6%A8%82%E7%A9%8E/100005807169194/">陳樂穎</a></blockquote>
<b>*未於期限內完成，視同<font color="#AE0000">放棄</font>錄取資格</b>

最後，再次恭喜您成為 2023 梅竹黑客松的一員，若有任何疑問請盡速回信，期待與您見面！

| 電子信箱		mchackathon2023@gmail.com   
| 梅竹黑客松 FB 粉專	https://www.facebook.com/HackMeiChu/
| 梅竹黑客松 IG 粉專	https://www.instagram.com/mc_hackathon/

2023 梅竹黑客松籌備團隊 敬上
        """
        txt = txt.replace('\n','<br>')
        print(txt)

        body = MIMEText(txt, "html")
        msg.attach(body)

        smtp_server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        