Title: <Portal> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/portal

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
<Portal>
Edit this page

<Portal> is a component that allows you to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

This is useful when your UI has some elements that need to appear on top of everything else, such as modals and tooltips.

import { Portal } from "solid-js/web"
import type { JSX } from "solid-js"


function Portal(props: {
  mount?: Node
  useShadow?: boolean
  isSVG?: boolean
  children: JSX.Element
}): Text

This inserts the element in the mount node. Useful for inserting Modals outside of the page layout. Events still propagate through the component hierarchy, however <Portal> will only run on the client and has hydration disabled.

The portal is mounted in a <div> unless the target is the document head. useShadow places the element in a Shadow Root for style isolation, and isSVG is required if inserting into an SVG element so that the <div> is not inserted.

<Portal mount={document.getElementById("modal")}>
  <div>My Content</div>
</Portal>
Props
Name	Type	Default	Description
mount	Node	document.body	The DOM node to mount the portal in.
useShadow	boolean	false	Whether to use a Shadow Root for style isolation.
isSVG	boolean	false	Whether the mount node is an SVG element.
Report an issue with this page
Previous
← <Index>
Next
<Show> →
