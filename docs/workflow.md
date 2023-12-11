# workflow

- later if you return to a project you should be able to read this page and understand where you left off on your project
- what the purpose of this folder is to begin with
- what file you were creating or updating
- where it is at on your computer or the cloud etc.
- this page is optional if you are on a simple task or project just use [todo](todo.md)
- sometimes you end up in your own or someone's elses mess

```mermaid
graph TD
workflow --> deployment
deployment --> apps
apps -- simple command line task management --> todocli
apps -- tiny command line automation --> aliases
apps -- larger command line automation --> click
```

- this template includes a few pages that are optional
- [tasks](todo.md)
- [project folders](projects.md)
- [click automations](click.md)

```text
index.md

# optional
todo.md
projects.md
workflow.md

# automations
click.md
utils/bash_aliases
```
