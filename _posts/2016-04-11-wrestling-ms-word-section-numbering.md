---
author: jason
date: 2016-04-11 22:50:42+00:00
layout: post
title: 'Wrestling MS Word:  Section Numbering'
tags: writing
---

If I want to typset a slick looking (and working) document with internal references, my preference is to use the LaTeX system. But there aren’t many people at a University that use that system. Most people use Microsoft Word. So I’m often forced touse MS Word, too.

As I’ve used it, I’ve learned some tricks to automate my documents into looking nicer. Most of those tricks involve customizing styles. One trick is to number section heading, sub-headings, and sub-sub-heading. But each time I use that trick, I need to re-figure it out. So, for my future self, I’m positing the reference that always seems to do the trick.<!-- more -->

The blog post that dpes the trick is this one: [How to Use Multilevel Numbered Headings in Word 2007](https://wordknowhow.wordpress.com/2013/01/30/how-to-use-multilevel-numbered-headings-in-the-word/). Notes that MS Word for OS X functions much like Word 2007.

The ideas is that you want to start by making a custom numbering scheme. On the ribbon, select the `Home' tab, and in the`Paragraph`tab, select the`Multilevel List` button.

![The Multilevel List button](/assets/images/1multilevellistbutton.png)

The Multilevel List button

Select `Define New Multilevel List`. In the dialog that opens, you format the way your list will look (via the `Indent at` field, _etc._), and link the `level` in the list to the styles you are using. In my case, it’s always the `Heading` styles.

Note the “reveal” button in the bottom left corner that allows you to access the `Link level` functions and the ‘Legal style numbering’ bit. By default, this material is not revealed.

![The Customization Dialog Box](/assets/images/2customize.png)

The Customization Dialog Box

After configuring how your levels work, click `OK` and you should be all set. The last step is modifying the Heading styles to use your customized multilevel list. That’s easy.

**Note:** Do not mess with the numbers in the first field under the “Number format” section of this customizing dialog box. What these mean, how they work, and how to use them is oblique and unfathomable. If you screw up by modifying these numbers, I’d advise starting over and making a new custom multilevel list.
