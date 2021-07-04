#! /bin/env python3
import os
import sys

var = input("Hi! I like cheese! Do you like cheese?").lower()
if var == "yes":
    print("That's awesome!")


if var != "yes":
    # os.execv(sys.argv[0], sys.argv)
    os.system("python3 /home/pandu/Documents/eksperimen/eksperimenClasify/testRestartOtherFile/clientFile.py")
