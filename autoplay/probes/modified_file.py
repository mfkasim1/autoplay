import os
import time
from autoplay.probes.probe_interface import ProbeInterface
from autoplay.probes.new_file_in_dir import NewFileInDir

__all__ = ["ModifiedFile"]

class ModifiedFile(ProbeInterface):
    def __init__(self, fname, timeout=2):
        self.fpath = os.path.abspath(fname)
        self._assert_file(self.fpath)
        fdir, f = os.path.split(self.fpath)
        self.obj = NewFileInDir(
            fdir,
            name_pattern=f,
            timeout=timeout,
            return_newest=True)

    def check(self):
        return self.obj.check()

    def getval(self):
        return self.obj.getval()

    def clear(self):
        self.obj.clear()

    def _assert_file(self, fpath):
        if not (os.path.exists(fpath) and os.path.isfile(fpath)):
            raise RuntimeError("%s must be an exist file" % fpath)
