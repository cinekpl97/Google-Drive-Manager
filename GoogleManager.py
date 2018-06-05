"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io


class Service:

    @staticmethod
    def authorization():
        scopes = 'https://www.googleapis.com/auth/drive'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', scopes)
            creds = tools.run_flow(flow, store)
        service = build('drive', 'v3', http=creds.authorize(Http()))
        return service

    def files_list(self, listsize, service):
        results = service.files().list(
            pageSize=listsize, fields="nextPageToken, files(mimeType, size, name, id)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            i = 0
            for item in items:
                print('{0} {1} ({2})'.format(i, item['name'], item['mimeType']))
                i = i + 1
        return items

    def files_upload(self, filename, path, mimetype):

        file_metadata = {'name': filename}
        media = MediaFileUpload(path, mimetype=mimetype)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def files_download(self, file_id, pathtosave):
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        with io.open(pathtosave, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())

    @staticmethod
    def files_search(size, phrase):
        query = "name contains '{0}'".format(phrase)
        results = service.files().list(
            pageSize=size, fields="nextPageToken, files(id, name, mimeType)", q=query).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            i = 0
            for item in items:
                print('{0} {1} ({2})'.format(i, item['name'], item['mimeType']))
                i = i + 1
        return items


drive = Service()
service = drive.authorization()
