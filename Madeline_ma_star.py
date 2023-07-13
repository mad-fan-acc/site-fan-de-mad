import streamlit as st

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "<3 Pour toi"
body = "Coeur sur toi Mad ! Ton plus grand fan"
sender_email = "love.mad@fan-account.fr"
receiver_email = "mad-la-star@fan-account.fr"
password = "love.mad@fan-account.fr"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

message.attach(MIMEText(body, "plain"))
text = message.as_string()

st.title("Madeline ma star")
love = st.button(":heartbeat: sur Mad :love_letter:")
if love :
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.ionos.fr", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    st.balloons()