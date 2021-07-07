---
title: "Test to Jekyll"
author: "jason"
date: 2021-07-07
layout: post
tags: mathematics statistics climate-change R 
output:
  md_document:
      variant: gfm
      preserve_yaml: true
---

In late June, I [wrote a short
post](http://thecoldfish.com/2021/06/23/heatwave-modeling.html) to
capture the feeling of meteorologists’ disbelief at the temperature
forecasts for the Pacific Northwest (PNW) for late June 2021. Their
reactions to the forecasts shows the clash between our weather
expectations from experience and the new reality of global climate
change. In this post, I look at the temps on June 26, 27, and 28 and put
them into a historical context using some statistics (and R).

What I wanted to do was get a record of the daily high temperatures on
June 28th in Portland, OR, and see how unusual a high of 115°F on the
28th would be.

## Historical Temperature Data

To get historical data on the daily high temperatures in Portland, OR, I
went to the web site for NOAA’s National Centers for Environmental
Information, and found their [Climate Data
Online](https://www.ncdc.noaa.gov/cdo-web/datasets) page. I then
searched their [Daily
Summaries](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND)
data for Portland stations.

After some fiddling with choices (there is data from many weather
stations in the Portland area), I downloaded [this temperature
data](/assets/data/weather-temp-0099-portland.csv) which included daily
temperatures from the Portland Regional Forecast Office (from January 1,
1900 to June 30, 1973) and the Portland International Airport (from May
1, 1936 until June 30, 1971) and the Portland International Airport
(from May 1, 1936 until December 31, 1999). For former has Station ID
USW00024274 and the latter has Station ID USW00024229. I chose the dates
to span the 20th century.

Once I had the data in CSV format (an option you have to specify on the
NOAA download page, otherwise you’ll get a useless PDF report), I saved
it as `weather-temp-0099-portland.csv` and imported into R.

``` r
library(readr)
df <- read_csv("weather-temp-0099-portland.csv")
```

I then did some R-foo to reformat the data variables (aka, column
headers) to lowercase, dropped some irrelevant columns, and got rid of
rows that had an ‘NA’ instead of a temp value.

``` r
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
df<-rename_with(df,tolower)
# drop irrelevant columns
df<-df[-c(5,7,8,10,12:14)]
library(tidyr)
df<-drop_na(df)
```

To isolate the annual daily highs on June 28th, I found a function in
the `openair` package and used it instead of rolling my own.

``` r
library(openair)
# for the SelectByDate function
# https://davidcarslaw.github.io/openair/reference/selectByDate.html
df628<-selectByDate(
  df,
  month = 6,
  day = 28,
)
```

Here you can see I save the data frame with a new name, indicating that
it’s the temps for June 28th. But these data set has temps from two
weather stations, the data from the two stations overlaps in time
(meaning that there are two temps for the same day for quite a few
days). So I teased the data apart by weather station using a `dplyr`
function.

``` r
# for station USW00024274
df1<-filter(df628,station=="USW00024274")

# for station USW00024229
df2<-filter(df628,station=="USW00024229")
```

The data from the Portland Regional Forecast Office had 74 measurements
and the data from the Portland International Airport has 62 measurement.
The highest temperature recorded at both these sites is 95°F in 1951.
The lowest high temperature on that day was 60°F and occurred in 1963,
1968, and 1971.

## How Unusual is 115°F on June 28th?

The fact that a high temperature of 115°F had *never* occurred in
Portland, OR, in recorded history makes the event unusual. But how
unusual?

Let’s assume that the daily high temperatures follow a normal, or
[Gaussian](https://en.wikipedia.org/wiki/Normal_distribution),
distribution (which we will see they don’t), we can come up with some
rough estimates for the rarity of a 115°F day. We’ll look at how this
temperature compares to the expected temperature on June 28th and how
the temperatures on that date have varied, historically. Specifically,
we’ll ask how 115&def;F compares to the mean temperature of June 28ths
in terms of standard deviations of historic temperatures on that day.

First, we’ll look at what the data tells us to expect the daily high on
28 June to be in any given year. This expected value is the mean of the
data sets, or

``` r
temp_ave1<-mean(df1$tmax)
temp_ave2<-mean(df2$tmax)
```

the values of which are 73.6756757°F and 74.8064516°F, respectively. The
2021 high exceeds both by over 40°F!

Second, we’ll express the record high in terms of the way our data is
spread out, or its standard deviation. A standard deviation can be used
as a unit to measure how far above or below a a value lies relative to a
distribution’s center. Generally, events closer to a distribution’s
center are more likely and events further away are less likely. The
standard deviation for each data set is

``` r
temp_sd1<-sd(df1$tmax)
temp_sd2<-sd(df2$tmax)
```

or about 9.0343456°F and 8.9622866°F, respectively. This means our
record high temperature is

``` r
df1n<-(df1$tmax-temp_ave1)/temp_sd1
df2n<-(df2$tmax-temp_ave2)/temp_sd2
```

or -0.4068558, -1.070988, -0.4068558, -0.4068558, 1.4748522, 0.035899,
-1.2923654, -1.070988, 0.2572764, -0.4068558, -0.8496106, -1.2923654,
-0.6282332, -0.7389219, 0.9214087, 0.9214087, -1.070988, -0.6282332,
-0.1854784, -1.070988, 0.5893426, 0.4786539, 0.5893426, 2.2496731,
1.2534748, -0.2961671, 0.9214087, -0.9602993, -0.4068558, 0.035899,
-0.5175445, -0.5175445, 1.3641635, -0.6282332, -0.0747897, -0.8496106,
-0.1854784, 2.0282957, 1.1427861, 1.3641635, 1.3641635, -0.6282332,
0.7000313, 1.1427861, 1.6962296, -0.2961671, -0.5175445, -0.7389219,
1.8069183, -0.9602993, 1.8069183, 2.3603618, -0.2961671, -0.9602993,
-0.4068558, -0.9602993, -0.4068558, -0.5175445, -0.5175445, -0.8496106,
1.0320974, -0.5175445, 0.81072, -0.9602993, -0.2961671, 0.4786539,
0.035899, 1.1427861, -1.5137428, -1.4030541, -0.9602993, -1.5137428,
1.2534748, -0.0747897 and 1.0258039, 1.2489612, 1.2489612, -0.5362975,
0.4679105, 1.0258039, 1.6952759, -0.5362975, -0.5362975, -0.7594548,
1.6952759, -1.3173481, 1.1373826, 2.2531692, -0.3131401, -0.7594548,
-0.5362975, -1.2057695, -0.6478761, -0.4247188, -0.8710335, -0.9826121,
0.8026465, -0.7594548, 0.6910679, -1.6520842, -0.5362975, 0.4679105,
-0.2015615, 1.0258039, -1.5405055, -1.5405055, -0.7594548, -1.6520842,
1.4721186, 0.0215959, 0.3563319, -0.9826121, 1.4721186, 0.8026465,
1.3605399, 0.5794892, -0.0899828, 0.4679105, 0.0215959, -0.3131401,
0.1331745, 0.2447532, -1.3173481, 1.3605399, -1.3173481, -0.7594548,
0.2447532, -0.5362975, -0.3131401, -0.8710335, 1.0258039, 1.3605399,
-0.7594548, -0.4247188, 1.0258039, -0.9826121 standard deviations from
the expected daily high temperature. This is huge!

Were the daily high temperatures distributed normally, we could use some
basic statistics to calculate the probability that June 28th in
Portland, OR, should have a high temperature of 115°F or higher. In R,
we can calculate those probabilities with the `dnorm` function:

``` r
dnorm(df1n)
```

    ##  [1] 0.36725298 0.22482203 0.36725298 0.36725298 0.13445402 0.39868530
    ##  [7] 0.17307285 0.22482203 0.38595515 0.36725298 0.27807689 0.17307285
    ## [13] 0.32749680 0.30363125 0.26094764 0.26094764 0.22482203 0.32749680
    ## [19] 0.39213871 0.22482203 0.33534318 0.35576201 0.33534318 0.03176300
    ## [25] 0.18185638 0.38182381 0.26094764 0.25157204 0.36725298 0.39868530
    ## [31] 0.34893673 0.34893673 0.15733004 0.32749680 0.39782810 0.27807689
    ## [37] 0.39213871 0.05099997 0.20764642 0.15733004 0.15733004 0.32749680
    ## [43] 0.31224710 0.20764642 0.09465317 0.38182381 0.34893673 0.30363125
    ## [49] 0.07797123 0.25157204 0.07797123 0.02461024 0.38182381 0.25157204
    ## [55] 0.36725298 0.25157204 0.36725298 0.34893673 0.34893673 0.27807689
    ## [61] 0.23420675 0.34893673 0.28720129 0.25157204 0.38182381 0.35576201
    ## [67] 0.39868530 0.20764642 0.12686304 0.14908794 0.25157204 0.12686304
    ## [73] 0.18185638 0.39782810

``` r
dnorm(df2n)
```

    ##  [1] 0.23572832 0.18288631 0.18288631 0.34550574 0.35757553 0.23572832
    ##  [7] 0.09480637 0.34550574 0.34550574 0.29899622 0.09480637 0.16752183
    ## [13] 0.20892957 0.03151397 0.37985453 0.29899622 0.34550574 0.19284307
    ## [19] 0.32341780 0.36453542 0.27299872 0.24617765 0.28907784 0.29899622
    ## [25] 0.31419988 0.10191363 0.34550574 0.35757553 0.39092012 0.23572832
    ## [31] 0.12178268 0.12178268 0.29899622 0.10191363 0.13499668 0.39884926
    ## [37] 0.37440217 0.24617765 0.13499668 0.28907784 0.15810863 0.33727981
    ## [43] 0.39733045 0.35757553 0.39884926 0.37985453 0.39542021 0.38717031
    ## [49] 0.16752183 0.15810863 0.16752183 0.29899622 0.38717031 0.34550574
    ## [55] 0.37985453 0.27299872 0.23572832 0.15810863 0.29899622 0.36453542
    ## [61] 0.23572832 0.24617765

returns 0.367253, 0.224822, 0.367253, 0.367253, 0.134454, 0.3986853,
0.1730728, 0.224822, 0.3859551, 0.367253, 0.2780769, 0.1730728,
0.3274968, 0.3036312, 0.2609476, 0.2609476, 0.224822, 0.3274968,
0.3921387, 0.224822, 0.3353432, 0.355762, 0.3353432, 0.031763,
0.1818564, 0.3818238, 0.2609476, 0.251572, 0.367253, 0.3986853,
0.3489367, 0.3489367, 0.15733, 0.3274968, 0.3978281, 0.2780769,
0.3921387, 0.051, 0.2076464, 0.15733, 0.15733, 0.3274968, 0.3122471,
0.2076464, 0.0946532, 0.3818238, 0.3489367, 0.3036312, 0.0779712,
0.251572, 0.0779712, 0.0246102, 0.3818238, 0.251572, 0.367253, 0.251572,
0.367253, 0.3489367, 0.3489367, 0.2780769, 0.2342067, 0.3489367,
0.2872013, 0.251572, 0.3818238, 0.355762, 0.3986853, 0.2076464,
0.126863, 0.1490879, 0.251572, 0.126863, 0.1818564, 0.3978281 and
0.2357283, 0.1828863, 0.1828863, 0.3455057, 0.3575755, 0.2357283,
0.0948064, 0.3455057, 0.3455057, 0.2989962, 0.0948064, 0.1675218,
0.2089296, 0.031514, 0.3798545, 0.2989962, 0.3455057, 0.1928431,
0.3234178, 0.3645354, 0.2729987, 0.2461777, 0.2890778, 0.2989962,
0.3141999, 0.1019136, 0.3455057, 0.3575755, 0.3909201, 0.2357283,
0.1217827, 0.1217827, 0.2989962, 0.1019136, 0.1349967, 0.3988493,
0.3744022, 0.2461777, 0.1349967, 0.2890778, 0.1581086, 0.3372798,
0.3973304, 0.3575755, 0.3988493, 0.3798545, 0.3954202, 0.3871703,
0.1675218, 0.1581086, 0.1675218, 0.2989962, 0.3871703, 0.3455057,
0.3798545, 0.2729987, 0.2357283, 0.1581086, 0.2989962, 0.3645354,
0.2357283, 0.2461777, respectively. This means we’d expect a high temp
of 115°F on 28 June about once every 10000 years.

This estimate is terribly rough, and we have little reason to have faith
in it for two reasons. First, there’s nothing special about June 28th.
We’d be just as troubled if a 115°F day had occurred on the 27th or
29th. So our estimate for the rarity of a of 115°F high is inflated. (It
should be *that* rare.) Second, we used an assumption that our
temperatures were normally distributed, but they aren’t.

To see how incorrect that assumption is, take a look at the distribution
of temperatures.

``` r
hist(df1$tmax, main="High temperatures on 28 June at the Portland Regional Forecast Office")
```

![](/images/hist-stations-1.png)<!-- -->

``` r
hist(df2$tmax, main="High temperatures on 28 June at the Portland International Airport")
```

![](/images/hist-stations-2.png)<!-- -->

A normal distribution is symmetric about its ‘center’, or highest point.
These distributions are both skewed right, having more mass above their
‘center’ and having a tail that extends farther to the right than to the
left. They also appear to be bi-modal, having two local maxima.

To see how poorly these distributions are described by a Gaussian, we
find the Gaussian of best fir for each and plot then with the data’s
frequency histogram.

``` r
dg1<-df1$tmax
dg2<-df2$tmax

library(MASS)
```

    ## 
    ## Attaching package: 'MASS'

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     select

``` r
pnormal1<-fitdistr(dg1,"normal")
pnormal2<-fitdistr(dg2,"normal")

h1<-hist(dg1,breaks=20);
```

![](/images/distns-1.png)<!-- -->

``` r
xhist1<-c(min(h1$breaks),h1$breaks)
yhist1<-c(0,h1$density,0)
xfit1<-seq(min(dg1),max(dg1),length=max(dg1)-min(dg1)+1)
ynfit<-dnorm(xfit1,pnormal1$estimate[1],pnormal1$estimate[2])


h2<-hist(dg2,breaks=20);
```

![](/images/distns-2.png)<!-- -->

``` r
xhist2<-c(min(h2$breaks),h2$breaks)
yhist2<-c(0,h2$density,0)
xfit2<-seq(min(dg2),max(dg2),length=max(dg2)-min(dg2)+1)
ynfit<-dnorm(xfit2,pnormal2$estimate[1],pnormal2$estimate[2])
```

``` r
{plot(xhist1,yhist1,type="s",ylim=c(0,max(yhist1,ynfit)),main="Best Normal approximation to highs at the Portland Regional Forecast Office")
lines(xfit1,ynfit,col="red")}
```

![](/images/bestfit-1.png)<!-- -->

``` r
{plot(xhist2,yhist2,type="s",ylim=c(0,max(yhist2,ynfit)),main="Best Normal approximation to highs at the Portland International Airport")
lines(xfit2,ynfit,col="red")}
```

![](/images/bestfit-2.png)<!-- --> Pretty terrible, right?

Now let’s consider 115°F in the context of historical June temperatures,
relaxing our fixation on the date of June 28th.

## How Unusual is 115°F in June?

Pulling all the June data from our NOAA data

``` r
df6<-selectByDate(
  df,
  month = 6,
)
```

and isolating the temperatures by weather station

``` r
# for station USW00024274
df61<-filter(df6,station=="USW00024274")

# for station USW00024229
df62<-filter(df6,station=="USW00024229")
```

we see the high temperature in Junes was 102°F on June 30, 1942. How
unusual is there?

R makes it easy to calculate that 115°F is 4.92 and 4.94 standard
deviations above the expected high temperature for a June day in
Portland, so a day that is that hot or hotter has about a 0.0000022
chance of happening in June. That’s about once every 50000 Junes, or
once every 4100 years.

This assumes that temperatures follow a Gaussian distribution, and we
already know that assumption is suspect. Let’s make a visual check of
this.

``` r
dg1<-df61$tmax
dg2<-df62$tmax

library(MASS)
pnormal1<-fitdistr(dg1,"normal")
pnormal2<-fitdistr(dg2,"normal")

h1<-hist(dg1,breaks=20);
```

![](/images/distns2-1.png)<!-- -->

``` r
xhist1<-c(min(h1$breaks),h1$breaks)
yhist1<-c(0,h1$density,0)
xfit1<-seq(min(dg1),max(dg1),length=max(dg1)-min(dg1)+1)
ynfit1<-dnorm(xfit1,pnormal1$estimate[1],pnormal1$estimate[2])


h2<-hist(dg2,breaks=20);
```

![](/images/distns2-2.png)<!-- -->

``` r
xhist2<-c(min(h2$breaks),h2$breaks)
yhist2<-c(0,h2$density,0)
xfit2<-seq(min(dg2),max(dg2),length=max(dg2)-min(dg2)+1)
ynfit2<-dnorm(xfit2,pnormal2$estimate[1],pnormal2$estimate[2])
```

``` r
{plot(xhist1,yhist1,type="s",ylim=c(0,max(yhist1,ynfit)),main="Best Normal approximation to highs at the Portland Regional Forecast Office")
lines(xfit1,ynfit1,col="red")}
```

![](/images/bestfit2-1.png)<!-- -->

``` r
{plot(xhist2,yhist2,type="s",ylim=c(0,max(yhist2,ynfit)),main="Best Normal approximation to highs at the Portland International Airport")
lines(xfit2,ynfit2,col="red")}
```

![](/images/bestfit2-2.png)<!-- -->

We see that the Gaussian fits better, but it’s not perfect. The mean of
the Gaussian is a bit above the mode of the temperature distribution,
and the right tail of the temperature distribution appears to lie above
the right tail of the Gaussian. This suggests that our estimate of how
unusual the high temperature is might be an underestimate.

Whgat happens if we broaden the range of dates we consider even further?
After all, high temperatures also occur in July, August, and September.

## How Unusual is 115°F in June through September?

Repeating the above with the data set for daily high temperatures in
June, July, August, and September,

``` r
dfsummer<-selectByDate(
  df,
  month = 6:9,
)
```

and separating out ot the records at the two stations

``` r
# for station USW00024274
dfsum1<-filter(dfsummer,station=="USW00024274")

# for station USW00024229
dfsum2<-filter(dfsummer,station=="USW00024229")
```

we see the high temperature during these months was 107°F on July 2,
1942, July 30, 1965, and August 8 and 10, 1981.

Even with a higher high temperature, we can calcualte that 115°F is 4.48
and 4.29 standard deviations above the expected temperature during this
period. So the probability that a day in June, July, August of September
has a high of 115°F or higher is 0.00004. That means that we expect a
day to have this temperature once every 833 years.

This assumes that temperatures follow a Gaussian distribution, and we
already know that assumption is suspect. Let’s make a visual check of
this.

``` r
dg1<-dfsum1$tmax
dg2<-dfsum2$tmax

library(MASS)
pnormal1<-fitdistr(dg1,"normal")
pnormal2<-fitdistr(dg2,"normal")

h1<-hist(dg1,breaks=20);
```

![](/images/distns3-1.png)<!-- -->

``` r
xhist1<-c(min(h1$breaks),h1$breaks)
yhist1<-c(0,h1$density,0)
xfit1<-seq(min(dg1),max(dg1),length=max(dg1)-min(dg1)+1)
ynfit1<-dnorm(xfit1,pnormal1$estimate[1],pnormal1$estimate[2])


h2<-hist(dg2,breaks=20);
```

![](/images/distns3-2.png)<!-- -->

``` r
xhist2<-c(min(h2$breaks),h2$breaks)
yhist2<-c(0,h2$density,0)
xfit2<-seq(min(dg2),max(dg2),length=max(dg2)-min(dg2)+1)
ynfit2<-dnorm(xfit2,pnormal2$estimate[1],pnormal2$estimate[2])
```

``` r
{plot(xhist1,yhist1,type="s",ylim=c(0,max(yhist1,ynfit)),main="Best Normal approximation to highs at the Portland Regional Forecast Office")
lines(xfit1,ynfit1,col="red")}
```

![](/images/bestfit3-1.png)<!-- -->

``` r
{plot(xhist2,yhist2,type="s",ylim=c(0,max(yhist2,ynfit)),main="Best Normal approximation to highs at the Portland International Airport")
lines(xfit2,ynfit2,col="red")}
```

![](/images/bestfit3-2.png)<!-- --> These plots show this set of daily
high temperaturews over a longer aprt of the year is much closer to a
Gaussian distribution, so we can feel more comfortable with the high
temp on June 28th was a “one in 800 year” event, at least in the context
of 20th century records for Portland, OR.

## Conclusion

Even though these methods used a very sketchy normality assumption, the
investigation shows that Portland, OR, having a high of 115°F is
historically very unlikely to happen. Even climate change skeptics
should look at this as undeniable evidence that something is changing in
the world around us to make events like this happen more often than this
historical record says they should be happening.
