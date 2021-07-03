---
title: How Unusual Was Portland's High Temp on June 28th?
author: Jason
layout: post
date: 2021-07-03
tags: mathematics statistics climate-change R
---

In late June, I wrote a short post to capture the feeling of meteorologists' disbelief at the temperature forecasts for the Pacific Northwest (PNW) for late June 2021.  Their reactions to the forecasts shows the clash between our weather expectations from experience and the new reality of global climate change.  In this post, I look at the temps on June 26, 27, and 28 and put them into a historical context using some statistics (and R).

What I wanted to do was get a record of the daily high temperatures on June 28th in Portland, OR, and see how unusual a high of 115&deg;F on the 28th would be.

## Historical Temperature Data

To get historical data on the daily high temperatures in Portland, OR, I went to the web site for NOAA's  National Centers for Environmental Information, and found their [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/datasets) page.  I then searched their [Daily Summaries](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND) data for Portland stations.

After some fiddling with choices (there is data from many weather stations in the Portland area), I downloaded [this temperature data](/assets/data/weather-temp-0099-portland.csv) which included daily temperatures from the Portland Regional Forecast Office (from January 1, 1900 to June 30, 1973) and the Portland International Airport (from May 1, 1936 until June 30, 1971) and the Portland International Airport (from May 1, 1936 until December 31, 1999).  For former has Station ID USW00024274 and the latter has Station ID USW00024229.  I chose the dates to span the 20th century.

Once I had the data in CSV format (an option you have to specify on the NOAA download page, otherwise you'll get a useless PDF report), I saved it as `weather-temp-0099-portland.csv` and imported into R.

```
library(readr)
df <- read_csv("weather-temp-0099-portland.csv")
```

I then did some R-foo to reformat the data variables (aka, column headers) to lowercase, dropped some irrelevant columns, and got rid of rows that had an 'NA' instead of a temp value.

```
library(dplyr)
df<-rename_with(df,tolower)
# drop irrelevant columns
df<-df[-c(5,7,8,10,12:14)]
library(tidyr)
df<-drop_na(df)
```

To isolate the annual daily highs on June 28th, I found a function in the `openair` package and used it instead of rolling my own.

```
library(openair)
# for the SelectByDate function
# https://davidcarslaw.github.io/openair/reference/selectByDate.html
df628<-selectByDate(
  df,
  month = 6,
  day = 28,
)
```

Here you can see I save the data frame with a new name, indicating that it's the temps for June 28th.  But these data set has temps from two weather stations, the data from the two stations overlaps in time (meaning that there are two temps for the same day for quite a few days).  So I teased the data apart by weather station using a `dplyr` function.

```
# for station USW00024274
df1<-filter(df628,station=="USW00024274")

# for station USW00024229
df2<-filter(df628,station=="USW00024229")
```
The data from the Portland Regional Forecast Office had 74 measurements and the data from the Portland International Airport has 62 measurement.  The highest temperature recorded at both these sites is 95&deg;F in 1951.  The lowest high temperature on that day was 60&deg;F and occurred in 1963, 1968, and 1971.

## How Unusual is 115&deg;F on June 28th?

The fact that a high temperature of 115&deg;F had *never* occurred in Portland, OR, in recorded history makes the event unusual.  But how unusual?

If we assume that the daily high temperatures follow a probability distribution, we can use that distribution to estimate how unlikely a temp of 115&deg;F would be.  If the high temperatures were [distributed normally](https://en.wikipedia.org/wiki/Normal_distribution), we could compute the likelihood of a temperature 115&deg;F or higher using Z-scores, a standard technique in Stats 101.  Plotting histograms for each of these datasets shows the distributions aren't normal.

[![ALT-TEXT](/assets/images/Rplot-hist628station1-thumbnail.jpg)](/assets/images/Rplot-hist628station1.png)

[![ALT-TEXT](/assets/images/Rplot-hist628station2-thumbnail.jpg)](/assets/images/Rplot-hist628station2.png)

A normal distribution is symmetry about its 'center', or highest point.  These are skewed right, having more mass above their 'center' and having a tail that extends farther to the right than to the left.  This means that we can't really use the normal distribution to get an accurate measure of the chances a high temp of 115&deg;F would occur.

Instead, we'll make some conservative estimates.  Let's start by looking at this record temp in the context of the data set.  

First, we'll look at what the data tells us to expect the daily high on 28 June to be in any given year.  This expected value is the mean of the data set, or

```
temp_ave1<-mean(df1$tmax)
temp_ave2<-mean(df2$tmax)
```

the values of which are 73.7&deg;F and 74.8&def;F, respectively.  The 2021 high exceeds both by over 40&def;F!

Second, we'll express the record high in terms of the way our data is spread out, or its standard deviation.  The standard deviation for each data set is

```
temp_sd1<-sd(df1$tmax)
temp_sd2<-sd(df2$tmax)
```

or about 9.03 and 8.96, respectively.  A standard deviation can be used as a unit to measure how far above or below a a value lies relative to a distribution's center.  Generally, events closer to a distribution's center are more likely and events further away are less likely.  Our record high temperature is

```
df1n<-(df1$tmax-temp_ave1)/temp_sd1
df2n<-(df2$tmax-temp_ave2)/temp_sd2
```

or 4.57 and 4.48 standard deviations from the expected daily high temperature.  This is huge!

The daily high temperatures are not distributed normally, but their distribution could be (very roughly) approximated by the upper half of a normal distribution.  With this assumption, we can calculate the probability that June 28th in Portland, OR, should have a high of 115&def;F or higher.  In R, we can calculate those probabilities with the `dnorm` function:

```
dnorm(4.57)
dnorm(4.48)
```

returns 0.0000114 and 0.0000171, respectively.  This means we'd expect a high temp of 115&def;F on 28 June about once every 10000 years.[^1]

## How Unusual is 115&deg;F in June?

The above analysis seems a bit unbelievable.  Because there's nothing really special about the date `June 28th`, we can redo the above analysis to see how likely it would be to see this temperature in June?

Pulling all the June data from our NOAA data

```
df6<-selectByDate(
  df,
  month = 6,
)
```

we see the high temperature in June was 102&deg;F on June 30, 1942.  The temperature distributions look like

[![ALT-TEXT](/assets/images/Rplot-hist6station1-thumbnail.jpg)](/assets/images/Rplot-hist6station1.png)

[![ALT-TEXT](/assets/images/Rplot-hist6station2-thumbnail.jpg)](/assets/images/Rplot-hist6station2.png)

R makes it easy to calculate that 115&deg;F is 4.92 and 4.94 standard deviations above the expected high temperature for a June day in Portland, so a day that is that hot or hotter has about a 0.0000022 chance of happening in June.  That's about once every 50000 Junes, or once every 4100 years.

## How Unusual is 115&deg;F in June through September?

Repeating the above with the data set for daily high temperatures in June, July, August, and September,

```
dfsummer<-selectByDate(
  df,
  month = 6:9,
)
```

we see the high temperature during these months was 107&deg;F on July 2, 1942, July 30, 1965, and August 8 and 10, 1981.  The temperature distributions look like

[![ALT-TEXT](/assets/images/Rplot-histsumstation1-thumbnail.jpg)](/assets/images/Rplot-histsumstation1.png)

[![ALT-TEXT](/assets/images/Rplot-histsumstation2-thumbnail.jpg)](/assets/images/Rplot-histsumstation2.png)

Even with a higher high temperature, we see that 115&deg;F is 4.48 and 4.29 standard deviations above the expected temperature during this period.  So the probability that a day in June, July, August of September has a high of 115;deg;F or higher is 0.00004.  That means that we expect a day to have this temperature once every 833 years.

## Conclusion

Even though these methods used a very sketchy normality assumption, the investigation shows that Portland, OR, having a high of 115&def;F is historically very unlikely to happen.  Even climate change skeptics should look at this as undeniable evidence that something is changing in the world around us to make events like this happen more often than this historical record says they should be happening.

[^1]:  Remember that 28 June occurs once a year.  That's why this analysis makes the even seem so rare.

<!--
SYNTAX FOR IMAGES
* use services to create JPG and to create thumbnail that is 720px wide

[![ALT-TEXT](/assets/images/filename-thumbnail.jpg)](/assets/images/filename.jpg)
-->

<!--
SYNTAX FOR VIDEO
* convert MOV to mp4 using VLC

<video width="480" height="320" controls="controls">
  <source src="/assets/media/filename.m4v" type="video/mp4">
</video>
-->
