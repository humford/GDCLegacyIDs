from lxml import html
import requests

project = 'TCGA-KIRC'
page = requests.get('https://gdc-portal.nci.nih.gov/legacy-archive/annotations?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22annotations.project.project_id%22,%22value%22:%5B%22TCGA-KIRC%22%5D%7D%7D%5D%7D')
tree = html.fromstring(page.content)

links = tree.xpath('//a[@class="ng-scope"]/href()')

print links

info = []

for link in links:
    page = requests.get(link)
    tree = html.fromstring(page.content)

    info.append(tree.xpath('//td[@class="ng-binding"]/test()'))

print info