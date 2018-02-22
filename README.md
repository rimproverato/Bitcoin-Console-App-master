# Bitcoin Console App
READ ME
DOCUMENTATION
This is a little project we created using python 3.65 that can do the following:
-	Generate Random bitcoin private keys
-	Generate Random bitcoin Public keys
-	Generate Random bitcoin wallet address
-	Generate Random bitcoin Multisig  wallet keys
-	Hashing Bitcoin Addresses 
-	Send user bitcoin information to email
-	Send bitcoin transactions to email 
-	Send notifications to phone number 
Required libraries / Packages to install before using
●	Install pip then install the following using this commands 
-	pip install bitcoin
-	pip install pybitcointools
-	pip install blockchain
-	pip install nexmo
-	pip install reportlab
Private, Public Bitcoin keys and Bitcoin addresses 
Using this script you are able to generate random private keys, but you can also generate keys using methods like sha256 by replacing random_key with sha256 then inserting any string as your parameter 
Example:
PrivateVar = sha256(“Hello there”)
Using this script you can also generate public random bitcoin keys from private random keys and generate bitcoin addresses with the public keys 
Multisig Addresses
Just like generating private keys you can also generate private keys for the multisig that will be used for the wallet address , also on this you can choose to use random or sha256(“any string of any length ”).
Hashing
Using this script you can hash any bitcoin address or multi sig address 
Sending Bitcoin Information to Email
You can send bitcoin information on the mail using the smtplib library which needs to be imported. 
On the fields:
Mail = smtplib.SMTP (“Fill the mail service provider smtp. E.g smtp.gmail.com”, “The port number”)
Sending Notifications to phone number 
-	Make an account with nexmo at nexmo.com
-	Get the key and secret code from front page or settings 
-	Client.send_message({
‘from’: ‘Write were the message will be coming from’,
‘to’: ‘Write a phone number’ (starting with the country code),
‘text’: ‘fill the message that you can to send’,
‘err-code’: ‘Status of the message’
})
In case of any suggestions please get in touch with us.
