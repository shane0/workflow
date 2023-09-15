# workflow template

[deploy this template](deploy.md){ .md-button } [update this template](update.md){ .md-button }

## layout

```text
├── docs <-- mkdocs
├── includes <-- snippets & gloassary (mkdocs in the browser)
├── plugins < command line automations
└── todocli <-- task management files (works in command line and can be viewed in mkdocs)
```

- options not installed by default

```text
more click plugins
docs readability measurement locally or remote on push and pull requests (lexi)
markdownlint in editor, command line or remote pipelines
github integrations for repos, actions and pages
local or remote tests (includes examples in cucumber, python & js)
more aliases and shell scripts
```

- update layout with:

```sh
tree -d -L 1
```

[TAGS]
