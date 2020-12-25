---
author: jason
date: 2017-06-10 15:57:11+00:00
layout: post
title: ImageMagick, Applescript, and Automator
tags: coding applescript
---

This week, I wanted to use the GoPro camera to grab timelapse shots of traffic on a neighborhood street. I also wanted to share the timelapse video online with neighbors. In this post, I'll describe how I brewed up some AppleScript and bash to get this done.

I knew how to set up a GoPro to grab shots every 30 seconds, but my circumstances required the camera to be set up askew. Pics were rotated 90 degrees (counterclockwise) from their real orientation. Also, the field of view was larger than necessary. While I knew how to create a timelapse movie with QuickTime Pro 7 (paid upgrade), using QuickTime required some preprocessing of the images (rotating and cropping) to make the video I’d envisioned. And after making a timelapse video by hand, I realized it would be nice to have a timestamp on each frame so viewers would know when the shots were taken.

Here's what one of the original pics looks liks.

[caption id="attachment_797" align="center" width="300"]![](http://www.thecoldfish.com/wp-content/uploads/2017/06/orig-G0010171-300x225.jpg) An example frame from the timelapse. [/caption]

I’m an Apple nerd because OS X has Darwin underpinnings. My pre-OS X computer days were linux-based. So I’m not afraid of the command line, and I knew cropping and rotating could be done using the command line tool [ImageMagick](http://www.imagemagick.org/script/index.php), which I had installed using [macports](https://www.macports.org).

I knew I could rotate my images by 90 degrees clockwise with the command

```    
convert -rotate "90" input.JPG output.JPG
```

and I knew that I could crop it the way I wanted with the command

```   
convert -crop -400-1320 input.JPG output.JPG.
```

The two commands can be combined into one

```    
convert -rotate "90" -crop -400-1320 input.JPG output.JPG
```

with the transformations happening [left to right](http://www.imagemagick.org/discourse-server/viewtopic.php?t=19342). (This is important because rotations and crops are not commutative operations, nerds.)

After testing ImageMagick on the images, I knew that I could transform the images in the way I wanted, image-by-image. But each timelapse video would consist of about 200 images. I wanted to do this in batch. It seemed like I could do so with a shell script that looked like this:

```shell    
for file in *.JPG
        do
            convert -rotate "90" -crop -400-1320 "$file" "crop-$file"
        done
```
ImageMagick also allows for putting a [watermark on an image](http://www.imagemagick.org/Usage/annotating/#anno_below) with a command that looks sometime like this:

```shell
convert -fill white  -undercolor '#00000080'  -gravity South -annotate +0+5  "TEXT" input.JPG output.JPG
```
where “TEXT” is the timestamp. I knew from Saghoian and Cheeseman’s [AppleScript 1–2–3](https://www.amazon.com/Apple-Training-AppleScript-Soghoian-2009-01-09/dp/B01FGKY68K/ref=sr_1_9?ie=UTF8&qid=1497109293&sr=8-9&keywords=applescript+1-2-3) that image metadata can easily be accessed using AppleScript like so:

```applescript  
set this_file to choose file without invisibles
try
    tell application "Image Events"
        launch
        set this_image to open this_file
        tell this_image
            set the stamp to the value of metadata tag "creation"
        end tell
        close this_image
    end tell
    display dialog stamp
on error error_message
    display dialog error_message
end try
```

So I wondered if my whole solution could be brewed in AppleScript. I knew that you could call command line functions from within AppleScript like so

```shell  
do shell script "COMMAND"
```

but I didn’t know if I could put all this together. The only way to find out is to try.

After much trial and error, I came up with the script that’s shown below. Below the script, I’ll comment on a couple things that were difficult for me.

```applescript    
set this_file to choose file without invisibles
set file_path to quoted form of the POSIX path of this_file
set filename to do shell script "basename " & file_path as string
set dirname to do shell script "dirname " & file_path as string
tell application "Image Events"
  launch
 set this_image to open this_file
   tell this_image
        set the stamp to the value of metadata tag "creation"
  end tell
   close this_image
end tell
set A to -400
set B to -1320
try
 do shell script "/opt/local/bin/convert -rotate '0' -crop +" & A & "+" & B & " " & file_path & " " & quoted form of (dirname & "/tmp-" & filename)
 do shell script "/opt/local/bin/convert " & dirname & "/tmp-" & filename & " -fill white  -pointsize 150 -undercolor '#00000080'  -gravity South -annotate +0+5 " & quoted form of stamp & " " & dirname & "/new-" & filename
  do shell script "rm " & dirname & "/tmp-" & filename
on error error_message
    display dialog error_message
end try
```

This is the timelapse movie that the script allowed me to create.

  [video width="720" height="720" m4v="/assets/media/Davenport-am-timelapse-v2-desktop.m4v"][/video]

A couple things that I learned when writing this script:

  * Because I’m using command line tools, I need to use POSIX paths for my files.

  * AppleScript uses `/bin/sh` to run command line tools; I use `/bin/bash` to run command line tools. Sometimes this difference is important (e.g., the shells might have different PATH variables set).

  * Passing variables (e.g., filenames) from AppleScript to the command line tools was pretty easy once I got the hang of concatenation and quoting.

  * Just because your script works when run in ScriptEditor does not mean it will run in Automator. My path has folder names with spaces and special characters. (What can I say?) Working with those as quoted strings in ScriptEditor worked great, but Automator doesn't like that one bit. This means that I need to be careful where I use this script as a workflow or folder action.

To allow this to run as part of an Automator workflow, I replaced the first line with

```applescript    
on run {input, parameters}
 set this_file to item 1 of input
    ...
 end run
```

Next task: tweak the script to be able to batch process a set of files. But this should be easy. In the meantime, I’ll create a folder action to get that done.

UPDATE: The tweak for batch processing files is easy in the context of Automator. When an Automator workflow runs, it passes a list called inputs to an AppleScript. When my list of inputs is longer than one (i.e., when I'm working on more than one file at a time), I need to iterate through that list. I can do so by adding this line

```applescript    
repeat with this_file in input
```

to the top of my script, and close that loop with

```applescript    
end repeat
```

at the bottom of the script. Easy peasy.
