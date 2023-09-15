---
tags:
  - alias 
  - click 
---
# alias shortcuts

- apps in this template have aliases documented on their mkdoc page
- click commands I add typically call an alias so they click is optional 

## alias workflow

- this seems obvious I'm surprised it's not included in .bashrc from day 1
- ea: edit alias file
- sa: updates aliases (sa = source alias)

```sh
-8<- "bash_aliases:4:7"
```

- when editing aliases use: <https://www.shellcheck.net/>

## julian date

```sh
alias day='date +%D && date +%j && date +%A && date +%d && date +%u'
alias fday='mkdir "$(date +%j)" && cd "$(date +%j)"'
alias mday='vim ./"$(date +%j)".md'
alias fj='vim ./"$(date +%F)".md'
alias week='date +%V'
alias month='date +%B && date +%m'
alias year='date +%Y'
```
