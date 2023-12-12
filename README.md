# Wedding
Static Jekyll site for my and B's wedding.

## Development Environment

![](/docs/dev-containers-arch.png)

Prerequisites:
- `ms-vscode-remote.remote-containers` to run the site inside of a container.
- Docker Desktop to run the container.

The `.devcontainer` folder contains the necessary configuration files.

Once the configuration files are correct, run the project using the **Reopen in Container** command from the command palette.

### Tips

Port forwarding seems to happen automatically once the Jekyll web server is running.

## Create a New Site

Only run this command once, to create a brand new website.
```sh
# creates a boilerplate site in the /website directory
# notably the Gemfile is created which itself contains good documentation
jekyll new website
```

When creating new containers, run this command each time. It cannot (easily) be part of the Dockerfile because the dev containers extension hasn't yet created the bind mount to the code repo, so the Gemfile doesn't exist in the container yet.
```sh
cd website
bundle install
# this warning can be safely ignored, because no other users are in the container
# Don't run Bundler as root. Installing your bundle as root will break this application for all non-root users on this machine.
```

Run this command to start the server. Do ctrl-c then rerun to see changes.
```sh
bundle exec jekyll serve
```

## Develop and Update the Site

Make sure changes are committed to git, then use the **Clone Repository in Container Volume** command. This will ensure a high-performance file system that auto-detects when files are changed.

*This is critical to ensure the Jekyll dev site automatically reflects changes made to source files.* The auto-update functionality does **not** work when opening the repo with a bind mount.

```sh
# build and install the site you've created
cd website
bundle install
bundle exec jekyll serve
```

The site should now be available at http://127.0.0.1:4000/

Any changes made to files should immediately be reflected after refreshing the browser.

### Image Link Previews in VS Code

The VS Code markdown previewer doesn't work, because the images on Jekyll posts need to be specified relative to the root of the Jekyll site directory (`/website`)

In other words, for a file located at `/website/assets/images/sample.png`, the correct image link syntax would be:
- Jekyll: `![alt text](/assets/images/sample.png)`
- VS Code `![alt text](/website/assets/images/sample.png)`
