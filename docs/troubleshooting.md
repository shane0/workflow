---
tags:
  - troubleshooting 
---
# troubleshooting template

- [gitlab troubleshooting topic](https://docs.gitlab.com/ee/development/documentation/topic_types/troubleshooting.html)

````markdown
## Troubleshooting

When working with <x feature>, you might encounter the following issues.

### The message or a description of it

You might get an error that states <error message>.

This issue occurs when...

The workaround is...

## Error: `unexpected disconnect while reading sideband packet`

Unstable networking conditions can cause Gitaly to fail when trying to fetch large repository
data from the primary site. Those conditions can result in this error:

```plaintext
curl 18 transfer closed with outstanding read data remaining & fetch-pack:
unexpected disconnect while reading sideband packet
```

To resolve this issue...

````
