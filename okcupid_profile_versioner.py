#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys

def login_as_user_and_get_response(session, url, login_info):
    p = session.post(url, data=login_info)
    authlink_cookie = p.cookies['authlink']
    # OkCupid does not give the 'session' cookie, but it seems to work anyway.
    logged_in_cookies = {"authlink":authlink_cookie}
    return logged_in_cookies

def main():
    """First, parse command line arguments.
    Arguments are: 
        username
    """
    try:
        username = sys.argv[1]
    except IndexError:
        print "Must specify a username. Type your username as the first argument."
        print "Eg. $ python okcupid_profile_versioner.py my_username"
        exit()

    file_name = "profile_okcupid_{}.html".format(username)
    file_path = "../okcupid/"

    # First, try posting login credentials to the site.
    # Note: Put in information for a dummy account!
    # Note: The empty 'p' and 'dest' keys are absolutely required.
    session = requests.session()
    login_info = {"username":"sandy_asaurus", "password":"sandyman", "p":"", "dest":""}
    logged_in_cookies = login_as_user_and_get_response(session, 
        "http://www.okcupid.com/login", 
        login_info)

    r = session.get('http://www.okcupid.com/profile/{}'.format(username), cookies=logged_in_cookies)
    
    list_of_divs = ['essay_text_0', 'essay_text_1', 'essay_text_2', 
        'essay_text_3', 'essay_text_4', 'essay_text_5', 'essay_text_6', 
        'essay_text_7', 'essay_text_8', 'essay_text_9']
    soup = BeautifulSoup(r.text)
    #print r.text

    html_output = ""
    for div_id in list_of_divs:
        # Get the HTML contents of the relevant div
        try:
            text = soup.select('div[id="{0}"]'.format(div_id))[0].contents
        except IndexError:
            print "No content found in {} for username '{}'.".format(div_id, username)
        for line in text:
            html_output += str(line)
        html_output += "<hr />"
    f = open(file_path + file_name, 'w+')
    f.write(html_output)
    f.close()

    print "-" * 80

if __name__ == "__main__":
    main()


