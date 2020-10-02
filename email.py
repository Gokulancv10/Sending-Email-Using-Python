
import smtplib

# SET EMAIL LOGIN REQUIREMENTS

gmail_user = 'your-gmail'
gmail_app_password = 'your-app-password---NOT-GMAIL-PASSWORD'
"""
1. For gmail app password got to link below
2. set app password (below 2-step-verification) -->  https://myaccount.google.com/u/1/security
3. choose mail and from the device you're running this python file.(eg. windows)
4. copy the 16 character password and paste it in gmail_app_password
5. Run the file.
"""

# SET THE INFO ABOUT THE SAID EMAIL
sent_from = gmail_user
sent_to = ['gmail1@gmail.com', 'gmail2@gmail.com']
sent_subject = "Subject"
sent_body = ("Hey, what's up? friend!\n\n"
             "I hope you have been well!\n"
             "\n"
             "Cheers,\n"
             "Jay\n")

# email context
email_text = """\
        From: %s
        To: %s
        Subject: %s       
        %s """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)