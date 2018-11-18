import time

__all__ = ["run"]

def run(probe, fcn, time_every=0.1):
    """
    Check the probe every `time_every` seconds. If the probe returns True,
    then execute the function, then clear the probe.
    """
    while True:
        val = probe.check()
        if val:
            fcn()
            probe.clear()
        time.sleep(time_every)
