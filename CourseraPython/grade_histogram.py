import tkinter.filedialog
import grade

##import sys
### Insert the directory path containing the file to be imported
##sys.path.insert(1, r'C:\Users\nabil\Documents')
### Now you can import the file
##import grade  


# or
# import filename

### If your python file is inside another folder, then you need to create a blank __init__.py file 
###that will help python to understand it's a package. Then you can import that as follows:
# from folderName import filename


a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')

a1_histfilename = tkinter.filedialog.askopenfilename()
a1_histfile = open(a1_histfilename, 'w')


###Read thegrades into a list:
grades = grade.read_grades(a1_file)

#count the grades per range:
range_counts = grade.count_grade_ranges(grades)

#write the histogram to the file:
grade.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_histfile.close()
