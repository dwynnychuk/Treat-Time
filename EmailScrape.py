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
        if h['name'] == 'Subject':
            subject = h['value']
            
    print(sender)
    print(subject)
    
# numMessages = readEmails()
# print(numMessages)
