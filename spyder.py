#!/usr/bin/python

from selenium import webdriver
import time
import smtplib
from email.mime.text import MIMEText
from selenium.common import exceptions

driver = webdriver.Chrome(executable_path=r"C:\projects\chromedriver.exe", service_args=['--whitelisted-ips="x.x.x.x'])
driver.get('https://www.livesquawk.com/player/?referer=forex_delay')
driver.maximize_window()
driver.implicitly_wait(3)  # wait 3 seconds.


def script():
    try:
        count = 1
        while True:
        time.sleep(5)
        nav = driver.find_element_by_id("messenger_display_inner")
        word = ["keywords", "xxxxx", "yyyyy"]
        if any (x in nav.text[:150] for x in word):
            safe = nav.text[:150]
            print("SEEEEEEEEEEEEND EMAIL")
            to = ["xxxxx gmail.com", "another email @someemail.com"] #Add email to be send to
            sender = "someone @gmail.com" #Add your sender email
            msg = MIMEText(nav.text[:150])
            msg["Subject"] = "script email"
            msg["From"] = sender
            msg["To"] = ", ".join(to)
            s = smtplib.SMTP_SSL(host= "smtp.gmail.com", port = 465) #Change if not using gmail
            s.login(user= "your username for gmail here", password = "your password for gmail here") #Your userhame and pass for gmail here
            s.sendmail(sender, to, msg.as_string())
            s.quit()
            print("MAIL was send")
            #checking just first 150 strings (change 150 to as you wish...)
            #send email
                while (x != nav.text[:150] for x in word):
                    if safe == nav.text[:150]:
                        time.sleep(5)
                        #dont do nothing
                        count += 1
                        print(count)
                        if count >= 200:
                            print(count)
                            count = 1
                            driver.refresh()
                        print("Same word as before!")
                    elif safe != nav.text[:150]:
                        print("New data came and I need to check if there is your keyword in!")
                        break

            elif (x not in nav.text[:150] for x in word):
                count += 1
                print(count)
                if count >= 200:
                    print(count)
                    count = 1
                    driver.refresh()
                print("No new keyword yet. Sorry!")
    except exceptions.StaleElementReferenceException: #exceptions handler. sometimes server is slow with refreshing web page and python raise an error. These one handles it to rerun all script.
        print("Oh no Error")
        script()

script()
