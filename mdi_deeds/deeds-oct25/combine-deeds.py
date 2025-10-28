import bs4
import os
import html
directory = './'
full_content = ''
tag_whitelist = ['br']
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.htm'):
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
            soup = bs4.BeautifulSoup(f.read(),'html.parser')
            for x in soup.find_all():
              if (len(x.get_text(strip=True)) == 0) and (x.name not in tag_whitelist):
                  x.extract()
            for content in soup.find_all('body'):
              final_content = content.decode_contents()
              full_content =  full_content + final_content
    else:
        continue

with open("all-deeds.html") as in_file:
    txt = in_file.read()
    soup = bs4.BeautifulSoup(txt,'html.parser')
    soup.body.append(full_content)

with open("all-deeds.html", "w", encoding='utf-8') as out_file:
    out_file.write(html.unescape(str(soup)))

