
import csv

import pandas as pd


import json

#from JSONStream import JSONStream
#import JSONStream

from jsonstream import JSONStream

from pprint import pprint

import time

import itertools







with open('extract_example.json') as f:
	for line in itertools.islice(f, 0, 22): #since every 7 lines is a json object
		d = json.loads(line)
		print(d)









# with open('extract_example.json') as jsns:
# 	lines = []
# 	try:
# 		for jsn in JSONStream(jsns):
# 			d = jsn.load(jsn)
# 			print(d)
# 			#print(city["name"])
# 			#print(jsn[0])
# 			#print(jsn)
# 			#print(type(jsn))
# 			# for jsn_item in jsn:
# 			# 	print(jsn_item)
# 			#print(jsn[0])
# 			#print(jsn[1])
# 			#lines.append(jsn)
# 	except:
# 		print("except")
# 		pass


# file_name = "%s_%s.csv" % (str(time.strftime("%Y-%m-%d")),
#                            str(time.strftime("%H%M%S")))
# columns = ["keys", "values"]

# pd.DataFrame(lines, columns = columns).to_csv(file_name, index = False)


			







# with open('extract_example.json') as jsns:
#     for jsn in JSONStream(jsns):
#        #print(city["name"])
#        d = json.load(jsn)
#        print(d)





# with open('extract_example.json') as json_data:
#     d = json.load(json_data)
#     print(d)

# with open('extract_example.json') as json_data:
#     d = json.loads(json_data)
#     json_data.close()
#     pprint(d)


# with open('extract_example.json') as json_data:
# 	for data in json_data:
# 		d = json.load(data)
# 		pprint(d)