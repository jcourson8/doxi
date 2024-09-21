Title: Environment variables - SolidDocs

URL Source: https://docs.solidjs.com/configuration/environment-variables

Markdown Content:
Environment variables - SolidDocs
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

Configuration

Environment variables
=====================

[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/configuration/environment-variables.mdx)

Solid is built on top of [Vite](https://vitejs.dev/), which offers a convenient way to handle environment variables.

* * *

[Public Environment Variables](https://docs.solidjs.com/configuration/environment-variables#public-environment-variables)
-------------------------------------------------------------------------------------------------------------------------

Public variables are considered safe to expose to the client-side code. These variables are prefixed with `VITE_` and are injected into the client-side code during compilation time.

In the root directory of the project, create a file called `.env`. This file will store environment variables in the `key = value` format.

If working with TypeScript it is possible to make such variables type-safe and enable your TypeScript Language Service Provider (LSP) to autocomplete them by creating a file called `.env.d.ts` in the root directory of the project.

```
interface ImportMetaEnv {  readonly VITE_USER_ID: string;  readonly VITE_PUBLIC_ENDPOINT: string;}
interface ImportMeta {  readonly env: ImportMetaEnv;}
```

Info:

To prevent accidental exposure of environment variables to the client, only variables prefixed with `VITE_` will be exposed.

For example:

```
VITE_SECRET_KEY = 123helloDB_PASSWORD = foobar
```

Only the `VITE_SECRET_KEY` will be exposed to client source code, while `DB_PASSWORD` will not, as shown below.

```
console.log(import.meta.env.VITE_SECRET_KEY); // 123helloconsole.log(import.meta.env.DB_PASSWORD); // undefined
```

```
function MyComponent() {  return (    <div>      <h2>        Component with environment variable used{" "}        {import.meta.env.VITE_VARIABLE_NAME}        the value will be replaced during compilation time.      </h2>    </div>  );}
```

* * *

[Private Environment Variables](https://docs.solidjs.com/configuration/environment-variables#private-environment-variables)
---------------------------------------------------------------------------------------------------------------------------

These variables should only be accessed in your backend code, and so it's best to not use `VITE_` prefix for them. Instead, use `process.env` to access them. Depending on the [Nitro preset](https://nitro.unjs.io/deploy) chosen, they'll be made available automatically or they will require an external dependency such as [dotenv](https://www.npmjs.com/package/dotenv).

```
DB_HOST="somedb://192.110.0"DB_PASSWORD = super_secret_password_hash
```

To access them, within your backend code, use `process.env`. For an example, check the pseudo-code below.

```
  "use server"
  const client = new DB({    host: process.env.DB_URL,    password: process.env.DB_PASSWORD  });}
```

It is also possible to make `process.env` type-safe via the same `.env.d.ts` file.

```
declare namespace NodeJS {  interface ProcessEnv {    readonly DB_URL: string    readonly DB_PASSWORD: string  }}
```

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/configuration/environment-variables.mdx)

Previous[← Zerops](https://docs.solidjs.com/guides/deployment-options/zerops)

Next[TypeScript →](https://docs.solidjs.com/configuration/typescript)

On this page

1.  [Overview](https://docs.solidjs.com/configuration/environment-variables#_top)

Contribute

1.  [Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/configuration/environment-variables.mdx)
2.  [Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/configuration/environment-variables.mdx)
