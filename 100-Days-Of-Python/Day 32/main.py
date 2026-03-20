import smtplib

my_email = "singhanamika5647@gmail.com"
password = "fyyxitktgkzetqer"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls() 
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="rashikasingh191@gmail.com", 
                        msg="Subject:Test\n\nThis is the dummy email."
                    )











#TLS stands for Transport Layer Security. 
# It is a cryptographic protocol that provides secure communication over a computer network. 
# When you use TLS, the data sent between your email client and the email server is encrypted,
# making it more difficult for unauthorized parties to intercept and read the information. 
# This helps protect your email credentials and the content of your emails from being accessed by malicious actors.


              