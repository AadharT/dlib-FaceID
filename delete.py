import glob
import os

name = raw_input("Enter the name of the person to be deleted:")

for filename in glob.glob('known/'+ name + '.npy'):
    os.remove(filename)
