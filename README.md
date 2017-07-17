# GDCLegacyIDs
Workaround for mapping UUIDs to TCGA barcodes for data on GDC legacy portal.

## Usage
Running "TCGA_barcode_transformer.py" script will prompt the user for the file path to a txt file list of GDC UUIDs, which it will convert to TCGA barcodes for use with the [GDC legacy portal](https://portal.gdc.cancer.gov/legacy-archive/search/f), which it will write to a file called "newBarcodes.txt". 

The "barcode_reformatter.py" script will convert the TCGA barcodes obtained from the previous script into an array which can be used as a manual search term on the GDC portal.

&copy; Henry Williams 2017
