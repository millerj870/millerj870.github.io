---
author: jason
date: 2017-07-28 18:56:25+00:00
layout: post
title: Python project - scraped text from web to CSV file
tags: coding python
---

Some neighborhood shenanigans led a group of home owners to start a GoFundMe page to raise money to file a lawsuit against the city. The backstory isn’t important.  I was curious to know who would support this bad behavior, and I wanted to practice my python.

I was able to cut-and-paste information about the people who made donations to the GoFundMe effort. That information went into a text file. Each line had a different bit of information: initials of a donor, how much they donated, their name (or “Anonymous”), and some information about when they made their donation. It’s not easy to aggregate information presented this way. Wouldn’t it be nice to have it in a spreadsheet where I could sort and pivot and all that?

So that was my project: taking the scraped text and messaging the information into CSV format that can be imported into a spreadsheet.

Sounds easy. Looksing back, it was easy.  But it took time.  I felt I was learning python for the first time.  Again.  The exercise taught me something about functions, lists, operators, and running python on my home computer. It also made me wrestle with types (and changing them when it suited me).

There’s not much to say about the process, and there are no creative steps that would much interest anybody else. This is the result of much pseudocoding, discarding of ideas, and trying things, making small tweaks until something works the way I hoped it would. Engineering, I guess.

Here’s the code:

```python 
    import numpy as np
    import csv
    
    # function takes a list and outputs the locations in the list that equal ''
    # in:  list
    # out:  list of location indices of '' elements
    def indices(listname):
        indices = [i for i,x in enumerate(listname) if x=='']
        return np.array(indices)
    
    # function that takes list of indices and give the lengths of the subsequences of strings between the '\n'
    # in: list of indices, original list of interest
    # out: list of lengths
    def lengths(indices,list):
        N=len(list)
        M=len(indices)
        lengths=np.zeros((M+1,), dtype=np.int)
        lengths[0]=np.array(indices[0])
        lengths[1:M-1]=np.array(indices[1:M-1]) - np.array(indices[0:M-2])-1
        lengths[M]=N-np.array(indices[M-1])
        return lengths
    
    # function that takes an index, a list of indices, and lengths of subsequences and returns a row of the CSV file I aim to creat
    # in: a row number, a list of indices, the lengths of the rows
    # out: indeces for the elements of the row in question
    def rowi_indices(i,indices,lengths):
        if i==0:
            list = [0]
            j=1
            while j < lengths[0]:
                list.extend([0+j])
                j+=1
        else:
            list = [indices[i]+1]
            j=1
            while j < lengths[i]:
                list.extend([indices[i]+1+j])
                j+=1
        return list   
    
    # function that takes an index, a list of data, and location indices of the line breaks and gives back a row of the CSV file
    # in: a row number, a list of data, a list of indices
    # out: the row in question
    def rowi(i, list, indices):
        len=lengths(indices,list)
        good_indices=rowi_indices(i,indices,len)
        row = [data[i] for i in good_indices]
        return row
    
    # -------------------------
    
    # this is the file that has the scraped data
    file="vatp_gofundme_list.txt"
    # read the file into python
    data=open(file).readlines()
    # strip the carriage retuns from the data; rows will be separated by "blanks" where there were only carriage returns, before
    data = [x.strip('\n') for x in data] 
    
    # locations of the row breaks
    indices = indices(data)
    
    # computing all the rows of the CSV file
    j=0
    rows=[]
    while j < len(indices):
        rows.extend([rowi(j,data,indices)])
        j+=1
    
    # Open File
    resultFile = open("output.csv",'w')
    # Write data to file
    for r in rows:
        # need to strip the square brackets from the start and end of each row, too
        resultFile.write(str(r).strip('][') + "\n")
    resultFile.close()
    
    # TADAH!
```
