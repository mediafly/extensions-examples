# Interactives Test Cases #

## Get Folder and Get Item ##

Supported devices: Web, iOS, Android, Windows 8

* Launch Interactive
* Tap the first line's "Get Folder" link
	* ER: JSON array that looks similar to this one:
	
			[
		    	{
			        "id": "9cf282320e6340ee8b830e5376d54531product165385",
			        "name": "Get Folder and Get Item",
			        "canDownloadAsset": true,
			        "canShare": true,
			        "canAccessAssetOffline": true,
			        "thumbnailUrl": "mfly://image/9cf282320e6340ee8b830e5376d54531product165385",
			        "type": "zip",
			        "url": "mfly://item/9cf282320e6340ee8b830e5376d54531product165385",
			    }
			]
		Specifically, ensure that:
		
		* The structure is a "JSON Array of JSON Objects"
		* There is a single JSON Object within
		* The JSON object has a correct id, name, and type (zip)
		* canShare, canDownloadAsset, canAccessAssetOffline are correct
* Tap the first line's "Get Item" link
	* ER: JSON object that looks similar to this one:
	
			{
			    "id": "9cf282320e6340ee8b830e5376d54531product91921",
			    "name": "Get Folder and Get Item",
			    "type": "folder",
			    "canDownload": "false",
			    "canShare": "false",
			    "date": "2014-02-11T03:40:42Z",
			    "description": " ",
			    "items": [
			        "9cf282320e6340ee8b830e5376d54531product165385"
			    ],
			    "thumbnailUrl": "mfly://image/9cf282320e6340ee8b830e5376d54531product91921",
			    "url": "mfly://folder/9cf282320e6340ee8b830e5376d54531product91921"
			}
		Specifically, ensure that:

		* The structure is a "single JSON Object"
		* The JSON object has a correct id, name, and type (folder)

* Tap the second line's "Get Item" link
	* ER: JSON object that looks similar to this one:

			{
			    "id": "9cf282320e6340ee8b830e5376d54531product168738",
			    "name": "Get Folder and Get Item",
			    "type": "zip",
			    "canAccessAssetOffline": true,
			    "canDownload": "false",
			    "canDownloadAsset": true,
			    "canShare": "true",
			    "date": null,
			    "description": "",
			    "launched": true,
			    "pages": 0,
			    "received": "2015-03-20T11:20:19Z",
			    "thumbnailUrl": "mfly://image/9cf282320e6340ee8b830e5376d54531product168738",
			    "url": "mfly://item/9cf282320e6340ee8b830e5376d54531product168738"
			}		
			
		Specifically, ensure that:

		* The structure is a "single JSON Object"
		* The JSON object has a correct id, name, and type (in this case, zip)



## Embed ##

Supported devices: Web, iOS, Android, Windows 8

* Launch Interactive
* Wait for loading and downloading to complete (if source items are not yet available)
	* ER: Row 1 shows Space Cat image
	* ER: Row 2 shows red embedded Interactive
	* ER: Row 3 shows JSON Data Item with value: ```{"node1":"value1"}```
	* ER: Row 4 shows CSV Data Item with value: ```1,2,3```
	* ER: Row 5 shows XML Data Item with value:

			<?xml version="1.0" encoding="UTF-8"?>
			<data>
				<name>mediafly</name>
				<type>sample</type>
			</data>
	* ER: Row 6 shows number of pages = 26 (Note: this does not yet work on Android or Windows 8)
	* ER: Row 7 shows a specific page from Aesop's Fables document (Note: this does not yet work on Windows 8)


## Open and Goto ##

Supported devices: iOS, Android, Windows 8. Somewhat supported on Web.

* Launch Interactive
* Tap "Open document"
	* ER: Acme Anvil Company.v1 loads
* Tap back/done
	* ER: Interactive opens again <-- Not currently working on Web
* Tap "Open URL item"
	* ER: Google.com loads. On iOS it should load within the app container. For other apps, it should kick the user out to another browser.
* Go back
* Tap "Open sub-links folder"
	* ER: The Open and Goto > Sub-links folder opens in the native interface
* Go back
	* ER: Interactive opens again <-- Not currently working on Web; broken on iOS
* Tap "Open slide 1 in sub-links"
	* ER: Sub-links item 1 should open
* Attempt to navigate left/right
	* ER: User cannot navigate left/right
* Go back
	* ER: User is taken back to the Interactive
* Tap "Goto slide 1 in sub-links" <-- Not currently working on Web
	* ER: Sub-links item 1 should open 
* Attempt to navigate right
	* ER: Sub-links item 2 should open
* Go back
	* ER: User is taken to the Sub-links folder
	

## Save and Retrieve Data ##

Supported devices: Web, iOS, Android, Windows 8. Note that Web uses localStorage, so GET ALL will result in a lot of extraneous key/value pairs returned (e.g. local bookmarks you may have saved).

* Launch Interactive
* Under PUT, enter key ```aa```, value ```{"a":"b"}```, and tap PUT
	* ER: SUCCESS!
* Under PUT, enter key ```ab```, value ```1```, and tap PUT
	* ER: SUCCESS!
* Under PUT, enter key ```b```, value ```1 & 2```, and tap PUT
	* ER: SUCCESS!
* Under GET, enter ```a``` and tap GET
	* ER: FAILURE
* Under GET, enter ```aa``` and tap GET
	* ER: SUCCESS!, Result: ```{"a":"b"}```
* Under GET PREFIX, enter ```a``` and tap GET
	* ER: Something that looks like: ```{"aa":"1","ab":"{\"a\":\"b\"}"}```. Note that the order may differ.  Note also that the exact sequence of quotes and backslashes is important.
* Under GET PREFIX, enter ```c``` and tap GET
	* ER: ```{}```
* Tap GET ALL
	* ER: Something that looks like: ```{"aa":"1","ab":"{\"a\":\"b\"}","b":"1 & 2"}```. Note that the order may differ, and you may see other entries in there from other saved keys. Note also that the exact sequence of quotes and backslashes is important.
	

## Kitchen Sink ##

Supported devices: Web, iOS, Android, Windows 8. Note that most features only work on iOS.

* Launch Interactive
* Tap "Get Interactive Info"
	* ER: App returns relevant information about Interactive, and renders it as a JSON object. Key information includes: id, osType, and parentId.

	

## Custom Metadata ##

Supported devices: Web, iOS, Android, Windows 8.

* Launch Interactive
* Wait for data to fill and images to show
	* ER: "Date of evaluation: 2014-07-25T09:15:00-05:00"
	* ER: Chromecast image, description, price (35), Technologies (miracast), and Segment (consumer) show
	* ER: AppleTV image, description, price (99), Technologies (proprietary), and Segment (consumer) show
	


## Search ##

Supported devices: iOS, Android.

* Launch Interactive
* Type 's'
	* ER: Result is []
* Type 'se'
	* ER: Result is a JSON Array of >2 JSON Objects
* Type 'search'
	* ER: Result is a JSON Array of >2 JSON Objects, but fewer number of items than previous ER.
	* ER: All items returned have "search" or "Search" somewhere in the name or description
	* ER: Both folders and items are returned
	
	
## Downloader Status ##

Supported devices: iOS, Android, Windows 8 (limited).

* Ensure settings are set to automatically download documents, video, audio
* Clear all downloaded content
* Kill app
* Launch app and then Interactive
	* ER: Progress and Error progresses from 0 to 1
* Tap "Get Download Status"
	* ER: {"progress":"[some value between 0 and 1]"}. May also include a block for "error".
* Tap "Get download status of this Interactive"
	* ER: {"progress":1}
* Tap "Show Native Downloader UI"
	* ER: App shows native Downloader UI


