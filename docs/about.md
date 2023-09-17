# about

- cut through the bs
- evetually I'll make a screencast of how to use this 

## layout

```text
├── docs <-- mkdocs
├── includes <-- snippets & gloassary (mkdocs in the browser)
├── plugins < command line automations
└── todocli <-- task management files (works in command line and can be viewed in mkdocs)
```

??? example

    ```sh
    tree -d -L 1
    ```

## options

- these are not installed by default

```text
more click plugins
docs readability measurement locally or remote on push and pull requests (lexi)
markdownlint in editor, command line or remote pipelines
github integrations for repos, actions and pages
local or remote tests (includes examples in cucumber, python & js)
more aliases and shell scripts
```

!!! info

        - a no nonsense workflow centered on the power of simplicity & ease of maintanence
        - using parts from:
        - git
        - linux standards
        - [data science template](https://github.com/patrickmineault/true-neutral-cookiecutter)
        - [readme (docs first) driven development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
        - [behavior (tests first) sdriven](https://cucumber.io/docs/cucumber/)
        - [gitlab style guide](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fdevelopment%2Fdocumentation%2Ftopic_types%2F)
        - <https://www.writethedocs.org>

!!! example

        - project templates: [cookiecutter](https://github.com/cookiecutter/cookiecutter)
        - task tracking: [todocli](https://github.com/francoischalifour/todo-cli)
        - modular command line automation: [click](https://click.palletsprojects.com/en/8.1.x/)
        - powerful documentaiton: [mkdocs](https://squidfunk.github.io/mkdocs-material/)
        - measurable readability: [lexi](https://github.com/Rebilly/lexi)
