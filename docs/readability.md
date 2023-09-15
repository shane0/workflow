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
- local action

### lexi from command line

```sh
yarn run:local:report ./test-data/old ./test-data/new
```

- action

```yaml
-8<- ".github/workflows/readability.yml"
```

```sh
yarn run v1.22.19
$ tsx ./src/cli/report.ts ./test-data/old ./test-data/new

**Overall readability score:** 0 (🟢 +0)

File | Readability
--- | ---
[new.md](https://github.com/repo-name/blob/commit-sha/new.md "new.md") | 0 (-)


<details>
  <summary>View detailed metrics</summary>

🟢 - Shows an _increase_ in readability
🔴 - Shows a _decrease_ in readability

File | Readability | FRE | GF | ARI | CLI | DCRS
--- | --- | --- | --- | --- | --- | ---
[new.md](https://github.com/repo-name/blob/commit-sha/new.md "new.md") | 0 | 0 | 19 | 22 | 19 | 11
&nbsp; | - | - | - | - | - | -


Averages:

&nbsp; | Readability | FRE | GF | ARI | CLI | DCRS
--- | --- | --- | --- | --- | --- | ---
Average | 0 | 0 | 19 | 22 | 19 | 11
&nbsp; | 🟢 +0 | 🟢 +0 | 🟢 +0 | 🟢 +0 | 🟢 +0 | 🟢 +0


<details>
  <summary>View metric targets</summary>

Metric | Range | Ideal score
--- | --- | ---
Flesch Reading Ease | 100 (very easy read) to 0 (extremely difficult read) | 60
Gunning Fog | 6 (very easy read) to 17 (extremely difficult read) | 8 or less
Auto. Read. Index | 6 (very easy read) to 14 (extremely difficult read) | 8 or less
Coleman Liau Index | 6 (very easy read) to 17 (extremely difficult read) | 8 or less
Dale-Chall Readability | 4.9 (very easy read) to 9.9 (extremely difficult read) | 6.9 or less

</details>

</details>

Done in 0.74s.
```
