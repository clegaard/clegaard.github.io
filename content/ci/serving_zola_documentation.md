+++
title = "Serving Zola documentation on GitHub pages"
date = 2022-10-05
+++

GitHub pages provides free hosting of static pages which is useful for building documentation and blogs like what you a currently reading.
A nice feature of this approach is that it integrates well with GitHubs actions, allowing documentation to be rebuild in response to source code changes and more.

This guide describes how to set up GitHub to serve content built by [Zola](https://github.com/getzola/zola).
The process is similar for other static site generators.

# Create a GitHub Pages repo

Create a new repo named `${username}.github.io`, where $username is replaced with your GitHub username.
For instance the documentation you are reading corresponds to `clegaard.github.io`.

# Clone repository and initialize Zola

Install instructions for Zola can be found [here](https://www.getzola.org/documentation/getting-started/installation/).
If you don't have a package manager Zola installed, is single self contained binary which can be found under the [releases](https://github.com/getzola/zola/releases) of the Zola repository. 

Clone the repository 
``` bash
git clone ${username}.github.io 
```
Initialize the Zola in the repo:
``` bash
cd ${username}.github.io && zola init
```
Finally test that everything is working by serving the documentation on localhost
```
zola serve
```

# Configure source of documentation.

By default GitHub pages will serve documentation from markdown files located in the root of the repository.
This can be changed by going to `Settings -> Pages -> Source` and set this to GitHub Actions.

![github pages repo settings](../github_pages_build_and_deploy.png)

# Add workflow to build and publish documentation




# README.md
https://stackoverflow.com/questions/48919200/github-pages-only-showing-readme-file



https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
https://github.com/orgs/community/discussions/30113