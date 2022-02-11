import smtplib, ssl,datetime

sender= "revamaskup@gmail.com"     #senders email id
password="reva@123"                #password



def email_pin(email,pin):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    if(date[0]=='0'):
        date=date[1:]
    subject="Pin for your MASK-UP app "
    text="\nYour pin for MASK-UP app is "+str(pin)

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, email, message)

    print("sent email!")



def send_email(receiver_mail,attendance):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    subject="Fine on "+str(date)
    text="\nWARNING!\n"+attendance

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver_mail , message)

    print("sent email!")