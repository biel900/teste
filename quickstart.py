{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting google-api-python-client\n",
      "  Downloading https://files.pythonhosted.org/packages/5e/19/9fd511734c0dee8fa3d49f4109c75e7f95d3c31ed76c0e4a93fbba147807/google-api-python-client-1.7.11.tar.gz (142kB)\n",
      "Collecting google-auth-httplib2\n",
      "  Downloading https://files.pythonhosted.org/packages/33/49/c814d6d438b823441552198f096fcd0377fd6c88714dbed34f1d3c8c4389/google_auth_httplib2-0.0.3-py2.py3-none-any.whl\n",
      "Collecting google-auth-oauthlib\n",
      "  Downloading https://files.pythonhosted.org/packages/7b/b8/88def36e74bee9fce511c9519571f4e485e890093ab7442284f4ffaef60b/google_auth_oauthlib-0.4.1-py2.py3-none-any.whl\n",
      "Collecting httplib2<1dev,>=0.9.2 (from google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/d2/84/f97b9efdb17c9b73e133bdbf2b4bfd09cd0be655e36e3ee3c4bec9095048/httplib2-0.14.0-py3-none-any.whl (94kB)\n",
      "Collecting google-auth>=1.4.1 (from google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/c5/9b/ed0516cc1f7609fb0217e3057ff4f0f9f3e3ce79a369c6af4a6c5ca25664/google_auth-1.6.3-py2.py3-none-any.whl (73kB)\n",
      "Requirement already satisfied, skipping upgrade: six<2dev,>=1.6.1 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from google-api-python-client) (1.12.0)\n",
      "Collecting uritemplate<4dev,>=3.0.0 (from google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/e5/7d/9d5a640c4f8bf2c8b1afc015e9a9d8de32e13c9016dcc4b0ec03481fb396/uritemplate-3.0.0-py2.py3-none-any.whl\n",
      "Collecting requests-oauthlib>=0.7.0 (from google-auth-oauthlib)\n",
      "  Downloading https://files.pythonhosted.org/packages/c2/e2/9fd03d55ffb70fe51f587f20bcf407a6927eb121de86928b34d162f0b1ac/requests_oauthlib-1.2.0-py2.py3-none-any.whl\n",
      "Collecting rsa>=3.1.4 (from google-auth>=1.4.1->google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/02/e5/38518af393f7c214357079ce67a317307936896e961e35450b70fad2a9cf/rsa-4.0-py2.py3-none-any.whl\n",
      "Collecting pyasn1-modules>=0.2.1 (from google-auth>=1.4.1->google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/52/50/bb4cefca37da63a0c52218ba2cb1b1c36110d84dcbae8aa48cd67c5e95c2/pyasn1_modules-0.2.7-py2.py3-none-any.whl (131kB)\n",
      "Collecting cachetools>=2.0.0 (from google-auth>=1.4.1->google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/2f/a6/30b0a0bef12283e83e58c1d6e7b5aabc7acfc4110df81a4471655d33e704/cachetools-3.1.1-py2.py3-none-any.whl\n",
      "Requirement already satisfied, skipping upgrade: requests>=2.0.0 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib) (2.22.0)\n",
      "Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->google-auth-oauthlib)\n",
      "  Downloading https://files.pythonhosted.org/packages/05/57/ce2e7a8fa7c0afb54a0581b14a65b56e62b5759dbc98e80627142b8a3704/oauthlib-3.1.0-py2.py3-none-any.whl (147kB)\n",
      "Collecting pyasn1>=0.1.3 (from rsa>=3.1.4->google-auth>=1.4.1->google-api-python-client)\n",
      "  Downloading https://files.pythonhosted.org/packages/a1/71/8f0d444e3a74e5640a3d5d967c1c6b015da9c655f35b2d308a55d907a517/pyasn1-0.4.7-py2.py3-none-any.whl (76kB)\n",
      "Requirement already satisfied, skipping upgrade: idna<2.9,>=2.5 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib) (2.8)\n",
      "Requirement already satisfied, skipping upgrade: chardet<3.1.0,>=3.0.2 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib) (3.0.4)\n",
      "Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib) (2019.6.16)\n",
      "Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\\users\\gabrielmatsumoto\\anaconda3\\lib\\site-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib) (1.24.2)\n",
      "Building wheels for collected packages: google-api-python-client\n",
      "  Building wheel for google-api-python-client (setup.py): started\n",
      "  Building wheel for google-api-python-client (setup.py): finished with status 'done'\n",
      "  Stored in directory: C:\\Users\\GabrielMatsumoto\\AppData\\Local\\pip\\Cache\\wheels\\b8\\f6\\f5\\b7bef1a5bc0e07ca4aa54c596b0b574c5afc07a9fddccf08f8\n",
      "Successfully built google-api-python-client\n",
      "Installing collected packages: httplib2, pyasn1, rsa, pyasn1-modules, cachetools, google-auth, google-auth-httplib2, uritemplate, google-api-python-client, oauthlib, requests-oauthlib, google-auth-oauthlib\n",
      "Successfully installed cachetools-3.1.1 google-api-python-client-1.7.11 google-auth-1.6.3 google-auth-httplib2-0.0.3 google-auth-oauthlib-0.4.1 httplib2-0.14.0 oauthlib-3.1.0 pyasn1-0.4.7 pyasn1-modules-0.2.7 requests-oauthlib-1.2.0 rsa-4.0 uritemplate-3.0.0\n"
     ]
    }
   ],
   "source": [
    "!pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'credentials.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-d58d478d6bd9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     53\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     54\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 55\u001b[1;33m     \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-3-d58d478d6bd9>\u001b[0m in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     30\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m             flow = InstalledAppFlow.from_client_secrets_file(\n\u001b[1;32m---> 32\u001b[1;33m                 'credentials.json', SCOPES)\n\u001b[0m\u001b[0;32m     33\u001b[0m             \u001b[0mcreds\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mflow\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun_local_server\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mport\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     34\u001b[0m         \u001b[1;31m# Save the credentials for the next run\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\google_auth_oauthlib\\flow.py\u001b[0m in \u001b[0;36mfrom_client_secrets_file\u001b[1;34m(cls, client_secrets_file, scopes, **kwargs)\u001b[0m\n\u001b[0;32m    194\u001b[0m             \u001b[0mFlow\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mThe\u001b[0m \u001b[0mconstructed\u001b[0m \u001b[0mFlow\u001b[0m \u001b[0minstance\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    195\u001b[0m         \"\"\"\n\u001b[1;32m--> 196\u001b[1;33m         \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mclient_secrets_file\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'r'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mjson_file\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    197\u001b[0m             \u001b[0mclient_config\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mjson_file\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    198\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'credentials.json'"
     ]
    }
   ],
   "source": [
    "from __future__ import print_function\n",
    "import pickle\n",
    "import os.path\n",
    "from googleapiclient.discovery import build\n",
    "from google_auth_oauthlib.flow import InstalledAppFlow\n",
    "from google.auth.transport.requests import Request\n",
    "\n",
    "# If modifying these scopes, delete the file token.pickle.\n",
    "SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']\n",
    "\n",
    "# The ID and range of a sample spreadsheet.\n",
    "SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'\n",
    "SAMPLE_RANGE_NAME = 'Class Data!A2:E'\n",
    "\n",
    "def main():\n",
    "    \"\"\"Shows basic usage of the Sheets API.\n",
    "    Prints values from a sample spreadsheet.\n",
    "    \"\"\"\n",
    "    creds = None\n",
    "    # The file token.pickle stores the user's access and refresh tokens, and is\n",
    "    # created automatically when the authorization flow completes for the first\n",
    "    # time.\n",
    "    if os.path.exists('token.pickle'):\n",
    "        with open('token.pickle', 'rb') as token:\n",
    "            creds = pickle.load(token)\n",
    "    # If there are no (valid) credentials available, let the user log in.\n",
    "    if not creds or not creds.valid:\n",
    "        if creds and creds.expired and creds.refresh_token:\n",
    "            creds.refresh(Request())\n",
    "        else:\n",
    "            flow = InstalledAppFlow.from_client_secrets_file(\n",
    "                'credentials.json', SCOPES)\n",
    "            creds = flow.run_local_server(port=0)\n",
    "        # Save the credentials for the next run\n",
    "        with open('token.pickle', 'wb') as token:\n",
    "            pickle.dump(creds, token)\n",
    "\n",
    "    service = build('sheets', 'v4', credentials=creds)\n",
    "\n",
    "    # Call the Sheets API\n",
    "    sheet = service.spreadsheets()\n",
    "    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,\n",
    "                                range=SAMPLE_RANGE_NAME).execute()\n",
    "    values = result.get('values', [])\n",
    "\n",
    "    if not values:\n",
    "        print('No data found.')\n",
    "    else:\n",
    "        print('Name, Major:')\n",
    "        for row in values:\n",
    "            # Print columns A and E, which correspond to indices 0 and 4.\n",
    "            print('%s, %s' % (row[0], row[4]))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
