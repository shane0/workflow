---
tags:
  - cookiecutter 
---
# cookiecutter

- [cookiecutter](https://github.com/cookiecutter/cookiecutter) is a folder template
- this repo is a cookiecutter
- it is so simple it is stupid that everyone has overlooked this
- I believe this spawned from the django web framework app spawn command

## `cookiecutter.json`

- here is the `cookiecutter.json` file that deploys this project

```json
-8<- "cookiecutter.json"
```

- these values provide variables with defaults
- they also become a command line prompt during deployment to override the defaults
- beyond this, these values can be used in folder & file names
- and inside files
- the format to reuse these variables

```json
{{ cookiecutter.<variable name> }}
```

- your project can contain anything you want
- multiple languages
- pre and post hooks are included to run commands before or after folder deployment

## cookiecutter command

- you can also list your installed templates `cookiecutter -l` among other options

```sh
Usage: cookiecutter [OPTIONS] [TEMPLATE] [EXTRA_CONTEXT]...

  Create a project from a Cookiecutter project template (TEMPLATE).

  Cookiecutter is free and open source software, developed and managed by
  volunteers. If you would like to help out or fund the project, please get in
  touch at https://github.com/cookiecutter/cookiecutter.

Options:
  -V, --version                Show the version and exit.
  --no-input                   Do not prompt for parameters and only use
                               cookiecutter.json file content
  -c, --checkout TEXT          branch, tag or commit to checkout after git
                               clone
  --directory TEXT             Directory within repo that holds
                               cookiecutter.json file for advanced
                               repositories with multi templates in it
  -v, --verbose                Print debug information
  --replay                     Do not prompt for parameters and only use
                               information entered previously
  --replay-file PATH           Use this file for replay instead of the
                               default.
  -f, --overwrite-if-exists    Overwrite the contents of the output directory
                               if it already exists
  -s, --skip-if-file-exists    Skip the files in the corresponding directories
                               if they already exist
  -o, --output-dir PATH        Where to output the generated project dir into
  --config-file PATH           User configuration file
  --default-config             Do not load a config file. Use the defaults
                               instead
  --debug-file PATH            File to be used as a stream for DEBUG logging
  --accept-hooks [yes|ask|no]  Accept pre/post hooks
  -l, --list-installed         List currently installed templates.
  -h, --help                   Show this message and exit.
```

## using a local folder without git

- this repository has a `template/` folder
- you do not have to learn git or use a git repository to use cookiecutte
- it contains a bare minimum cookiecutter template
- this is how you can run cookiecutter locally

```sh
cookiecutter template/
# then it prompts you
proj_name [project name]: example
variable_a [variable a]: abc
variable_b [variable b]: def
release_date [2023-10-05]: 
version [0.1.0]: 
```

## empty template

- there is a bare minimum cookiecutter template in `templat/`
- you can reuse it in your project or deploy it by itself

```sh
cookiecutter https://github.com/shane0/workflow --directory template/
```
