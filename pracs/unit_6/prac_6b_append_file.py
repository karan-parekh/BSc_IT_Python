# PYTHON PROGRAM TO APPEND A TEXT FILE AND DISPLAY CONTENTS

# text to append to file
text ="""
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""

# open file object
file = open('demo.txt', 'a+')

# write (append) the text at end of file 
file.write(text)

# The below step is required to reset file poistion 
# from end-of-file to begining-of-file
# places file position at the offset (0)
file.seek(0)

# read and store file contents 
contents = file.read()

# output
print(contents)

# close file object
file.close()
