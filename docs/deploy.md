---
tags:
  - cookiecutter 
  - deployments 
---
# deployment

- not all files are included
- find more options here: <https://github.com/shane0/workflow>  

## recent deployments

- 2023-09-17: [buddhism mkdocs](https://shane0.github.io/buddhism/){ .md-button }
  - added some docs here for the optional mkdocs github deployment
- 2023-09-19: [cheatsheets and snippets](https://shane0.github.io/cheatsheets/){ .md-button }

## first time

- on a new machine

- install [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- deploy this cookiecutter the first time[^1]

```sh
cookiecutter  https://shane0.github.io/workflow/  
```

## after that

- just use the name

```sh
cookiecutter workflow 
```

[^1]: note: by default cookiecutter  saves a copy of this template in  `~/.cookiecutters/workflow/` the first time you use
