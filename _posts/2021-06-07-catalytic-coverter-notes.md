---
title: State of the LC, 6 June 2021 --  CA Smog Test
author: Jason
layout: post
date: 2021-06-07
tags: land-cruiser
---

A few weeks ago, CA sent the letter that said it's time to get the LC smog tested.  The last time this happened, the LC failed the test and I brought it to my local auto shop to see if they had any tricks that would help it pass.  They 'cleaned' the catalytic converter with some sort of fluid.  Cost me about $200.  At the time, I thought it was worth it.

Worried that this smog test would set me back an extra $200, again, I decided to do some homework.  My Check Engine light was on, and my ScanGuage II showed a PO430 code:  catalytic converter.  "Don't bother testing your truck," the smog guy said.  "If it has a code, I can't test it.  You'll just end up giving me money for nothing."

"If I reset the code, how long before it's ready to be tested again," I asked.

"Fifty to a hundred miles."

I cleared the codes with my ScanGauge II, zeroed my tripometer, and crossed my fingers that the LC would give me a little window of grace between the computer being ready for a test and throwing that PO430 code, again.

The diagnostic code P0420 means [Catalyst System Efficiency Below Threshold (Bank 1)](https://parts.olathetoyota.com/p0420-code-toyota), which indicates something is amiss in the driver side catalytic converter system.  (The code P0430 is the analogous Bank 2, or passenger side, error.)  This system includes [two oxygen sensors](https://partsouq.com/en/catalog/genuine/unit?c=Toyota&ssd=%24%2AKwHE8OH3qba7mceBvaPwypyIqK-xwM_Cw9HP_Y3VhNPM1arQg4Pe1M3EjIiCmZbv2p-VnpTTzMPc0MnI2dTN0snCx8HQg4PUmNXK087DxMufmfzUio6Hn5OwiY3IydTN0qe_udLejcjO1M3Su6KyuKaflPfCw8LBwMTFypmDkdSUk9PM1cfLnpWIxtXc05uU0siN9Oe8xsDButq3vO7k9rfV3NOQnpTQlZPAAAAAACD1RTY%24&vid=0&cid=&uid=349504&q=JTEHT05J442063586), one upstream of the catalytic converter and one downstream.  The catalyst system operated by comparing the readings from the two oxygen sensors.  If everything is working correctly and if the readings are too similar, then the catalytic converter isn't working right.

Reading the 100 series forums on [ih8mud](https://forum.ih8mud.com/search/3562667/?q=P0430&o=date), I learned that

* catalytic converters in LCs are tough and unlikely to fail,
* the upstream oxygen sensor takes a beating and is likely the first point of failure in the catalyst system, and
* there could be a leak around the oxygen sensor fitting that could be repaired by a new [gasket](https://partsouq.com/en/search/all?q=8946620020).

If my error code came back, I was going to try a few things before bringing my LC to the shop:

1. swap upstream and downstream O2 sensors[^1] on the passenger side system to see if the error code persisted, and
2. check the fittings on the O2 sensors to make sure there's no leak, and
3. swap O2 sensors with those on the driver's side to see if the code changes.

I also wondered if there's a way to clean an O2 sensor to improve its performance.  Fortunately, I wasn't able to do any of these because before my tripometer hit 50 miles my ScanGauge II said my LC was 'ready' for its smog test.  All the system tests had run after my reset and no codes were thrown!

Instead of rolling up my sleeves to address a PO430 code, I'm sitting down to write up these troubleshooting thoughts for 2023 when CA sends me the next notice that I need a smog test.

[^1]: According to partsouq, the upstream and downstream sensors have different part numbers (8946560150 and 8946569175, respectively) and are priced differently.  This might mean they can't be swapped within a bank, though it appears they could be swapped between banks.

