# emailnotification

The purpose of this project is to automate the process of let your vendors know about the payment you 
did on their behalf.

The main process is simples:

Language primary: Python 3.6.3
Dependencies: openpyxl, smtplib and sys

Requirements: e-mail API for smtp connection -- looking for a way no to use it.

Process:
	Control your payments through a spreadsheet: Openoffice or MS
	If you have 2 or more companies to control payments, so it should start a process in row.
	Look at your payments base:
		The base should contain vendors name, amount paid by invoice, reference number and contact e-mail. 
		For one vendor, if you were paying more the one invoice, it should calculate the whole amount you payd for this specific vendor, aggregate in a string the reference code (such as reservation number for hotels, etc.) and the invoice numbers in another string.
		With buffer, will create two variables, on buffer, an email assumption and a subject email. Both strings.

	Collect this both string variables and them use assumption a body to create a customized email.
	Look at the base and collect the emails and store in a tupple.

	After this, it will build and send the e-mail.
	If there is a swift receipt or any other kind of bank receipt, it should attach to the email as well.

	Look for the next vendor and loop over the data base.

	Close smpt connection, register on the base if the payment was notified and them save and close the base.


If you find it helpful, feel free for using this program.
Also, I would appreciate if you comment, sugest or even pull this repository. 
