Title: CSS modules - SolidDocs

URL Source: https://docs.solidjs.com/guides/styling-components/css-modules

Markdown Content:
Styling your Components[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/css-modules.mdx)

CSS Modules are CSS files where class names, animations, and media queries are scoped locally by default. These provide a way to encapsulate styles within components, preventing global conflicts and optimizing the final output by bundling only the used selectors.

* * *

Begin by creating a CSS module file. Conventionally, these files have a `.module.css` extension, like `style.module.css`. However, you can also use other other extensions, such as `.scss` and `.sass`.

```
.foo {  color: red;}.bar {  background-color: blue;}
```

**Note:** Avoid the use of HTML tags in CSS modules. Since they are not considered pure selectors, it can lead to specificity issues which can make it more difficult to override with other styles and lead to unexpected behaviors.

* * *

1.  **Importing styles:** In your component file (eg. `Component.jsx`), import the styles from the CSS module.

```
import styles from "styles.module.css";
```

2.  **Applying styles:** Use the imported styles by referencing them as properties of the styles object in your JSX:

```
function Component() {  return (    <>      <div class={`${styles.foo} ${styles.bar}`}>Hello, world!</div>    </>  );}
```

3.  **Using a single style:** If you only need one style from the module, import and apply it directly:

```
import styles from "styles.module.css";function Component() {  return (    <>      <div class={styles.foo}>Hello, world!</div>    </>  );}
```

4.  **Mixing with regular class names:** You can combine CSS module syntax with regular string class names, as well:

```
import styles from "styles.module.css";function Component() {  return (    <>      <div class={`${styles.foo} container`}>Hello, world!</div>    </>  );}
```

**Note:** If your styles have dashes in their names, use bracket notation:

```
const className = styles["foo-with-dash"];
```

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/css-modules.mdx)
