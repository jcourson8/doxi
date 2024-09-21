Title: Error boundary - SolidDocs

URL Source: https://docs.solidjs.com/concepts/control-flow/error-boundary

Markdown Content:
Error boundary - SolidDocs
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

Control Flow

Error boundary
==============

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/control-flow/error-boundary.mdx)

`<ErrorBoundary>` is a component that can be used to catch errors thrown by child components. When encountering an error, this component will render a fallback UI instead of the problematic child component(s).

```
import { ErrorBoundary } from "solid-js";
<ErrorBoundary fallback={(err) => <div>Error: {err.message}</div>}>  <ProblematicComponent /></ErrorBoundary>
```

`<ErrorBoundary>` accepts a `fallback` prop that can be used to render a custom error message, or to provide a friendly notification to the user. This prop accepts a function that receives the caught error as an argument, providing a flexible way to handle different error scenarios.

[View on Eraser![Image 1](https://app.eraser.io/workspace/maDvFw5OryuPJOwSLyK9/preview?elements=aSw5yYrSY22mI_YqoZlpGQ&type=embed)](https://app.eraser.io/workspace/maDvFw5OryuPJOwSLyK9?elements=aSw5yYrSY22mI_YqoZlpGQ)By wrapping parts of your application in `<ErrorBoundary>`, you can prevent the entire application from crashing when an error occurs due to a single component.

When an error is encountered, the `<ErrorBoundary>` component will catch the error and render the fallback UI instead of the problematic component(s). This way, even when a component fails, the user has a controlled UI response instead of a broken interface.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/control-flow/error-boundary.mdx)

Previous[← Portal](https://docs.solidjs.com/concepts/control-flow/portal)

Next[Effects →](https://docs.solidjs.com/concepts/effects)

On this page

1.  [Overview](https://docs.solidjs.com/concepts/control-flow/error-boundary#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/control-flow/error-boundary.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/control-flow/error-boundary.mdx)
