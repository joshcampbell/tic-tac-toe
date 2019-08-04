from subprocess32 import Popen

class Voice:

    def __init__(self):
        self.subprocess = None

    def say(self,quote):
        self.stop()
        self.subprocess = Popen(["espeak", \
                                 "-s", "140",\
                                 quote])

    def stop(self):
        if self.subprocess != None:
            # FIXME how do we know the process really terminated?
            self.subprocess.kill()
        self.subprocess = None
