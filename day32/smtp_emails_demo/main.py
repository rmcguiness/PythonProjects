import smtplib

my_email = 'enter_email@gmail.com'
password = 'get_password_from_gmail_for_new_app'

with smtplib.SMTP("smtp.gmail.come") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='enter_TO_email@gmail.com',
        msg="Subject:Your Subject here \n\n This is the Body of the email."
    )
