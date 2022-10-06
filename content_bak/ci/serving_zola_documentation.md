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

![repo name](../repo.png)

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

By default the commmand will serve content to 127.0.0.1:1111, accessing the url in your browser should show an empty page similar to
![zola localhost](../zola_localhost.png)

# Configure source of documentation.

By default GitHub pages will serve documentation from markdown files located in the root of the repository.
This can be changed by going to `Settings -> Pages -> Source` and set this to GitHub Actions.

![github pages repo settings](../github_pages_build_and_deploy.png)

# Add workflow to build and publish documentation

Next we need to define the step required to convert the markdown files into html, css, and javascript files that can be served by GitHub pages.
Using GitHub actions this boils down to the following steps:
1. Checkout repo
2. Install Zola
3. Run zola build
4. Publish the files using the `actions/deploy-pages@v1` action

Add a new file named `build_and_deploy.yml` to `.gihub/workflows` with the following content

``` yml
name: Build and deploy Zola documentation
on:
  workflow_dispatch:
  push:
    branches: main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          submodules: recursive
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v2
      - name: Install zola
        run: curl -L https://github.com/getzola/zola/releases/download/v0.16.1/zola-v0.16.1-x86_64-unknown-linux-gnu.tar.gz | tar -xzv
      - name: Build with zola
        run: ./zola build --base-url "${{ steps.pages.outputs.base_path }}" --output-dir ./_site
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

Finally add the new file to Git and commit the changes
``` bash
git add . && git commit -m "add workflow" && git push
```

Pushing the file to the repo should trigger the workflow

![GitHub Action](../github_action_trigger.png)

After the action has finished you can access the content on `${username}.github.io`. For now the content wi

# Installing a theme

https://www.getzola.org/themes/

# Adding a to README.md
https://stackoverflow.com/questions/48919200/github-pages-only-showing-readme-file



https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
https://github.com/orgs/community/discussions/30113