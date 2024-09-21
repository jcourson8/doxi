Title: Understanding JSX - SolidDocs

URL Source: https://docs.solidjs.com/concepts/understanding-jsx

Markdown Content:
JSX is an extension for JavaScript. It allows you to write HTML-like code inside your JavaScript file which keeps your rendering logic and content in the same place. This provides a concise and readable way to create and represent components.

* * *

Solid was designed to align closely with HTML standards.

```
const element = <h1>I'm JSX!!</h1>
```

It offers a distinct advantage, however: to copy/paste solutions from resources like Stack Overflow; and to allow direct usage of templates from design tools. Solid sets itself apart by using JSX immediately as it returns [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) elements. This lets you use dynamic expressions within your HTML by allowing variables and functions to be references with the use of curly braces (`{ }`):

```
const Component = () => {  const animal = { breed: "cat", name: "Midnight" }  return (    <p>      I have a {animal.breed} named {animal.name}!    </p>  )}
```

This means JavaScript content can be rendered on web pages based on an application's state or logic.

Additionally, Solid's [reactive](https://docs.solidjs.com/concepts/intro-to-reactivity) system introduces [fine-grained reactivity](https://docs.solidjs.com/advanced-concepts/fine-grained-reactivity) with JSX. This updates only the necessary parts of the DOM when changes occur in the underlying state.

* * *

### [Return a single root element](https://docs.solidjs.com/concepts/understanding-jsx#return-a-single-root-element)

Where HTML lets you have disconnected tags at the top level, JSX requires that a component to return a single root element.

JSX maintains the familiar nested, tree-like structure found in HTML. As a result, parent-child relationships between elements become easier to follow.

### [Close all tags](https://docs.solidjs.com/concepts/understanding-jsx#close-all-tags)

Self-closing tags are a must in JSX. Unlike in HTML, where elements like `<input>`, `<img>`, or `<br>` don't require explicit closure, JSX requires consistent self-closing tags. This helps to avoid potential rendering issues.

```
<img src="./image-here.png" />
```

### [Properties vs. attributes](https://docs.solidjs.com/concepts/understanding-jsx#properties-vs-attributes)

HTML attributes and JSX properties may seem similar, but they serve different purposes and behave differently. Both offer ways to specify configurations or pass information. However, HTML is used for standard web content and JSX creates Solid's component logic.

#### [HTML attributes](https://docs.solidjs.com/concepts/understanding-jsx#html-attributes)

[HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) are values set directly on HTML elements. They provide additional information about an element to guide its initial behavior and state. These attributes are often translated into properties on DOM objects once the browser parses the HTML.

In JSX files, HTML attributes are used much like regular HTML, with a few key differences due to the blend of HTML and JavaScript:

*   Event listeners such as `onClick` can be in camelCase or lowercase. (**Note:** When using ESLint, you will get a warning if you use lowercase.)
*   In cases where you can dynamically specify a value, you can replace the `"` and `"` with curly braces (`{ }`):

```
<button class="myClass" onClick={handleClick}>  Click me!</button>
```

### [JSX properties (props)](https://docs.solidjs.com/concepts/understanding-jsx#jsx-properties-props)

JSX properties, commonly known as "props," help with the passing of data and configurations to components within an application. They connect the component with the data it requires, for seamless data flows and dynamic interactions.

#### [Core concepts](https://docs.solidjs.com/concepts/understanding-jsx#core-concepts)

*   **Static props**: In Solid's JSX, static props are integrated directly into the HTML by cloning the template and using them as attributes.
    
*   **Dynamic props**: Dynamic props rely on state, allowing the content or properties to be dynamic. An example is changing the style of an element in response to interactions within an application. This can be expressed in the form of signals (`value={value()}`).
    
*   **Data transfer**: Props are also used to fill components with data that comes from resources, like [`createResource`](https://docs.solidjs.com/reference/basic-reactivity/create-resource) calls. This results in components that react in real-time to data changes.
    

For how to use props effectively in Solid, explore the [props page](https://docs.solidjs.com/concepts/components/props).
