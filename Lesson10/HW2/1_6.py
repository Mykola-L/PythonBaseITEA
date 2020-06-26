import lxml.html

t = lxml.html.parse(url)
print(t.find(".//title").text)