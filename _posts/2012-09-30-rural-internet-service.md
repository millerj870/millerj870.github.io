---
author: jason
date: 2012-09-30 00:00:00+00:00
layout: post
title: Coaxing Internet Service from a Rural Provider
tags: local
---

A few days ago, I had a deeply moving experience with my ISP that taught me something about tech support, speed tests, and customer star ratings.

My family lives and works in rural Missouri, and about five years ago we chose to live in a slightly more rural location.  (Just 10 miles from a county seat.)  Securing internet service has been a challenge.

When we lived in  town, we had access to broadband internet through the local cable provider.  Our current home is too far from the nearest 'hub' or 'thingamagig' for cable to provide anything or ATT to provide DSL.  For a while we subscribed to the outlandishly expensive [Wild Blue satellite internet][] service.  The satellite signal speed was slow and varied with weather, and it certainly wasn't worth the $100 per month that we were paying for it.

A few years ago our ISP, [Mark Twain Telecommunications][], began to offer wireless internet.  It was cheaper, faster, and less susceptible to weather.  Very quickly, we chalked up the hardware cost of satellite service to 'sunk costs', and bought in to wireless.

Since internet service was mainly a luxury for us, we opted for a low level of service.  Web pages loaded slowly, but we could check email, and bills were less.  This served us well for several years.

This year, feeling the pinch of increased costs and stagnant wages, we decided that some costs need to go.  The luxury of satellite, commercial television was first in line to the guillotine while Netflix waiting in the wings to take its place.  Netflix streaming requires reliable internet download speeds, so we jacked up our service level to 3 Mbps down and 0.5 Mbps up and tested Netflix for a month.<!-- more -->Frustrating.  We tested Netflix by watching 'The Killing', season 1, and we sat through buffer-filling-pauses and audio-video sync problems.  The show was great, but Netflix didn't provide an enjoyable viewing experience.

Meanwhile, I was using [speedtest.net][speedtest] to test our ISP's performance.  This is the service that their tech support people always have me use when I call to complain about low service levels.  By creating a speedtest account, I could collect testing data and look for patterns that might let me understand the limitations of our ISP.  As long as I conducted the tests in load-neutral  settings [^load-neutral], I felt I could use the data to help me communicate concerns (or praise) to the Mark Twain techs.

As Ph.D. mathematician who teaches at an undergraduate University, I like to think that I've learned a lot about internet technology as I've waded into the shallows of linux, open source software, scripting, and web technologies.  So I cringe when a tech support specialist asks me what version of Windows I'm using (I'm an OS X person) or asks me to reboot my system to fix a problem.  And when a tech support specialist steers clear of using technical terms when talking to me about solving technical problems, I feel the urge to go a little bugfuck with them.  Usually, I can hold back on that.  Sometimes, I don't.

As I was testing our broadband speeds, I kept getting many tests with slow or very slow speeds.  Some speeds would be so slow that the test would fail.[^failtest]  Down in the left bottom corner, I saw that speedtest.net allowed me to rate my ISP.  Disappointed in my service, and disappointed in their professionalism, I gave Mark Twain one star.

You can see in the following plots of download speeds why I would do so.   In each plot, a horizontal red dotted line represents the 80% service level (of 2.4 Mbps) that Mark Twain wants to provide.  The first plot shows that download speed do vary by day, and they second shows that they vary by hour.  The crappiest hours for service are the post-school and post-work hours that a typical family might want to watch television.[^Rnote]

![Boxplot Downloadbydays V2](http://www.thecoldfish.com/wp-content/uploads/2012/09/boxplot-downloadbydays-v2.png)

![Boxplot Downloadbyhours V2](http://www.thecoldfish.com/wp-content/uploads/2012/09/boxplot-downloadbyhours-v2.png)

After seeing these numbers, my partner and I decided that our ISP wasn't performing to their promised 80% service level.  So I took time late one night to call tech support to talk with them about it.  The guy I talked with was great!  He respected my comments and perspective on the ISP's performance, he appreciated my desire to use Netflix, and seemed to know what he was talking about.[^heknew]  He elevated our support request and said that a technician would contact us in one or two business days.

Within 48 hours, a couple techs showed up to look at our setup.  I wasn't there, but my partner's story describe a thorough and thoughtful analysis of our situation.  They ended up replacing out antenna with a WiMax antenna, which they felt would eliminate an interference that could have been caused by our Apple wireless router.

Remarkably, they claimed to be installing this antenna at a $600 cost to the ISP without confirming that interference was causing our problem.  That was nice of them.

Then, just as the techs were getting in their truck to leave, the lead turned to my partner and said something like, "We noticed that you had given us a low rating online.  We use those ratings when we apply for grants, and we hope that you can reconsider that rating."  With that, they drove off.

## Things that make you go, hmmmm ##

This is where I raise my eyebrow.  I rated my ISP on a third party web site.  At what point does that rating get communicated back to the ISP, and how do they identify that rating with me and my partner?  (On speedtest.net, I identified myself through an email address that's I didn't share with my ISP.)

Did my rating give me better telephone tech service?  Did it make the on-site techs treat us better?  Did it contribute to their installation of a new $600 antenna?

I don't know the answer to any of this.

But I've increased my ISP's rating from one star to three.  When I get a chance to collect more data on the download speeds they provide, I'd be happy to increase that rating to four stars.

Check back here for an update, if you're interested.


[Wild Blue satellite internet]: http://internet.satelliteinternet.me/wild-blue/?gclid=CO7u3eKA3rICFdEWMgodFAYA3A
[Mark Twain Telecommunications]: http://portal.marktwain.net/corporate/index.php?cat_id=9e011d3e6bf99747ed352759d522c20d
[speedtest]: http://speedtest.net
[r]: http://www.r-project.org


[^load-neutral]:  When I tested, I had Dropbox syncing turned off on all my machines.  I made sure nobody was watching Netflix.  I also had my test machine plugged directly into my home network (as opposed to the wireless network).  It's true that  a tech support person asked me over the phone to plug directly into my antenna modem, I would say 'done' when I'd actually left my machine plugged directly into my home router.  

[^failtest]:  When a [speedtest.net][speedtest] fails, no records are written to the test record.  This means that a user's test records are a liberal representation of the service levels they receive.

[^heknew]:  My desktop was plugged into my home router, but I'd told the tech that it was plugged into the antenna.  At one point, the tech asked me for my computer's IP by going to the Network settings.  I told him what I saw.  (And I immediately knew that the IP was not the ISP's IP, it was my router's IP.)  He then asked me to to a speed test to that IP (i.e., to my router) and then a speed test to the ISP.  The former was negligibly fast, and the latter was terribly slow.  He never said anything, but I knew that the tech new I wasn't connected directly to the antenna, but I also knew (and appreciated) that the tech saw the antenna as the source of the sub-par connectivity performance.

[^Rnote]:  These boxplots were created from the test records using the open source statistical environment called [R][r].  I'm happy to share the scripts with those who ask.
