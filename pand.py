from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']
#'https://www.googleapis.com/auth/drive.metadata.readonly',
def fun():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    # results = service.files().list(
    #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])
    return service

if __name__ == '__main__':
    service=fun()
    folder_id='1586raJeuanYEQv54hNQDwy9uzS1bzfrC'
    folder_only='application/vnd.google-apps.folder'
    query=f"mimeType = '{folder_only}' and parents='{folder_id}' "
    results = service.files().list(q=query,spaces='drive').execute()
    folders = results.get('files', [])
    #print(items[3])
    colname=[]
    colid=[]
    songname=['a','b','c','d','e']
    recommendations=[['000141','000997'],['000141'],['000141'],['000141'],['000141']]
    tags=[['at'],['bt'],['ct'],['dt'],['et']]
    df=pd.DataFrame()
    
    for folder in folders:
        id=folder['id']
        results = service.files().list(q=f"parents='{id}'",spaces='drive').execute()
        items = results.get('files', [])
        for item in items:
            #print(u'{0} ({1})'.format(item['name'][:-1], item['id']))
            colname.append(item['name'][:-4])
            colid.append(item['id'])
    df=pd.DataFrame({'googleid':colid,'name':colname,'songname':songname,'recommendations':recommendations,'tags':tags})
    
    print(df)
    df.to_csv('tid.csv',index=False)
    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['name'], item['id']))
