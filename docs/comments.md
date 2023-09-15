# comments

- scroll down to see the comments, has voting & reactionn
- very useful for leaving quicknotes if you are not at are not at your laptop

## installation

- this is much simpler than in the documentation
- <https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/>
- repo: general > settings > features
- configure the giscus app
- <https://giscus.app/>
- use their snippet with defaults: `pathname` & category `general`
- add it to `overrides/partials/comments.html`
- in `mkdocs.yml` add overrides here

```yml
theme:
  name: material
  custom_dir: overrides
  icon:
```
