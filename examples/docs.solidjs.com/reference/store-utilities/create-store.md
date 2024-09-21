Title: createStore - SolidDocs

URL Source: https://docs.solidjs.com/reference/store-utilities/create-store

Markdown Content:
createStore - SolidDocs
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

createStore
===========

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/store-utilities/create-store.mdx)

Stores were intentionally designed to manage data structures like objects and arrays but are capable of handling other data types, such as strings and numbers.

* * *

[Types Signature](https://docs.solidjs.com/reference/store-utilities/create-store#types-signature)
--------------------------------------------------------------------------------------------------

```
import { createStore } from "solid-js/store"import type { StoreNode, Store, SetStoreFunction } from "solid-js/store"
function createStore<T extends StoreNode>(  state: T | Store<T>): [get: Store<T>, set: SetStoreFunction<T>];
type Store<T> = T; // conceptually readonly, but not typed as such
```

* * *

[Usage](https://docs.solidjs.com/reference/store-utilities/create-store#usage)
------------------------------------------------------------------------------

```
import { createStore } from "solid-js/store";
// Initialize storeconst [store, setStore] = createStore({  userCount: 3,  users: [    {      id: 0,      username: "felix909",      location: "England",      loggedIn: false,    },    {      id: 1,      username: "tracy634",      location: "Canada",      loggedIn: true,    },    {      id: 1,      username: "johny123",      location: "India",      loggedIn: true,    },  ],});
```

* * *

[Getter](https://docs.solidjs.com/reference/store-utilities/create-store#getter)
--------------------------------------------------------------------------------

Store objects support the use of getters to store derived values.

```
const [state, setState] = createStore({  user: {    firstName: "John",    lastName: "Smith",    get fullName() {      return `${this.firstName} ${this.lastName}`;    },  },});
```

* * *

[Setter](https://docs.solidjs.com/reference/store-utilities/create-store#setter)
--------------------------------------------------------------------------------

Changes can take the form of function that passes previous state and returns new state or a value. Objects are always shallowly merged. Set values to undefined to delete them from the Store. In TypeScript, you can delete a value by using a non-null assertion, like `undefined!`.

```
const [state, setState] = createStore({  firstName: "John",  lastName: "Miller",});
setState({ firstName: "Johnny", middleName: "Lee" });// ({ firstName: 'Johnny', middleName: 'Lee', lastName: 'Miller' })
setState((state) => ({ preferredName: state.firstName, lastName: "Milner" }));// ({ firstName: 'Johnny', preferredName: 'Johnny', middleName: 'Lee', lastName: 'Milner' })
```

* * *

To learn more about using stores check the [Stores Guide](https://docs.solidjs.com/concepts/stores), and the **Store utilities** section for more advanced APIs.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/store-utilities/create-store.mdx)

Previous[← createMutable](https://docs.solidjs.com/reference/store-utilities/create-mutable)

Next[modifyMutable →](https://docs.solidjs.com/reference/store-utilities/modify-mutable)

On this page

1.  [Overview](https://docs.solidjs.com/reference/store-utilities/create-store#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/reference/store-utilities/create-store.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/reference/store-utilities/create-store.mdx)
