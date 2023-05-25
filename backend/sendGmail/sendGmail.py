from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.text import MIMEText
content = MIMEMultipart()  
content["subject"] = "IOT TEST "  #郵件標題
content["from"] = "sender gmail"  #寄件者
content["to"] = "receiver gmail" #收件者
content.attach(MIMEText("Demo python send email"))  #郵件內容
content.attach(MIMEImage(Path("music.png").read_bytes()))  # 郵件圖片內容

import smtplib
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("sender gmail", "two steps key")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)