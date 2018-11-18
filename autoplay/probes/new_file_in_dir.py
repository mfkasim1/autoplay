import os
import fnmatch
import time
from autoplay.probes.probe_interface import ProbeInterface

__all__ = ["NewFileInDir"]

class NewFileInDir(ProbeInterface):
    """
    This probe checks if there's a new file in the given directory.
    It waits until the file size does not change within a certain duration
    before it returns True on the check.
    The value of this class is the full path of the new file.
    """

    def __init__(self,
            fdir, # directory to be probed
            name_pattern="*", # the filename to be matched with fnmatch
            timeout=2, # wait for this long (in s) before get True check
            return_newest=True, # if false, return all the newest files
            ):
        self.fdir = fdir
        self._assert_dir(fdir)
        self.name_pattern = name_pattern
        self.timeout = timeout
        self.return_newest = return_newest
        self.filesinfo = self._get_file_sizes() # dict with {fname: [t,size]}

        self.changing_files = []
        self.newest_files = []

    def check(self):
        new_filesinfo = self._get_file_sizes()
        for f in new_filesinfo:
            if f not in self.filesinfo:
                self.filesinfo[f] = new_filesinfo[f]
                self.changing_files.append(f)
            else:
                old_t, old_sz = self.filesinfo[f]
                t, sz = new_filesinfo[f]
                if sz != old_sz:
                    # the file is changing
                    self.filesinfo[f] = (t, sz)
                    if f not in self.changing_files:
                        self.changing_files.append(f)

                # if the changing files no longer changing, then serve it
                elif (t - old_t) > self.timeout and f in self.changing_files:
                    self.newest_files.append(f)
                    self.changing_files.remove(f)

        return len(self.newest_files) > 0

    def getval(self):
        if self.return_newest:
            if len(self.newest_files) > 0:
                return self.newest_files[-1]
            return None
        else:
            return self.newest_files

    def clear(self):
        self.newest_files = []

    def _assert_dir(self, fdir):
        if not (os.path.exists(fdir) and os.path.isdir(fdir)):
            raise RuntimeError("%s must be an exist directory" % fdir)

    def _get_file_sizes(self):
        res = {}
        t = time.time()
        for f in os.listdir(self.fdir):
            # if not match the pattern, skip
            if not fnmatch.fnmatch(f, self.name_pattern): continue

            # if not a file, skip
            fname = os.path.abspath(os.path.join(self.fdir, f))
            if not os.path.isfile(fname): continue

            # store the checking time and size
            res[fname] = (t, os.path.getsize(fname))
        return res
