import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, password, subject, body):
    """
    寄送電子郵件的函式
    
    參數：
    - sender_email: 寄件者的 Email
    - receiver_email: 收件者的 Email
    - password: 寄件者 Gmail 的應用程式密碼
    - subject: 郵件主題
    - body: 郵件內容
    """
    
    # 建立 MIMEMultipart 物件
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # 將郵件內容附加到郵件中
    message.attach(MIMEText(body, "plain"))

    # 使用 Gmail 的 SMTP 伺服器
    smtp_server = "smtp.gmail.com"
    port = 587  # Gmail 的 SMTP 伺服器端口

    try:
        # 連線到 Gmail 的 SMTP 伺服器
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # 啟用安全連線 (TLS)

        # 登入 Gmail 帳戶
        server.login(sender_email, password)

        # 寄送郵件
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("郵件已成功發送")

    except Exception as e:
        print(f"發送郵件時發生錯誤: {e}")

    finally:
        # 關閉連線
        server.quit()

# 範例用法
sender = "your_email@gmail.com"
receiver = "recipient_email@gmail.com"
password = "your_application_password"
subject = "測試郵件"

body = """
您好，

這是一封由 Python 程式發送的測試郵件。

祝好，
發件者姓名
"""

send_email(sender, receiver, password, subject, body)
