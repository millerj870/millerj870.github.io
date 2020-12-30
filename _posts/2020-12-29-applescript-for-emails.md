---
title:  Applescript for sending batch emails with attachment
author: jason
date: 2020-12-29
layout: post
tags: coding teaching applescript mastery-grading
---

When I teach, I often want to send out an individualized email to my students.  This is especially important when I am emailing a student about their grade in the course.

Composing thirty-odd emails by hand in my email client is tedious work, and since I do this sort of thing a couple times a semester (more in courses I'm using mastery grading), it was [worth the investment in time](https://xkcd.com/1205/) to write a script to do this.

In this post, I share an applescript that does exactly this.

## Using the Script

To use this script, you need a list of information for your recipients:

* a last name,
* a first name, and
* a complete email address.

I use this to send PDF grade reports to students.  The file name of each report contains a character string unique to the student and the report (e.g., the student's last name concatenated with a date string).  That unique identifier is also used in the script.  (Alternatively, the unique identifier could be the report's entire filename.)

This information is represented by these lines in the string, and the last line sets the type of delimiter used in the list.

```applescript
set addresses to "Lastname1,Firstname1,email-address1@dev.null,unique-identifying-string1
lastname2,firstname2,email-address2@dev.null,unique-identifying-string2
lastname3,firstname3,email-address3@dev.null,unique-identifying-string3"
set text item delimiters to ","
```

(A future improvement to the script will have it import a CSV file with this information.)

There are several other variables you need to set in preparatino for sending out your email.  First, your email address:

```applescript
set theSender to "your-email@dev.null"
```

Second, the subject line of your message

```applescript
set theSubject to "grade report for COURSE"
```

Then there's the body of your email message.  I keep it simple plain text.

```applescript
set theBody to "Dear " & text item 2 of l & "," & linefeed & linefeed & "Attached is a copy of your last grade report for COURSE.  Please review to make sure the information contained in the report is accurate." & linefeed & linefeed & "All learning target quizzes have been graded and this report reflects my final assessment of your mastery of course learning targets." & linefeed & linefeed & "Let me know if you have any questions or concerns about this report.  Have a restful holiday break and recharge your batteries so you're ready to return to schoolwork in January!  I hope to see many of you in COURSE II!" & linefeed & linefeed & "Sincerely," & linefeed & "Dr. Miller" & linefeed & linefeed & fileName
```

Here you can see where the script calls a variable (recipient's first name), how line breaks are created with `linefeed`, and where the name of the file that's attached is appended.  (This latter bit is probably not needed.)

The rest of the script is about creating and sending the messages by looping through the 'addresses' information at the start of the script.

There's a block of commands that catch errors related to the file attachment; this works but it's hard to assess where in the list of 'addresses' the loop broke.  It's reasonable to add some more error checking into the script.

After the script creates an email message to be sent, it will log that it attached a file.  The script paiuses for two beats (because sometimes it takes a moment for the OS to attached the PDF to the outgoing message) before it sends.  By adjusting the value of the `delay` you can tune this to your comfort level and the ability of your system.

The `send` command tells the script to send the email it created before it increments the loop for the next message.

```applescript
log "message_attachment = " & message_attachment
delay 2
send
```

When I'm feeling cautious, I will comment out the `send` command

```applescript
-- send
```

before running the script.  This will generate a stack of email message that I can send by hand after reviewing.

## The Complete Script

This is the complete script for those who are interested.  Comments are welcome.

```applescript 
-- script to send a personalized uniform email to a collection on individuals
-- adapted from from https://stackoverflow.com/questions/15386794/applescript-for-sending-emails-from-a-list-in-excel
-- ###############################################################
set addresses to "Lastname1,Firstname1,email-address1@dev.null,unique-identifying-string1
lastname2,firstname2,email-address2@dev.null,unique-identifying-string2
lastname3,firstname3,email-address3@dev.null,unique-identifying-string3"
set text item delimiters to ","
repeat with l in paragraphs of addresses
    tell application "Finder"
        set folderPath to folder "PATH:TO:ATTACHMENT:DIRECTORY:"
        set theFile to (first file of folderPath whose name contains text item 4 of l) as alias
        set fileName to name of theFile
    end tell
    set theAttachment to theFile
    set theSender to "your-email@dev.null"
    set theSubject to "grade report for COURSE"
    set theBody to "Dear " & text item 2 of l & "," & linefeed & linefeed & "Attached is a copy of your last grade report for COURSE.  Please review to make sure the information contained in the report is accurate." & linefeed & linefeed & "All learning target quizzes have been graded and this report reflects my final assessment of your mastery of course learning targets." & linefeed & linefeed & "Let me know if you have any questions or concerns about this report.  Have a restful holiday break and recharge your batteries so you're ready to return to schoolwork in January!  I hope to see many of you in COURSE II!" & linefeed & linefeed & "Sincerely," & linefeed & "Dr. Miller" & linefeed & linefeed & fileName
    tell application "Mail"
        set theNewMessage to make new outgoing message with properties {subject:theSubject, content:theBody & return & return, visible:true}
        tell theNewMessage
            set visible to true
            set sender to theSender
            make new to recipient at end of to recipients with properties {name:text item 2 of l, address:text item 3 of l}
            try
                make new attachment with properties {file name:theAttachment} at after the last word of the last paragraph
                set message_attachment to 0
            on error errmess -- oops
                log errmess -- log the error
                set message_attachment to 1
            end try
            log "message_attachment = " & message_attachment
            --          send
            delay 2
            send
        end tell
    end tell
end repeat
```