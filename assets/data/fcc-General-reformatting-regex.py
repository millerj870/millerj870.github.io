#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 08:23:00 2021

@author: jason.miller
"""

# testing regex in a file by reformatting title

import re, os, sys
os.chdir('/Users/jason.miller/Library/Mobile Documents/com~apple~CloudDocs/To Do/2021/7/17/')
input = open("tmp.txt","r")
output = open("tmp.md", "w")
input_str=input.read()

# -----------------------------------
# Reformat title lines
in_title=re.compile('(\s*)(2019-2023 General Class.*)')
new_title = in_title.sub(r"\n\n# \2",input_str)
# -----------------------------------
# Reformat section lines
in_section=re.compile('^(SUBELEMENT\sG\d)',re.MULTILINE|re.DOTALL)
new_section = in_section.sub(r"## \1",new_title)
# -----------------------------------
# Reformat subsection lines
in_subsection=re.compile('^(G[0-9]\D\s-)',re.MULTILINE|re.DOTALL)
new_subsection = in_subsection.sub(r"### \1",new_section)
# -----------------------------------
# Reformat question and answer lines
in_question=re.compile('(^G[0-9]\D\d\d\s*\()(?P<answer>[A-D])\)(\s.*\n|\s*\n*)(.*\?.*\n)((.*\s*){0,3})(((?P=answer)\.\s)(.*\s*))((.*\s*){0,3})(\~\~)\n', re.MULTILINE)
new_questions = in_question.sub(r"\1\2)\3\4\5**\7**\10\12\n",new_subsection)
# -----------------------------------
# Add backslash in from of brackets
openbrackets=re.compile('(\[)', re.MULTILINE)
new_fwdbrackets = openbrackets.sub(r"\\[",new_questions)
closebrackets=re.compile('(\])', re.MULTILINE)
new_closebrackets = closebrackets.sub(r"\\]",new_fwdbrackets)

# ----------- reformatting done --------------

output.write(new_closebrackets)
input.close()
output.close()



## for troubleshooting
#found=in_question.findall(new_subsection)
#in_section.findall(input_str)
#print(found)
