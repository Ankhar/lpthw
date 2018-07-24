from sys import argv

script, filename = argv

print 'This programm will read created file from ex16.py %s' %filename
txt = open(filename)
txtread = txt.read()
print txtread