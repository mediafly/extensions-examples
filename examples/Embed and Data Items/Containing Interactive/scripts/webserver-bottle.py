#!/usr/bin/python

"""
webserver-bottle.py: A webserver that mimics the Interactives platform on iOS and Android. 
Requires the Python Bottle web framework.
"""

__author__      = "Jason Shah"
__copyright__   = "Copyright 2013-2015, Mediafly, Inc."
__version__		= "1.6"



from bottle import route, get, post, put, run, static_file, request, response, abort
from pprint import pprint
from json import dumps
import re
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# Helper functions
### convertAndReformatForJson performs the following transformations:
### 1. Converts strings from Unicode to UTF-8, as JSON chokes on Python-style Unicode strings
### 2. Convert mfly://data/image/ prefixes to Placeholder.it links
### 3. Convert Python True/False/None to JavaScript true/false/{empty string}
def convertAndReformatForJson(input):
	if isinstance(input, dict):
		return {convertAndReformatForJson(key): convertAndReformatForJson(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [convertAndReformatForJson(element) for element in input]
	elif isinstance(input, unicode):
		input = input.replace('mfly://data/image/', 'http://placehold.it/600x600&text=')
		return input.encode('utf-8')
	else:
		if (input == True and str(input) == "True"):
			return True
		if (input == False and str(input) == "False"):
			return False
		if (input == None):
			return ""
		if isinstance(input, str):
			input = input.replace('mfly://data/image/', 'http://placehold.it/600x600&text=')
		return input




###
### Initialization
###
# mflyDataInit return value
mflyDataInit_response = {
	'user': "jdoe@mediafly.com",
	'displayName': "John Doe",
	'id': "5559d4a298225972b02301597product82851",
	'item': "Interactive",
	'osType': "Development",
	'osVersion': "6.1.3",
	'appVersion': "6.1.4.405",
	'deviceId': "46a5f0630a13a8744e8b5cc6309b46",
	'appId': "1de8c94235905abbbf7638acce",
	'lastUpdated': "2014-02-03T07:04:07-06:00"
}



# Load hierarchy into memory

json_file = open('scripts/hierarchy.json')
hierarchy = convertAndReformatForJson(json.load(json_file))
isOnline = True


#############################
# Interactive baseline data #
#############################
@get('/data/interactive')
def getInteractiveData():
	response.content_type = 'application/json'
	return json.dumps(mflyDataInit_response)



##########################
# Save and restore state #
##########################
memory = {}

@get('/data/info/<key:re:.*>')
def getOrPut(key):
	method = request.query.method
	value = request.query.value
	if method.lower() != "put":
		# Treat as GET
		if key not in memory.keys():
			abort(404)
		return memory[key]
	else:
		# Treat as PUT
		memory[key] = value


@get('/data/info')
def getMany():
	prefix = request.query.prefix
	if prefix:
		if sys.version_info.major == 2:
			return {k:v for (k,v) in memory.iteritems() if k.startswith(prefix)}
		else:
			return {k:v for (k,v) in memory.items() if k.startswith(prefix)}
	else:
		return memory
		 


##############
# Get Folder #
##############

@get('/data/folder/<id:re:.*>')
def getFolder(id):
	if id in hierarchy:
		# Now lets construct the folder
		folder = []
		this_folder = hierarchy[id]
		if this_folder['items']:
			for itemkey in this_folder['items']:
				folder.append(hierarchy[itemkey])
			response.content_type = 'application/json'
			return json.dumps(folder)
		else:
			response.content_type = 'application/json'
			return '[]'
	else:
		abort(404, id + ' not found')

############
# Get Item #
############

@get('/data/item/<id:re:.*>')
def getItem(id):
	if id in hierarchy:
		response.content_type = 'application/json'
		return json.dumps(hierarchy[id])
	else:
		abort(404, id + ' not found')

##############
# Downloader #
##############
@get('/data/download/status')
def getDownloadStatus():
	response.content_type = 'application/json'
	return '{ "progress": 0.12, "fails": 1 }'
@get('/data/download/status/<id:re:.*>')
def getDownloadStatusForItem(id):
	response.content_type = 'application/json'
	return '{ "progress": 0.5 }'



###############
# Collections #
###############
collections = {}
collectionsIdCounter = 1

@get('/data/collections')
def getCollections():
	ret = []
	for c in collections:
		ret.append(collections[c])
	response.content_type = 'application/json'
	return json.dumps(ret)

@get('/data/createCollection')
def createCollection():
	global collectionsIdCounter

	_name = request.query.name
	_id = str(collectionsIdCounter)
	collectionsIdCounter += 1
	obj = {
		"id": _id,
		"name": _name,
		"items": []
	}
	collections[_id] = obj
	response.content_type = 'application/json'
	return json.dumps(obj)

@get('/data/addItemToCollection')
def addItemToCollection():
	_collectionId = request.query.id
	_itemId = request.query.item
	if _itemId in hierarchy:
		item = hierarchy[_itemId]
		if _collectionId in collections:
			collection = collections[_collectionId]
			if not "items" in collection:
				collection["items"] = []
			collection["items"].append(item["id"])
			return ""
		else:
			abort(404, 'Collection ' + _collectionId + ' not found')
	else:
		abort(404, 'Item ' + _itemId + ' not found')


@get('/data/collection/<id:re:.*>')
def getCollection(id):
	if id in collections:
		# Construct the response
		collection = []
		for itemId in collections[id]['items']:
			collection.append(hierarchy[itemId])
		response.content_type = 'application/json'
		return json.dumps(collection)
	else:
		abort(404, id + ' not found')


##########
# Search #
##########

DO_NOT_SEARCH_LIST = ["autoStart", "id", "items", "thumbnailUrl", "type", "url", "launched", "progress", "pages"]
@get('/data/search')
def search():
	term = request.query.term

	ret = []
	for k in hierarchy:
		if (k != 'version'):
			for v in hierarchy[k]:
				if not(v in DO_NOT_SEARCH_LIST) and type(hierarchy[k][v]) is str and term in hierarchy[k][v]:
					ret.append(hierarchy[k])
	response.content_type = 'application/json'
	return json.dumps(ret)


##########
# Filter #
##########
@get('/data/filter')
def filter():
	ret = []

	for k_id in hierarchy:
		if (k_id != 'version'):
			foundcount = 0
			for key in request.query:
				# Loop through each of the key=value queryparams and test each key=value combination
				val = request.query[key]
				if (val.startswith('"') and val.endswith('"')):
					val = val.strip('"')
				elif (val == 'true'):
					val = True
				elif (val == 'false'):
					val = False

				for k_key in hierarchy[k_id]:
					if (key == k_key):
						if str(val) == str(hierarchy[k_id][k_key]):
							foundcount = foundcount + 1
							break
			# We found each of the key=value combinations for this object k_id
			if foundcount == len(request.query):
				ret.append(hierarchy[k_id])
	response.content_type = 'application/json'
	return json.dumps(ret)



#########
# Embed #
#########
# To work with Embed, place the item that will be embedded into the
# [Interactive root]/embeds folder with the same name as the ID of the item.
# Images will be of the form [id].png.
# Other interactives will be of the form [id], where [id] is a folder, and
#   within that folder is, at least, index.html.
# Data items (JSON, CSV, XML) will be of the form [id] with no extension
# Pages of documents will be of the form [id]/[page].png, where [id] is a
#   folder, and [page].png is the specified page of the document as a PNG image.
@get('/data/embed/<id:re:.*>')
def embed(id):
	if id in hierarchy:
		if hierarchy[id]['type'] == 'image':
			# XXX TODO Generalize this for all images. And return a default image if the specific one doesn't exist.
			return static_file(id + '.png', root='embeds')
		elif hierarchy[id]['type'] == 'zip':
			return static_file(id + '/index.html', root='embeds')
		elif hierarchy[id]['type'] == 'data':
			return static_file(id, root='embeds')
		elif hierarchy[id]['type'] == 'pdf':
			return static_file(id + '/' + request.query.position + '.png', root='embeds')
	else:
		abort(404, id + ' not found')


###############
# Other calls #
###############


@get('/data/onlineStatus')
def getOnlineStatus():
	isOnlineString = 'online' if isOnline else 'offline'
	response.content_type = 'application/json'
	return '{ "status": "' + isOnlineString + '" }'



#############
# Heartbeat #
#############
@get('/_heartbeat')
def hearbeat():
	global isOnline
	if (request.query.isOnline != ''):
		isOnline = True if (request.query.isOnline == 'true') else False

	seq = int(request.query.seq)
	if seq == 0:
		return "mflyDataInit(" + str(json.dumps(mflyDataInit_response)) + ")"
	elif seq == 1:
		return "mflyResume()"
	elif seq == 2:
		return 'mflyInit(' + str(json.dumps(hierarchy)) + ')'
	return ''



#################
# Static Routes #
#################
@get('/')
def index():
	return static_file('index.html', root='app/')

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='app/js')

@get('/bower_components/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='bower_components')

@get('/lib/<filename:re:.*\.js>')
def js_libraries(filename):
	return static_file(filename, root='app/lib')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='app/css')

@get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='app/img')

@get('/fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='app/fonts')



run(host='127.0.0.1', port=8000, debug=True, reloader=True)

