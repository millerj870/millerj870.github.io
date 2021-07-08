---
title: Using Rmarkdown and Jekyll
author: Jason
layout: post
date: 2021-07-07
tags: R markdown jekyll
---

Last week I was writing up [some thoughts](http://thecoldfish.com/2021/07/03/portland-temp-anomaly.html) on trying to understand how unexpected the high temperatures on June 28th in Portland, OR, were.  (They hit 115&deg;F!)  My goal was to think through some quantitative reasoning based on statistics, and I used R to support my calculations.  Today, I realized I should have been able to write that post up in Rmarkdown in RStudio and post it to my Jekyll site (hosted in Github) with graphs and computations so much more easily.  So I sat down to try to figure it out.

Well, I sat down in from of Google and quickly turned up two pages with helpful information.

The first was Johannes C. Hellmuth’s [“Posting Rmarkdowns to your Jekyll website
”](https://jchellmuth.com/news/jekyll/website/code/2020/01/04/Rmarkdown-posts-to-Jekyll.html).  It showed me what to add to the YAML header:

```
---
layout: post
title: title
author: author
date: YYYY-MM-DD
output:
  md_document:
    variant: markdown_github
    preserve_yaml: true
---
```
The ‘variant’ value gave me a post with different styling than my Jekyll instance, unfortunately.

Then Steven V. Miller’s [“Two Helpful R Markdown/Jekyll Tips for an Easier Blogging Experience”](http://svmiller.com/blog/2019/08/two-helpful-rmarkdown-jekyll-tips/) showed me how to fix that style issue.  It also showed me how to integrate knitting with my local Jekyll site’s organization.

Miller recommended using ‘gfm’ (Github-flavored markdown) for the ‘variant’ value.  When I made this change, my posts looked exactly the way they should.

Miller showed ways to set knitr options so images produced by R would be written in a place the Jekyll looks for images.

```
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
knitr::opts_knit$set(base.dir = 	"/Users/userename/Documents/GitHub/userename.github.io/", base.url = "/")
knitr::opts_chunk$set(fig.path = "assets/images/subdirectory-for-post/")
```
```

I'm planning to make a different iamge subdirectory each time I used Rmarkdown for a Jekyll post.  This way I don't need to worry about naming conventions and accidentally overwriting images I created from previous Rmarkdown posts.



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
