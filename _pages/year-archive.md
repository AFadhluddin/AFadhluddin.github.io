---
title: Writing archive
permalink: /posts/
description: Earlier writing by Ahmed Fadhluddin.
---
<ul class="archive-list">
{% for post in site.posts %}
  {% assign body = post.content | strip_html | strip %}
  {% if body != '' %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%-d %B %Y' }}</time></li>
  {% endif %}
{% endfor %}
</ul>
