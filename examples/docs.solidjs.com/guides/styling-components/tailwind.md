Title: TailwindCSS - SolidDocs

URL Source: https://docs.solidjs.com/guides/styling-components/tailwind

Markdown Content:
Styling your Components[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/styling-components/tailwind.mdx)

[Tailwind CSS](https://tailwindcss.com/) is an on-demand utility CSS library that integrates seamlessly with Solid as a built-in PostCSS plugin.

* * *

1.  Install Tailwind CSS as a development dependency:

2.  Next, run the init command to generate both `tailwind.config.js` and `postcss.config.js`.

3.  Since TailwindCSS is configuration-driven, after initializing, a `tailwind.config.js` file will be created at the root of your project directory:

```
/** @type {import('tailwindcss').Config} */module.exports = {  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],  theme: {    extend: {},  },  plugins: [],};
```

For a deeper dive into configuration, you can check out the [Tailwind Official Documentation](https://tailwindcss.com/docs/configuration).

* * *

In your `src/index.css` file, add the following Tailwind directives:

```
@tailwind base;@tailwind components;@tailwind utilities;
```

These directives inform PostCSS that you're using Tailwind and establish the order of the directives. You can append custom CSS below these directives.

* * *

Import your `index.css` file into the root `index.jsx` or `index.tsx` file:

```
import { render } from "solid-js/web"import App from "./App"import "./index.css"render(() => <App />, document.getElementById('root') as HTMLElement);
```

* * *

With Tailwind CSS set up, you can now utilize its utility classes. For instance, if you previously had a `Card.css` file, you can replace or remove it:

```
/* Remove or replace these styles with Tailwind utility classes */
```

Update your components to use Tailwind's utility classes:

```
function Card() {  return (    <div class="grid place-items-center min-h-screen">      <div class="h-[160px] aspect aspect-[2] rounded-[16px] shadow-[0_0_0_4px_hsl(0_0%_0%_/_15%)]">        Hello, world!      </div>    </div>  );}
```

* * *

For additional assistance, refer to the [Tailwind CSS/Vite integration guide](https://tailwindcss.com/docs/guides/vite).

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/styling-components/tailwind.mdx)
