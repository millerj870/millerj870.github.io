---
author: jason
date: 2011-02-27 19:56:00+00:00
layout: post
title: 'Nerdgasm:  Automating Student Peer Reviews, Part 1'
tags: coding applescript teaching hackedu
---

So, I've just had a chance to bend Google tools and Applescript to the service of teaching.  In the event that someone else might find this interesting, I thought I'd share the story.  Details are available to those who request them in the comments.

This semester, I get to teach an interdisciplinary seminar for juniors that's writing enhanced.  This means that the students need to write a lot and I need to read and comment on their writing.  When I began teaching this course, I took advantage of peer reviewing.  This is where each student has two other students read their writing and share comments.  It gets the students to think about 'good writing' more (theirs and that of others).  To keep them focused on the issues of interest to us in the course, I made a two-page Writing Checklist for each peer reader to fill out as they read another's writing.

Enter this semester, where economizing and cost have led me to try to reduce the amount of paper we use in class.  (Students turn in their work electronically, for example.)  These 'Writing Checklists' require students to print the two pages out, so each essay written generates six pages (three if everyone duplexes) of paper that will be recycled in a few weeks.  All this paper creates a organizational challenge for me in collecting, grading, and returning all the paperwork, meanwhile not losing anything.  So I took some steps to digitize the process.

At first, I tried turning the checklist into a PDF form with Adobe Acrobat Pro.  This seemed like a great idea, until I learned that such a PDF form saves its data in an FDF form.  This data requires a copy of the original PDF form document to view (though the FDF form is a flat text file that _could_ be parsed and made readable, but that's too much work for me and my students).  All this asked too much of my students.  I ended up processing their FDF forms myself and sending that on to the students they reviewed.  We reduced the production of paper, but PDF forms required me to do more work.  Not good.

![](http://agate.truman.edu/~millerj/blog/comment flow.png)Wanting to reduce the work required of my by peer reviews, I turned to Google.  Their Google Docs suite includes a Form service that allows a person to create an online survey.  When a user submits data through such a survey, their data is saved in a Google Spreadsheet.  Could I use this mechanism to streamline the peer review process in my class?

Turning our 'Writing Checklist' into a Google Form was easy.  When I made it available to students, a few used it right away.  Along with the survey data, the Google Spreadsheet includes a cell with the time and date the form was submitted.  Nice.  In addition, Google has a nice page that summarizes the data that is in the spreadsheet.  I turned that off, initially.

Having this, I needed to close the loop.  I needed a way to get a peer reviewer's comments to writers.  For this, I repurposed a tool I made last year.  This tool uses a Numbers spreadsheet to hold my data.  The spreadsheet also includes a template for a report, in this case the 'Writing Checklist.'  An [Applescript](http://agate.truman.edu/~millerj/blog/cycle through names - writing checklist.scpt) goes through the data sheet and, for each row, creates a PDF report that can be emailed to an individual.  This worked like a dream.  It only left me to email (by hand) the PDFs.  TextExpander and keyboard shortcuts for attaching files made this relatively easy.  The diagram at left summarizes this flow; vertical arrows require a human, horizontal arrows are automated.
