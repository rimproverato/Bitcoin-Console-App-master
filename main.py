from bitcoin import*
from blockchain import blockexplorer
from blockchain import pushtx
import nexmo
import smtplib
from reportlab.pdfgen import canvas
from email.mime.text import MIMEText
from  email.mime.base import MIMEBase
from email import encoders

print ("Press 1 to generate a random private key")
print ("Press 2 to generate a random Public key")
print ("Press 3 to generate a random Wallet Address")
print ("press 4 to create a multisig address")
print(" Press 5 Hash Address")
print ("Press 6 Send Bitcoin Info to Email")
print ("Press 7 to Send bitcoin Transtions to Email")
print ("Press 8 Send Notification to phone Number")
print ("Press 7 to Exit")
print ("-----------------------------------------------")

Transaction = history("1CucinVK34txDn6Lxp1VjTpzi2J8FLXxe7")
EmailReport = canvas.Canvas ("Transactions.pdf")
EmailReport.drawString(200,800, "YOUR BITCOIN  TRANSACTION " + str(Transaction))
EmailReport.save()

answer = input ()
PrivateVar = random_key()

#Generating a Random Private Key
if answer == "1":
    print (PrivateVar)
    print ("-----------------------------------------------")

PublicVar = privtopub(PrivateVar)

#Generating a Random Public Key
if answer == "2":
    print (PublicVar)
WalletAddress = pubtoaddr(PublicVar)

# Generating a Random Wallet Address
if answer == "3":
    print (WalletAddress)

#Generating a ,ultiSig Wallet Address
if answer == "4":
    PrivateVar1 = privtopub(random_key())
    PrivateVar2 = privtopub(random_key())
    PrivateVar3 = privtopub(random_key())
    PrivateVar4 = privtopub(random_key())
    PrivateVar5 = privtopub(random_key())
    MultiSigAddressMaker = mk_multisig_script(PrivateVar2,PrivateVar1,PrivateVar3,PrivateVar4, PrivateVar5, 5,5)
    MultiSigAddress = scriptaddr (MultiSigAddressMaker)
    print(MultiSigAddress)
    SigAddress = str(MultiSigAddress)

#Hashing Address
if answer == "5":
    print("Enter Your Bitcoin Address")
    WalletAddress = input()
    Hashed = txhash(WalletAddress)
    print(Hashed)

#Sending  info to Email
if answer == "6":
    print("Please enter your Email Address: ")
    EmailAddres = input()
    subject = "Your Bitcoins Info"
    content = "Below Are you Bitcoin Details \n\n" + "Private Key "  + PrivateVar + "\n\n" + "Public Key: " + PublicVar + "\n\n" + "Wallet Address " + WalletAddress + "\n\n"
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("Your Email Address", "Your Password")
    mail.sendmail("africanbitcoins@gmail.com", EmailAddres, content)
    print("Email send Succesfully ")
    mail.close()

#Sending Transactions to  Email
if answer == "7":
    print("Please enter your Email Address: ")
    EmailAddres = input()
    print("Enter Your Bitcoin Address")
    UserAddress = input()
    BitTransaction = (history (UserAddress))
    subject = "Your BitCoin Transactions"
    content = "Bitcoin Transaction: " + BitTransaction
    print(BitTransaction)
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("Your Email Address", "Your Password")
    mail.close()

# Sending Notification to Phone Number
if answer == "8":
    print("Please enter phone number e.g +2547XXXXXXXXX: ")
    PhoneNumber = input()
    client = nexmo.Client(key="Nexmo Key",secret="Nexmo Secret")
    client.send_message ({
        'from': 'BitHub Africa',
        'to': PhoneNumber,
        'text': 'Thank you for resgistering with BitHub Africa. Here are your Details: \n' + WalletAddress,
        'err-code': "0"
    })

