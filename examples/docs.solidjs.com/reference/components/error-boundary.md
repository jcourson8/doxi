Title: <ErrorBoundary> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/error-boundary

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
<ErrorBoundary>
Edit this page

Catches uncaught errors and renders fallback content.

import { ErrorBoundary } from "solid-js"
import type { JSX } from "solid-js"


function ErrorBoundary(props: {
  fallback: JSX.Element | ((err: any, reset: () => void) => JSX.Element)
  children: JSX.Element
}): () => JSX.Element

Here's an example of how to use it:

<ErrorBoundary fallback={<div>Something went terribly wrong</div>}>
  <MyComp />
</ErrorBoundary>

If you want to customize the error message, you can pass a function as the fallback prop. The function will be called with the error and a reset function. The reset function will reset the error boundary and re-render the children.

<ErrorBoundary
  fallback={(err, reset) => <div onClick={reset}>Error: {err.toString()}</div>}
>
  <MyComp />
</ErrorBoundary>
Props
Name	Type	Description
fallback	JSX.Element | ((err: any, reset: () => void) => JSX.Element)	The fallback content to render when an error is caught.
Report an issue with this page
Previous
← <Dynamic>
Next
<For> →
