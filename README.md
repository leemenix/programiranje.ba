# Podesavanje permalink-a
```
_config.yml - permalink: [pretty,none]
```

# Build with Docker
sudo docker run --rm -v $PWD:/srv/jekyll -it -p 4000:4000 jekyll/jekyll jekyll serve --watch
sudo docker run --rm -v $PWD:/srv/jekyll -it -p 4000:4000 --env JEKYLL_ENV=production jekyll/jekyll jekyll build --destination programiranje.ba

https://www.iconfinder.com/search/?q=python&from=navbar&price=free

# Debug Jekyll
<pre>
    site: {{ site.collections | jsonify | escape }}
    page: {{ page | jsonify | escape }}
    layout: {{ layout | jsonify | escape }}
    content: {{ content | jsonify | escape }}
    paginator: {{ paginator | jsonify | escape }}
</pre>

# Jekyll useful tips & tricks
export JEKYLL_VERSION=3.8
sudo docker run --rm -v $PWD:/srv/jekyll -it -p 4000:4000 jekyll/jekyll:$JEKYLL_VERSION jekyll serve
sudo docker run -v $PWD:/srv/jekyll -it -p 4000:4000 --env JEKYLL_ENV=production jekyll/jekyll:$JEKYLL_VERSION jekyll build --destination programiranje.ba

# Creative Theme for Jekyll

A Jekyll implementation of the [Creative Theme](http://startbootstrap.com/template-overviews/creative/) template by [Start Bootstrap](http://startbootstrap.com).

Creative is a one page Bootstrap theme for creatives, small businesses, and other multipurpose uses.
The theme includes a number of rich features and plugins that you can use as a great boilerplate for your next Jekyll project! 

See it live in action at <https://volny.github.io/creative-theme-jekyll/>

## To use the Creative Theme template in your project

- Start by adding your info in `_config.yml`
- In `_layouts/front.html` reorder or remove section as you prefer.

