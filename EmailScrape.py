# Scrape sender information of latest email

import os.path
import base64
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials
import json


# import re
# import time
# import logging
# import requests

#pip google-api-python-client
#pip google_auth_oauthlib
#pip google.auth

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

def scrapeSender():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
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
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages')
    print(len(messages))

    # grab latest email
    msg = messages[0]
    txt = service.users().messages().get(userId="me", id=msg['id']).execute()
    payload = txt['payload']
    headers = payload['headers']

    for h in headers:
        if h['name'] == 'From':
            sender = h['value']
    print(sender)
    quit()
    if not messages:
        print('No new messages.')
    else:
        message_count = 0
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()                
            email_data = msg['payload']['headers']
            for values in email_data:
                name = values['name']
                if name == 'From':
                    from_name= values['value']                
                    for part in msg['payload']['parts']:
                        try:
                            data = part['body']["data"]
                            byte_code = base64.urlsafe_b64decode(data)

                            text = byte_code.decode("utf-8")
                            print ("This is the message: "+ str(text))

                            # mark the message as read (optional)
                            msg  = service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()                                                       
                        except BaseException as error:
                            pass                            

# numMessages = readEmails()
# print(numMessages)
