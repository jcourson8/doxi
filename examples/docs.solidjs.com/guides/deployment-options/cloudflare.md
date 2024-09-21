Title: Cloudflare - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/cloudflare

Markdown Content:
Cloudflare - SolidDocs
===============

These docs are currently in Beta! [Share your feedback with us!](https://shr.link/pna6n)

[**Solid**](https://docs.solidjs.com/)

*   [Core](https://docs.solidjs.com/)
*   [Router](https://docs.solidjs.com/solid-router)
*   [SolidStart](https://docs.solidjs.com/solid-start)
*   [Meta](https://docs.solidjs.com/solid-meta)

Search⌘K[](https://github.com/solidjs/solid)[](https://discord.com/invite/solidjs)

LearnReference

*   [Quick start](https://docs.solidjs.com/quick-start)
*   Concepts
    *   [Intro to reactivity](https://docs.solidjs.com/concepts/intro-to-reactivity)
    *   [Understanding JSX](https://docs.solidjs.com/concepts/understanding-jsx)
    *   Components
        
        *   [Basics](https://docs.solidjs.com/concepts/components/basics)
        *   [Class and style](https://docs.solidjs.com/concepts/components/class-style)
        *   [Event handlers](https://docs.solidjs.com/concepts/components/event-handlers)
        *   [Props](https://docs.solidjs.com/concepts/components/props)
        
    *   [Signals](https://docs.solidjs.com/concepts/signals)
    *   Control Flow
        
        *   [Conditional rendering](https://docs.solidjs.com/concepts/control-flow/conditional-rendering)
        *   [Dynamic](https://docs.solidjs.com/concepts/control-flow/dynamic)
        *   [List rendering](https://docs.solidjs.com/concepts/control-flow/list-rendering)
        *   [Portal](https://docs.solidjs.com/concepts/control-flow/portal)
        *   [Error boundary](https://docs.solidjs.com/concepts/control-flow/error-boundary)
        
    *   [Effects](https://docs.solidjs.com/concepts/effects)
    *   Derived Values
        
        *   [Derived signals](https://docs.solidjs.com/concepts/derived-values/derived-signals)
        *   [Memos](https://docs.solidjs.com/concepts/derived-values/memos)
        
    *   [Context](https://docs.solidjs.com/concepts/context)
    *   [Stores](https://docs.solidjs.com/concepts/stores)
    *   [Refs](https://docs.solidjs.com/concepts/refs)
*   Advanced Concepts
    *   [Fine-grained reactivity](https://docs.solidjs.com/advanced-concepts/fine-grained-reactivity)
*   Guides
    *   [Styling your components](https://docs.solidjs.com/guides/styling-your-components)
    *   [State management](https://docs.solidjs.com/guides/state-management)
    *   [Routing & navigation](https://docs.solidjs.com/guides/routing-and-navigation)
    *   [Complex state management](https://docs.solidjs.com/guides/complex-state-management)
    *   [Fetching data](https://docs.solidjs.com/guides/fetching-data)
    *   [Testing](https://docs.solidjs.com/guides/testing)
    *   [Deploy your app](https://docs.solidjs.com/guides/deploying-your-app)
*   Configuration
    *   [Environment variables](https://docs.solidjs.com/configuration/environment-variables)
    *   [TypeScript](https://docs.solidjs.com/configuration/typescript)

Deploying your App

Cloudflare
==========

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/cloudflare.mdx)

[Cloudflare Pages](https://pages.cloudflare.com/) is a JAMstack platform for frontend developers, where JAMstack stands for JavaScript, APIs, and Markup. For additional details and features, you can [visit the Cloudflare website](https://pages.cloudflare.com/).

* * *

[Using the Cloudflare's web interface](https://docs.solidjs.com/guides/deployment-options/cloudflare#using-the-cloudflares-web-interface)
-----------------------------------------------------------------------------------------------------------------------------------------

1.  Navigate to the [Cloudflare login page](https://dash.cloudflare.com/login) and log in or sign up.

[View on Eraser![Image 1](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=UE1AFe5oESDQkepKNaMxtA&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=UE1AFe5oESDQkepKNaMxtA)

2.  After logging in, find "Pages" in the left-hand navigation bar. Add a new project by clicking "Create a project," then choose "Connect to Git."

[View on Eraser![Image 2](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=XcbVyX2a69kSAP1m1220Ug&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=XcbVyX2a69kSAP1m1220Ug)

3.  You'll have the option to install Cloudflare Pages on all your repositories or select ones. Choose the repository that contains your Solid project.

[View on Eraser![Image 3](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=SsbGUghc_Vwlvxefe1xAFg&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=SsbGUghc_Vwlvxefe1xAFg)

4.  Configure your build settings:

*   The project name will default to the repository name, but you can change it if you wish.
*   In the "build command" field, enter `npm run build` .
*   For the "build output directory" field, use `dist` .
*   Add an environment variable `NODE_VERSION` and set its value to the version of Node.js you're using.

**Note:** This step is crucial because Cloudflare Pages uses a version of Node.js older than v13, which may not fully support Vite, the bundler used in Solid projects.

[View on Eraser![Image 4](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=1HpIQUkxqNl9j3JlXIUvTg&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=1HpIQUkxqNl9j3JlXIUvTg)

5.  Once you've configured the settings, click "Save and Deploy." In a few minutes, your Solid project will be live on Cloudflare Pages, accessible via a URL formatted as `project_name.pages.dev`.

* * *

[Using the Wrangler CLI](https://docs.solidjs.com/guides/deployment-options/cloudflare#using-the-wrangler-cli)
--------------------------------------------------------------------------------------------------------------

Wrangler is a command-line tool for building Cloudflare Workers. Here are the steps to deploy your Solid project using Wrangler.

1.  Use your package manager of choice to install the Wrangler command-line tool:

2.  Open your terminal and run the following command to log in:

```
wrangler login
```

3.  Execute the following commands to build your project and deploy it using Wrangler:

After running these commands, your project should be live. While the terminal may provide a link, it's more reliable to check your Cloudflare Pages dashboard for the deployed URL, which usually follows the format `project-name.pages.dev`.

**Note:** Make sure to navigate to the `Speed` -\> `Optimization settings` section in your Cloudflare website dashboard and disable the `Auto Minify` option. This is important as minification and comment removal can interfere with hydration.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/cloudflare.mdx)

Previous[← AWS via Flightcontrol](https://docs.solidjs.com/guides/deployment-options/aws-via-flightcontrol)

Next[Firebase →](https://docs.solidjs.com/guides/deployment-options/firebase)

On this page

1.  [Overview](https://docs.solidjs.com/guides/deployment-options/cloudflare#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/cloudflare.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/cloudflare.mdx)
