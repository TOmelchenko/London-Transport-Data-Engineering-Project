# ETL
## which files were used in the main ETL join
For final report the following files have been used:
    stations.csv,
    lines.csv,
    boroughs.csv,
    zones.csv,
    journeys.json

## what kinds of data quality problems were found
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
  
## which records were skipped and why
The duplicates and the records that were without id's. 
The duplicates will deteriorate the final report. The records without id's can be joined.

## what the final reporting table represents
It represent the dataset, which can be used to build report.

# ELT

# which raw tables were created
The raw tables for stations, lines, boroughs and journeys have been created.

# what kinds of bad data were filtered out in SQL
Duplicated raws. But I'd add report_month for boroughs, snapshot_date for lines and report_date for zones to take the most recent one.
Missing fields. I added also the condition for boroughs
```sql
TRIM(borough_name) != '' 
```
because just SELECT DISTINCT returns one row but with empty name.

# how the ELT design differs from ETL
In ELT version the  transformations are being done on database level vs python on memory transformation for ETL. The ELT is more suitable when we have big amount of data. 

# what the final transport_report_elt table represents
It contains data extract that can be used for reporting.

