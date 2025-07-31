import os

filename = input("Enter the filename to check permissions: ")
print("Readable:", os.access(filename, os.R_OK))
print("Writable:", os.access(filename, os.W_OK))
