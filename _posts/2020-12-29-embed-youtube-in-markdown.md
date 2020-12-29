---
title: Embed YouTube clip in Markdown
author: Jason
date: 2020-12-29
layout: post
tags: coding markdown jekyll tool
---

Wanting to share on this site a video of a malfunction on my rig, I learned that they don't embed like inline images.

Searching for instructions on how to do this, I found this tool.

[convert Youtube url to GitHub comment](http://embedyoutube.org)

It creates 'iterated' markdown that looks like this.

```markdown
[![](http://img.youtube.com/vi/G_QPG6clT_o/0.jpg)](http://www.youtube.com/watch?v=G_QPG6clT_o "LC100 relay")
```

which genericized looks like

```markdown
[![](thumbnail-URL)](video-URL)
```


It's like an inline link that starts with an inline (static) image.  That image is the thumbnail  you create (in YouTube) for your video.  Once you creadt that, the above command 'just works'.