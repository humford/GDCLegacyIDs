import json
from urllib2 import urlopen

url = "https://gdc-api.nci.nih.gov/v0/legacy/annotations?facets=&fields=entity_id,entity_submitter_id&filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22annotations.project.project_id%22,%22value%22:%5B%22TCGA-KIRC%22%5D%7D%7D%5D%7D&from=1&size=10000&sort=entity_type:asc"
jsonIDs = urlopen(url)
parsed_jsonIDs = json.loads(jsonIDs)

IDs = []

for entity in parsed_jsonIDs['data']['hits']:
    IDs[entity['entity_id']] = entity['entity_submitter_id']

print IDs