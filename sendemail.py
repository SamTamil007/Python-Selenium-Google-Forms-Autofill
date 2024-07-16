from flask import Flask, send_file
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

@app.route('/send_email')
def send_email():
    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    gmail_user = 'samsathyaseelan1972@gmail.com'  # Your Gmail email address
    gmail_password = 'hths gpib klll bdli'  # Your Gmail password or app-specific password

    # Create message
    sender_email = 'samsathyaseelan1972@gmail.com'  # Your Gmail email address
    receiver_email = 'mynewworkmail007@gmail.com'  # Recipient's email address
    cc_email = 'deathgamingpro7@gmail.com'  # CC recipient's email address
    subject = 'Python (Selenium) Assignment - Obeth Samuel Raj S'
    message = '''
    1.	Screenshot of the form filled via code is Attached.
	2.	Source code (GitHub repository) : .
	3.	Brief documentation of your approach.
	4.	Your resume.
	5.	Links to past projects/work samples.
	6.	Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months.'''

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Cc'] = cc_email  # Adding CC recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Attach PDF file
    pdf_file = 'path_to_your_pdf_file.pdf'  # Replace with the path to your PDF file
    if os.path.exists(pdf_file):
        with open(pdf_file, 'rb') as f:
            pdf_attachment = MIMEBase('application', 'pdf')
            pdf_attachment.set_payload(f.read())
        encoders.encode_base64(pdf_attachment)
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_file)}')
        msg.attach(pdf_attachment)

    # Attach screenshot
    screenshot_file = 'path_to_your_screenshot.png'  # Replace with the path to your screenshot file
    if os.path.exists(screenshot_file):
        with open(screenshot_file, 'rb') as f:
            screenshot_attachment = MIMEBase('image', 'png')
            screenshot_attachment.set_payload(f.read())
        encoders.encode_base64(screenshot_attachment)
        screenshot_attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(screenshot_file)}')
        msg.attach(screenshot_attachment)

    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(gmail_user, gmail_password)  # Login

        # Send email
        recipients = [receiver_email] + [cc_email]  # Combine main recipient and CC recipient
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()  # Logout from Gmail SMTP server

        return 'Email sent successfully!'
    except Exception as e:
        return 'Failed to send email. Error: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)