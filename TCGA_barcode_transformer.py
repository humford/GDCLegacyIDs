import json
from urllib import urlopen

def getUUIDs(filepath):
    file = open(filepath, "r")
    UUIDs = file.read().split("\n")
    return UUIDs

def barcode(UUID):
    url = "https://gdc-api.nci.nih.gov/legacy/files/" + UUID + "?pretty=rue&fields=cases.samples.portions.analytes.aliquots.submitter_id&format="
    jsonID = urlopen(url).read()
    parsed_jsonID = json.loads(jsonID)
    if parsed_jsonID.keys()[0] == "message":
        return UUID + " NOT FOUND"
    elif parsed_jsonID.keys()[0] != "data":
        return UUID + " UNKNOWN ERROR"
    else:
        return parsed_jsonID

def export(barcodes):
    outstr = ""
    for x in barcodes:
        outstr += (barcodes[x] + "\n")
    output = open('TCGA Barcodes.txt', 'w')
    output.write(outstr)

def main():
    filepath = raw_input("UUID File Path: ")
    UUIDs = getUUIDs(filepath)
    barcodes = {}
    for UUID in UUIDs:
        print UUID
        print barcode(UUID)
        barcodes[UUID] = barcode(UUID)["data"]["cases"][0]["samples"][0]["portions"][0]["analytes"][0]["aliquots"][0]["submitter_id"]
    export(barcodes)

main()