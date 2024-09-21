Title: classList - SolidDocs

URL Source: https://docs.solidjs.com/reference/jsx-attributes/classlist

Markdown Content:
classList - SolidDocs
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

JSX Attributes

classList
=========

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/jsx-attributes/classlist.mdx)

Solid offers two ways to set the class of an element: class and classList attributes.

First, you can set class=... like any other attribute. For example:

```
// Two static classes<div class="active editing" />
// One dynamic class, deleting class attribute if it's not needed<div class={state.active ? 'active' : undefined} />
// Two dynamic classes<div class={`${state.active ? 'active' : ''} ${state.currentId === row.id ? 'editing' : ''}`} />
```

Info:

Note that `className` was deprecated in Solid 1.4 in favor of `class`.

Alternatively, the `classList` pseudo-attribute lets you specify an object, where each key is a class and the value is treated as a boolean representing whether to include that class. For example (matching the last example):

```
<div  classList={{ active: state.active, editing: state.currentId === row.id }}/>
```

This example compiles to a render effect that dynamically calls [element.classList.toggle](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle) to turn each class on or off, only when the corresponding boolean changes. For example, when `state.active` becomes true \[false\], the element gains \[loses\] the `active` class.

The value passed into `classList` can be any expression (including a signal getter) that evaluates to an appropriate object. Some examples:

```
// Dynamic class name and value;<div classList={{ [className()]: classOn() }} />
// Signal class listconst [classes, setClasses] = createSignal({})setClasses((c) => ({ ...c, active: true }));<div classList={classes()} />
```

It's also possible, but dangerous, to mix class and classList. The main safe situation is when class is set to a static string (or nothing), and classList is reactive. (class could also be set to a static computed value as in `class={baseClass()}`, but then it should appear before any classList pseudo-attributes.) If both class and classList are reactive, you can get unexpected behavior: when the class value changes, Solid sets the entire class attribute, so will overwrite any toggles made by classList.

Because classList is a compile-time pseudo-attribute, it does not work in a prop spread like `<div {...props} />` or in `<Dynamic>`.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/jsx-attributes/classlist.mdx)

Previous[← attr:\*](https://docs.solidjs.com/reference/jsx-attributes/attr)

Next[innerHTML or textContent →](https://docs.solidjs.com/reference/jsx-attributes/innerhtml-or-textcontent)

On this page

1.  [Overview](https://docs.solidjs.com/reference/jsx-attributes/classlist#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/jsx-attributes/classlist.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/jsx-attributes/classlist.mdx)
