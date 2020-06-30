import os
import sys 
import time
import subprocess


class Watcher(object):
    running = True
    refresh_delay_secs = 1

    # Constructor
    def __init__(self, watch_file):
        self.filename = watch_file
        self._cached_stamp = os.stat(self.filename).st_mtime
        self.runningProgram = False
        self.runProgram()

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            print('File changed')
            if self.runningProgram != False:
              self.program.terminate()
            self.runProgram()


    def runProgram(self):
      self.program = subprocess.Popen(f'pythonw3 {sys.argv[1]}')
      self.runningProgram = True


    # Keep watching in a loop        
    def watch(self):
        while self.running: 
            try: 
                # Look for changes
                time.sleep(self.refresh_delay_secs) 
                self.look() 
            except KeyboardInterrupt: 
                print('\nDone') 
                break 
            except FileNotFoundError:
                # Action on file not found
                pass
            except: 
                print('Unhandled error: %s' % sys.exc_info()[0])


watch_file = str(sys.argv[1])

watcher = Watcher(watch_file) 
watcher.watch()  # start the watch going