Title: Refs - SolidDocs

URL Source: https://docs.solidjs.com/concepts/refs

Markdown Content:
Refs, or references, are a special attribute that can be attached to any element, and are used to reference a DOM element or a component instance. They are particularly useful when you need to access the DOM nodes directly or invoke methods on a component.

* * *

One way of accessing DOM elements is through [element selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors) such as [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) or [`document.getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById). Since elements in Solid can be added or removed from the DOM based on state, you need to wait until the element is attached to the DOM before accessing it. This can be done by using [`onMount`](https://docs.solidjs.com/reference/lifecycle/on-mount) to wait until the element is attached to the DOM before accessing it:

Accessing DOM elements through element selectors is not recommended for this reason. As elements with the same selectors are added and removed from the DOM, the first element that matches the selector will be returned, which may not be the element you want.

* * *

JSX can be used as a value and assigned to a variable when looking to directly access DOM elements.

```
function Component() {  const myElement = <p>My Element</p>  return <div>{myElement}</div>}
```

This lets you create and access DOM elements similar to [`document.createElement`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement) but without having to wait until it is attached to the DOM. It can be used multiple times without having to worry about duplicate selectors.

The downside to this approach is it separates the element and any child elements from the rest of the JSX structure. This makes the component's JSX structure more difficult to read and understand.

* * *

Solid provides a ref system to access DOM elements directly inside the JSX template, which keeps the structure of the elements intact.

To use [`ref`](https://docs.solidjs.com/reference/jsx-attributes/ref), you declare a variable and use it as the `ref` attribute:

```
function Component() {  let myElement;  return (    <div>      <p ref={myElement}>My Element</p>    </div>  )}
```

These assignments occur at _creation time_ prior to the element being added to the DOM. If access to an element is needed before it is added to the DOM, you can use the callback form of `ref`:

```
<p ref={(el) => {  myElement = el // el is created but not yet added to the DOM  }}>  My Element</p>
```

### [Signals as refs](https://docs.solidjs.com/concepts/refs#signals-as-refs)

[Signals](https://docs.solidjs.com/concepts/signals) can also be used as refs. This is useful when you want to access the element directly, but the element may not exist when the component is first rendered, or may be removed from the DOM at some point.

```
function App() {  const [show, setShow] = createSignal(false)  const [element, setElement] = createSignal()  return (    <div>      <button onClick={() => setShow((isShown) => !isShown)}>Toggle</button>      <Show when={show()}>        <p ref={setElement}>This is the ref element</p>      </Show>    </div>  )}
```

In this example, the paragraph element is only rendered when the `show` signal is `true`. When the component initializes, the paragraph element does not exist, so the `element` variable is not assigned. Once the `show` signal is set to `true`, the paragraph element is rendered, and the `element` variable is assigned to the paragraph element.

You can see a detailed view of the ref update lifecycle in this [Solid playground example](https://playground.solidjs.com/anonymous/22a1abfa-a0f5-44a6-bbe6-40387cf63b95).

* * *

Forwarding refs is a technique that allows you to pass a ref from a parent component to a child component. This is useful when you want to access the DOM element of a child component from the parent component.

To forward a ref, you need to pass the ref to the child component, and then assign the ref to the child component's element.

When a child component receives a `ref` attribute from its parent, the `ref` is passed as a callback function. This is regardless of whether the parent passed it as a simple assignment or a callback.

Once the child component receives the `ref`, it can be assigned to the element that the child component wants to expose through the `ref` attribute. To access the `ref` in the child component, it is passed as a prop:

```
// Parent componentimport { Canvas } from "./Canvas.jsx"function ParentComponent() {  let canvasRef  const animateCanvas = () => {    // Manipulate the canvas using canvasRef...  }  return (    <div>      <Canvas ref={canvasRef} />      <button onClick={animateCanvas}>Animate Canvas</button>    </div>  )}// Child componentfunction Canvas(props) {  return (    <div className="canvas-container">      <canvas ref={props.ref} /> {/* Assign the ref to the canvas element */}    </div>  )}
```

In this example, the `canvas` element is directly assigned the `ref` attribute through the `props.ref` variable. This forwards the reference to the parent component, giving it direct access to the `canvas` element.

* * *

Directives allow the attachment of reusable behaviours to DOM elements. The [`use:`](https://docs.solidjs.com/reference/jsx-attributes/use) prefix is used to denote these custom directives. Unlike props or attributes, directives operate at a lower level through providing fine-grained control over the elements they are attached to.

Directives are like callback refs but they enable two extra features:

*   Having multiple directives on an element.
*   Passing in reactive data to the callback.

A directive is essentially a function with a specific signature:

```
function directive(element: Element, accessor: () => any): void
```

*   `element`: The DOM element that the directive is applied to.
*   `accessor`: A function that gives access to the value(s) passed to the directive.

The directive functions are called at render time, but are called before the element is added to the DOM. Due to this order, elements are fully primed with their attributes, properties, or event listeners, therefore minimizing unexpected behaviors or premature interactions.

Within directives, you're able to perform a variety of tasks, including:

*   creating [signals](https://docs.solidjs.com/concepts/signals)
*   initiating [effects](https://docs.solidjs.com/guides/state-management#reacting-to-changes)
*   adding [event listeners](https://docs.solidjs.com/concepts/components/event-handlers)
*   and more.

To learn more about directives and how they work with TypeScript, refer to our [TypeScript for Solid guide](https://docs.solidjs.com/configuration/typescript).
