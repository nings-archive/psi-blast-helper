#! /usr/bin/env python3

import re
from selenium import webdriver
from Hit import Hit

NCBI_BLAST_URL_REGEX = '^https://blast\.ncbi\.nlm\.nih\.gov/Blast\.cgi'
HIDE_FEEDBACK_JS_SCRIPT = 'hide-feedback-button.js'

global driver

def init():
    global driver
    driver = webdriver.Chrome()

def is_results_page():
    return get_hit_rows() != []

def get_hits():
    hide_feedback_button()
    return [
        Hit(web_element) for web_element in
        driver.find_elements_by_xpath("//table[@id='dscTable']/tbody/tr")
    ]

def hide_feedback_button():
    script = get_js_script()
    driver.execute_script(script)

def get_js_script():
    with open(HIDE_FEEDBACK_JS_SCRIPT, 'r') as js_file:
        return js_file.read()

if __name__ == '__main__':
    init()
