#!/usr/bin/env python
# AUTHOR:  Dan Oblinger  <code@oblinger.us>
# CREATE:  2014-
# MODULE:  

import os
import time
import re
import traceback
import json

debug=False
launcher_keys = None    # This is set to the 'keys' parsed from the launcher


KEY_REGEX = re.compile('^# ([^:]*):(.*)$')
APP_SRC_FOLDER = '/Applications/ll.app/Contents/MacOS'
TRAMPOLINE_FILE = '/tmp/ll_trampoline'
LAUNCH_LOG = '%s/.ll_launchlog' % os.getenv('HOME')

PATH = 'path'
ACTION = 'action'
TARGET = 'target'
IO = 'io'
PROMPT = 'prompt'
ARG = 'arg'

# chrome  nstr   shell  run   console   script

def main():
    global debug
    argv = os.sys.argv
    print('### launcher.py called with: %s' % argv)
    if len(argv)>1 and argv[1]=='--debug':
        debug=True
        argv = argv[1:]
    a1 = argv[1] if len(argv)>1 else ''
    if a1=='--launch' or a1=='--now_in_console':
        return cmd_launch(argv)
    error("unknown command %r" % a1)


def cmd_launch(argv):
    global launcher_keys
    now_in_console = argv[1]=='--now_in_console'
    keys = appkeys(argv[2])
    launcher_keys = keys
    if (debug or keys.get(IO) in ['console', 'pinned']) and not now_in_console:
        print "Trampoline into console:  %s" % cap_to_str(keys)
        write_file(TRAMPOLINE_FILE, '#!/bin/sh\n%s/launcher.py %s --now_in_console "%s"\n' %
                   (APP_SRC_FOLDER, '--debug' if debug else '', keys[PATH]))
        os.system('chmod 755 "%s"' % TRAMPOLINE_FILE)
        os.system('open "%s"' % TRAMPOLINE_FILE)
        return
    if now_in_console and not debug:
        print '\033[0;0H\033[2J'
    else:
        for k,v in keys.iteritems():
            print "###   %s = %r" % (k,v)
    print '\n\n'
    with open(LAUNCH_LOG, 'a+') as f:
        f.write(json.dumps(argv[2:]))
        f.write('\n')
    if keys.get(PROMPT):
        line = 'from_user'
        line = user_input(keys[PROMPT])
        keys[ARG] = line
        if not line:
            return                          # EXIT: terminate command w/o user input

    try:
        fn=globals()['type_%s' % keys['action']]
    except KeyError:
        error("Unknown action type '%s'" % keys.get('action'))
    try:
        #user_input(keys[PROMPT])
        fn(keys)
    except Exception, err:
        keys[IO]='pinned'
        print traceback.format_exc()
        #print sys.exc_info()[0]
    if keys.get(IO)=='pinned' or debug:
        raw_input('\n(press RETURN to exit)')


def type_app(keys):
    run('open -a "%s"' % keys[TARGET])
def type_console(keys):
    print 'Triggering console'
    osa('tell application "Terminal" to do script "echo hello"')
def type_doc(keys):
    run('open "%s"' % keys[TARGET])
def type_edit(keys):
    run('open -e "%s"' % keys[TARGET])
def type_folder(keys):
    run('open "%s"' % keys[TARGET])
def type_none(keys):
    pass
def type_nstr(keys):
    osa('tell application "growl" to activate')
    write_file('/ob/data/notester/mac/control.txt', 'GOTO\n%s' % keys[TARGET])
    osa('tell application "Notester" to activate')
def type_python(keys):
    return type_script(keys, 'python')
def type_script(keys, target=None):
    template = {'python':'/usr/bin/env python "%s" %s', 'sh':'/bin/bash "%s" %s'}.get(target or keys.get(TARGET))
    if not template:
        error("Unknown script interpreter.")
    arg = ('"%s"' % keys[ARG]) if ARG in keys else ''
    run(template % (keys[PATH], arg))
def type_sh(keys):
    return type_script(keys, 'sh')
def type_command(keys):
    line = keys[TARGET]
    if ARG in keys:
        if '%' in line:
            line = line % keys[ARG]                  # if target has a '%' then treat it as a python template
        else:
            line = '%s "%s"' % (line, keys[ARG])     # else just append arg to target (inside quotes)
    run(line)
def type_url(keys):
    run('open "%s"' % keys[TARGET])




def appkeys(file):
    keys = {PATH:os.path.join(os.getcwd(), file)}
    with open(file, 'r') as f:
        for line in f.readlines():
            result = re.search(KEY_REGEX, line)
            if result: keys[result.group(1).strip()] = result.group(2).strip()
    return keys

def error(err_str):
    raw_input("\nERROR: %s  (hit return to exit)" % err_str)
    os.sys.exit(1)




def write_file(path, contents):
    with open(path,'w') as f:
        f.write(contents)


def cap_to_str(cap):
    """Returns string summary of a cap's parameters."""
    return 'P:%s  A:%s  T:%s' % (cap['path'], cap['action'], cap.get('target')
    )

def run(str):
    if 0!=os.system(str):
        error('Command Failed.')


# Executes multi-line applescript.  (cannot contain single quote (') character)
def osa(*lines):
    """Executes multi-line applescript script"""
    os.system("osascript %s" % ' '.join(["-e '%s'" % line for line in lines]))


# Runs apple script lines and captures output
def osa_fn(*lines):
    """Executes multi-line applescript script, and returns the captured output."""
    cmd = ['/usr/bin/osascript']
    for l in lines:        cmd.append('-e'); cmd.append(l)
    p = subprocess.Popen(cmd, bufsize=0, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    return stdout.rstrip()



### --------


from Tkinter import *


user_input_result = None

def user_input(prompt):
    global user_input_result, launcher_keys
    user_input_result = None
    if launcher_keys.get('io'):
        user_input_result = raw_input('%s ' % prompt)
    else:
        title = os.path.splitext(os.path.basename(os.path.dirname(
            os.path.dirname(os.path.dirname(launcher_keys[PATH])))))[0]
        one_line_input_gui(field=prompt, title=title)
        #time.sleep(0.1)
        #os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        #osa('tell app "Finder" to set frontmost of process "Python" to true')
    return user_input_result

def one_line_input_gui(**kwargs):
    title = kwargs.get('title', 'Enter Command Arguments')
    field = kwargs.get('field', 'Input')
    root = Tk()
    root.title(title)
    ents = make_form(root, [field])
    root.bind('<Return>', (lambda event, e=ents: fetch_and_execute(e, root)))
    root.mainloop()

def make_form(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, text=field, anchor='w')
        ent = Entry(row)
        ent.focus()
        x_but = Button(row, text='X', command=root.quit)
        x_but.pack(side=RIGHT, padx=0, pady=0)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


def fetch_and_execute(entries, root):
    global user_input_result
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        user_input_result = text
    root.destroy()
    root.quit()



main()
