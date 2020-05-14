import datetime
import pickle
import os.path
from googleapiclient.discovery import build, Resource
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class ServiceBuilder(object):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def __init__(self):
        self._creds = None
        self._service = None
        self._try_import_creds()

    def _try_import_creds(self) -> None:
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self._creds = pickle.load(token)

    def _export_creds(self) -> None:
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(self._creds, token)

    def _creds_are_valid(self) -> bool:
        return self._creds and self._creds.valid

    def _creds_are_fresh(self) -> bool:
        return self._creds and self._creds.expired and self._creds.refresh_token

    def _refresh_creds(self) -> None:
        if self._creds_are_fresh():
            self._creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
            self._creds = flow.run_local_server(port=0)
        self._export_creds()

    def build(self) -> Resource:
        # If there are no (valid) credentials available, let the user log in.
        if not self._creds_are_valid():
            self._refresh_creds()
        self._service = build('calendar', 'v3', credentials=self._creds)
        return self._service

    def now(self) -> str:
        return datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    @property
    def service(self) -> Resource:
        service = self._service or self.build()
        return service
