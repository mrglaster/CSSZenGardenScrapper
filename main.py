# Import Required Library
import errno
import os
import  urllib.request

import requests
from bs4 import BeautifulSoup

sourcepath=os.getcwd()

for i in range(132,250):
    string_siteadr=''
    if i<10:
        string_siteadr="00"+str(i)
    elif i>=10 and i<=90:
        string_siteadr="0"+str(i)
    else:
        string_siteadr=str(i)

    web_url = "http://www.csszengarden.com/" + string_siteadr + '/' + string_siteadr + ".css"
    html = requests.get(web_url).content
    soup = BeautifulSoup(html, "html.parser")

    if not "Apache" in soup:

        src_soup = str(soup)
        neo_soup=src_soup
        src_soup = src_soup.replace('(', ' ')
        src_soup = src_soup.replace(')', ' ')
        files_to_download = [word for word in src_soup.split() if
                             word.endswith('gif') or word.endswith("png") or word.endswith("jpeg") or word.endswith(
                                 "jpg") or word.endswith("bmp")]
        soup = src_soup
        start = soup.find("'")
        soup = soup[start:]
        finish=soup.find("by")
        css_name =str(soup[1:finish-2])
        if css_name !='':
            if not os.path.exists("CSSGarden"):
                os.mkdir("CSSGarden")
            os.chdir("CSSGarden")
            print("Downloading: "+css_name)
            if not os.path.exists(css_name):
                css_name=css_name.replace(':',' ',1)
                css_name=css_name.replace('*',' ')
                css_name=css_name.replace('/',' ')
                if '!' in css_name:
                    css_name=css_name[:css_name.find('!')]
                os.mkdir(css_name)
            if not os.path.exists(sourcepath + "\\" + "CSSGarden" + "\\" + css_name + "\\" + string_siteadr):
                os.mkdir(sourcepath + "\\" + "CSSGarden" + "\\" + css_name + "\\" +string_siteadr)
            os.chdir(sourcepath + "\\" + "CSSGarden" + "\\" + css_name + "\\" + string_siteadr)
            file = open(string_siteadr + ".css", "w", encoding='utf-8')
            file.write(neo_soup)
            file.close()
            for j in files_to_download:
                j=j.replace('/','')
                j=j.replace(string_siteadr,'')
                if len(j)!=4:
                    try:
                        urllib.request.urlretrieve("http://www.csszengarden.com/" + string_siteadr + '/' + j, j)
                        print("http://www.csszengarden.com/" + string_siteadr + '/' + j)
                    except:
                        print(
                            "Oh-oh! We gon an error with image downloading. We guess, there was used another directory tree. You should download them by itself. link: http://www.csszengarden.com/" + string_siteadr + '/' + j)

            os.chdir(sourcepath + '\\' + "CSSGarden" + '\\' + css_name)
            url = "http://www.csszengarden.com/" + string_siteadr + '/'
            req = requests.get(url, 'html.parser')
            corr = "<link href=" + '"' +string_siteadr + '/' + string_siteadr + ".css" + '"' + " type=" + '"text/css" rel="stylesheet">'
            with open("index.html", 'w') as f:
                f.write(corr)
                f.write(req.text)
                f.close()
            os.chdir(sourcepath)


