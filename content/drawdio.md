Title: Drawdio: The $1 Musical Pencil
Tags: Project, Electronics, Circuit, Stub
Category: Electronics
Coverimg: http://scienceclass.github.io/images/drawdio/coverimage.png
Author: Omphalosskeptic
Summary: <strong>Build a pencil that draws music!</strong> The Drawdio is a simple musical synthesizer that uses the conductive properties of pencil graphite to create different sounds.

<span class="grayscale"> 
	![The Drawdio In Use](http://scienceclass.github.io/images/drawdio/1-use-crop.png)
</span>

The Drawdio is a simple musical synthesizer that uses the conductive properties of pencil graphite to create different sounds. It was designed by [Jay Silver](http://web.media.mit.edu/~silver/drawdio/) and makes use of the famous 555 timer integrated circuit. 

It is now a [popular beginner electronics kit](http://www.makershed.com/product_p/mkad12.htm). The kit costs $19 — however, the circuit was released under the Creative Commons license, and the plans are freely available: Why not build one from scratch?

<span class="grayscale"> 
	![The Circuit](http://scienceclass.github.io/images/drawdio/2-circuit-crop.png)
</span>

I built the one in the photos in under an hour, and because I salvaged everything other than the 555 Timer chip and the transistor, it cost less than a dollar.

### Building it

For many science and electronics projects, the resources I find on the web are unclear or incomplete. The Drawdio is an exception to this, as there are quite adequate instructions already available online; a full build tutorial is therefor unnecessary, and I will just point you to the resources that I used.

I built the prototype from Make Projects’ excellent tutorial video:

<span class="grayscale">
<iframe width="560" height="315" src="//www.youtube.com/embed/P4-Wl0W1004" frameborder="0" allowfullscreen></iframe>
</span>

Other useful information about the Drawdio can be found on [Jay Silver’s Site](http://web.media.mit.edu/~silver/drawdio/), and the [Make: Projects](http://makezine.com/projects/drawdio-musical-pencil/) site.

### My Modifications

All the tutorials I ran across called for the low-power [CMOS](http://en.wikipedia.org/wiki/Cmos) chip [TCL555](http://en.wikipedia.org/wiki/555_timer#Derivatives), and I only had the original 5V 555s on hand, so I substituted it and used 5V instead of 3V. Here is the finished product:

<span class="grayscale"> 
	![The Finished Product](http://scienceclass.github.io/images/drawdio/4-done-crop.png)
</span>

<span class="grayscale"> 
	![In use](http://scienceclass.github.io/images/drawdio/5-use-crop.png)
</span>

### Schematic

<span class="grayscale"> 
	![Drawdio Schematic](http://scienceclass.github.io/images/drawdio/6-schematic-crop-fixed.png)
</span>

Here is a (slapdash) schematic for the circuit. It uses the original 5v 555 chip, and also corrects a mistake I found in Make’s schematic, which had the battery symbol backwards!

