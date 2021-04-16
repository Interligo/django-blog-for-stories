# My blog for stories and Django learning

![Python 3.8](https://img.shields.io/badge/Python-v3.8-blue) ![Django 3.1](https://img.shields.io/badge/Django-v3.1-red) ![DRF 3.12](https://img.shields.io/badge/DRF-v3.12-yellow)

![Tests](https://img.shields.io/badge/Tests-30/30-green)

[Tap me to go on the site](http://interligo.pythonanywhere.com/ "Blog's URL")

### Site structure and my goals:
I am self-educating to became a real programmer, so some of my decisions may seem strange. I am open to any advices or criticism (but please don't beat me hard) and I'll try to explain it.
* Site structure:
    * All site's elements are divided into groups (apps, templates and tests). And that groups are divided into smaller pieces by apps' names. So, if you want to find some template, for example, you just need to go to "templates" folder. Perhaps it is an old approach in website creation, but I think, that such a system is quite logical and harmonious.
    * I like inheritance in OOP, so often I use extends in HTML templates.
    * There is a sticky navigation bar on the top of my site. I love it: it's so simple and convenient.
    * A bit about my Django apps:
        * The stories include comments pagination because I wanted to try it.
        * The book has a navigation panel (to navigate between the chapters). Do you remember that I already have sticky panel? The book's chapter can be so big that I need to have another sticky panel. I made it, but I think, that there will be some problems with displaying. 
* Database: sqlite. I don't expect many visitors or comments, which I should save to db. If it is necessary I will change db to PostgreSQL or MySQL.
* There is no users registration, because I really don't need it. Visitors can leave comments under each story without registration and they are able to contact me easily. If they want to get an answer from me, there is an opportunity to leave an email address.

### Django REST Framework API:
You can get stories' list by API and after that get the full information about each story. There are a lot of functionalities like adding, changing and deleting stories by API, but they are all only for admins (lol, only for me).
For example:

`https://interligo.pythonanywhere.com/api/v1/stories/` - to get information about all stories
`https://interligo.pythonanywhere.com/api/v1/stories/{story_id}/` - to changing story data by ID
`https://interligo.pythonanywhere.com/api/v1/stories/add/` - to add new story

### The nearest plans for improving the site:
1. Adaptive layout of the site. Oh, no... Here we go again (hate to move forms).
1. API documentation, like a big boy site.
1. JS scripts (or just Vue) to make my site fashionable. But firstly I need to learn JS :(
1. MORE TESTS FOR THE TEST GOD!
