from autoplay.probes.probe_interface import ProbeInterface

__all__ = ["AndProbe", "OrProbe"]

class AndProbe(ProbeInterface):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check(self):
        return self.a.check() and self.b.check()

    def getval(self):
        va = self.a.getval()
        vb = self.b.getval()
        return [va, vb]

    def clear(self):
        self.a.clear()
        self.b.clear()

def OrProbe(AndProbe):
    def check(self):
        return self.a.check() or self.b.check()
