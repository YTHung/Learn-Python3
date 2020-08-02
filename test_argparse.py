# REF: https://docs.python.org/3/library/argparse.html
# argparse: An easy way to write user-friendly command-line interfaces,
#           which composing of arguments.

# Usage: type 'python3 test_argparse.py -h' in Terminal
#              python test_argparse.py 1 2 3 4
#              python test_argparse.py 1 2 3 4 --sum



import argparse

#---------- creating a parser ------------------
parser = argparse.ArgumentParser(description='Process some integers.')

#---------- adding arguments in an ArgumentParser ----------------------
'''
add_argument(name or flags, ...)
    [name or flags]: 
        optional arguments   : '-f' or '--foo'
        
        positional arguments : such as 'bar'
            *For positional argument actions, 
             dest is normally supplied as the first argument to add_argument()
    
    [metavar]:
        When ArgumentParser generates help messages, 
        it needs some way to refer to each expected argument
        
    [action]:
        The action keyword argument specifies how the command-line arguments should be handled
         
        store_const :               This stores the value specified by the const keyword argument
        store_true, store_false  :  These are special cases of 'store_const' 
                                    used for storing the values True and False respectively.
'''
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

#-------------- Converting argument strings to objects ----------------------
'''
parse_arg() method 
    Converting arguments string to objects and assign them as attributes of the namespace.
'''
args = parser.parse_args()


print(args.accumulate(args.integers))