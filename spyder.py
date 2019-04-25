from selenium import webdriver
import time
import smtplib
from email.mime.text import MIMEText

#download chrome for selenium that match your OS...
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", service_args=['--whitelisted-ips="x.x.x.x'])
driver.get('your web page address here')
driver.maximize_window()
driver.implicitly_wait(3)  # wait 30 seconds.

try:
    while True:
        time.sleep(5)
        nav = driver.find_element_by_id("messenger_display_inner")
        word = ["keywords", "xxxxx", "yyyyy"]
        if any (x in nav.text[:150] for x in word):
            safe = nav.text[:150]
            print("SEEEEEEEEEEEEND EMAIL")
            to = ["xxxxx gmail.com", "another email @someemail.com"]
            sender = "someone @gmail.com"
            msg = MIMEText(nav.text[:150])
            msg["Subject"] = "script email"
            msg["From"] = sender
            msg["To"] = ", ".join(to)
            s = smtplib.SMTP_SSL(host= "smtp.gmail.com", port = 465)
            s.login(user= "your username for gmail here", password = "your password for gmail here")
            s.sendmail(sender, to, msg.as_string())
            s.quit()
            print("MAIL was send")
            #checking just first 150 strings (change 150 to as you wish...)
            #send email
            while (x != nav.text[:150] for x in word):
                if safe == nav.text[:150]:
                    time.sleep(5)
                    #dont do nothing
                    print("Same word as before!")
                elif safe != nav.text[:150]:
                    print("New data came and I need to check if there is your keyword in!")
                    break

        elif (x not in nav.text[:150] for x in word):
            print("No new keyword yet. Sorry!")

except KeyboardInterrupt:
    print("Bye!")
    driver.close()
