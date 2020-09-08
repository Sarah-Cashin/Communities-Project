import requests
import json
from atlassian import Confluence
import sys

confluence ='https://communities.atlassian.net'
username='sarah.cashin@raytheon.co.uk'
password = 'a6tWtHkQRGvtcxc4Iy3a354E'

spaces = confluence.get_all_pages_from_space('space= ENGINEERIN, start=0, limit=None, status=None, expand=none, content_type=page')
#all_pages = get_all_page_ids_from_space('confluence=confluence,space_key=ENGINEERIN')

my_dict = {}
(['displayName']).append(page_history['createdDate'])
#print(my_dict)
print(sys.version)

#def get_all_page_ids_from_space(confluence, space_key):
  #  limit = 500
   # flag = True
    #step = 0
    #page_ids = []

    #while flag:
     #values = confluence.get_all_pages_from_space(space=space_key, start=limit * step, limit=limit)
    #step += 1
    #if len(values) == 0:
     # flag = False
     #print(\"Did not find any pages, please, check permissions\")
    #else:
     # for value in values:
    #print(\"Retrieve page with title: \" + value['title'])
   # page_ids.append((value['id']))
    #print(\"Found in space {} pages {}\".format(space_key, len(page_ids)))
    #return page_ids

   #Printing names of people who has created page

#names = []

#for x in all_pages:
   # page_history = confluence.history(x)
   # print(page_history['createdBy']['displayName'])

    #names = []
    #for x in all_pages:
   # print(x)
   # page_history = confluence.history(x)


    #if (x == '62881810')
    # print(page_history)

    #    sd = confluence.get_parent_content_id(x)
    #  print(sd)
    # z = confluence.get_content_history_by_version_number(62881810, 57)
    #   print(z)
    #   for y in page_history:
    #     print(y)\n
    #   print(page_history)
    #   print(page_history['createdBy'])
    #   break
    #   print(page_history['createdBy']['displayName'])

    #   print(\"%s %s\" % (x, page_history['createdBy']['displayName']))

  #Printing history of individual page for each version

  # v = confluence.get_page_by_id(98306, expand=None, status=None, version=1)

   #print (v)

    #Displaying information on date created

   #spaces = confluence.get_all_pages_from_space(space='ENGINEERIN', start=0, limit=None, status=None, expand='none', content_type='page')
    #all_pages = get_all_page_ids_from_space(confluence=confluence,space_key='ENGINEERIN')

    #oldest = []

    #for o in all_pages:
    #page_history = confluence.history(o)
    #print(page_history['createdDate'])

