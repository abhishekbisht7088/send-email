import smtplib, ssl

def send_email(msg):
        port = 465 #for SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "" #sender email
        reciever_email = "" # reciever's email
        password = "" #password of sender's email id 

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            try:
                server.login(sender_email, password) #login
                res = server.sendmail(sender_email,reciever_email,msg) #send mail to one or list of recievers
                print('email sent successfull !')
            except:
                print('Cannot send mail due to issue')


send_email("hola amigo")