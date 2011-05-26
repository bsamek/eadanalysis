import os, os.path, re, sys

def save_comments(directory, comments_file):
    '''Saves XML comments from files in directory to a file.'''

    dirname = os.path.abspath(directory)
    
    # Get directory contents and sort
    dir_list = os.listdir(directory)
    dir_list.sort()

    # Find number of files in directory and start at 0
    number_of_files = len(dir_list)    
    current_file = 0

    comment_pattern = re.compile(r"<!--.*?-->", re.DOTALL)

    with open(comments_file, "w") as outfile:
        
        os.chdir(directory)
        for infile in dir_list:
                
            with open(os.path.join(dirname, infile), "r") as infile_open:
                
                # Parse file
                data = infile_open.read()
                comments = comment_pattern.findall(data)
                
                # Write filename and any comment data to file
                outfile.write("\n\n%s\n" % infile)
                comment_string = "\n".join(comments)
                outfile.write(comment_string)
            
                current_file += 1
                print "File %d of %d done: %s" % (current_file, number_of_files, infile)

def count_files_containing_tag(tag, directory):
    '''Counts number of files in a directory that contain a tag.'''

    if "<" in tag or ">" in tag:
        print "Do not include the \"<\" or \">\" characters with the tag name."
        return
    
    dirname = os.path.abspath(directory)
    dir_list = os.listdir(directory)
    
    number_of_files = len(dir_list)    
    current_file = 0
    num_files_containing_tag = 0

    comment_pattern = re.compile("<%s" % tag)

    for infile in dir_list:

        with open(os.path.join(dirname, infile), "r") as infile_open:

                # Parse file
                data = infile_open.read()
                if comment_pattern.search(data):
                    num_files_containing_tag += 1

                current_file += 1

    print "%d of %d files contain %s" % (num_files_containing_tag, number_of_files, tag)

