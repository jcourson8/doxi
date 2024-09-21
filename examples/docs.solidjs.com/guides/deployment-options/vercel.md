Title: Vercel - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/vercel

Markdown Content:
Vercel - SolidDocs
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

Vercel
======

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/vercel.mdx)

[Vercel](https://vercel.com/) is a widely-used platform specialized in hosting frontend projects. For detailed information regarding build and deployment instructions, as well as features they offer, please visit the [Vercel documentation](https://vercel.com/docs).

* * *

[Using Vercel web interface](https://docs.solidjs.com/guides/deployment-options/vercel#using-vercel-web-interface)
------------------------------------------------------------------------------------------------------------------

1.  Navigate to [vercel.com/login](https://vercel.com/login) to log in or create a new account. Connect with your preferred Git repository hosting service.

[View on Eraser![Image 1](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=0mwBl275l6WC3YD5Uz_IcQ&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=0mwBl275l6WC3YD5Uz_IcQ)

2.  Once on the dashboard, click the button at the top right corner and choose "Add New Project." On the next page, select "Continue with GitHub" or your preferred Git service.

[View on Eraser![Image 2](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=QhW5b3iEbwyWzJ5fhUDrZw&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=QhW5b3iEbwyWzJ5fhUDrZw)

3.  You will then see with a list of your repositories. Use the search bar if needed to find the specific repository you want to deploy. Click the "Import" button to proceed.
    
4.  After importing your Solid project repository, you will be taken to a configuration screen. If your project requires any environment variables, add them in the designated field. Click "Deploy" to start the deployment process.
    

[View on Eraser![Image 3](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=_OhHyCQRVxMqXdCkkTE3nw&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=_OhHyCQRVxMqXdCkkTE3nw)

5.  Once the build and deployment are finished, you will be redirected to a screen that displays a screenshot of your live site.

[View on Eraser![Image 4](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe/preview?elements=hAbTtvs_2l4xDqySVYsiVA&type=embed)](https://app.eraser.io/workspace/w9y9PNVjwSqDCEPNTEoe?elements=hAbTtvs_2l4xDqySVYsiVA)

* * *

[Using the Vercel CLI](https://docs.solidjs.com/guides/deployment-options/vercel#using-the-vercel-cli)
------------------------------------------------------------------------------------------------------

1.  Install the Vercel CLI using your preferred package manager.

2.  Open your terminal, navigate to your project directory, and run the following command to log in:

```
vercel
```

3.  Follow the on-screen instructions from the CLI to finalize the deployment. Once completed, your project will be live on Vercel and accessible via the provided URL.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/vercel.mdx)

Previous[← Railway](https://docs.solidjs.com/guides/deployment-options/railway)

Next[Stormkit →](https://docs.solidjs.com/guides/deployment-options/stormkit)

On this page

1.  [Overview](https://docs.solidjs.com/guides/deployment-options/vercel#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/vercel.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/vercel.mdx)
