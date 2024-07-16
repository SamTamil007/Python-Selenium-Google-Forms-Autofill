from flask import Flask, send_file
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

@app.route('/')
def send_email():
   
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    gmail_user = 'mail@gmail.com'  # Your Gmail email address
    gmail_password = 'password'  # Your Gmail password or app-specific password

    # Create message
    sender_email = 'sendermail'  
    receiver_email = 'receiver_email' 
    cc_email = 'cc_email '  
    subject = 'subject'
    message = '''message'''

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Cc'] = cc_email  
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Attach PDF file
    pdf_file = 'path.pdf'  
    resume_pdf_file = 'path.pdf' 
    pdf_files = [pdf_file,resume_pdf_file]
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            with open(pdf_file, 'rb') as f:
                pdf_attachment = MIMEBase('application', 'pdf')
                pdf_attachment.set_payload(f.read())
            encoders.encode_base64(pdf_attachment)
            pdf_attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_file)}')
            msg.attach(pdf_attachment)
        else:
            return f'PDF file {pdf_file} does not exist.'

    # Attach screenshot
    screenshot_file = 'path' 
    if os.path.exists(screenshot_file):
        with open(screenshot_file, 'rb') as f:
            screenshot_attachment = MIMEBase('image', 'png')
            screenshot_attachment.set_payload(f.read())
        encoders.encode_base64(screenshot_attachment)
        screenshot_attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(screenshot_file)}')
        msg.attach(screenshot_attachment)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(gmail_user, gmail_password) 

        # Send email
        recipients = [receiver_email] + [cc_email] 
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit() 

        return 'Email sent successfully!'
    except Exception as e:
        return 'Failed to send email. Error: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)