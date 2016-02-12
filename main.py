#!/usr/bin/env python2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import re


def say_stuff(tbox, stuff):
    tbox.send_keys(stuff)
    tbox.send_keys(Keys.RETURN)


def process_command(tbox, command):
    if command.startswith("trampman"):
        return

    if "gci" in command.lower():
        say_stuff(tbox, "XDDDDD")

    if command.lower()==".time":
        import datetime
        say_stuff(tbox, str(datetime.datetime.now()))


if __name__ == "__main__":
    dv = webdriver.Firefox()
    dv.get("http://www.facebook.com/")
    email = dv.find_element_by_id("email")
    password = dv.find_element_by_id("pass")
    email.send_keys("ignauy1")
    password.send_keys("contra123")
    password.send_keys(Keys.RETURN)

    time.sleep(10)

    dv.get("http://www.facebook.com/messages/")
    dv.implicitly_wait(10)
    dv.find_element_by_id("recent:thread:224877137849663").click()
    tbox = dv.find_element_by_css_selector(".uiTextareaNoResize.uiTextareaAutogrow")
    say_stuff(tbox, "hi im join xdddd")

    while True:
        # Hang for new element in .null group
        olds = dv.find_elements_by_css_selector(".null")
        while True:
            elems = dv.find_elements_by_css_selector(".null")
            if elems!=olds:
                tbox = dv.find_element_by_css_selector(".uiTextareaNoResize.uiTextareaAutogrow")
                process_command(tbox, elems[-1].find_element_by_css_selector("p").text)
                break
                    
    dv.close()

