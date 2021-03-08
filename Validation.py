""" Send OTP to email  """
from random import randint
import smtplib

def validate():
	otp = randint(1000, 9999)
	senderEmail = input("Enter your email: ")
	password = input("Enter your password: ")
	
	try:
		smtpObject = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObject.starttls()
		smtpObject.login(senderEmail, password)
		print("login success!")
		receiverEmail = input("Enter receiver's email: ")	
		message = str(otp)
		smtpObject.sendmail(senderEmail, receiverEmail, message)         
		print("OTP sent to " + receiverEmail + " successfully.")
	except Exception as E:
		print("Error: unable to send email", E)	

	otpByUser = int(input("Enter your otp: "))
	if otp != otpByUser:		
		print("You have entered invalid OTP!")
		exit()

 
	
