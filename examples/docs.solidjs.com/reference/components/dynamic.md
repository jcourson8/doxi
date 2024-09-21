Title: <Dynamic> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/dynamic

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
<Dynamic>
Edit this page

This component lets you insert an arbitrary Component or tag and passes the props through to it.

import { Dynamic } from "solid-js/web"
import type { JSX } from "solid-js"


function Dynamic<T>(
  props: T & {
    children?: any
    component?: Component<T> | string | keyof JSX.IntrinsicElements
  }
): () => JSX.Element

Here's an example of how you can use it:

<Dynamic component={MyComponent} someProp={state.something} />
Props
Name	Type	Description
component	Component<T> | string | keyof JSX.IntrinsicElements	The component to render.
children	any	The children to pass to the component.
...	T	Any other props to pass to the component.
Report an issue with this page
Previous
← useContext
Next
<ErrorBoundary> →
