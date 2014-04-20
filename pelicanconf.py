#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Omphalosskeptic'
SITENAME = u'Science Class'
SITE_TITLE = 'The Free & Open Science Class'
SITESUBTITLE = 'Science for Smart-Alecs'
SITEURL = 'http://scienceclass.github.io'
META_DESCRIPTION = 'Science Class aims to stimulate and inform bright people like you by providing resources on how to build all kinds of fun, no-nonsense science projects.'

FEED_DOMAIN = SITEURL

PDF_GENERATOR = True

USE_CLEAN_SUBTHEME = True

SITELOGO = SITEURL+'/images/scienceclass.png'

PATH  = 'content'

MENUITEMS = (('⌂ Home', '/'),('⚛ Projects', '/category/projects.html'),('✑ Thoughts', '/category/thoughts.html'),('☏ Contact', '/pages/contact.html'),)

DEFAULT_CATEGORY = 'Projects'

USE_FOLDER_AS_CATEGORY = True

THEME = 'bohemian'

PAGE_DIR = 'pages'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_RSS = 'rss.xml'
# FEED_ALL_RSS = 'rss.xml'

# Blogroll
# LINKS =  (('Algebrarules.com', 'http://algebrarules.com/'),
        #   ('Automathic.org', 'http://automathic.org/'),
        #   ('Science Class RSS', 'http://scienceclass.github.io/rss.xml'),
        #  ('Github', 'http://github.com/omphalosskeptic'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)
          
GITHUB_URL = 'http://github.com/omphalosskeptic/scienceclass'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
