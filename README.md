Repository for source files for my personal [blog](https://clegaard.github.io) currently hosted on GitHub pages.

**🚨The blog is work in progress and mostly used by me to toy around with static site generators and GitHub pages🚨**

# Building the documentation
The documentation is build using [Zola](https://github.com/getzola/zola) which is distributed as a single binary, found under the *releases* of the repository.

To download the binary:
``` bash
curl -L https://github.com/getzola/zola/releases/download/v0.16.1/zola-v0.16.1-x86_64-unknown-linux-gnu.tar.gz | tar -xzv
```
For convenience the binary can be moved to a folder that is in the system's path.
The documentation can be served on localhost using:
``` bash
./zola serve
```
