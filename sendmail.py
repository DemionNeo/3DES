import yagmail
username = "leonnel230"
password = "elht hjhn bfpr vvxf"
def mail_send(receiver_email,content):
    yag = yagmail.SMTP(username,password)
    yag.send(receiver_email, 'subject', content)







