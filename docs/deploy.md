---
tags:
  - cookiecutter 
  - deployments 
---
# deployment

- after deployment you can add more options found here
- <https://github.com/shane0/workflow>  

## screencast

## deploying the first time

- on a new machine
- install [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- deploy this cookiecutter the first time[^1]

```sh
cookiecutter https://github.com/shane0/workflow
```

## deploying seubsequently

- after you have used it once you can just use it by name

```sh
cookiecutter workflow 
```

## empty cookiecutter template

```sh
cookiecutter https://github.com/shane0/workflow --directory template/
```

## recent deployments

- 2023-09-17: [buddhism mkdocs](https://shane0.github.io/buddhism/){ .md-button }
  - added some docs here for the optional mkdocs github deployment
- 2023-09-19: [cheatsheets and snippets](https://shane0.github.io/cheatsheets/){ .md-button }

[^1]: note: by default cookiecutter  saves a copy of this template in  `~/.cookiecutters/workflow/` the first time you use
