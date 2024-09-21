Title: Derived signals - SolidDocs

URL Source: https://docs.solidjs.com/concepts/derived-values/derived-signals

Markdown Content:
Derived signals - SolidDocs
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

Derived Values

Derived signals
===============

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/derived-values/derived-signals.mdx)

Derived signals are functions that rely on one or more [signals](https://docs.solidjs.com/concepts/signals) to produce a value.

These functions are not executed immediately, but instead are only called when the values they rely on are changed. When the underlying signal is changed, the function will be called again to produce a new value.

```
const double = () => count() * 2;
```

In the above example, the `double` function relies on the `count` signal to produce a value. When the `count` signal is changed, the `double` function will be called again to produce a new value.

Similarly you can create a derived signal that relies on a store value because stores use signals under the hood. To learn more about how stores work, [you can visit the stores section](https://docs.solidjs.com/concepts/stores).

```
const fullName = () => store.firstName + ' ' + store.lastName;
```

These dependent functions gain reactivity from the signal they access, ensuring that changes in the underlying data propagate throughout your application. It is important to note that these functions do not store a value themselves; instead, they can update any effects or components that depend on them. If included within a component's body, these derived signals will trigger an update when necessary.

While you can create derived values in this manner, Solid created the [`createMemo`](https://docs.solidjs.com/reference/basic-reactivity/create-memo) primitive. To dive deeper into how memos work, [check out the memos section](https://docs.solidjs.com/concepts/derived-values/memos).

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/derived-values/derived-signals.mdx)

Previous[← Effects](https://docs.solidjs.com/concepts/effects)

Next[Memos →](https://docs.solidjs.com/concepts/derived-values/memos)

On this page

1.  [Overview](https://docs.solidjs.com/concepts/derived-values/derived-signals#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/derived-values/derived-signals.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/derived-values/derived-signals.mdx)
