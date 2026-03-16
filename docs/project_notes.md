# which files were used in the main ETL join
For final report the following files have been used:
    stations.csv,
    lines.csv,
    boroughs.csv,
    zones.csv,
    journeys.json

# what kinds of data quality problems were found
The following issues have been discovered:
Duplicates records in station file - 1
Duplicates records in lines file - 204
Duplicates records in boroughs file - 199
No id's records in boroughs file - 1
Duplicates records in zones file - 213
No id's records in zones file - 1
No id's records in journeys file - 1

Beside this there were records, that have fields:
- with additional spaces -> removed
- with low and upper case  -> transformed to title case
- with NULL -> replaced with ''
  
# which records were skipped and why
The duplicates and the records that were without id's. 
The duplicates will deteriorate the final report. The records without id's can be joined.

# what the final reporting table represents
It represent the dataset, which can be used to build report.