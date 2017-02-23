def reformatBarcodes(filepath):
	file = open(filepath, "r")
	barcodes = file.read().split("\n")
	return barcodes

def export(barcodes):
    outstr = ""
    for x in range(0,len(barcodes)):
        outstr += (barcodes[x])
    output = open('newBarcodes.txt', 'w')
    output.write(outstr)

b = reformatBarcodes(raw_input("Barcode Filepath: "))
for x in range(0, len(b)):
	b[x] = "\"" + b[x] + "\","

export(b)