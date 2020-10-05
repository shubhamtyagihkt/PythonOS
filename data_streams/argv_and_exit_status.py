import sys

# here to access command line argument
print(sys.argv)
# first argument is filename itself at zeorth index

# EXIT VALUES
# 0 => process completed successfully
# any thing other than 1 => some error

# in cmdline, if you want to see exit status of last executed command
# then use the following command
# it is contained in "?" variable
# > wc $?

# in python we can use sys.exit(number) -> sys.exit(1)
# to exit program representing some error value
sys.exit(0)