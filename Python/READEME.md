

Objective - 

Create a password Generator & Vault which encrypts all generated passwords; 

Arhcitecture: 

	-Password main 


		this file will prompt the user to generate a password, with length 
		and special characters in mind. That will then send a request to the
		passoword vualt 

		-User Login /Restricts access to service 


	- Password Vault 
		this file will have vault.txt file attached to it. The purpose of this file
		is to, upon request, generate a password for the user with requests made 
		in mind. Next, it will be encrypted and stored in the vault.txt.
		
		using some sort of identifier(either ssh key or login credentials)will 
		allow for the main file to recieve the password in plain text. 

		Based on the user login, they will be able to directly access their
		passwords. 
			
