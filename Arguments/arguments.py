#Assignment

                  #1
# A function named concatenate_args 
# that takes any number of string arguments in positional arguments format 
# and concatenates them into a single string

def concatenate_args(*allnames):
    """
   
    """
    return ''.join(allnames)


                #2
# A function named concatenate_kwargs 
# that takes any number of string arguments in keyword arguments  format 
# and concatenates them into a single string
def  concatenate_kwargs(**names):
    """
    """
    return ''.join(names.values()) 
