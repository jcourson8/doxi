Title: Firebase - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/firebase

Markdown Content:
Firebase - SolidDocs
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

Firebase
========

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/firebase.mdx)

[Firebase](https://firebase.google.com/) is an all-in-one app development platform by Google, offering a range of services from real-time databases to user authentication. For a detailed overview of the services available, you can visit [Firebase's documentation](https://firebase.google.com/docs).

Before proceeding, make sure you've already set up a project in your Firebase console. If you haven't, you can follow [Firebase's official guide](https://firebase.google.com/docs/projects/learn-more#creating-cloud-projects) to create a new Firebase project.

* * *

[Using the Firebase CLI Tool](https://docs.solidjs.com/guides/deployment-options/firebase#using-the-firebase-cli-tool)
----------------------------------------------------------------------------------------------------------------------

1.  Use your preferred package manager to install the Firebase command-line tool with one of the following commands:

npmyarnpnpmbun

```
npm i -g firebase-tools
```

```
yarn global add firebase-tools
```

```
pnpm add -g firebase-tools
```

```
bun add -g firebase-tools
```

2.  Execute the `firebase login` command to ensure that you're logged into the Firebase account associated with your project.
    
3.  In the root directory of your Solid project, create two new files: `firebase.json` and `.firebaserc`.
    

*   In `firebase.json`, add the following code:

```
{  "hosting": {    "public": "dist",    "ignore": []  }}
```

*   In `.firebaserc`, insert the following code (replace `<YOUR_FIREBASE_PROJECT_ID>` with your Firebase project ID):

```
{  "projects": {    "default": "<YOUR_FIREBASE_PROJECT_ID>"  }}
```

4.  Run `npm run build` , followed by `firebase deploy` to build and deploy your project.

Upon completion, a `Hosting URL` will be displayed, indicating the live deployment of your project.

[![Image 1](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=YncoDoKDPPVyet1EOrsa_w&type=embed) ![Image 2: Open in Eraser](https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&token=968381c8-a7e7-472a-8ed6-4a6626da5501)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=YncoDoKDPPVyet1EOrsa_w&)

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/firebase.mdx)

Previous[← Cloudflare](https://docs.solidjs.com/guides/deployment-options/cloudflare)

Next[Netlify →](https://docs.solidjs.com/guides/deployment-options/netlify)

On this page

1.  [Overview](https://docs.solidjs.com/guides/deployment-options/firebase#_top)
2.  [Using the Firebase CLI Tool](https://docs.solidjs.com/guides/deployment-options/firebase#using-the-firebase-cli-tool)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/firebase.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/firebase.mdx)
