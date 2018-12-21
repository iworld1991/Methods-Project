
import os
import sys
sys.path.insert(0, os.path.abspath('../lib'))

# Find pathname to this file:
my_file_path = os.path.dirname(os.path.abspath("do_all.py"))
KrusellSmithRep_py =  os.path.join(my_file_path,"KrusellSmithRep.py")
exec(open(KrusellSmithRep_py).read())
