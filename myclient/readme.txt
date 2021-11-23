Weelcome to the guide for the profeseor rating system.
The client application invokes a number of API's to retrieve/send data to the professor rating server domain found at:

sc17s2e.pythonanywhere.com

The user credentials to be used are as followed (to access admin functions/account):
Username = 'ammar'
Password = 'Django20'

Please find information regarding the client application and the commands/syntax below:

•	register – To register a new account: which will then ask you for a username, password and email address.
•	login <URL> - To log into an existing account: which will ask you then for username and passoword.
•	logout – To logout when client is logged in.
•	list – To view a list of all module instances and the professors teaching them.
•	view – To view the average rating of all professors, rounded to the nearest digit.
•	average <professor_id> <module_code> - To view the average rounded rating of a certain professor in a certain module, additional arguments for unique professor ID and unique Module ID are needed here.
•	rate <professor_id> <module_code> <year> <semester> <rating> - If user is authenticated, rate the professor by supplying the additional arguments, where year is the teaching year (i.e. 2019), semester is a number from 1-2, and rating is a value between 1-5.
•	exit – To quit the client application.
