__all__ = ["probefn"]

"""
Example of use:

    @probefn
    def fcn(file1, file2):
        pass

    def main():
        probe1 = autoplay.probes.NewFileInDir(".")
        probe2 = autoplay.probes.NewFileInDir("..")
        probe = probe1 * probe2
        autoplay.run(probe, fcn(probe1, probe2))
"""

def probefn(fcn):
    def decorator(*probes):
        def function():
            args = [probe.getval() for probe in probes]
            return fcn(*args)
        return function
    return decorator
