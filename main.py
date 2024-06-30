#main.py

import sys
import admin, voter

try:
    args = sys.argv[1].removeprefix("-")

    if args == "admin":
        admin.main()
    elif args == "voter":
        voter.main()
    else:
        print("Invalid argument. Please use '-admin' or '-voter'.")
except IndexError:
    print("No argument provided. Please use '-admin' or '-voter'.")