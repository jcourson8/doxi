Title: runWithOwner - SolidDocs

URL Source: https://docs.solidjs.com/reference/reactive-utilities/run-with-owner

Markdown Content:
runWithOwner - SolidDocs
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

Reactive Utilities

runWithOwner
============

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/reactive-utilities/run-with-owner.mdx)

```
import { runWithOwner } from "solid-js"import type { Owner } from "solid-js"
function runWithOwner<T>(owner: Owner, fn: (() => void) => T): T
```

Executes the given function under the provided owner, instead of (and without affecting) the owner of the outer scope. By default, computations created by `createEffect`, `createMemo`, etc. are owned by the owner of the currently executing code (the return value of `getOwner`), so in particular these will get disposed when their owner does. Calling `runWithOwner` provides a way to override this default to a manually specified owner (typically, the return value from a previous call to `getOwner`), enabling more precise control of when computations get disposed.

Having a (correct) owner is important for two reasons:

*   Computations without an owner cannot be cleaned up. For example, if you call `createEffect` without an owner (e.g., in the global scope), the effect will continue running forever, instead of being disposed when its owner gets disposed.
    
*   useContext obtains context by walking up the owner tree to find the nearest ancestor providing the desired context. So without an owner you cannot look up any provided context (and with the wrong owner, you might obtain the wrong context).
    

Manually setting the owner is especially helpful when doing reactivity outside of any owner scope. In particular, asynchronous computation (via either `async` functions or callbacks like `setTimeout`) lose their automatically set owner, so remembering the original owner via `getOwner` and restoring it via `runWithOwner` is necessary in these cases. For example:

```
const owner = getOwner()setTimeout(() => {  // This callback gets run without owner.  // Restore owner via runWithOwner:  runWithOwner(owner, () => {    const foo = useContext(FooContext)    createEffect(() => {      console.log(foo)    })  })}, 1000)
```

**Note:** that owners are not what determines dependency tracking, so `runWithOwner` does not help with tracking in asynchronous functions; use of reactive state in the asynchronous part (e.g. after the first `await`) will not be tracked as a dependency.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/reactive-utilities/run-with-owner.mdx)

Previous[← on](https://docs.solidjs.com/reference/reactive-utilities/on)

Next[splitProps →](https://docs.solidjs.com/reference/reactive-utilities/split-props)

On this page

1.  [Overview](https://docs.solidjs.com/reference/reactive-utilities/run-with-owner#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/reactive-utilities/run-with-owner.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/reactive-utilities/run-with-owner.mdx)
