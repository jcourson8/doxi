Title: Zerops - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/zerops

Markdown Content:
[Zerops](https://zerops.io/) is a dev-first cloud platform that can be used to deploy both Static and SSR Solid Node.js Apps.

For additional one-to-one support, details, and features, you can join the [Zerops Discord server](https://discord.gg/xxzmJSDKPT) and [visit the Zerops Docs](https://docs.zerops.io/).

Deploy and test Zerops Solid recipes with one click:

*   [Deploy Solid Node.js & Static Together](https://app.zerops.io/recipe/solidjs) - [Node.js](https://github.com/zeropsio/recipe-solidjs-nodejs) and [Static](https://github.com/zeropsio/recipe-solidjs-static).
*   [Deploy Solid Node.js](https://app.zerops.io/recipe/solidjs-nodejs) - [Source Repository](https://github.com/zeropsio/recipe-solidjs-nodejs)
*   [Deploy Solid Static](https://app.zerops.io/recipe/solidjs-static) - [Source Repository](https://github.com/zeropsio/recipe-solidjs-static)

* * *

1.  Go to [Zerops Registration](https://app.zerops.io/registration) and sign up using GitHub, GitLab, or just your email.

* * *

There are two ways to set up a Zerops project and a service:

#### [Using Project Add Wizard (GUI)](https://docs.solidjs.com/guides/deployment-options/zerops#using-project-add-wizard-gui)

1.  Go to your [Zerops dashboard](https://app.zerops.io/dashboard/projects).
2.  Add a new project using your sidebar. If you're in compact mode, click on your profile and then "Add new project."
3.  You'll be redirected to a page where you can choose a service.

##### [For Static:](https://docs.solidjs.com/guides/deployment-options/zerops#for-static)

1.  Choose Static.
2.  Scroll down and change the hostname to your preference.
3.  Scroll down and click on the "Add New Static" button.

##### [For SSR - Node.js:](https://docs.solidjs.com/guides/deployment-options/zerops#for-ssr---nodejs)

1.  Choose `Node.js` and select `version 20`.
2.  Scroll down and change the hostname to your preference.
3.  Scroll down and click on the "Add New Node.js" button.

#### [Using Project Import YAML](https://docs.solidjs.com/guides/deployment-options/zerops#using-project-import-yaml)

**Note**: This is only used for project creation using YAML on the web interface—no need to add it to the project.

1.  Go to your [Zerops dashboard](https://app.zerops.io/dashboard/projects) and click on your profile icon if you are a new user. If not, check your sidebar and click on `Import Project`.

##### [Static:](https://docs.solidjs.com/guides/deployment-options/zerops#static)

```
project:  name: recipe-solidjsservices:  - hostname: app    type: static    enableSubdomainAccess: true
```

##### [SSR - Node.js:](https://docs.solidjs.com/guides/deployment-options/zerops#ssr---nodejs)

```
project:  name: recipe-solidjsservices:  - hostname: app    type: nodejs@20    enableSubdomainAccess: true
```

* * *

The `zerops.yml` configuration file is used to tell Zerops how to build and run your application, it should be placed to the root of your appplication's repository.

Example for **SSR (Server-Side Rendering)** Apps:

Set up the `zerops.yml` file in the root of your SSR project. Make sure the setup parameter's value is the same as the hostname of the service.

```
zerops:  - setup: app    build:      base: nodejs@latest      buildCommands:        - pnpm i        - pnpm build      deployFiles:        - .output        - node_modules        - public        - package.json    run:      base: nodejs@latest      ports:        - port: 3000          httpSupport: true      start: pnpm start
```

Example for **SSG (Static Site Generation)** Apps:

Set up the `zerops.yml` file in the root of your SSG project. Make sure the setup parameter's value is the same as the hostname of the service.

```
zerops:  - setup: app    build:      base: nodejs@latest      buildCommands:        - pnpm i        - pnpm build      deployFiles:        - dist/~    run:      base: static
```

Push the changes to your GitHub/GitLab repository (necessary if you are planning to use GitHub/GitLab).

* * *

### [Triggering the pipeline automatically by connecting Github/Gitlab repository](https://docs.solidjs.com/guides/deployment-options/zerops#triggering-the-pipeline-automatically-by-connecting-githubgitlab-repository)

You can push your project by [Triggering the pipeline using Zerops CLI](https://docs.solidjs.com/guides/deployment-options/zerops#triggering-the-pipeline-using-githubgitlab) or by connecting the app service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

### [Triggering the pipeline manually using Zerops CLI](https://docs.solidjs.com/guides/deployment-options/zerops#triggering-the-pipeline-manually-using-zerops-cli)

To download the zCLI binary directly, use [zCLI/releases](https://github.com/zeropsio/zcli/releases) or:

1.  Install the Zerops CLI using Terminal.

Linux/MacOS

```
curl -L https://zerops.io/zcli/install.sh | sh
```

Windows

```
irm https://zerops.io/zcli/install.ps1 | iex
```

Npm

2.  Open Settings \> [Access Token Management](https://app.zerops.io/settings/token-management) in the Zerops app and generate a new access token.
3.  Log in using your access token with the following command:

4.  Navigate to the root of your app (where zerops.yml is located) and run the following command in Terminal to trigger the deploy:

Check the official docs if you need more advanced use-cases for [Zerops Docs](http://docs.zerops.io/).