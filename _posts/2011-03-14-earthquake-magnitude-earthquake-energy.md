---
author: jason
date: 2011-03-14 05:57:00+00:00
layout: post
title: Earthquake Magnitude & Earthquake Energy
tags: weather nature mathematics
---

Japan's terrifying earthquake, tsunami, and nuclear disasters have the world watching, talking, and thinking hopeful thoughts for people in that island nation.  Yesterday, I listened as a seismologist talked to an NPR radio host about the magnitude of the Sendai earthquake, which has now been upgraded to a 9.0 magnitude earthquake.

The seismologist said that Japan is no stranger to earthquakes, and has put considerable effort into quake-proofing their infrastructure.  But their preparations have targeted magnitude 7.0 quakes.  Nobody would have predicted a quake as large as the Sendai quake happening in Japan.  "It was almost 1000 times more powerful than a 7.0 magnitude quake," he said.

This confused me.

Earthquake magnitude is measured on the Richter scale, a base-10 logarithmic scale.  This means that two quakes whose Richter measurement differ by _k_ differ by a factor of 10_k_ in magnitude.  How can two quakes that differ by two on the Richter scale differ by a factor of 1000=10^3 in power?

I asked a physicist friend of mine, and said he didn't really know the details of the Richter scale, so he couldn't explain the apparent discrepancy.

The answer was only a little internet sleuthing away.  The discrepancy is no discrepancy at all:  magnitude and energy are two different ideas, after all.

## Earthquake magnitude

The Richter scale measures magnitude relative to a 'base' quake, one that can be felt 100km away with an amplitude of 1mm.  (Amplitude must refer to the amplitude of a wave recorded by a seismograph, but I'm not sure.)  Such a quake is assigned a magnitude of 3.0[^1]

The Sendai quake had a 9.0 magnitude.  It was 100 larger than the 7.0 magnitude quakes that are said to be common in Japan.

## Earthquake Energy

The energy radiated through the earth by an earthquake can be estimated from the magnitude of the quake.  Let M<sub>s</sub> be the seismic magnitude of the earthquake measured on the Richter scale.  The Richter formula relates M<sub>s</sub> to the seismic energy of the earthquake, E<sub>s</sub>, as follows

log(E<sub>s</sub>) = 4.8 + 1.5*M<sub>s</sub>

Thus

E<sub>s</sub> = 104.8*101.5*M<sub>s</sub>

which shows that an increase in one on the Richter scale corresponds to an energy that is increased by a factor of 101.5 [^2]

So, the seismologist was right when he said that the Sendai earthquake was _101.5*2=103=1000_ times more powerful than the typical 7.0 quake.

### More:  Derivation (almost)

Research always raises more questions than it answers, and now I wanted to know where the Richter formula, above, came from.

The energy computation require summing (or integrating) the energy flux of an earthquake over all the wave frequencies that it can generate.  The original estimate of that summation was

log(E<sub>s</sub>) = 5.24 + 1.44 M<sub>s</sub>.  

This starts to answer the questions about the origin of the Richter formula.

* * *

  [^1]: [The Richter Scale: Measuring Earthquake Magnitude](http://mathcentral.uregina.ca/beyond/articles/earthquakes/richter.html)

  [^2]: [US Geological Service:  How much energy is released in an earthquake?](https://www.usgs.gov/natural-hazards/earthquake-hazards/science/earthquake-magnitude-energy-release-and-shaking-intensity?qt-science_center_objects=0#qt-science_center_objects)




