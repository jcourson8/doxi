Title: <Switch> / <Match> - SolidDocs

URL Source: https://docs.solidjs.com/reference/components/switch-and-match

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
<Switch> / <Match>
Edit this page

Useful for when there are more than 2 mutual exclusive conditions. It is a more flexible version of the if-else-if-else-if-else-... chain.

import { Switch, Match } from "solid-js"
import type { MatchProps, JSX } from "solid-js"


function Switch(props: {
  fallback?: JSX.Element
  children: JSX.Element
}): () => JSX.Element


type MatchProps<T> = {
  when: T | undefined | null | false
  children: JSX.Element | ((item: T) => JSX.Element)
}
function Match<T>(props: MatchProps<T>)

A super simple implementation of this component would be:

function Switch(props) {
  let children = props.children


  if (!Array.isArray(children)) children = [children]


  for (let i = 0; i < children.length; i++) {
    const child = children[i]
    if (child.props.when) return child
  }


  return props.fallback
}

For example, it can be used to perform basic routing:

<Switch fallback={<div>Not Found</div>}>
  <Match when={state.route === "home"}>
    <Home />
  </Match>
  <Match when={state.route === "settings"}>
    <Settings />
  </Match>
</Switch>

Match also supports function children to serve as keyed flow.

Props
Switch
Name	Type	Default	Description
fallback	JSX.Element	undefined	The fallback element to render if no Match component has a truthy when prop.
Match
Name	Type	Default	Description
when	T | undefined | null | false	undefined	The condition to check. If it is truthy, the children will be rendered.
Report an issue with this page
Previous
← <Show>
Next
<Suspense> →
