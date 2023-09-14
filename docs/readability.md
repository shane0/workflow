# readability

- I use a combination of readability tools
- lexi
- markdown linters
- eli5
- active voice
- present tense
- avoid jargon
- when jargon is unavoidable I use mkdocs abbreviations

## jargon

- mkdocs has a site wide glossary
- example: hover the mouse over: DUKKHA
- to use it just add your jargon in ALLCAPS
- add the jargon to: `includes/abbreviations.md`

## lexi

- example: <https://github.com/shane0/workflow/pull/3>
- add this permission in your reposettings for the lexi action to work
- repo > settings > actions > general > change `Workflow permissions` to read/write
- add this file `.github/workflows/readability.yml`

```yaml
-8<- ".github/workflows/readability.yml"
```
