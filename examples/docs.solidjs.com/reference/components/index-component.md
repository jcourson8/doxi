Title: <Index> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/index-component

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
<Index>
Edit this page

Non-keyed list iteration (rendered nodes are keyed to an array index). This is useful when there is no conceptual key, like if the data consists of primitives and it is the index that is fixed rather than the value.

import { Index } from "solid-js"
import type { JSX } from "solid-js"


function Index<T, U extends JSX.Element>(props: {
  each: readonly T[];
  fallback?: JSX.Element;
  children: (item: () => T, index: number) => U;
}): () => U[];

A super simple implementation of this component might look like this:

function Index<T, U extends JSX.Element>(props: {
  each: readonly T[];
  fallback?: JSX.Element;
  children: (item: () => T, index: number) => U;
}) {
  return () => {
    const [items, setItems] = createSignal(props.each);
    return props.each.map((_, i) => props.children(() => items()[i], i));
  };
}

Here's a look at the implementation of the Index component in Solid:

<Index each={state.list} fallback={<div>Loading...</div>}>
  {(item) => <div>{item()}</div>}
</Index>

Notice that the item is a signal unlike the For component. This is because the Index component is not keyed to the item itself but rather the index.

Optional second argument is an index number:

<Index each={state.list} fallback={<div>Loading...</div>}>
  {(item, index) => (
    <div>
      #{index} {item()}
    </div>
  )}
</Index>
Props
Name	Type	Description
each	readonly T[]	The array to iterate over.
fallback	JSX.Element	Optional fallback element to render while the array is loading.
children	(item: () => T, index: number) => U	The function that renders the children.
Report an issue with this page
Previous
← <For>
Next
<Portal> →
