Title: Context - SolidDocs

URL Source: https://docs.solidjs.com/concepts/context

Markdown Content:
Context provides a way to pass data through the component tree without having to pass props down manually at every level.

* * *

[When to use context](https://docs.solidjs.com/concepts/context#when-to-use-context)
------------------------------------------------------------------------------------

When you have a large [component tree](https://docs.solidjs.com/concepts/components/basics#component-trees) that requires state to be shared, context can be used. Context can be employed to avoid [prop drilling](https://docs.solidjs.com/concepts/components/props#prop-drilling), which is the practice of passing props through intermediate elements without using them directly.

If you want to avoid passing some props through a few layers, when applicable, adjusting your component hierarchy may be an easier solution. [Signals](https://docs.solidjs.com/concepts/signals) are often the simplest solution since they can be imported directly into the components that need them.

Context, however, is designed to share data that is global to an application or for information that is regularly accessed by multiple components in an application's component tree. This offers a way to access state across an application without passing props through intermediate layers or importing them directly into components.

* * *

[Creating context](https://docs.solidjs.com/concepts/context#creating-context)
------------------------------------------------------------------------------

Context is created using the [`createContext`](https://docs.solidjs.com/reference/component-apis/create-context) function. This function has a `Provider` property that wraps the component tree you want to provide context to.

```
import { createContext } from "solid-js";const MyContext = createContext();export const Provider = (props) => {  return <MyContext.Provider>{props.children}</MyContext.Provider>;};
```

* * *

[Providing context to children](https://docs.solidjs.com/concepts/context#providing-context-to-children)
--------------------------------------------------------------------------------------------------------

To pass a value to the `Provider`, you use the `value` prop which can take in any value, including [signals](https://docs.solidjs.com/concepts/context#updating-context-values). Once a value is passed to the `Provider`, it is available to all components that are descendants of the `Provider`.

When passing a single value, it can be directly passed to the `value` prop:

```
import { createContext, useContext } from "solid-js";const MyContext = createContext("initial");const Provider = (props) => (  <MyContext.Provider value="new value">{props.children}</MyContext.Provider>);
```

However, if you need to access multiple values, they must be passed as an object literal, or using double curly braces (`{{ }}`):

```
import { createContext, createSignal } from "solid-js";const MyContext = createContext("default value");export const Provider = (props) => {  const stringVal = "new value";  const numberVal = 3;  const objVal = {    foo: "bar",    obj: true,  };  return (    <MyContext.Provider      value={{        stringVal,        numberVal,        objVal,      }}    >      {props.children}    </MyContext.Provider>  );};
```

* * *

[Consuming context](https://docs.solidjs.com/concepts/context#consuming-context)
--------------------------------------------------------------------------------

Once the values are available to all the components in the context's component tree, they can be accessed using the [`useContext`](https://docs.solidjs.com/reference/component-apis/use-context) utility. This utility takes in the context object and returns the value(s) passed to the `Provider`:

```
import { createContext, useContext } from "solid-js";const MyContext = createContext();const Provider = (props) => (  <MyContext.Provider value="new value">{props.children}</MyContext.Provider>);const Child = () => {  const value = useContext(MyContext);  return <>{value}</>;};export const App = () => (  <Provider>    <Child /> {/* "new value" */}  </Provider>);
```

When you are passing multiple values into the `Provider`, you can destructure the context object to access the values you need. This provides a readable way to access the values you need without having to access the entire context object:

```
import { createContext, useContext, createSignal } from "solid-js";const MyContext = createContext();const Provider = (props) => {  const stringVal = "new value";  const numberVal = 3;  const objVal = {    foo: "bar",    obj: true,  };  return (    <MyContext.Provider      value={{        stringVal,        numberVal,        objVal,      }}    >      {props.children}    </MyContext.Provider>  );};const Child = () => {  const { stringVal, numberVal } = useContext(MyContext);  return (    <>      <h1>{stringVal}</h1>      <span>{numberVal}</span>    </>  );};export const App = () => (  <Provider>    <Child />  </Provider>);
```

* * *

[Customizing context utilities](https://docs.solidjs.com/concepts/context#customizing-context-utilities)
--------------------------------------------------------------------------------------------------------

When an application contains multiple context objects, it can be difficult to keep track of which context object is being used. To solve this issue, you can create a custom utilities to create a more readable way to access the context values.

For example, when wrapping a component tree, you may want to create a custom `Provider` component that can be used to wrap the component tree. This also provides you with the option of re-using the `Provider` component in other parts of your application, if needed.

```
import { createSignal, createContext, useContext } from "solid-js";const CounterContext = createContext();export function CounterProvider(props) {  let count = 0;  return (    <CounterContext.Provider value={count}>      {props.children}    </CounterContext.Provider>  );}
```

Now if you had to access the Provider in different areas of your application, you can simply import the `CounterProvider` component and wrap the component tree:

```
import { CounterProvider } from "./counterProvider";export function App() {  return (    <CounterProvider count={1}>      <h1>Welcome to Counter</h1>      <NestedComponents />    </CounterProvider>  );}
```

Similarly, you can create a custom utility to access the context values. Instead of importing `useContext` and passing in the context object on each component that you're using it in, creating a customized utility can make it easier to access the values you need:

```
export function useCounter() {  return useContext(CounterContext);}
```

The `useCounter()` utility in this example can now be imported into any component that needs to access the context values:

```
import { useCounter } from "./counter";export function CounterProvider(props) {  const count = useCounter();  return (    <>      <div>{count()}</div>    </>  );}
```

* * *

[Updating context values](https://docs.solidjs.com/concepts/context#updating-context-values)
--------------------------------------------------------------------------------------------

[Signals](https://docs.solidjs.com/concepts/signals) offer a way to synchronize and manage data shared across your components using context. You can pass a signal directly to the `value` prop of the `Provider` component, and any changes to the signal will be reflected in all components that consume the context.

This offers a way to manage state across your components without having to pass props through intermediate elements.

* * *

[Debugging with context](https://docs.solidjs.com/concepts/context#debugging-with-context)
------------------------------------------------------------------------------------------

`createContext` takes in an _optional_ default value and it is possible it can return `undefined` if not provided. When working with TypeScript, this can introduce type issues that make it difficult to determine why your component is not rendering as expected.

To solve this issue, a default value can be specified when creating a context object, or errors can be handled manually through the use of a custom `useMyContext` utility:

```
import { createContext, useContext } from "solid-js";const MyContext = createContext<string>();function useMyContext() {  const value = useContext(MyContext);  if (value === undefined) {    throw new Error("useMyContext must be used within a MyContext.Provider");  }  return value;}function Child() {  const value = useMyContext();  return <div>{value}</div>;}
```
