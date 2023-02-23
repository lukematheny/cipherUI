from os.path import dirname, basename
from glob import glob
modules = glob(dirname(__file__) + "/*.py")
call = "\nYou really thought that would work, didn't you?\n"
__all__ = [basename(x)[:-3] for x in modules if not x.endswith('_.py')]