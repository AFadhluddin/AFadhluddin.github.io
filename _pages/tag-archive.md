---
title: Posts by tag
permalink: /tags/
---
{% for tag in site.tags %}
<h2 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h2>
<ul class="archive-list">
{% for post in tag[1] %}
{% assign body = post.content | strip_html | strip %}{% if body != '' %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endif %}{% endfor %}
</ul>
{% endfor %}
