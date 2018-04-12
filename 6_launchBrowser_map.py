#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

address = 'https://www.google.co.in/maps/place/'

if len(sys.argv) > 1:
    # Get address from command line.
	urls = address + sys.argv[1:]
	

# TODO: Get address from clipboard.
else:
	urls = address + pyperclip.paste()
	
webbrowser.open(urls)