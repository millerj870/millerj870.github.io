---
author: jason
date: 2011-03-03 18:00:00+00:00
layout: post
title: 'Nerdgasm:  Automating Student Peer Reviews, Part 2'
wordpress_id: 130
tags: applescript hackedu teaching
---

The other day, I wrote about how I used Google Docs and Applescript to lubricate the peer review workflow in a class I'm teaching.  My set-up is certainly imperfect, and here I want to comment on a couple improvements that I could make, when I can find the time.

At present, a student submits peer review comments to a Google Form that gets written to a Google spreadsheet that I need to download by hand to a Numbers spreadsheet and process with an Applescript.  The script produces a PDF that I need to email to students by hand.<!-- more -->

## Python?

My first thought was to create a python script that would take the PDF's produced by the applescript and email them to the proper student.  Naming the PDFs carefully and consistently using the student's name would allow me to use a simple dictionary to choose the email addresses to use.  And it's easy to create an email message with the PDF attachment by calling mutt.
 
  
```python
     #!/usr/bin/env python
     import os
     
     # from http://www.shelldorado.com/articles/mailattachments.html
     
     os.system("mutt -s "Birthday celebration" -a tmp.png username@truman.edu < tmp.py")
```

The tricky part, it turns out, is sending the email.  This requires an SMTP connection to our school's servers, and this requires python skills I do not have.  Here's a sanitized copy of my incomplete python script:

```python
#!/usr/bin/env python
import sys, glob, re
import smtplib
import email,email.encoders,email.mime.text,email.mime.base

import smtp

# script:  distribute contents
#  -- each item in a folder is names 'name-identifier.pdf'
#  -- the script email's each item (as an attachment) to the email address associated with 'name'
#  -- Q:  can python invoke Mail.app so that Mail.app sends the emails out?

SERVER = "mail.truman.edu"
FROM = "AAAA@truman.edu"
SUBJECT = "FYI:  your concept map"
TEXT = "This is an automatically generated email -- 2.  Attached is a PDF of the work you turned in for the assignment to construct a concept map for the economic way of thinking."


# create {name:email address} dictionary
emailinfo = {'grossa':'AAAAAA@me.com', 'thee':'BBBBBB@gmail.com','whackson':'CCCCC@DDDDD.com'}

# upon execution of the script
# 0. directory of contents chosen
# 1. dialog box: ask user for email specifics
# 2. list of directory contents made
filelist = glob.glob('*.pdf')
# 3. for each item in the list, 'name' is identified
#p=re.compile('([a-z]+)\s-\s.*\.pdf')  -- why doesn't this regex work to pull out the first block of text?
p=re.compile('([a-z]+)')
server = smtplib.SMTP(SERVER)
for filename in filelist:
    m=p.match(filename)
    name=m.group()
# identify the email address for m.group
    address = emailinfo[name]
# 5. an email message is created to 'name' with subject, body, reply-to, etc. and with the item attached
# 6. the email is sent to 'name'

    TO = [address]
    message = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    smtp = Smtp(SERVER, "YYYYY", "XXXXX")
    smtp.subject(SUBJECT)
    smtp.message(TEXT)
    smtp.from_addr(FROM)
    smtp.rcpt_to(TO)
    smtp.attach(filename)
    smtp.send()

        
# 7.  write log file that records basic information about the action
#   - date, time, who emailed, path of contents directory, subject, body, reply-to information, etc.



#####  look at http://www.finefrog.com/2008/05/06/sending-email-with-attachments-in-python/
## Better  vvvv
### look at http://www.pastequestion.com/blog/python/send-email-with-attachments-using-python.html
```

The above script doesn't address the work required to get data from Google to my laptop.  The next idea does.

## Google Scripting

It turns out that Google spreadsheets allow JavaScript scripts to be run.  Since I can't code my way out of a paper bag with HTML, JavaScript is out of my reach.  But I can cut-and-paste with the best of them, and there are good bits of example code out there for the stealing.  So there's a good chance that I will take advantage of this functionality sooner or later.

Here's what I would do.

I would modify example scripts to automagically send an email to the reviewer (who submitted data via the form) and the writer with review comments.  The script would keep track of which rows of data in the spreadsheet have already been reported (ignoring old rows), and it would send a copy of the data to both the reviewer (who submitted the data) and the writer.  In addition, the email sent would be formatted to look like the original 'Writing Checklist' form.

This script would be triggered to run when someone submits a review form.  A trigger like this is set as follows.

Select Tools -> Scripts … -> Script Editor to open a window displaying a script (maybe), and the window will have a menu bar that includes a Triggers menu.  Select Triggers -> Current Script's Triggers.  This will bring up a dialog box that will allow you to set triggers for the script in the Script editor.  The spreadsheet event triggers are 'On open', 'On edit', and 'On form submit.'  The last one is the one I'd use.  (See [Google's Instructions](http://code.google.com/googleapps/appsscript/guide_events.html#ActionTriggers) for doing this.)

## (Future) End Result

This would give me a workflow that requires no human intervention (except reading) after a reviewer submits comments.  (See the diagram below; vertical arrows are actions that require human intervention and horizontal arrows are actions that are automated.)  This would be kinda slick, I think.  Weaknesses of the  Google-ified model include

  * Ugly reports sent to students; the Google forms and Google email (templates) are spare.  This could be addressed by sending HTML emails, but it's not clear if this adds difficulty.
  * The data is never transferred to the instructor's laptop.  This is OK, but it means that calculating grades requires access to the Cloud.
  * Google Forms, as I use them, do not require any sort of authentication.  This means any yahoo could create dummy reviews and bother students.  Getting even elementary authentication (e.g., matching a user-supplied email address with one on record and accessible to an authentication routine) is beyond my skills.  At least at this point.

Part of me would like to maintain a bit more control over the process by automating the downloading of the review data and sending out PDF reports.  This keeps me in touch with what the students are doing, and when.  But it's not clear to me how to import Google spreadsheet rows into an existing iWork (Numbers) spreadsheet.

But enough of my critical reflection.  The functionality made possible by Google is really quite wonderful.  I may implement it soon, just to show myself that I can do it.

![](http://agate.truman.edu/~millerj/blog/comment flow - Google.png)
