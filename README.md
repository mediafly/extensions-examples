# Mediafly Extensions Tools and Examples

## Overview

### What are Extensions?
Customers often wish to create rich, engaging content that include advanced UI effects, form entry, dynamic content, and more features that extend well beyond the limitations of PowerPoint or PDFs. With Mediafly Extensions and the Mediafly Platform, customers can create, release and control these packages. Please see [devdocs.mediafly.com/extensions/](http://devdocs.mediafly.com/extensions) for details.

Extensions are zip files consisting of all the HTML, CSS, JavaScript, and images required to render the page offline. They are uploaded to the content management system as items and can be easily updated.

Extensions work on Mediafly's web, Windows, Mac, iOS, and Android apps.

### What can they be used for?
Extensions are typically used for two purposes:

1. To create custom themes that replaces the standard Mediafly navigation
2. To create interactive documents that do much more than the traditional PDF, PowerPoint, or Word document can, such as interactive graphs, calculators, etc. that work on mobile devices


### How can an Extension interact with the native app?
Extensions can utilize the mfly API. [Read the documentation to learn more](http://devdocs.mediafly.com/extensions/).


## Examples

Mediafly creates and maintains a detailed list of examples. These examples illustrate many of the features of Interactives and can serve as QA for client app developers.

* Open and Goto: active the different kinds of links available through the platform
* Get Folder and Get Item: get the contents of a folder with the mfly://data/folder/id and mfly://data/item/id calls
* Collections: features around showing and managing Collections
* Kitchen Sink: various options and features too small to have their own Interactive
* mflyDataInit and mflyInit logger: display results of mflyInit and mflyDataInit function calls into HTML textboxes. Great for obtaining the hierarchy for use in a local development environment
* Save and retrieve data: Illustrate how to save and retrieve key/value data
* Downloader status: obtain and show status of Downloader
* Embed and Data Items: embed an Interactive into another Interactive. Also used to retrieve data items (JSON, CSV, XML) and use the data in the app
* Custom metadata: use custom metadata that has been set up in Airship as a part of the Interactive. Also uses Embed.
* Incremental Search: demonstrates how to interact with iOS's incremental search capability through Interactives
* Swipe: show how, with hammer.js, we can swipe to next/previous items from within the Interactive. Note that swiping doesn't actually move to the next/previous item yet, but instead shows where that call would go.
* Refresh and mflySync: allow refresh of the underlying app, and show the output of mflySync. This is a great tool to test and understand the capability of mflySync.
* GPS: show how to use GPS within Mediafly apps.
* Widescreen and Second Screen Options: show how to initiate widescreen support and handle second-screen toggling in iOS
