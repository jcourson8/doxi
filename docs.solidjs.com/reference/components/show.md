Title: <Show> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/show

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
<Show>
Edit this page

The Show control flow is used to conditional render part of the view: it renders children when the when is truthy, a fallback otherwise. It is similar to the ternary operator (when ? children : fallback) but is ideal for templating JSX.

import { Show } from "solid-js"
import type { JSX } from "solid-js"


function Show<T>(props: {
  when: T | undefined | null | false
  keyed: boolean
  fallback?: JSX.Element
  children: JSX.Element | ((item: T) => JSX.Element)
}): () => JSX.Element

Here's an example of using the Show control flow:

<Show when={state.count > 0} fallback={<div>Loading...</div>}>
  <div>My Content</div>
</Show>

Show can also be used as a way of keying blocks to a specific data model. For example the function is re-executed whenever the user model is replaced.

<Show when={state.user} fallback={<div>Loading...</div>} keyed>
  {(user) => <div>{user.firstName}</div>}
</Show>
Props
Name	Type	Description
when	T | undefined | null | false	The value to test for truthiness
keyed	boolean	Whether to key the block to the value of when
fallback	JSX.Element	The fallback to render when when is falsy
Report an issue with this page
Previous
← <Portal>
Next
<Switch> / <Match> →
