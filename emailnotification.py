# this project is intended to automate the process to let your vendor know about your payments
# consider this a prototype and should no be used by nobody unless it is considered stable.

# also, this does not support two ways verification login

import smtplib

print("""
		This project was developed by raph-nov and its \n
		purpose is to automate the process of letting \n
		hotels and others accomodation services about \n 
		the payment. \n
		In the futere, i will let you choose or input your \n
		e-mail service provider. Default: Gmail. \n
		It may take a while to connect, but aways be sure \n
		to stay connected to the internet.
	""")
	
#connecting to servers
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# for future, if error smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

response = smtpObj.ehlo()
if response[0] == 250:
	smtpObj.starttls()
	smtpObj.login(input('User login: '), input('User password: '))
	

else:


