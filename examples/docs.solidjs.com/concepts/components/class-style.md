Title: Class and style - SolidDocs

URL Source: https://docs.solidjs.com/concepts/components/class-style

Markdown Content:
Similar to HTML, Solid uses `class` and `style` attributes to style elements via [CSS (Cascading Style Sheets)](https://developer.mozilla.org/en-US/docs/Glossary/CSS).

*   **Class attribute**: Enables styling one or more elements through CSS rules.
*   **Style attribute**: Inline styles that style single elements.

* * *

The `style` attribute allows you to style a single element and define CSS variables dynamically during runtime. To use it, you can pass either a string or an object.

```
// String<div style="color: red;">This is a red div</div>// Object<div style={{ color: "red" }}>This is a red div</div>
```

When using an object, the keys represent the CSS property names, and the values represent the CSS property values. The keys must be in dash-case, and the values must be strings.

While inline styles are useful for rapid prototyping, they are not recommended for production use. This is because they are not reusable, and they can be difficult to maintain over time.

* * *

The `class` attribute allows you to style one or more elements through CSS rules. This provides a more structured approach to styling, as it allows you to reuse styles across multiple elements.

Classes are defined in CSS files, which are then imported into the component files that use them. You can import these files using the `import` statement at the top of your component file. Once imported into a component, the classes are scoped to that component and any of its children.

```
import "./Card.css";function Card() {  // ...}
```

### [Dynamic styling](https://docs.solidjs.com/concepts/components/class-style#dynamic-styling)

Dynamic styling provides a way to change the appearance of a component based on state or other factors like user inputs. This is useful for creating components that can adapt to different scenarios without having to create multiple versions of the same component:

```
const [theme, setTheme] = createSignal("light");<div class={theme() === "light" ? "light-theme" : "dark-theme"}>  This div's theme is determined dynamically!</div>;
```

[Props](https://docs.solidjs.com/concepts/components/props) are another way to change styles. By passing props to components, you can adapt styles based on the component's usage or the data it receives:

```
function ThemedButton(props) {  return (    <button class={props.theme}>      {props.theme === "light" ? "Light Button" : "Dark Button"}    </button>  );}
```

### [`classList`](https://docs.solidjs.com/concepts/components/class-style#classlist)

When you want to apply multiple classes to an element, you can use the [`classList` attribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList). To use it, you can pass either a string or an object where the keys represent the class names and the values represent a boolean expression. When the value is `true`, the class is applied; when `false`, it is removed.

```
const [current, setCurrent] = createSignal("foo");<button  classList={{ "selected" : current() === "foo" }}  onClick={() => setCurrent("foo")}>  foo</button>;
```

`classList` is often more efficient than `class` when handling multiple conditional classes. This is because `classList` selectively toggles only the classes that require alteration, while `class` will be re-evaluated each time. For a single conditional class, using `class` might be simpler but as the number of conditional classes increases, `classList` offers a more readable and declarative approach.

For a guide on how to style your components, see [Styling Your Components](https://docs.solidjs.com/guides/styling-your-components), where we cover the different ways to style your components using libraries such as [TailwindCSS](https://tailwindcss.com/).
