Here we will already have allcolumns_final.csv before hand.

pand.py: Using drive api store the trackid and google id in csv using pandas.dataframe and saves as newtid.csv.

mergecsv.py: merge allcolumns_final.csv and newtid.csv .

mongo_up_csv: connect to mongodb with mongouri. Upload a csv(forupload_final.csv) which we have stored after running pand.py using pandas.dataframe.  
