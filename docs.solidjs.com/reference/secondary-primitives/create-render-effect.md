Title: createRenderEffect - SolidDocs

URL Source: https://docs.solidjs.com/reference/secondary-primitives/create-render-effect

Markdown Content:
createRenderEffect - SolidDocs
===============

These docs are currently in Beta! [Share your feedback with us!](https://shr.link/pna6n)

[**Solid**](https://docs.solidjs.com/)

*   [Core](https://docs.solidjs.com/)
*   [Router](https://docs.solidjs.com/solid-router)
*   [SolidStart](https://docs.solidjs.com/solid-start)
*   [Meta](https://docs.solidjs.com/solid-meta)

Search⌘K[](https://github.com/solidjs/solid)[](https://discord.com/invite/solidjs)

LearnReference

*   Basic Reactivity
    *   [createEffect](https://docs.solidjs.com/reference/basic-reactivity/create-effect)
    *   [createMemo](https://docs.solidjs.com/reference/basic-reactivity/create-memo)
    *   [createResource](https://docs.solidjs.com/reference/basic-reactivity/create-resource)
    *   [createSignal](https://docs.solidjs.com/reference/basic-reactivity/create-signal)
*   Component APIs
    *   [children](https://docs.solidjs.com/reference/component-apis/children)
    *   [createContext](https://docs.solidjs.com/reference/component-apis/create-context)
    *   [createUniqueId](https://docs.solidjs.com/reference/component-apis/create-unique-id)
    *   [lazy](https://docs.solidjs.com/reference/component-apis/lazy)
    *   [useContext](https://docs.solidjs.com/reference/component-apis/use-context)
*   Components
    *   [<Dynamic\>](https://docs.solidjs.com/reference/components/dynamic)
    *   [<ErrorBoundary\>](https://docs.solidjs.com/reference/components/error-boundary)
    *   [<For\>](https://docs.solidjs.com/reference/components/for)
    *   [<Index\>](https://docs.solidjs.com/reference/components/index-component)
    *   [<Portal\>](https://docs.solidjs.com/reference/components/portal)
    *   [<Show\>](https://docs.solidjs.com/reference/components/show)
    *   [<Suspense\>](https://docs.solidjs.com/reference/components/suspense)
    *   [<SuspenseList\>](https://docs.solidjs.com/reference/components/suspense-list)
    *   [<Switch\> / <Match\>](https://docs.solidjs.com/reference/components/switch-and-match)
*   JSX Attributes
    *   [@once](https://docs.solidjs.com/reference/jsx-attributes/once)
    *   [attr:\*](https://docs.solidjs.com/reference/jsx-attributes/attr)
    *   [classList](https://docs.solidjs.com/reference/jsx-attributes/classlist)
    *   [innerHTML or textContent](https://docs.solidjs.com/reference/jsx-attributes/innerhtml-or-textcontent)
    *   [on:\* and oncapture:\*](https://docs.solidjs.com/reference/jsx-attributes/on-and-oncapture)
    *   [on\*](https://docs.solidjs.com/reference/jsx-attributes/on_)
    *   [prop:\*](https://docs.solidjs.com/reference/jsx-attributes/prop)
    *   [ref](https://docs.solidjs.com/reference/jsx-attributes/ref)
    *   [style](https://docs.solidjs.com/reference/jsx-attributes/style)
    *   [use:\*](https://docs.solidjs.com/reference/jsx-attributes/use)
*   Lifecycle
    *   [onCleanup](https://docs.solidjs.com/reference/lifecycle/on-cleanup)
    *   [onMount](https://docs.solidjs.com/reference/lifecycle/on-mount)
*   Reactive Utilities
    *   [batch](https://docs.solidjs.com/reference/reactive-utilities/batch)
    *   [catchError](https://docs.solidjs.com/reference/reactive-utilities/catch-error)
    *   [createRoot](https://docs.solidjs.com/reference/reactive-utilities/create-root)
    *   [from](https://docs.solidjs.com/reference/reactive-utilities/from)
    *   [getOwner](https://docs.solidjs.com/reference/reactive-utilities/get-owner)
    *   [indexArray](https://docs.solidjs.com/reference/reactive-utilities/index-array)
    *   [mapArray](https://docs.solidjs.com/reference/reactive-utilities/map-array)
    *   [mergeProps](https://docs.solidjs.com/reference/reactive-utilities/merge-props)
    *   [observable](https://docs.solidjs.com/reference/reactive-utilities/observable)
    *   [on](https://docs.solidjs.com/reference/reactive-utilities/on)
    *   [runWithOwner](https://docs.solidjs.com/reference/reactive-utilities/run-with-owner)
    *   [splitProps](https://docs.solidjs.com/reference/reactive-utilities/split-props)
    *   [startTransition](https://docs.solidjs.com/reference/reactive-utilities/start-transition)
    *   [untrack](https://docs.solidjs.com/reference/reactive-utilities/untrack)
    *   [useTransition](https://docs.solidjs.com/reference/reactive-utilities/use-transition)
*   Rendering
    *   [DEV](https://docs.solidjs.com/reference/rendering/dev)
    *   [hydrate](https://docs.solidjs.com/reference/rendering/hydrate)
    *   [hydrationScript](https://docs.solidjs.com/reference/rendering/hydration-script)
    *   [isServer](https://docs.solidjs.com/reference/rendering/is-server)
    *   [render](https://docs.solidjs.com/reference/rendering/render)
    *   [renderToStream](https://docs.solidjs.com/reference/rendering/render-to-stream)
    *   [renderToString](https://docs.solidjs.com/reference/rendering/render-to-string)
    *   [renderToStringAsync](https://docs.solidjs.com/reference/rendering/render-to-string-async)
*   Secondary Primitives
    *   [createComputed](https://docs.solidjs.com/reference/secondary-primitives/create-computed)
    *   [createDeferred](https://docs.solidjs.com/reference/secondary-primitives/create-deferred)
    *   [createReaction](https://docs.solidjs.com/reference/secondary-primitives/create-reaction)
    *   [createRenderEffect](https://docs.solidjs.com/reference/secondary-primitives/create-render-effect)
    *   [createSelector](https://docs.solidjs.com/reference/secondary-primitives/create-selector)
*   Store Utilities
    *   [createMutable](https://docs.solidjs.com/reference/store-utilities/create-mutable)
    *   [createStore](https://docs.solidjs.com/reference/store-utilities/create-store)
    *   [modifyMutable](https://docs.solidjs.com/reference/store-utilities/modify-mutable)
    *   [produce](https://docs.solidjs.com/reference/store-utilities/produce)
    *   [reconcile](https://docs.solidjs.com/reference/store-utilities/reconcile)
    *   [unwrap](https://docs.solidjs.com/reference/store-utilities/unwrap)
*   Server Utilities
    *   [getRequestEvent](https://docs.solidjs.com/reference/server-utilities/get-request-event)

Secondary Primitives

createRenderEffect
==================

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/secondary-primitives/create-render-effect.mdx)

```
import { createRenderEffect } from "solid-js"
function createRenderEffect<T>(fn: (v: T) => T, value?: T): void
```

A render effect is a computation similar to a regular effect (as created by [`createEffect`](https://docs.solidjs.com/reference/basic-reactivity/create-effect)), but differs in when Solid schedules the first execution of the effect function. While `createEffect` waits for the current rendering phase to be complete, `createRenderEffect` immediately calls the function. Thus the effect runs as DOM elements are being created and updated, but possibly before specific elements of interest have been created, and probably before those elements have been connected to the document. In particular, **refs** will not be set before the initial effect call. Indeed, Solid uses `createRenderEffect` to implement the rendering phase itself, including setting of **refs**.

Reactive updates to render effects are identical to effects: they queue up in response to a reactive change (e.g., a single signal update, or a batch of changes, or collective changes during an entire render phase) and run in a single [`batch`](https://docs.solidjs.com/reference/reactive-utilities/batch) afterward (together with effects). In particular, all signal updates within a render effect are batched.

Here is an example of the behavior. (Compare with the example in [`createEffect`](https://docs.solidjs.com/reference/basic-reactivity/create-effect).)

```
// assume this code is in a component function, so is part of a rendering phaseconst [count, setCount] = createSignal(0)
// this effect prints count at the beginning and when it changescreateRenderEffect(() => console.log("count =", count()))// render effect runs immediately, printing `count = 0`console.log("hello")setCount(1) // effect won't run yetsetCount(2) // effect won't run yet
queueMicrotask(() => {  // now `count = 2` will print  console.log("microtask")  setCount(3) // immediately prints `count = 3`  console.log("goodbye")})
// --- overall output: ---// count = 0   [this is the only added line compared to createEffect]// hello// count = 2// microtask// count = 3// goodbye
```

Just like `createEffect`, the effect function gets called with an argument equal to the value returned from the effect function's last execution, or on the first call, equal to the optional second argument of `createRenderEffect`.

* * *

[Arguments](https://docs.solidjs.com/reference/secondary-primitives/create-render-effect#arguments)
---------------------------------------------------------------------------------------------------

Name

Type

Description

`fn`

`(v: T) => T`

The effect function to be called.

`value`

`T`

The initial value to be passed to the effect function.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/secondary-primitives/create-render-effect.mdx)

Previous[← createReaction](https://docs.solidjs.com/reference/secondary-primitives/create-reaction)

Next[createSelector →](https://docs.solidjs.com/reference/secondary-primitives/create-selector)

On this page

1.  [Overview](https://docs.solidjs.com/reference/secondary-primitives/create-render-effect#_top)
2.  [Arguments](https://docs.solidjs.com/reference/secondary-primitives/create-render-effect#arguments)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/secondary-primitives/create-render-effect.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/secondary-primitives/create-render-effect.mdx)
