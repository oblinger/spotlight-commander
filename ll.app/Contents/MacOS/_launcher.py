#!/usr/bin/env python
# AUTHOR:  Dan Oblinger  <code@oblinger.us>
# CREATE:  2012-06-01
# MODULE:  Supporting code for launcher .scpt files




#                 WARNING:  Current system uses the RUBY version of this launcher.





#
# - In order to avoid creation of a console window, an applescript files is used to
#   launch this python script.  
# - The arg passed to the script is the full path of the .scpt file that launched this script.
# - The 'scriptKey' function uses this path to parse keywards of the form:  # KEYNAME:  some value
#   from the invoking script file.
#   The '# action: ...' key must have the name of one of the 'show_fns' listed below.
#   The '# target: ...' key is the argument specifying what to show is passed to the 'show' fn
#
#
# LAUNCH ACTIONS
#   show_app
#   show_doc
#   show_folder
#   show_incognito
#   show_note
#   show_url
#   show_chrome

import os

def main():
	print "in python"
	global scriptLines
	with open(os.sys.argv[1]) as f: scriptLines = f.readlines()
	
	action = scriptKey("action")
	target = scriptKey("target")
	if action in globals(): lastCmdCache(target); globals()[action](target)
	else: print "ERROR: Unknown action '%s'" % action

def run(t):
	show_app(t)

def execute(t):    # Not used
	show_app(t)

def app(t):
	show_app(t)

def doc(t):
	show_doc(t)
	
def folder(t):
	show_folder(t)

def url(t):
	show_url(t)
	
def nstr(t):
	show_note(t)
	
def chrome(t):
	show_chrome(t)
	

def show_app(target):
	os.system('open "%s"' % target)

def show_doc(target):
	os.system('open "%s"' % target)

def show_folder(target):
	os.system('open "%s"' % target)

def show_incognito(target):
	print "in show incog <%s>" % target
	runScpt(
		'on show_incognito(arg)', 
			'tell application "Google Chrome"', 
				'set aWin to make new window with properties {mode:"incognito"}',
				'tell aWin',
					'set newTab to make new tab with properties {URL:arg}',
					'tell active tab',
						'repeat -- wait completion of loading',
							'set curStat to loading',
							'if curStat = false then exit repeat',
							'delay 0.1',
						'end repeat',
					'end tell',
				'end tell',
			'end tell',
		'end show_incognito',
		'show_incognito("%s")' % target
	)

def show_note(target):
	os.system('/ob/bin/cmd --app %s' % target)

def show_note2(target):
	print "in show note %s" % target
	runScpt(
		'tell application "Keyboard Maestro Engine"',
			'make variable with properties {name:"test", value:"%s"}' % target,
			'do script "Nstr_Goto"',
		'end tell')


def show_url(target):
	os.system('open "%s"' % target)


def show_chrome(target):
	runScpt(
		'on show_chrome_window(arg)',
			'tell application "Google Chrome"',
				'activate',
				'set aWin to make new window with properties {mode:"normal"}',
				'tell aWin',
					'set newTab to make new tab with properties {URL:arg}',
				'end tell',
			'end tell',
		'end show_chrome_window',
		'show_chrome_window("%s")' % target
	)
	print "in show"


###############################################################################

# Executes multi-line applescript.  (cannot contain single quote (') character)
def runScpt(*lines):
	os.system("osascript %s" % ' '.join(["-e '%s'" % line for line in lines]))

def scriptKey(key):
	global scriptLines
	for line in scriptLines:
		if line.startswith("# %s:" % key): return line[len(key)+3:].strip()

def lastCmdCache(target):
	pass


main()
