#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH='content'

# Basic site info
AUTHOR = u'Daniel Zappala'
BIO = u'I serve on the City Council for Cedar Hills, Utah. Please comment below and share this post. We want to hear from residents on issues concerning the city. Email me at dzappala@cedarhills.org'
TAGLINE = u'City Council'
SITENAME = u'Cedar Hills Blog'
SITEURL = 'http://cedarhillsblog.org'

# Contact info
EMAIL = 'dzappala@cedarhills.org'
FACEBOOK_URL = 'https://www.facebook.com/daniel.zappala'

PHONE = '801-362-3704'

LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

# Tage cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# How to save pages
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'index.html'

# Templates
DIRECT_TEMPLATES = ('index', 'tags', 'archives')

# Feeds
FEED_DOMAIN = SITEURL
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'

# Misc
STATIC_PATHS = ['images','docs']
DEFAULT_PAGINATION = 10

# Theme
USER_LOGO_URL = "/images/zappala.jpg"
THEME = "themes/pelican-blog"

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['assets','neighbors', 'summary']

# Comments
DISQUS_SITENAME	= 'cedarhillsblog'

# For development only
RELATIVE_URLS = True
