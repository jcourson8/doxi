Title: <For> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/for

Markdown Content:
These docs are currently in Beta! Share your feedback with us!
Solid
Core
Router
SolidStart
Meta
Search
⌘K
Learn
Reference
Basic Reactivity
createEffect
createMemo
createResource
createSignal
Component APIs
children
createContext
createUniqueId
lazy
useContext
Components
<Dynamic>
<ErrorBoundary>
<For>
<Index>
<Portal>
<Show>
<Suspense>
<SuspenseList>
<Switch> / <Match>
JSX Attributes
@once
attr:*
classList
innerHTML or textContent
on:* and oncapture:*
on*
prop:*
ref
style
use:*
Lifecycle
onCleanup
onMount
Reactive Utilities
batch
catchError
createRoot
from
getOwner
indexArray
mapArray
mergeProps
observable
on
runWithOwner
splitProps
startTransition
untrack
useTransition
Rendering
DEV
hydrate
hydrationScript
isServer
render
renderToStream
renderToString
renderToStringAsync
Secondary Primitives
createComputed
createDeferred
createReaction
createRenderEffect
createSelector
Store Utilities
createMutable
createStore
modifyMutable
produce
reconcile
unwrap
Server Utilities
getRequestEvent
Components
<For>
Edit this page

The <For> component is used to render a list of items. It is similar to the .map() function in JavaScript.

import { For } from "solid-js"
import type { JSX } from "solid-js"


function For<T, U extends JSX.Element>(props: {
  each: readonly T[]
  fallback?: JSX.Element
  children: (item: T, index: () => number) => U
}): () => U[]

A referentially keyed loop with efficient updating of only changed items. The callback takes the current item as the first argument:

<For each={state.list} fallback={<div>Loading...</div>}>
  {(item) => <div>{item}</div>}
</For>

The each prop can also be a function that returns a list. This is useful for creating a loop that depends on a state value:

<For each={stateSignal()}>{(item) => <div>{item}</div>}</For>

The optional second argument is an index signal:

<For each={state.list} fallback={<div>Loading...</div>}>
  {(item, index) => (
    <div>
      #{index()} {item}
    </div>
  )}
</For>
Props
Name	Type	Description
each	readonly T[]	The list of items to render.
fallback	JSX.Element	A fallback element to render while the list is loading.
children	(item: T, index: () => number) => U	A callback that returns a JSX element for each item in the list.
Report an issue with this page
Previous
← <ErrorBoundary>
Next
<Index> →
