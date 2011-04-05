#!/usr/bin/python
'''Usage: xmlcomments.py <dir> <newfile>

Adds all comments from XML comments in
files in <dir> to <newfile>'''

import codecs, os, sys
from chardet import detect
from HTMLParser import HTMLParser

class StripComments(HTMLParser):
    # Initialize class with comment_list
    def __init__(self):
        HTMLParser.__init__(self)
        self.comment_list = []

    # Append comment data to comment_list
    def handle_comment(self, data):
        self.comment_list.append(data + "\n")

def parse(dir, comments_file):
    
    # Get directory contents and sort
    dir_list = os.listdir(dir)
    dir_list.sort()

    # Script is assumed to be in directory, so remove
    dir_list.remove("xmlcomments.py")

    number_of_files = len(dir_list)    
    current_file = 0

    with open(comments_file, "w") as outfile:
        
        for infile in dir_list:
            print "Processing: %s" % infile
            current_file += 1
            
            strip_comments = StripComments()

            # Open XML file with detected encoding from chardet
            encoding = detect(open(infile, "r").read())['encoding']
            with codecs.open(infile, "r", encoding) as input_file:

                data = input_file.read()
                
                # Parse file
                strip_comments.feed(data)
                strip_comments.close()
                
                # Write filename and any comment data to file
                outfile.write("\n%s\n" % infile)
                outfile.writelines(strip_comments.comment_list)
            
            print "File %d of %d done: %s" % (current_file, number_of_files, infile)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        dir = sys.argv[1]
        file = sys.argv[2]
        parse(dir, file)
    else:
        print __doc__
