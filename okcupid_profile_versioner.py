import requests
from bs4 import BeautifulSoup

file_name = "okcupid_profile{}".format('.html')
file_path = "../okcupid/"
r = requests.get('http://www.okcupid.com/profile/paragonrg')
list_of_divs = ['essay_text_0', 'essay_text_1', 'essay_text_2', 'essay_text_3', 'essay_text_4', 'essay_text_5', 'essay_text_6', 'essay_text_7', 'essay_text_8', 'essay_text_9']
#list_of_divs = ['essay_text_0']
soup = BeautifulSoup(r.text)


f = open(file_path + file_name, 'w+')
for div_id in list_of_divs:
    text = soup.select('div[id="{0}"]'.format(div_id))[0].contents
    for line in text:
        #print str(line)
        f.write(str(line))
    f.write("<hr />")
    #print text
    #print text
f.close()

print "-" * 80
