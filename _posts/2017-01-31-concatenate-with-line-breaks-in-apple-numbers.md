---
author: jason
layout: post
date: 2017-01-31 21:35:23+00:00
title: Concatenate with Line Breaks in Apple Numbers
tags: coding spreadsheet
---

If you want to concatenate two elements in a Numbers spreadsheet and include a line break between them, use `CHAR(8232)`` to represent the line break.  For example, putting a line break between the contents of cell A1 and B1 would look like

```
=A1 & CHAR(8232) & B1
```

If you were in Microsoft Excel on a Mac, the analogous command would be `CHAR(13);` on a PC it would be `CHAR(10)`.
