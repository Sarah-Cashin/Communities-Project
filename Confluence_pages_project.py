from typing import Type

import requests
import json
from atlassian import Confluence
import logging
import os
import time
import pandas as pd

confluence: Type[Confluence] = Confluence
url='https://communities.atlassian.net'
username='sarah.cashin@raytheon.co.uk'
password='a6tWtHkQRGvtcxc4Iy3a354E'

spaces = confluence.get_all_pages_from_space('space= ENGINEERIN, start=0, limit=None, status=None, expand=none, content_type=page')
all_pages = get_all_page_ids_from_space('confluence=confluence,space_key=ENGINEERIN')

my_dict = {}
['displayName'])].append(page_history['createdDate'])
print(my_dict)

    names = []

    for x in all_pages:
    page_history = confluence.history(x)
    print(page_history['createdBy']['displayName']

    #print(\"%s %s\" % (x, page_history['createdBy']['displayName']))

    #Displaying dates when pages Last Updated

    updated =[];
    for d in all_pages:
    page_history = Confluence.history('d')
    print(page_history['lastUpdated']['friendlyWhen'])
    #print(\"%s %s\" % (d, page_history['lastUpdated']['friendlyWhen']))


