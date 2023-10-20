#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--apple", # short and long form argument
                    help="Description of what this does",
                    required=False, # set to True to make script fail without this argument
                    action="store" # store whatever follows
                    )

parser.add_argument("-b", "--banana", # short and long form argument
                    help="Description of what this does",
                    required=False, # set to True to make script fail without this argument
                    action="store_true" # store a boolean
                    )

parser.add_argument("-c", "--cfruit", # short and long form argument
                    help="Description of what this does",
                    required=False, # set to True to make script fail without this argument
                    action="append", # appends the argument to a running list
                    nargs="+" # this matters but I don't remember why
                    )
# this allows for multiple arguments passed to "-c" as well as multiple instances of "-c"
# Example:
#   argsWithArgparse.py -c herp derp blerp
#   argsWithArgparse.py -c herp -c derp
#   argsWithArgparse.py -c herp derp blerp -c foo bar
# WARNING: "append" and "nargs" generates nested lists, which might suck
args = parser.parse_args()
print(args)

if args.cfruit is not None:
    flattened = []
    for nestedList in args.cfruit:
        # add items from each nested list to one big list
        flattened += nestedList
    print(f"Flattened list of -c/--cfruit options: {str(flattened)}")
