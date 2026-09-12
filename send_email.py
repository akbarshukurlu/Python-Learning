import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

print("""
****************************
Smtp Mail Gönderme
****************************
""")

# Göndərən
sender_email = "akbarshukurlu@gmail.com"
sender_password = "************"  # Gmail App Password

# Alıcı
receiver_email = "akbarshukulu@gmail.com"

# Məktubun məzmunu
subject = "Smtp Mail Gönderme"
body = """
Salam, mənim adım Akbar."""

# MIME obyekti yaradırıq
message = MIMEMultipart()

message["From"] = sender_email

message["To"] = receiver_email

message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

try:
    # Gmail SMTP serverinə qoşuluruq
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Şifrələnmiş əlaqə
    server.login(sender_email, sender_password)

    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Məktub uğurla göndərildi!")

except Exception as e:
    sys.stderr.write("Deqiq Xeta: {e}\n")
    sys.stderr.flush()

finally:
    server.quit()

