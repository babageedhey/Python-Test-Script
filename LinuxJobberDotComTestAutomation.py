import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common import keys

parser = ConfigParser()

#Create a credentials.ini file with the your following details to test.
# [web.linuxjobber.com/admin]
# username : your username
# password : your password

# [web.linuxjobber.com]
# firstname : your name
# lastname : your last name
# username : your username
# password : your password
# fullname : any name

parser.read("credentials.ini")

driver = webdriver.Chrome(r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobber\chromedriver.exe")

#################################################################################################################

#################################################################################################################
def Login(username, password):

	driver.find_element_by_link_text("Log In").click()

	driver.find_element_by_id("username").send_keys(username)

	driver.find_element_by_id("password").send_keys(password)
	
	driver.find_element_by_xpath(".//*[@id='UserLoginForm']/div[5]/button").click()

def login(username, password):
	driver.find_element_by_id("username").send_keys(username)

	driver.find_element_by_id("password").send_keys(password)
	
	driver.find_element_by_xpath(".//*[@id='UserLoginForm']/div[6]/button").click()


def sign_up(fullname, email, password):
	driver.find_element_by_link_text("Sign Up").click()

	driver.find_element_by_id('fullname').send_keys(fullname)

	driver.find_element_by_id('email').send_keys(email)

	driver.find_element_by_id('password').send_keys(password)

	driver.find_element_by_xpath(".//*[@id='myform']/div[6]/button").click()


def create_account(fullname, email, password):
	driver.find_element_by_id('fullname').send_keys(fullname)

	driver.find_element_by_id('email').send_keys(email)

	driver.find_element_by_id('password').send_keys(password)

	driver.find_element_by_xpath(".//*[@id='myform']/div[6]/button").click()


def view_personal_profile():
	driver.get("http://web.linuxjobber.com")
	driver.implicitly_wait(10)
	username = input("Enter the Username you wish to login with and hit Enter: ")
	password = input("Enter the Password and hit Enter: ")
	Login(username, password)
	driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[3]/nav/ul/li/a").click()
	driver.find_element_by_xpath(".//*[@id='profile']/div/div[1]/ul/li[1]/a").click()


def in_person_training():
	driver.get('http://web.linuxjobber.com/homes/liveinstructor')
	contact_us = int(input("If you want to see contact us page Press 1 and hit Enter \n If you would want to proceede with payment press 0 and hit Enter: "))
	if contact_us is 1:
		driver.find_element_by_link_text('Contact Us').click()
		call_us = int(input("If you wish to contact via phone call press 1 and hit enter \n If you would want to contact via message hit 0 and press Enter: "))

		if call_us is 1:
			driver.find_element_by_partial_link_text('1.443.538').click() #click phone number but clicking this redirects to same page instead of placing call.
		elif call_us is 0:
			fullname = input("Enter fullname of sender of message and hit Enter: ")
			phone_number = input("Enter phone number and hit Enter: ")
			email = input("Enter email and hit Enter:")
			subject = input("Enter the message subject and hit Enter:")
			message = input("Type Message and hit Enter: ")

			driver.find_element_by_id('fname').send_keys(fullname)
			driver.find_element_by_id('phone').send_keys(phone_number)
			driver.find_element_by_id('email').send_keys(email)
			driver.find_element_by_id('subject').send_keys(subject)
			driver.find_element_by_id('message').send_keys(message)
			driver.find_element_by_class_name('btn').click()
		else:
			print("The option you selected is not valid")
			in_person_training()
	elif contact_us is 0:
		driver.find_element_by_link_text('Buy Now').click() #Flow diagram doesnt cover what happens if user has already subscribed and if user hasnt already subscribed
		name = input("Enter the name of the user and hit Enter: ")
		phone_number = input("Enter phone number and hit Enter: ")
		email = input("Enter email and hit Enter:")

		driver.find_element_by_id('name').send_keys(name)
		driver.find_element_by_id('email').send_keys(email)
		driver.find_element_by_id('phone').send_keys(phone_number)
		driver.find_element_by_id('sub').click()
		driver.find_element_by_class_name('stripe-button-el').click()
		driver.switch_to.frame("stripe_checkout_app")
		driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
		driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
		driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
		driver.find_element_by_xpath("//*[@type='submit']").click()


def account_settings():
	driver.get('http://web.linuxjobber.com')
	already_sign_up = int(input("To run test as registered user press 1 and hit enter \n To run test as unregistered user press 0 and hit enter: "))
	if already_sign_up is 1:
		email = input("Enter an email and hit enter: ")
		password = input("Enter a password and hit enter: ")
		Login(email, password)
		driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[3]/nav/ul/li/a").click()
		driver.find_element_by_xpath(".//*[@id='profile']/div/div[1]/ul/li[2]/a").click()
		driver.find_element_by_xpath(".//*[@class='video-study']/div/div/p/iframe").click()
		time.sleep(10)
		driver.find_element_by_name("data[csvfile]").send_keys("C:\\Users\\Louis\\LinuxjobberWorkSpace\\incomming  files\\extracted\\credentials.csv")
		driver.find_element_by_xpath("html/body/div[2]/div/section[1]/div/div/div/form/button").click()
		driver.find_element_by_xpath("html/body/div[2]/div/section[3]/div/div").click()
	elif already_sign_up is 0:
		fullname = input("Enter a name and hit enter: ")
		email = input("Enter an email and hit enter: ")
		password = input("Enter a password and hit enter: ")
		sign_up(fullname, email, password)
		driver.get('http://web.linuxjobber.com')
		Login(email, password)
		driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[3]/nav/ul/li/a").click()
		driver.find_element_by_xpath(".//*[@id='profile']/div/div[1]/ul/li[2]/a").click()
		driver.find_element_by_xpath(".//*[@class='video-study']/div/div/p/iframe").click()
		time.sleep(10)
		driver.find_element_by_name("data[csvfile]").send_keys("C:\\Users\\Louis\\LinuxjobberWorkSpace\\incomming  files\\extracted\\credentials.csv")
		driver.find_element_by_xpath("html/body/div[2]/div/section[1]/div/div/div/form/button").click()
		driver.find_element_by_xpath("html/body/div[2]/div/section[3]/div/div").click()
	else:
		print("--------The option you selected is not valid, please try again--------")
		account_settings()


def group_class():

	driver.get('http://web.linuxjobber.com')
	registered = int(input("--------To run test as unregistered user press 0 and hit Enter-------- \n --------To run test as registered user press 1 and hit Enter--------: "))
	if registered is 0:

		fullname = input("Enter a name and hit enter: ")
		email = input("Enter an email and hit enter: ")
		password = input("Enter a password and hit enter: ")

		driver.find_element_by_link_text("Group Class").click()
		driver.find_element_by_link_text("Enroll Now").click()
		driver.find_element_by_id("fullname").send_keys(fullname)
		driver.find_element_by_id("email").send_keys(email)
		driver.find_element_by_id("password").send_keys(password)
		driver.find_element_by_class_name("submit").click()
		driver.find_element_by_class_name('stripe-button-el').click()
		driver.switch_to.frame("stripe_checkout_app")
		driver.find_element_by_xpath("//*[@placeholder='Email']").send_keys(email)
		driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
		driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
		driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
		driver.find_element_by_xpath("//*[@type='submit']").click() #on completion user should be logged in automatically and should see payment page.
	elif registered is 1:
		logged_in = int(input("--------To run test as logged-in user press 1 and hit Enter-------- \n --------To run test as a not logged-in user press 0 and hit Enter--------: "))
		if logged_in is 0:

			fullname = input("Enter a name and hit enter: ")
			email = input("Enter an email and hit enter: ")
			password = input("Enter a password and hit enter: ")

			driver.find_element_by_link_text("Group Class").click()
			driver.find_element_by_link_text("Enroll Now").click()
			driver.find_element_by_id("fullname").send_keys(fullname)
			driver.find_element_by_id("email").send_keys(email)
			driver.find_element_by_id("password").send_keys(password)
			driver.find_element_by_class_name("submit")
		elif logged_in is 1:

			fullname = input("Enter a name and hit enter: ")
			email = input("Enter an email and hit enter: ")
			password = input("Enter a password and hit enter: ")

			Login(email, password)

			driver.find_element_by_link_text("Group Class").click()
			driver.find_element_by_link_text("Enroll Now").click()
			driver.find_element_by_id("fullname").send_keys(fullname)
			driver.find_element_by_id("email").send_keys(email)
			driver.find_element_by_id("password").send_keys(password)
			driver.find_element_by_class_name("submit").click()
		else:
			print("--------The option you selected is not valid, please try again--------")
			group_class()
	else:
		print("--------The option you selected is not valid, please try again--------")
		group_class()


def resume_service():
	#This is for both loggedin user and not logged in user.

	firstname = input("Enter a firstname and hit enter: ")
	lastname = input("Enter a lastname and hit enter: ")
	email = input("Enter an email and hit enter: ")

	driver.get('http://web.linuxjobber.com')
	driver.find_element_by_link_text('Resume Services').click()
	driver.find_element_by_link_text('Buy Now').click()
	driver.find_element_by_id('fname').send_keys(firstname)
	driver.find_element_by_id('lname').send_keys(lastname)
	driver.find_element_by_id('email').send_keys(email)
	driver.find_element_by_id('btnpaynow').click()
	#No working paypal account to proceed with testing.
	#After successful payment, user should be able to upload sample resume
	#Live professional guides user
	#User colpletes and review resume.


def student_package():
	#This test case covers both logged-in users and not registered/not logged-in users

	driver.get('http://web.linuxjobber.com')
	driver.find_element_by_link_text('Student Packages').click()

	firstname = input("Enter a firstname and hit enter: ")
	lastname = input("Enter a lastname and hit enter: ")
	email = input("Enter an email and hit enter: ")

	plan = int(input("--------To test Standard package press 1 and hit Enter--------\n --------To test premium package subscription press 2 and hit Enter--------: "))
	if plan  is 1:
		driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[1]/div/div[3]/a").click()
		driver.find_element_by_id('fname').send_keys(firstname)
		driver.find_element_by_id('lname').send_keys(lastname)
		driver.find_element_by_id('email').send_keys(email)
		driver.find_element_by_name('submit').click()
		driver.find_element_by_class_name('stripe-button-el').click()
		driver.switch_to.frame("stripe_checkout_app")
		driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
		driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
		driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
		driver.find_element_by_xpath("//*[@type='submit']").click()
	elif plan is 2:
		driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[3]/div/div[3]/a").click()
		driver.find_element_by_id('fname').send_keys(firstname)
		driver.find_element_by_id('lname').send_keys(lastname)
		driver.find_element_by_id('email').send_keys(email)
		driver.find_element_by_name('submit').click()
		driver.find_element_by_class_name('stripe-button-el').click()
		driver.switch_to.frame("stripe_checkout_app")
		driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
		driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
		driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
		driver.find_element_by_xpath("//*[@type='submit']").click()
	else:
		print("--------The option you selected is not valid, please try again--------")
		student_package()



def job_placement():
	driver.get('http://web.linuxjobber.com')

	firstname = input("Enter a firstname and hit enter: ")
	lastname = input("Enter a lastname and hit enter: ")
	email = input("Enter an email and hit enter: ")
	password = input("Enter a password and hit enter: ")

	loggedin = int(input("--------To run as logged-in user press 1 and hit Enter--------\n--------To run test with a not logged in user press 0 and hit Enter--------: "))
	if loggedin is 1:
		level = int(input('-------To test application for Entry Level press 1 and hit Enter--------\n --------To test application for senior level press 2 and hit Enter--------: '))
		if level is 1:
			driver.find_element_by_xpath('html/body/div[4]/div[2]/div/div[1]/a/button').click() #user is on job placement page here
			driver.find_element_by_xpath('html/body/section[4]/div[1]/div/div[1]/div/div/a').click()
			login(email, password) #After this login, the next page user sees should be jobplacement form page.
			driver.find_element_by_id('firstname').send_keys(firstname)
			driver.find_element_by_id('lastname').send_keys(lastname)
			driver.find_element_by_id('email').send_keys(email)
			driver.find_element_by_xpath(".//*[@id='education']/option[5]").click()
			driver.find_element_by_id('JobplacementsResume').send_keys("C:\\Users\\Louis\\LinuxjobberWorkSpace\\DjangoLabs\\LabsDocs\\Lab 1 Installing Django.docx")
			driver.find_element_by_xpath(".//*[@id='app']/div[7]/input").click()
			has_certificate = int(input("--------To run test as user with certificate press 1 and hit Enter--------\n--------To run test as user without certificate press 0 and hit Enter--------: "))
			if has_certificate is 1:
				driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[6]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsCertificate']").send_keys("C:\\Users\\Louis\\LinuxjobberWorkSpace\\DjangoLabs\\LabsDocs\\Lab 1 Installing Django.docx")
				driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
				driver.find_element_by_id("but").click()
			elif has_certificate is 0:
				driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[6]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[2]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
				driver.find_element_by_id("but").click()
			else:
				print("--------The option you selected is not valid, please try again--------")
				job_placement()
		elif level is 2:
			driver.find_element_by_xpath('html/body/div[4]/div[2]/div/div[1]/a/button').click() #user is on job placement page here
			driver.find_element_by_xpath('html/body/section[4]/div[2]/div/div/div[2]/div/div/a').click()
			login(email, password) #After this login, the next page user sees should be jobplacement form page.
			driver.find_element_by_id('firstname').send_keys(firstname)
			driver.find_element_by_id('lastname').send_keys(lastname)
			driver.find_element_by_id('email').send_keys(email)
			driver.find_element_by_xpath(".//*[@id='education']/option[5]").click()
			driver.find_element_by_id('JobplacementsResume').send_keys("C:\\Users\\Louis\\LinuxjobberWorkSpace\\DjangoLabs\\LabsDocs\\Lab 1 Installing Django.docx")
			driver.find_element_by_xpath(".//*[@id='app']/div[7]/input").click()
			has_experience = int(input("--------To run test as user with Experience press 1 and hit Enter--------\n--------To run test as user without Experience press 0 and hit Enter--------: "))
			if has_experience is 1:
				driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[8]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsExperience']/option[5]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
				driver.find_element_by_id("but").click()
			elif has_experience is 0:
				driver.find_element_by_xpath(".//*[@id='JobplacementsCareer']/option[8]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsExperience']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsCertification']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsTraining']/option[1]").click()
				driver.find_element_by_xpath(".//*[@id='JobplacementsWilliness']/option[1]").click()
				driver.find_element_by_id("but").click()	
			else:
				print("--------The option you selected is not valid, please try again--------")
				job_placement()
		else:
			print("--------The option you selected is not valid, please try again--------")
			job_placement()


	elif loggedin is 0:
		driver.find_element_by_xpath('html/body/div[4]/div[2]/div/div[1]/a/button').click()
		level = int(input('-------To test application for Entry Level press 1 and hit Enter--------\n --------To test application for senior level press 2 and hit Enter--------: '))
		if level is 1:
			driver.find_element_by_xpath('html/body/section[4]/div[1]/div/div[1]/div/div/a').click()
		elif level is 2:
			driver.find_element_by_xpath('html/body/section[4]/div[2]/div/div/div[2]/div/div/a').click()
		else:
			print("--------The option you selected is not valid, please try again--------")
			job_placement()
	else:
		print("--------The option you selected is not valid, please try again--------")
		job_placement()



def work_experience():
	driver.get("http://web.linuxjobber.com")

	email = input("Enter an email and hit enter: ")
	password = input("Enter a password and hit enter: ")

	user = int(input("--------To run test as anonymous user press 0 and hit enter-------- \n --------To run test as an unanonymous user press 1 and hit enter--------: "))
	if user is 0:
		driver.find_element_by_id('wkexbtn').click()
		driver.find_element_by_xpath("html/body/section[3]/div/div/div[2]/div/div/a") #At this point user is not allowed to see the payment page and is redirected to login page
	elif user is 1:
		signed_up = int(input('--------To run test as registered user press 1 and hit Enter--------\n To run test as unregistered user press 0 and hit Enter--------: '))
		if signed_up is 0:
			driver.find_element_by_id("wkexbtn").click()
			driver.find_element_by_xpath("html/body/section[3]/div/div/div[2]/div/div/a").click() #Clicks on Apply now under Areas of Specilization
			driver.find_element_by_xpath(".//*[@id='UserLoginForm']/div[5]/a[2]/p").click() #Clicks on create account on login page
			create_account()
			login(email, password)
			#Test fails here, user is suppose to see payment page as soon as login is successful.
			driver.find_element_by_class_name('stripe-button-el').click()
			driver.switch_to.frame("stripe_checkout_app")
			driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
			driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
			driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
			driver.find_element_by_xpath("//*[@type='submit']").click()
			driver.find_element_by_link_text("Proceed to agreement page").click()
		elif signed_up is 1:
			Login(email, password)
			driver.find_element_by_id("wkexbtn").click()
			driver.find_element_by_xpath("html/body/section[5]/div/div/div[1]/div/div/a").click()#Clicks on apply now under 'For Fresh Students'
			driver.find_element_by_class_name('stripe-button-el').click()
			driver.switch_to.frame("stripe_checkout_app")
			driver.find_element_by_xpath("//*[@type='tel']").send_keys("42424242424242424")
			driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys("1219")
			driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys("1234")
			driver.find_element_by_xpath("//*[@type='submit']").click()
			driver.find_element_by_link_text("Proceed to agreement page").click()
		else:
			print("--------The option you selected is not valid, please try again--------")
			work_experience()
	else:
		print("--------The option you selected is not valid, please try again--------")
		work_experience()

#Refactoring code begins here
def login_auto():
	driver.get("http://web.linuxjobber.com/users/login")#navigate to linuxjobber.com
	username = parser.get('web.linuxjobber.com/users/login', 'username')
	password = parser.get('web.linuxjobber.com/users/login', 'password')
	driver.find_element_by_id('username').send_keys(username)
	driver.find_element_by_id('password').send_keys(password)
	driver.find_element_by_xpath(".//*[@type='submit']").click()

def login_autoAdmin():
	driver.get("http://web.linuxjobber.com/admin")#navigate to linuxjobber.com/admin
	username = parser.get('web.linuxjobber.com/admin', 'username')
	password = parser.get('web.linuxjobber.com/admin', 'password')
	driver.find_element_by_id('username').send_keys(username)
	driver.find_element_by_id('password').send_keys(password)
	driver.find_element_by_xpath(".//*[@type='submit']").click()	




def instructor_filter():
	#Only Admin user persmission can test
	login_autoAdmin()
	driver.find_element_by_xpath(".//*[@id='sidebar']/ul/li[5]/a").click() #Click the lab tab link
	driver.find_element_by_xpath(".//*[@class='form-horizontal']/select").click() #Select Option from dropdown menu
	driver.find_element_by_xpath(".//*[@class='form-horizontal']/select/option[2]").click()#Select the first option in the dropdown menu
	driver.find_element_by_xpath(".//*[@class='form-horizontal']/input").click() #click the search button

def clickGroupClass():
		driver.find_element_by_link_text('Group Class').click()


def groupClass_videoSelect():
		
	driver.get('http://web.linuxjobber.com')
	#Two  Test Cases Regular User and Guest User
	user = int(input("""Test as Guest User no option selected press 0 enter:\n
		 Test as a Guest User option selected press 1 and enter:\n
		 Test as Regular User no option selected press 2 and enter:\n
		 Test as Regular User option selected press 3 and enter: """))
	if user is 0:
		#Guest User no option selected 
		clickGroupClass()
		driver.find_element_by_xpath(".//*[@id='register']/button").click()
		groupClass_videoSelect()

	elif user is 1:
		#Guest User option selected
		clickGroupClass()
		driver.find_element_by_xpath(".//*[@class='groupbox']/input").click()
		driver.find_element_by_xpath(".//*[@id='register']/button").click()
		groupClass_videoSelect()
	elif user is 2:
		#Regular User no option selected
		login_auto()
		clickGroupClass()
		driver.find_element_by_xpath(".//*[@id='register']/button").click()
		groupClass_videoSelect()
	elif user is 3:
		#Regular User option selected
		clickGroupClass()
		driver.find_element_by_xpath(".//*[@class='groupbox']/input").click()
		driver.find_element_by_xpath(".//*[@id='register']/button").click()
		groupClass_videoSelect()
	else:
		print('Invalid Option Selected... please use 0, 1, 2, 3')












def main():
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("To select ")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	choice = int(input
	("""1 : Test Account Settings\n 
		2 : Test Group Class\n 
		3 : Test In-Person Training\n 
		4 : Test Job Placement\n 
		5 : Test Resume Services\n 
		6 : Test Student Package\n 
		7 : Test Work Experience\n 
		8 : Test Personal Profile View\n 
		9:  Test Instructor Filter\n 
		10: Test Group Class Select\n
		Enter choice number:"""))
	if choice is 1:
		account_settings()
	elif choice is 2:
		group_class()
	if choice is 3:
		in_person_training()
	elif choice is 4:
		job_placement()
	if choice is 5:
		resume_service()
	elif choice is 6:
		student_package()
	if choice is 7:
		work_experience()
	elif choice is 8:
		view_personal_profile()
	if choice is 9:
		instructor_filter()
	elif choice is 10:
		groupClass_videoSelect()
	else:
		print("You have selected an invalid option, please try again")
		main()


if __name__ == '__main__':
	main()
