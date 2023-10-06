# {{ cookiecutter.proj_name }}

- example
- this example was ran from this workflow repo 
- you can use -o to specify a different folder name than the project name

```sh
cookiecutter template/
# then it prompts you
proj_name [project name]: example
variable_a [variable a]: abc
variable_b [variable b]: def
release_date [2023-10-05]: 
version [0.1.0]: 
```

## variables

- {{ cookiecutter.variable_a }}
- {{ cookiecutter.variable_b }}

- {{ cookiecutter.release_date }}
