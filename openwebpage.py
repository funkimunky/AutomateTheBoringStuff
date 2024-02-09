import webbrowser
import sys


parameters = sys.argv
url = parameters[1]

webbrowser.open('https://' + url)

