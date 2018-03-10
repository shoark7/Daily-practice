"""Send a simple email message via Gmail open server


Date: 2018/03/06
"""

import getpass
import smtplib
import sys


from_ = 'shoark7@gmail.com'
to_ = ['dlwngud37@gmail.com', 'shoark7@naver.com']
subject = "A test message"
body = "Hey, whats's up!!\n\n From Sunghwan"


email_text = """\
From: {from_}
To: {to_}
Bcc: shoark7@naver.com
Subject: {subject}

{body}
""".format(from_=from_, to_=to_,
           subject=subject, body=body)

if __name__ == '__main__':
    id_ = input("ID(@)   : ").strip()
    password = getpass.getpass()
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    except:
        print("Connection cannot be made...")

    try:
        server.login(id_, password)
    except:
        sys.exit('Login not successful')
    else:
        server.sendmail(from_, to_, email_text)
        server.close()
        print("Email sent")
        print("Something went wrong")

