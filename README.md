# Cedar Hills blog

This is a blog I keep while I am on the city council of Cedar Hills, UT.
You can find it at [cedarhillsblog.org](http://cedarhillsblog.org)

The pages are built using:

- [Pelican](http://docs.getpelican.com/en/3.3.0/)
- [Pelican Sparrow](https://github.com/zappala/pelican-sparrow)
- [Fabric](http://docs.fabfile.org/en/1.8/)

## Setup

First, create a virtual environment for pelican:

```
sudo pip install virtualenv
virtualenv ~/virtualenv/pelican
source ~/virtualenv/pelican/bin/activate
```

Then, install the required packages:

```
pip install -r requirements.txt
```

## Use

Use

```
fabric build
```

to build the web pages. Alternatively, use

```
fab regenerate
```

to automatically regenerate the pages when they are changed. To
serve the pages, use

```
fab serve
```

To publish, use

```
fab publish
```

## Copyright

Copyright (c) 2014 Daniel Zappala

Released under the <a
href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative
Commons Attribution-ShareAlike 3.0 Unported License</a>.
