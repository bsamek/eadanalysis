#!/usr/bin/python
'''Usage: xmlcomments.py <dir> <newfile>

Adds all comments from XML comments in
files in <dir> to <newfile>'''

import os, re, sys

def parse(dir, comments_file):
    
    # Get directory contents and sort
    dir_list = os.listdir(dir)
    dir_list.sort()

    # Script is assumed to be in directory, so remove
    dir_list.remove("xmlcomments.py")

    number_of_files = len(dir_list)    
    current_file = 0

    comment_pattern = re.compile(r"<!--.*?-->", re.DOTALL)

    with open(comments_file, "w") as outfile:
        
        for infile in dir_list:
                
            with open(infile, "r") as infile_open:
                
                # Parse file
                data = infile_open.read()
                comments = comment_pattern.findall(data)
                
                # Write filename and any comment data to file
                outfile.write("\n\n%s\n" % infile)
                comment_string = "\n".join(comments)
                outfile.write(comment_string)
            
                current_file += 1
                print "File %d of %d done: %s" % (current_file, number_of_files, infile)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        dir = sys.argv[1]
        file = sys.argv[2]
        parse(dir, file)
    else:
        print __doc__
