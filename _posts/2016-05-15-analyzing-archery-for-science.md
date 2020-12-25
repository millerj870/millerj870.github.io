---
author: jason
date: 2016-05-15 21:37:22+00:00
layout: post
title: Analyzing Archery for Science!
tags: coding imageJ R
---

My daughter is in eigth grade. When she was asked to come up with a science project, she thought of her compound bow and how she could use that to study the effect of changing some variable and holding others constant. For her project she is asking, “What effect will varying the draw poundage have on my accuracy?” To study this, we have spent some time at the regional archery range (home of the Conejo Valley Archery club) and shot rounds on their 13m and 18m lanes.

I want to write up is the process that I, the Dad, am using to look at her data before she has a chance to look at it herself. (She’s procrastinating a bit.)

To do my analysis, I’m taking digital images of the struck targets and putting them into ImageJ to make measurements. I record the Cartesian coordinates of each strike (with the center of the target as the origin). Then I use R, with this data in a data frame, to visualize the strikes and do some basic statistics to get a sense of my daughter’s accuracy and precision.

This post describes how I am doing the above.

# ImageJ

First, I load my digital image of the target into ImageJ. (I drag and drop the image onto the ImageJ icon in my doc.) The picture of the target has strikes labeled according to their set and order in the set.

Second, I set the origin of the image to the target center. To do this, I mouse over the center and read the xy-coordinates of the point in the image. (Remember, the natural origin of an image in ImageJ is the upper-left corner.) I write the coorindate down, open the Image > Properties submenu, and enter the coordinates into the Origin (pixels): field, both values separated by a comma.

NOTE: This worked the first few times I tried it, but the last few times, the orign does not get set right. Typically, the vertical coordinate is off by a number of pixels. So I hand-adjust the origin location until I get (0,0) when I mouse-over the target center. Why is ImageJ doing this?

Once the target center is (0,0), Analyze > Set Measurements. This opens a dialog box with many check-boxes. I make sure “Invert Y coordinates” is checked (so that the y-values increase as you move up the image).

Third, I set the scale of the image so distances are measured in centimeters. (“It’s more scientific,” my daughts says.) To do this, I use the line tool to draw a straight line from the center of the target to the perimeter of the target. Then in Analyze > Set Scale, the ‘distance in pixels’ is set to the length of the line. Then I fill in “10” for the known distance, and I fill in “cm” for the unit of length. I then click ‘OK’.

At this point, I’m ready to get location data on the arrow strikes. I double-click on the ‘point selection tool’ in ImageJ’s tool bar. This brings up a ‘Point Tool’ dialog box which lets me select the appearance of my point markers. There are some check-boxes. The one I want to check is the ‘Add to ROI Manager’ so the point coordiantes are recorded by ImageJ. I can then download them later using the Save-As menu function.

Now I’m ready to click on the center of each of my arrow strikes. Each click puts an entry into the ROI manage dialog box. When I’ve clicked all the strikes of interest, I hit the “Measure” button in the ROI Manager dialog box, and the measurements get copied into the Results window from which I can save the data. (I also hand-write the measurements in paper that is functioning as my lab notebook. But that’s because I’m careful and particular.)

# R

Using R, I create a data frame that has columns that track the following:

  * date of the shoot (“date”, a factor),
  * in set in which the shot occured on that date (“group”, a factor),
  * when the shot occured in the group (“ingroupshot”, a factor),
  * when the shot occured on the date (“shot”, a numeric),
  * the length of the shooting lane (“dist”, a factor),
  * the draw poundage (“drawlbs”, a factor),
  * the horizontal distance of the shot from the center of the target (“x”,a double), and
  * the vertical distance of the shot from the center of the target (“y”, a double).

I can visualize the shots using ggplot, and I can do calculations on the measurements. At the time of this writing, I haven’t done much, but my thoughts on exploring the data center on the ideas of accuracy and precisioiu. Accuracy is the concept of being close the the points at this wyou are aiming. Precision is the concept of having your arrows land in tight bunches. The former is a statement that concerns the (average) distance to the center of the target. The latter is a statement about standard deviations of distances or coordiante measurements (i.e., a set is precise if the average distance to a set’s centroid is small.)
