# SAMHSA SUD Utils
Code snippets, utilities, and notes related to SAMHSA SUD dataset and project.

**Only 2015-2019**

# DATA
The Treatment Episode Data Set (TEDS) system comprises demographic and drug history information about individuals admitted to and discharged from treatment. The TEDS system is admission-based, therefore, TEDS admissions and discharges do not represent individuals.  Each row represents an admission/discharge. TEDS-A records the admissions while TEDS-D records the discharges. The two data sets are separate but linkable. 

The raw data is open access and is available for download from the [SAMHSA](https://www.samhsa.gov/data/data-we-collect/teds/datafiles) website. This repo contains code used to filter and process raw data files. 

*Currently only TEDS-D data files from 2015-2021 are processed.*

**Data Folder**: ```/secure_net/datasets/opendata/samhsa_sud/```

**Data dictionary**: The current data dictionary is relevant to the variables included in the 2015-2021 TEDS-D processed file on the server, and additional details can be obtained from the [2021 TEDS-D Codebook](https://www.samhsa.gov/data/system/files/media-puf-file/TEDS-D-2021-DS0001-info-codebook.pdf) available on the SAMHSA website. Variables that were dropped from the raw data are not included in the data dictionary.

# NOTES
- When loading the processed csv file using pandas, must set *keep_default_na=False* to prevent conversion of None str into NA (see tedsd_sample_notebook)
- All true missing are coded as such, therefore there should be no *na* values on import. 
- PREG: Pregnant at admission 
    - For males and females not of child-bearing age this variable should be recoded to something like "Not Applicable"
- LOS: Length of stay 
    - recorded as individual numbers until 31, then binned. 
    - Consider binning the individual numbers as well so it's all categorical

## Updates:
- 18 Nov 2024 
    - Fixed an issue where None values in 2021 were being converted to *na*
    - Fixed IDU and MARSTAT mapping issues.
    - Reprocessed the 2015-2021 raw files and generated new clean derived dataset.
