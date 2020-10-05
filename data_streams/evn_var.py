import os

# we can also use it like this 
# if ENV varible not found then this method gives error
print(os.environ['HOME'])

# this get method is safe to use
# provide default value if variable not found
print('HOME: ' + os.environ.get('HOME', ''))
print('SHELL: ' + os.environ.get('SHELL', ''))
print('FRUIT: ' + os.environ.get('FRUIT', ''))

# to see all evnviroment variable in linux
# type the command:> env

# to see particular evn variable type:
# > echo $PATH

# to set new enviroment variable use the following command
# > export FRUIT=Grapes