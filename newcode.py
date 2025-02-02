import json, pandas as pd, logging, Variables, sys,csv
from datetime import datetime
import gc
#Define title for JSON parsing
title='JSON Parsing'

def json_parsing(dataFile, batch_size):
    try:

        with open (dataFile) as d:
            dataFile = json.load(d)
            if isinstance(dataFile, dict):
                dataFile =[dataFile]

            total_records =len(dataFile)
            processed_records =0
            df_3 =pd.DataFrame()
            while processed_records < total_records:
                batch_data = dataFile[processed_records:processed_records+batch_size]
                df01=pd.json_normalize(dataFile, sep='_')
                exploded=False
                jsonConverted=False
                print(df01)
                for i in list(df01.columns):
                    if isinstance(df01[i].iloc[0],list):
                        df01=df01.explode(i)
                        exploded=True
                        print(df01)
                if exploded:
                    for i in list(df01.columns):
                        if isinstance(df01[i].iloc[0],dict):
                            df_json=df01.to_json(orient='records')
                            dataFile=json.loads(df_json)
                            jsonConverted=True
                            break
                        if not jsonConverted:
                            break

                else:
                    #Rename columns as per json to postgres mapping
                    df01.rename(columns=Variables.columnMapping, inplace=True)
                    #Create empty dataframe with postgres column names
                    df02=pd.DataFrame(columns=list(Variables.columnMapping.values()))
                    #Align the two dataframes so that the dataframe has no columns not in 
                    #not present in json are populated with nulls
                    #df_3 = df02.align(df01,'left',1)
                    df_3 = df_3.append(df01,ignore_index=True)
                    processed_records +=len(batch_data)
                    print (df_3)
            df_3.to_csv (r'File Name.csv',index=null)
    except Exception as err:

        text= 'JSON parsing faled'+f'\n\n{err}'
        logging.error(text)
        status='Fail'
        return df_3,status,text

    text='JSON parsed successfully'
    status='pass'
    return df_3,status,text

if __name__=="__main__":
    if len(sys.argv)< 3:
        print("usage:python filename.py<dataFile.json><batch_size>")
        sys.exit(1)
    dataFile=sys.argv[1]
    batch_size=int(sys.argv[2])
    json_parsing(dataFile,batch_size)

                
