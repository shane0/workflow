# comments

- <https://giscus.app/>
- <https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/>

To add GitHub Discussions to mkdocs-material, you can use the Giscus integration. Giscus is a comment system that uses GitHub Discussions as a backend.

To use Giscus, you need to:

1. Install the Giscus GitHub App and grant access to the repository that should host comments as GitHub discussions. Note that this can be a repository different from your documentation.
2. Add the following code to your mkdocs.yml file:

```
extra:
  comments:
    giscus:
      repo: <your-repo-name>
      repo_id: <your-repo-id>
```

3. Build your documentation and deploy it to a web server.

Once you have done this, you will be able to see a Giscus comment box on every page of your documentation. Visitors can use this comment box to post comments and replies.

Here is an example of a mkdocs.yml file that uses the Giscus integration:

```
site_name: My Documentation

theme:
  name: material

extra:
  comments:
    giscus:
      repo: my-documentation
      repo_id: 123456789
```

This will add a Giscus comment box to every page of your documentation, using the `my-documentation` repository on GitHub.

Here are some additional things to keep in mind:

- You can customize the appearance of the Giscus comment box by adding CSS to your documentation.
- You can also enable or disable the Giscus comment box on specific pages by adding the following code to the front matter of those pages:

```
---
comments: false
---
```

This will disable the Giscus comment box on the current page.
