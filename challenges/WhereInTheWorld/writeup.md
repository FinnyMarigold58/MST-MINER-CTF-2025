---
layout: post
title: "Where In The World"
date: 2025-10-10
---

# Where In The World
**CTF:** MST Miner 2025
**Challenge Description:**

```md
Last week Joe Miner misplaced his phone. Today he received a picture this text:

"Sorry! I think I grabbed your phone by accident! This is a rather roundabout way of returning it, but I can get it back to you if you meet me here."

The flag for this week's challenges is the name of the street in the center of the photo (not the top left).
Flag format=flag{location_name} 
```

## First Steps

Opening the image in google's reverse image search and inputting the file, many articles appeared talking about Place Charles de Gaulle in Paris, France.

I had thought I needed the exact road in the top left (Av. Mac-Mahon), but after going to submit and rereading the flag format paragraph, I realized I only needed the center road, which I wasn't even sure was a road.

Making the challenge flag: `flag{PI. Charles de Gaulle}`