"""
Time complexity maybe O(n * m) wher 'n' is the number of files 
and 'm' is the number of directories present in input path
"""

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    list_of_files=list()
    for entry in os.listdir(path):
        entry.strip()
        abs_path=os.path.join(path,entry)
        if os.path.isdir(abs_path):
            list_of_files=list_of_files + find_files(suffix,abs_path)
        elif abs_path.endswith(suffix):
            list_of_files.append(abs_path)
    return list_of_files


print(find_files('.c','/Users/tony/Downloads/testdir'))