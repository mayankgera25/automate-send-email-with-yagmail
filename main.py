import yagmail
import os

sender = 'abc1@gmail.com'
receiver = 'abc2@gmail.com'

subject = "This is the subject"

contents ="""
Hi!
Here is the content of the email!
"""
sender_password = input(f'Please enter the password for {sender}: \n')
yag = yagmail.SMTP(user=sender, password=sender_password)

yag.send (to=receiver, subject = subject, contents=contents)


print('EMail Sent')