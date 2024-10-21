import os
import smtplib
from email.mime.text import MIMEText

# SMTP 서버 설정
smtp_server = "smtp.gmail.com"
smtp_port = 587  # TLS 포트
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SMTP_PASSWORD")

# 수신자 이메일과 메시지 설정
receiver_email = os.getenv("RECEIVER_EMAIL")
subject = "Test Email"
html_body = """
<html>
  <body>
    <h1>This is an HTML email!</h1>
    <p>Hello, this is a <b>test email</b> with <i>HTML formatting</i>.</p>
  </body>
</html>
"""

# 이메일 메시지 생성
msg = MIMEText(html_body, "html")  # 텍스트 형식
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# SMTP 서버 연결 및 이메일 전송
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # TLS(Transport Layer Security) 시작
    server.login(sender_email, password)  # 이메일 계정 로그인
    server.sendmail(sender_email, receiver_email, msg.as_string())  # 이메일 전송
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()  # 서버 연결 종료
