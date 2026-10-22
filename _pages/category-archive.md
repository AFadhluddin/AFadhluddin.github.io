---
title: Posts by category
permalink: /categories/
---
{% for category in site.categories %}
<h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2>
<ul class="archive-list">
{% for post in category[1] %}
{% assign body = post.content | strip_html | strip %}{% if body != '' %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endif %}{% endfor %}
</ul>
{% endfor %}
