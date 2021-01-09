---
title: Putting MP4 Video in a Post
author: jason
tags: jekyll
date: 2021-01-09
layout: post
---

Today, I was writing a post documenting the coup attempt on January 6th, and I wanted to include a video of the crowd chanting, 'Hang Mike Pence!'.  I found a video on Twitter, downloaded it, and put it in the post like this:

```md
![](/assets/media/coup-hang-mike-pence.mp4)
```

The pages rendered OK with the video starting automatically.  But there was not sound and there were no video controls.  _No bueno._

I did a quick Google search.  Found [this](https://github.com/mmistakes/minimal-mistakes/discussions/101).  Did this

```html
<video width="480" height="320" controls="controls">
  <source src="/assets/media/coup-hang-mike-pence.mp4" type="video/mp4">
</video>
```

and it worked like a charm.  So much for the elegance of markdown.