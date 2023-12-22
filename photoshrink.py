import os
import subprocess
import sys

# inspired by this post
# https://guides.wp-bullet.com/batch-resize-images-using-linux-command-line-and-imagemagick/

def main():
    max_len = sys.argv[1]
    relative_in_dir = sys.argv[2]
    relative_out_dir = sys.argv[3]

    # the maximum length in any direction (width or height)
    # aspect ratio will automatically be maintained by the library
    # setting at 1600 because full HD (1920x1080) seems larger than necessary
    # this will allow 1600x900 (or portrait 900x1600) images.
    size_parm = max_len+'x'+max_len+'>' #https://legacy.imagemagick.org/Usage/resize/#shrink

    # files in the input directory will remain untouched.
    # files with identical names will be created in the output directory.
    # files in the output directory are OVERWRITTEN (if the names match)
    project_dir = os.path.dirname(os.path.realpath(__file__))
    absolute_in_dir = project_dir + relative_in_dir
    absolute_out_dir = project_dir + relative_out_dir

    # show what is about to happen
    print ('Input: ', absolute_in_dir)
    print ('Output:', absolute_out_dir)
    print ('Resize Geometry:', size_parm)

    for filename in os.listdir(absolute_in_dir):
        # get full file paths
        infile =  os.path.join(absolute_in_dir, filename)
        outfile = os.path.join(absolute_out_dir, filename)

        # convert and print output
        subprocess.check_output(['convert', infile, '-verbose', '-resize', size_parm, outfile])

if __name__ == '__main__':
    main()
