'''
https://pypi.org/project/requests-html/


pip install requests-HTML




from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get(url)

html = r.html
or
html = HTML(html, source). # source could be a file or a url

match = html.find('title'). # returns the title tag as a list so use [n] or first=True

print(match[0])
print(match[0].text)
print(match[0].html)

match = html.find('title', first = True)

match = html.find('#footer', first = True)

match = html.find('header', first = True)

match = html('div.article', first = True)

match = html('div#article', first = True)

submatch = match.find('h2', fist = True)

submatch = match.find('p', fist = True)

match = html.find('.classname', first = True)

match_text = html.find('.classname', first = True).text

submatch_text = match.find('.classname p', first = True).text

vid_src = html.find('iframe')

link = vid_src.attrs['src']

abs_links = r.html.absolute_links


#### Dynamic Sites ####

s = HTMLSession()

r = s.get(url)

r.html.render(sleep = 1)
r. status_code

products = r.html.xpath('xpath from inspector', first = True)

products.absolute_links

print(r.html.find('div.classname', first = True).text)

print(r.html.find('target tag', first = True).full_text)

print(r.html.find('div[data-asin]'))

r.html.search('Python is a {} language')[0] # search for text


'''
