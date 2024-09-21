Title: LESS - SolidDocs

URL Source: https://docs.solidjs.com/guides/styling-components/less

Markdown Content:
LESS - SolidDocs
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

LESS
====

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/less.mdx)

[LESS](https://lesscss.org/) is a preprocessor based on JavaScript. It provides the ability to use mixins, variables, and other programmatic tools, making styling code cleaner and less redundant.

* * *

[Installation](https://docs.solidjs.com/guides/styling-components/less#installation)
------------------------------------------------------------------------------------

To utilize LESS in a Solid app, it will need to be installed as a development dependency:

* * *

[Using LESS in your app](https://docs.solidjs.com/guides/styling-components/less#using-less-in-your-app)
--------------------------------------------------------------------------------------------------------

Start by creating a `.less` file in the `src` directory:

styles.less

```
.foo {  color: red;}.bar {  background-color: blue;}
```

The basic syntax of LESS is very similar to CSS. However, LESS allows the declaration and usage of variables:

styles.less

```
@plainred: red;@plainblue: blue;.foo {  color: @plainred;}.bar {  background-color: @plainblue;}
```

To use these styles in a Solid component, import the `.less` file:

component.jsx

```
import "./styles.less";
function Component() {  return (    <>      <div class="foo bar">Hello, world!</div>    </>  );}
```

By changing the file extension of the imported styles to `.less`, Vite will recognize it as a LESS file and compile it to CSS on demand.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/less.mdx)

Previous[← SASS](https://docs.solidjs.com/guides/styling-components/sass)

Next[CSS modules →](https://docs.solidjs.com/guides/styling-components/css-modules)

On this page

1.  [Overview](https://docs.solidjs.com/guides/styling-components/less#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/less.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/less.mdx)
