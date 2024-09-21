Title: createMutable - SolidDocs

URL Source: https://docs.solidjs.com/reference/store-utilities/create-mutable

Markdown Content:
createMutable - SolidDocs
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

Store Utilities

createMutable
=============

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/store-utilities/create-mutable.mdx)

`createMutable` creates a new mutable Store proxy object that provides a way to selectively trigger updates only when values change.

By intercepting property access, it allows automatic tracking of deep nesting via proxy making it useful for integrating external systems or serving as a compatibility layer with frameworks like MobX or Vue.

```
import { createMutable } from "solid-js/store"import type { Store, StoreNode } from "solid-js/store"
function createMutable<T extends StoreNode>(state: T | Store<T>): Store<T>;
```

Info:

It's important to recognize that a mutable state, which can be passed around and modified anywhere, may complicate the code structure and increase the risk of breaking unidirectional flow.

For a more robust alternative, it is generally recommended to use `createStore` instead. Additionally, the [`produce`](https://docs.solidjs.com/reference/store-utilities/produce) utility can provide many of these same benefits without the associated downsides.

```
import { createMutable } from "solid-js/store"
const state = createMutable({  someValue: 0,  list: [],});
// read valuestate.someValue;
// set valuestate.someValue = 5;
state.list.push(anotherValue);
```

Mutables support setters along with getters.

```
const user = createMutable({  firstName: "John",  lastName: "Smith",  get fullName() {    return `${this.firstName} ${this.lastName}`;  },  set setFullName(value) {    [this.firstName, this.lastName] = value.split(" ");  },});
```

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/store-utilities/create-mutable.mdx)

Previous[← createSelector](https://docs.solidjs.com/reference/secondary-primitives/create-selector)

Next[createStore →](https://docs.solidjs.com/reference/store-utilities/create-store)

On this page

1.  [Overview](https://docs.solidjs.com/reference/store-utilities/create-mutable#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/store-utilities/create-mutable.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/store-utilities/create-mutable.mdx)
