#!/usr/bin/env python
# AUTHOR:  Dan Oblinger  <code@oblinger.us>
# CREATE:  2014-
# MODULE:  

import os
import re
import traceback


KEY_REGEX = re.compile('^# ([^:]*):(.*)$')
APP_SRC_FOLDER = '/Applications/ll.app/Contents/MacOS'
TRAMPOLINE_FILE = '/tmp/ll_trampoline'

PATH = 'path'
ACTION = 'action'
TARGET = 'target'
IO = 'io'

# chrome  nstr   shell  run   console   script

def main():
    a1 = os.sys.argv[1] if len(os.sys.argv)>1 else ''  
    a2 = os.sys.argv[2] if len(os.sys.argv)>2 else ''  
    os.system('echo Launcher ARGV %s' % os.sys.argv)
    if a1=='--launch' or a1=='--now_in_console':
        return cmd_launch(os.sys.argv)
    error("unknown command %r" % a1)

        
    

def cmd_launch(argv):
    now_in_console = argv[1]=='--now_in_console'
    keys = appkeys(argv[2])
    if keys.get(IO) in ['console', 'pinned'] and not now_in_console:
        print "Trampoline into console"
        write_file(TRAMPOLINE_FILE, '#!/bin/sh\n%s/launcher.py --now_in_console "%s"\n' % (APP_SRC_FOLDER, keys[PATH]))
        os.system('chmod 755 "%s"' % TRAMPOLINE_FILE)
        os.system('open "%s"' % TRAMPOLINE_FILE)
        return
    if now_in_console:
        print '\033[2J\n'
    else:
        for k,v in keys.iteritems():
            print "###   %s = %r" % (k,v)

    try:   fn=globals()['type_%s' % keys['action']]
    except KeyError:
        error("Unknown action type '%s'" % keys.get('action'))
    try:
        fn(keys)
    except Exception, err:
        keys[IO]='pinned'
        print traceback.format_exc()
        #print sys.exc_info()[0]
    if keys.get(IO)=='pinned':
        os.sys.stdout.write('\n(press RETURN to exit)')
        raw_input()


def type_console(keys):
    print 'Triggering console'
    osa('tell application "Terminal" to do script "echo hello"')
    #type_script(keys)
def type_doc(keys):
    os.system('open "%s"' % keys[TARGET])
def type_folder(keys):
    os.system('open "%s"' % keys[TARGET])
def type_script(keys, prefix = ''):
    template = {'python':'/usr/bin/env python "%s"', 'sh':'/bin/sh "%s"'}.get(keys.get(TARGET))
    if not template: error("Unknown script interpreter.")
    os.system(prefix + (template % keys[PATH]))
def type_sh(keys):
    os.system(keys[TARGET])
def type_url(keys):
    os.system('open "%s"' % keys[TARGET])




def appkeys(file):
    keys = {PATH:os.path.join(os.getcwd(), file)}
    with open(file, 'r') as f:
        for line in f.readlines():
            result = re.search(KEY_REGEX, line)
            if result: keys[result.group(1).strip()] = result.group(2).strip()
    return keys

def error(err_str):
    os.sys.stdout.write("ERROR: %s.  (hit return to exit)" % err_str)
    raw_input()
    os.exit(1)




def write_file(path, contents):
    with open(path,'w') as f:
        f.write(contents)



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


main()
