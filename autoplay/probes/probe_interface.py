from abc import ABCMeta, abstractmethod

class ProbeInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def check(self):
        """
        Perform the routine check, whether the change has been made, and if
        True, change the internal value. This function should returns a boolean.
        """
        pass

    @abstractmethod
    def getval(self):
        """
        Returns the value of the object to be evaluated on a function.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear the state of the change.
        """
        pass

    def __mult__(self, a):
        from autoplay.probes.operators import AndProbe
        self._assert_probe_interface(a)
        return AndProbe(self, a)

    def __add__(self, a):
        from autoplay.probes.operators import OrProbe
        self._assert_probe_interface(a)
        return OrProbe(self, a)

    def _assert_probe_interface(self, a):
        if not isinstance(a, ProbeInterface):
            raise ValueError("The probe object can only operate on another " \
                "probe object")
