Title: Dynamic - SolidDocs

URL Source: https://docs.solidjs.com/concepts/control-flow/dynamic

Markdown Content:
Dynamic - SolidDocs
===============

These docs are currently in Beta! [Share your feedback with us!](https://shr.link/pna6n)

[**Solid**](https://docs.solidjs.com/)

*   [Core](https://docs.solidjs.com/)
*   [Router](https://docs.solidjs.com/solid-router)
*   [SolidStart](https://docs.solidjs.com/solid-start)
*   [Meta](https://docs.solidjs.com/solid-meta)

Search⌘K[](https://github.com/solidjs/solid)[](https://discord.com/invite/solidjs)

LearnReference

*   [Quick start](https://docs.solidjs.com/quick-start)
*   Concepts
    *   [Intro to reactivity](https://docs.solidjs.com/concepts/intro-to-reactivity)
    *   [Understanding JSX](https://docs.solidjs.com/concepts/understanding-jsx)
    *   Components
        
        *   [Basics](https://docs.solidjs.com/concepts/components/basics)
        *   [Class and style](https://docs.solidjs.com/concepts/components/class-style)
        *   [Event handlers](https://docs.solidjs.com/concepts/components/event-handlers)
        *   [Props](https://docs.solidjs.com/concepts/components/props)
        
    *   [Signals](https://docs.solidjs.com/concepts/signals)
    *   Control Flow
        
        *   [Conditional rendering](https://docs.solidjs.com/concepts/control-flow/conditional-rendering)
        *   [Dynamic](https://docs.solidjs.com/concepts/control-flow/dynamic)
        *   [List rendering](https://docs.solidjs.com/concepts/control-flow/list-rendering)
        *   [Portal](https://docs.solidjs.com/concepts/control-flow/portal)
        *   [Error boundary](https://docs.solidjs.com/concepts/control-flow/error-boundary)
        
    *   [Effects](https://docs.solidjs.com/concepts/effects)
    *   Derived Values
        
        *   [Derived signals](https://docs.solidjs.com/concepts/derived-values/derived-signals)
        *   [Memos](https://docs.solidjs.com/concepts/derived-values/memos)
        
    *   [Context](https://docs.solidjs.com/concepts/context)
    *   [Stores](https://docs.solidjs.com/concepts/stores)
    *   [Refs](https://docs.solidjs.com/concepts/refs)
*   Advanced Concepts
    *   [Fine-grained reactivity](https://docs.solidjs.com/advanced-concepts/fine-grained-reactivity)
*   Guides
    *   [Styling your components](https://docs.solidjs.com/guides/styling-your-components)
    *   [State management](https://docs.solidjs.com/guides/state-management)
    *   [Routing & navigation](https://docs.solidjs.com/guides/routing-and-navigation)
    *   [Complex state management](https://docs.solidjs.com/guides/complex-state-management)
    *   [Fetching data](https://docs.solidjs.com/guides/fetching-data)
    *   [Testing](https://docs.solidjs.com/guides/testing)
    *   [Deploy your app](https://docs.solidjs.com/guides/deploying-your-app)
*   Configuration
    *   [Environment variables](https://docs.solidjs.com/configuration/environment-variables)
    *   [TypeScript](https://docs.solidjs.com/configuration/typescript)

Control Flow

Dynamic
=======

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/control-flow/dynamic.mdx)

`<Dynamic>` is a Solid component that allows you to render components dynamically based on data. By passing either a string representing a [native HTML element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) or a component function to the `component` prop, you can render the chosen component with the remaining props you provide.

```
import { createSignal, For } from "solid-js"import { Dynamic } from "solid-js/web"
const RedDiv = () => <div style="color: red">Red</div>const GreenDiv = () => <div style="color: green">Green</div>const BlueDiv = () => <div style="color: blue">Blue</div>
const options = {  red: RedDiv,  green: GreenDiv,  blue: BlueDiv,}
function App() {  const [selected, setSelected] = createSignal("red")
  return (    <>      <select        value={selected()}        onInput={(e) => setSelected(e.currentTarget.value)}      >        <For each={Object.keys(options)}>          {(color) => <option value={color}>{color}</option>}        </For>      </select>      <Dynamic component={options[selected()]} />    </>  )}
```

This example renders a `<select>` element that allows you to choose between three colors. Once a color is selected, the `<Dynamic>` component will render the chosen color's corresponding component or element.

`<Dynamic>` creates more concise code than alternative conditional rendering options. For example, the following code renders the same result as the previous example:

```
import { createSignal, Switch, Match, For } from "solid-js"
const RedDiv = () => <div style="color: red">Red</div>const GreenDiv = () => <div style="color: green">Green</div>const BlueDiv = () => <div style="color: blue">Blue</div>
const options = {  red: RedDiv,  green: GreenDiv,  blue: BlueDiv,}
function App() {  const [selected, setSelected] = createSignal("red")
  return (    <>      <select        value={selected()}        onInput={(e) => setSelected(e.currentTarget.value)}      >        <For each={Object.keys(options)}>          {(color) => <option value={color}>{color}</option>}        </For>      </select>      <Switch fallback={<BlueDiv />}>        <Match when={selected() === "red"}>          <RedDiv />        </Match>        <Match when={selected() === "green"}>          <GreenDiv />        </Match>      </Switch>    </>  )}
```

Instead of a more verbose [`<Switch>` and `<Match>`](https://docs.solidjs.com/concepts/control-flow/conditional-rendering) statement, `<Dynamic>` offers a more concise way to render components dynamically.

* * *

[Props](https://docs.solidjs.com/concepts/control-flow/dynamic#props)
---------------------------------------------------------------------

When working with these components, you can pass [props](https://docs.solidjs.com/concepts/components/props) to the component you are rendering by passing them to the `<Dynamic>` component. This makes them available to the component you are rendering, similar to how you would pass props to components in JSX.

```
import { Dynamic } from "solid-js/web"
function App() {  return (    <Dynamic component={someComponent} someProp="someValue" />  )}
```

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/control-flow/dynamic.mdx)

Previous[← Conditional rendering](https://docs.solidjs.com/concepts/control-flow/conditional-rendering)

Next[List rendering →](https://docs.solidjs.com/concepts/control-flow/list-rendering)

On this page

1.  [Overview](https://docs.solidjs.com/concepts/control-flow/dynamic#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/concepts/control-flow/dynamic.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/concepts/control-flow/dynamic.mdx)
