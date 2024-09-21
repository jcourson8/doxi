Title: UnoCSS - SolidDocs

URL Source: https://docs.solidjs.com/guides/styling-components/uno

Markdown Content:
UnoCSS - SolidDocs
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

Styling your Components

UnoCSS
======

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/uno.mdx)

[UnoCSS](https://unocss.dev/) is an on-demand utility CSS library that integrates seamlessly with Solid as a Vite plugin.

* * *

[Install Vite plugin](https://docs.solidjs.com/guides/styling-components/uno#install-vite-plugin)
-------------------------------------------------------------------------------------------------

To get started with UnoCSS in your Solid app:

* * *

[Import Vite plugin](https://docs.solidjs.com/guides/styling-components/uno#import-vite-plugin)
-----------------------------------------------------------------------------------------------

After installation, open your `vite.config.js` or `vite.config.ts`. The default Solid Vite configuration looks like this:

```
import { defineConfig } from "vite";import solidPlugin from "vite-plugin-solid";
export default defineConfig({  plugins: [solidPlugin()],  server: {    port: 3000,  },  build: {    target: "esnext",  },});
```

Now, import `unocssPlugin` from "unocss/vite" and add it to the plugins array:

```
import { defineConfig } from "vite";import unocssPlugin from "unocss/vite";import solidPlugin from "vite-plugin-solid";
export default defineConfig({  plugins: [unocssPlugin(), solidPlugin()],  server: {    port: 3000,  },  build: {    target: "esnext",  },});
```

Ensure that `unocssPlugin` is ordered before `solidPlugin` to prevent certain edge cases.

* * *

[Import UnoCSS](https://docs.solidjs.com/guides/styling-components/uno#import-unocss)
-------------------------------------------------------------------------------------

In your root `index.jsx` or `index.tsx` file, import UnoCSS:

```
/* @refresh reload */import "uno.css"import { render } from "solid-js/web"import "./index.css"import App from "./App"
render(() => <App />, document.getElementById('root') as HTMLElement);
```

Alternatively, you can use the alias `import "virtual:uno.css"`:

```
/* @refresh reload */import "virtual:uno.css"import { render } from "solid-js/web"import "./index.css"import App from "./App"
render(() => <App />, document.getElementById('root') as HTMLElement);
```

#### [Support](https://docs.solidjs.com/guides/styling-components/uno#support)

For additional assistance, refer to the [UnoCSS/Vite integration guide](https://unocss.dev/integrations/vite) .

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/uno.mdx)

Previous[← TailwindCSS](https://docs.solidjs.com/guides/styling-components/tailwind)

Next[State management →](https://docs.solidjs.com/guides/state-management)

On this page

1.  [Overview](https://docs.solidjs.com/guides/styling-components/uno#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/uno.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/uno.mdx)
