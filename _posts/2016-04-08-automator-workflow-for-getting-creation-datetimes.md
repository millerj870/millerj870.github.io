---
author: jason
date: 2016-04-08 15:18:56+00:00
layout: post
title: Automator Workflow for getting creation datetimes
tags: coding script
---

My day job involves grant applications, and we have a long way to go when it comes to gathering data on our performance. It’s been my feeling that our workload has been increasing over the past few years, and that we have boom and bust cycles. A count of proposals is an easy way to verify the upward trend in overal production, but looking for the cycles requires data that we’re just not logging.

However, we do keep our projects on a shared drive that everyone can access, and they are organized into fodlers by (fiscal year) and, in those folders, by the order they first come to our attention. When a faculty member tells us they want to apply for a grant, my staff creates a folder for the project. On OS X, one can get information on a folder and see its creation date.

My idea: get the creation date of all the project folders and look at the pattern in those dates. This would illuminate the way our work cycles. But I don’t want to gather these dates by hand, using the ‘Get Info’ function on each folder and loggin the creation date int a spreadsheet. I wanted a script.

First, I found a command line tool that’s part of the OS X Developer Tools called [`GetFileinfo`](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/GetFileInfo.1.html).

Executing

```shell
/usr/bin/GetFileInfo -d foldername
```

would get me the creation datetime stamp for foldername. I then found [this question](http://apple.stackexchange.com/questions/222022/how-preserve-jpeg-date-stamps-during-automator-scaling) about modifying images in batches. One proposed solution uses `GetFileInfo` in a script called by Automator. I modified that script into the following:

```shell    
touch ./datetimes.csv  
for f in "$@"; do  
# Get the creation date time stamp of the target file, saved as 't'.  
t="$(/usr/bin/GetFileInfo -d "$f")"  
echo "$f , $t" >> datetimes.txt  
done
```

This creates a CSV file of creation datetimes for a set of selected folders. The CSV file is created on the desktop because the workflow’s “Start at” is set to this folder.

![This is what the worklow looks like.](/assets/images/workflow.png)

This is what the worklow looks like.

This workflow worked great. It could be improved in a couple ways, but the core functionality is here.
