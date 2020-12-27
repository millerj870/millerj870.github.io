---
author: jason
date: 2010-03-24 15:44:00+00:00
layout: post
title: Progress on ePUB mathematical documents
tags: mathematics writing ebook
---

For months, I've been casting about for tools that will allow me to create mathematical eBook documents in the ePUB format. I chose that format because it's open, supported by the major readers (e.g., Kindle, Nook, iPad software), and can be authored in a way that's very similar to authoring HTML documents. 

Here are a couple articles that demystify the ePUB format and show how it is related to HTML: 

* <a href="http://bit.ly/aCpouk">ePub demystified – Tomorrow’s e-book reader the web browser?</a> 

* <a href="http://bit.ly/aLydzB">epub eBooks Tutorial</a> 

Since I've been hand-coding HTML documents since 1993, making an ePUB eBook looks easy. There's a problem, however. Math in HTML sucks. It's been a significant challenge to the mathematical community to put mathematics on the web in a standard way that renders well in all browsers (see <a href="http://www.w3.org/Math/">http://www.w3.org/Math/</a>, looks like we're close to a standard?). 

For this reason, many people have suggested to me that ePUB is not an ideal format for eBooks that require a significant of technical typesetting. Well, this is what's required by mathematical and scientific writing. The equations, graphs, diagrams, and so forth are technical. <a href="http://en.wikipedia.org/wiki/LaTeX">LaTeX</a>, the document preparation system created by Leslie Lamport to lay on top of the TeX typsetting system of Knuth, is the system most mathematicians like me use to typeset high-quality mathematical manuscripts. (It's output is so professional, many people use LaTeX instead of a word processor for even less technical products.) LaTeX's default output is a DVI file which is device (platform) independent, but LaTeX can easily output PDF, another very portable document format. Many people have suggested that I just create eBooks using PDF. But components of PDF files do not scale for a device's display in the same way that ePUB files will, so PDF eBook are not as reader-friendly as ePUBs should be. This is why I've been working hard to find a way to author mathematical content for ePUB. 

Honestly, my ultimate goal is to figure out how to author rich media mathematics documents in ePUB. To have mathematical biology modules published to ePUB that can be used and interacted with through an iPad-like device might be fun and useful to teachers and students across the country. <p /> So, I've been poking about the interwebs looking for a tool to prepare mathematics for ePUB publication. I've used Google and posted questions to various forums. I've posed questions to my network in Twitter and to FriendFeed. Nobody seems to want to talk about this. It's almost as if publishing companies are trying to keep their workflow and tools locked up to keep some competitive advantage in the preparation of content rich media. But maybe I'm just being too suspicious. <p /> So it was with great joy today that I ran across <a href="http://www.cse.ohio-state.edu/~gurari/TeX4ht/">TeX4ht</a>, a LaTeX to HTML conversion program. It was with greater joy that I discovered it to be installed on my OS X laptop. Now I can finally explore authoring mathematical eBooks in ePUB format. I'll share what I learn here.
