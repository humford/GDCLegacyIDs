import json
from urllib import urlopen

project = raw_input("Project: ")
count = raw_input("Number of Patients: ")
UUID = "entity_id"
url = "https://gdc-api.nci.nih.gov/v0/legacy/annotations?facets=&fields=" + UUID + ",entity_submitter_id&filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22annotations.project.project_id%22,%22value%22:%5B%22" + project + "%22%5D%7D%7D%5D%7D&from=1&size=" + count + "&sort=entity_type:asc"
jsonIDs = urlopen(url).read()
parsed_jsonIDs = json.loads(jsonIDs)

IDs = {}

for entity in parsed_jsonIDs['data']['hits']:
    IDs[entity[UUID]] = entity['entity_submitter_id']

print IDs