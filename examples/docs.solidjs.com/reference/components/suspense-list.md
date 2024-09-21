Title: <SuspenseList> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/suspense-list

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
<SuspenseList>
Edit this page

SuspenseList allows for coordinating multiple parallel Suspense and SuspenseList components. It controls the order in which content is revealed to reduce layout thrashing and has an option to collapse or hide fallback states.

import { SuspenseList } from "solid-js"
import type { JSX } from "solid-js"


function SuspenseList(props: {
  children: JSX.Element
  revealOrder: "forwards" | "backwards" | "together"
  tail?: "collapsed" | "hidden"
}): JSX.Element

Note: SuspenseList is still in the experimental stage and does not have full SSR support.

Here's an example of how to use SuspenseList:

<SuspenseList revealOrder="forwards" tail="collapsed">
  <ProfileDetails user={resource.user} />
  <Suspense fallback={<h2>Loading posts...</h2>}>
    <ProfileTimeline posts={resource.posts} />
  </Suspense>
  <Suspense fallback={<h2>Loading fun facts...</h2>}>
    <ProfileTrivia trivia={resource.trivia} />
  </Suspense>
</SuspenseList>
Props
Name	Type	Default	Description
revealOrder	"forwards" | "backwards" | "together"	"forwards"	Determines the order in which the SuspenseList children should be revealed.
tail	"collapsed" | "hidden"	undefined	TODO
revealOrder

"forwards" | "backwards" | "together"

"forwards": Reveals each item in the list once the previous item has finished rendering. This is the default.
"backwards": Reveals each item in the list once the next item has finished rendering.
"together": Reveals all items in the list at the same time.
tail

"collapsed" | "hidden"

Report an issue with this page
Previous
← <Suspense>
Next
attr:* →
