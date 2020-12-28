---
title: Teaching Statistics with R - t-test
author: jason
date:  2020-12-27
layout: post
tags: teaching R
---

This tweet was about three months late for me.  At the last minute, I was tapped to teach a major-level introductory probability and statistics course this Fall.  It was something I accepted with grace because I knew my Chair was coming to be because a junior colleague had special COVID-related leave.  In my career, I've learned statistics on the fly, first through teaching an introductory class for non-majors and later through mentoring research with undergraduates.  Statistics if cool, but it requires a different way of thinking.

I've been playing with R for quite some time, primarily in support of undergraduate research and also to support some service work (e.g., grant evaluation and program assessment).  I think all introductory statistics courses should use R to facilitate the learning of the topic.  Some of my colleagues think that the command-line and script-based nature of R make it especially difficult for students to learn, since they're used to menu-based computer solftware, making SPSS a better environment for learning.  But I think SPSS is black-box in a way that R is not, so I will not conceed.

And [R is free](https://www.r-project.org).  And R has [R Studio](https://rstudio.com), which also has a free version.  This makes R a perfect fit for keeping the cost of a STEM education low.  And the bonus is that R is hot in inductry and academia.  People take it seriously because it does some serious lifitng.

When I was asked to teach a statistics class this fall, integrating R was an immediate priority.  The statistician who designed the course I was to teach used the free [Grinstead and Snell](https://math.dartmouth.edu/~prob/prob/prob.pdf) test for probability and [another standard](https://www.amazon.com/Statistics-Engineers-Scientists-William-Navidi/dp/0073401331/ref=pd_lpo_14_img_0/144-7088179-1250558?_encoding=UTF8&pd_rd_i=0073401331&pd_rd_r=d4df0a79-4c28-477c-bb3f-6aa2a6b8d7b8&pd_rd_w=2VGwc&pd_rd_wg=yeGPZ&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=0HASBREQPVD2BZAXMNZC&psc=1&refRID=0HASBREQPVD2BZAXMNZC) (_i.e._, expensive) test for the statistics.  The Grinstead text is interesting from an R perspective because it uses a bunch of scripting to help students understand new concepts in the topic.  Unfortunately, those scripts are presented as Java Applets which can't be run in modern browsers or modern operating systems.  Instead of being frustrated, I was excited.  This was an opportunity for me.

I used my limited knowledge of R to write R-scripts that would do what the Grinstead's Java Applets would have done.  You and anyone else can find those scripts here, on GitHub:  [R-for-Grinstead-and-Snell](https://github.com/jasonemiller/R-for-Grinstead-and-Snell).  They are not a complete set of scripts, but I'm pretty happy with what I've done.  Comments that will improve them are always welcome.

When it comes to the descriptive and inferential statistics part of the course, there was less for me to work with.  I have to wade deep into documentation for base R to give students function-level instructions for using R.

My digging taught me a lot.  One think it taught me is that there wasn't a pre-baked way to compute confidence intervals or to do hypothesis testing.  This was OK for me as a novice instructor because it allowed me to lean on the procedural approach to which I was accustomed.  

Today, I saw a tweet about [this post](https://www.r-bloggers.com/2020/02/students-t-test-in-r-and-by-hand-how-to-compare-two-groups-under-different-scenarios-2/) and immediately wiched I'd had something like it for reference while I was preparing for the conclusion of my stats class, this fall.  It has such nice, detailed instructions for doing tests that I know my students would appreciate.  And that's why I'm writing this, now. 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Student’s t-test in R and by hand: how to compare two groups under different scenarios {<a href="https://t.co/4MEx93OZpa">https://t.co/4MEx93OZpa</a>} <a href="https://twitter.com/hashtag/rstats?src=hash&amp;ref_src=twsrc%5Etfw">#rstats</a> <a href="https://twitter.com/hashtag/DataScience?src=hash&amp;ref_src=twsrc%5Etfw">#DataScience</a></p>&mdash; R-bloggers (@Rbloggers) <a href="https://twitter.com/Rbloggers/status/1343316295794749440?ref_src=twsrc%5Etfw">December 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


