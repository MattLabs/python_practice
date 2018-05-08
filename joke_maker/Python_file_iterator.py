import glob
import errno
path = r'C:\Users\mtebi\OneDrive\Documents\Python.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
            pass # do what you want
print(name)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise