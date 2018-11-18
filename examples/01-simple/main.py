import os
import autoplay as ap

@ap.probefn
def fcn(fname):
    print("The file '%s' has just created/modified" % fname)

def mkdir(fdir):
    if not os.path.exists(fdir):
        os.makedirs(fdir)

def main():
    fdir = "probed_dir"
    pattern = "*.txt"
    print("The directory '%s' is now probed for new or modified files "
          "with pattern %s" % (fdir, pattern))
    mkdir(fdir)
    probe = ap.probes.NewFileInDir(fdir, pattern)
    ap.run(probe, fcn(probe))

if __name__ == "__main__":
    main()
