# workflow

## three amigos

- the three amigos are from business dev & test
- map it out

![g](images/map.png)

- good to go

![g](images/good_example.png)

- slice up the story
![g](images/slice_story.png)
- someone is missing or not answering questions
![g](images/someone_missing.png)
- finish the story
![g](images/unfinished_story.png)

## mermaid template

```mermaid
graph TD
story --> rule
rule --> example_1
rule --> example_2
question --> question_1
question --> question_2
style question fill:#e74c3c
style question_1 fill:#e74c3c
style question_2 fill:#e74c3c
style story fill:#f1c40f
style rule fill: #2e86c1
style example_1 fill: #28b463
style example_2 fill: #28b463
```

### running tests

- run your test

```sh
behave
```

- Rule docs: <https://cucumber.io/docs/gherkin/reference/?sbsearch=Rule#rule>
- <https://behave.readthedocs.io/en/latest/>
- this folder was deployed using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)
- to update this template use the `rule/` folder at <https://github.com/shane0/workflow>
- see docs/workflow.md in docs/
- or use the local mkdocs server <https://squidfunk.github.io/mkdocs-material/>
- start the server
- it runs at <http://127.0.0.1:3000/>

```sh
mkdocs serve
```
