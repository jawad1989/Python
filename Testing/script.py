#pylint  VS Code
#PEP-8 Standard style guide for python
#pyflakes  Repl

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err


# main is the file it self
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")