Title: Stores - SolidDocs

URL Source: https://docs.solidjs.com/concepts/stores

Markdown Content:
Similar to [signals](https://docs.solidjs.com/concepts/signals), stores are state management primitive. However, while signals manage a single piece of state, stores create a centralized location to reduce code redundancy. Within Solid, these stores can spawn a collection of reactive signals, each corresponding to a particular property which can be useful when working with complex state.

* * *

Stores can manage many data types, including: objects, arrays, strings, and numbers.

Using JavaScript's [proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) mechanism, reactivity extends beyond just the top-level objects or arrays. With stores, you can now target nested properties and elements within these structures to create a dynamic tree of reactive data.

```
import { createStore } from "solid-js/store"// Initialize storeconst [store, setStore] = createStore({  userCount: 3,  users: [    {      id: 0,      username: "felix909",      location: "England",      loggedIn: false,    },    {      id: 1,      username: "tracy634",      location: "Canada",      loggedIn: true,    },    {      id: 1,      username: "johny123",      location: "India",      loggedIn: true,    },  ],})
```

* * *

Store properties can be accessed directly from the state proxy through directly referencing the targeted property:

```
console.log(store.userCount) // Outputs: 3
```

Accessing stores within a tracking scope follows a similar pattern to signals. While signals are created using the [`createSignal`](https://docs.solidjs.com/reference/basic-reactivity/create-signal) function and require calling the signal function to access their values, store values can be directly accessed without a function call. This provides access to the store's value directly within a tracking scope:

```
const App = () => {  const [mySignal, setMySignal] = createSignal("This is a signal.")  const [store, setStore] = createStore({    userCount: 3,    users: [      {        id: 0,        username: "felix909",        location: "England",        loggedIn: false,      },      {        id: 1,        username: "tracy634",        location: "Canada",        loggedIn: true,      },      {        id: 2,        username: "johny123",        location: "India",        loggedIn: true,      },    ],  })  return (    <div>      <h1>Hello, {store.users[0].username}</h1> {/* Accessing a store value */}      <span>{mySignal()}</span> {/* Accessing a signal */}    </div>  )}
```

When a store is created, it starts with the initial state but does _not_ immediately set up signals to track changes. These signals are created **lazily**, meaning they are only formed when accessed within a reactive context.

Once data is used within a reactive context, such as within the return statement of a component function, computed property, or an effect, a signal is created and dependencies are established.

For example, if you wanted to print out every new user, adding the console log below will not work because it is not within a tracked scope.

```
const App = () => {  const [store, setStore] = createStore({    userCount: 3,    users: [ ... ],  })  const addUser = () => { ... }  console.log(store.users.at(-1)) // This won't work  return (    <div>      <h1>Hello, {store.users[0].username}</h1>      <p>User count: {store.userCount}</p>      <button onClick={addUser}>Add user</button>    </div>  )}
```

Rather, this would need to be in a tracking scope, like inside a [`createEffect`](https://docs.solidjs.com/reference/basic-reactivity/create-effect), so that a dependency is established.

```
const App = () => {  const [store, setStore] = createStore({    userCount: 3,    users: [ ... ],  })  const addUser = () => { ... }  console.log(store.users.at(-1))  createEffect(() => {    console.log(store.users.at(-1))  })  return (    <div>      <h1>Hello, {store.users[0].username}</h1>      <p>User count: {store.userCount}</p>      <button onClick={addUser}>Add user</button>    </div>  )}
```

* * *

Updating values within a store is best accomplished using a setter provided by the `createStore` initialization. This setter allows for the modification of a specific key and its associated value, following the format `setStore(key, newValue)`:

```
const [store, setStore] = createStore({  userCount: 3,  users: [ ... ],})setStore("users", (currentUsers) => [  ...currentUsers,  {    id: 3,    username: "michael584",    location: "Nigeria",    loggedIn: false,  },])
```

The value of `userCount` could also be automatically updated whenever a new user is added to keep it synced with the users array:

```
const App = () => {  const [store, setStore] = createStore({    userCount: 3,    users: [ ... ],  })  const addUser = () => { ... }  createEffect(() => {    console.log(store.users.at(-1))    setStore("userCount", store.users.length)  })  return (    <div>      <h1>Hello, {store.users[0].username}</h1>      <p>User count: {store.userCount}</p>      <button onClick={addUser}>Add user</button>    </div>  )}
```

* * *

Modifying a store using this method is referred to as "path syntax." In this approach, the initial arguments are used to specify the keys that lead to the target value you want to modify, while the last argument provides the new value.

String keys are used to precisely target particular values with path syntax. By specifying these exact key names, you can directly retrieve the targeted information. However, path syntax goes beyond string keys and offers more versatility when accessing targeted values.

Instead of employing the use of just string keys, there is the option of using an array of keys. This method grants you the ability to select multiple properties within the store, facilitating accessed to nested structures. Alternatively, you can use filtering functions to access keys based on dynamic conditions or specific rules.

The flexibility in path syntax makes for efficient navigation, retrieval, and modification of data in your store, regardless of the store's complexity or the requirement for dynamic access scenarios within your application.

* * *

Path syntax provides a convenient way to modify arrays, making it easier to access and update their elements. Instead of relying on discovering individual indices, path syntax introduces several powerful techniques for array manipulation.

### [Appending new values](https://docs.solidjs.com/concepts/stores#appending-new-values)

To append a new element to an array within a store, you specify the target array and set the index to the desired position. For example, if you wanted to append the new element to the end of the array, you would set the index to `array.length`:

```
setStore("users", (otherUsers) => [  ...otherUsers,  {    id: 3,    username: "michael584",    location: "Nigeria",    loggedIn: false,  },])// can becomesetStore("users", store.users.length, {  id: 3,  username: "michael584",  location: "Nigeria",  loggedIn: false,})
```

### [Range specification](https://docs.solidjs.com/concepts/stores#range-specification)

With path syntax, you can target a subset of elements to update or modify by specifying a range of indices. You can do this using an array of values:

```
setStore("users", [1, 3], "loggedIn", false)
```

### [Dynamic value assignment](https://docs.solidjs.com/concepts/stores#dynamic-value-assignment)

Path syntax also provides a way to set values within an array using functions instead of static values. These functions receive the old value as an argument, allowing you to compute the new value based on the existing one. This dynamic approach is particularly useful for complex transformations.

```
setStore("users", 3, (loggedIn) => !loggedIn)
```

### [Filtering values](https://docs.solidjs.com/concepts/stores#filtering-values)

In scenarios where you want to update elements in an array based on a specific condition, you can pass a function as an argument. This function will act as a filter, allowing you to select elements that satisfy the condition. It receives the old value and index as arguments, providing the flexibility to make conditional updates.

```
setStore("users", (user) => user.username.startsWith("t"), "loggedIn", false)
```

In addition to [`.startsWith`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith), you can use other array methods like [`.find`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) to filter for the values that you need.

* * *

When using store setters to modify objects, if a new value is an object, it will be shallow merged with the existing value. What this refers to is that the properties of the existing object will be combined with the properties of the "new" object you are setting, updating any overlapping properties with the values from the new object.

What this means, is that you can directly make the change to the store _without_ spreading out properties of the existing user object.

```
setStore("users", 0, {  id: 109,})// is equivalent tosetStore("users", 1, (user) => ({  ...user,  id: 69420,}))
```

* * *

### [Store updates with `produce`](https://docs.solidjs.com/concepts/stores#store-updates-with-produce)

Rather than directly modifying a store with setters, Solid has the `produce` utility. This utility provides a way to work with data as if it were a [mutable](https://developer.mozilla.org/en-US/docs/Glossary/Mutable) JavaScript object. `produce` also provides a way to make changes to multiple properties at the same time which eliminates the need for multiple setter calls.

```
import { produce } from "solid-js/store"// without producesetStore("users", 0, "username", "newUsername")setStore("users", 0, "location", "newLocation")// with producesetStore(  "users",  0,  produce((user) => {    user.username = "newUsername"    user.location = "newLocation"  }))
```

`produce` and `setStore` do have distinct functionalities. While both can be used to modify the state, the key distinction lies in how they handle data. `produce` allows you to work with a temporary draft of the state, apply the changes, then produce a new [immutable](https://developer.mozilla.org/en-US/docs/Glossary/Immutable) version of the store. Comparatively, `setStore` provides a more straightforward way to update the store directly, without creating a new version.

It's important to note, however, `produce` is specifically designed to work with **arrays** and **objects**. Other collection types, such as JavaScript [Sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) and [Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), are not compatible with this utility.

### [Data integration with `reconcile`](https://docs.solidjs.com/concepts/stores#data-integration-with-reconcile)

When new information needs to be merged into an existing store `reconcile` can be useful. `reconcile` will determine the differences between new and existing data and initiate updates only when there are _changed_ values, thereby avoiding unnecessary updates.

```
const { createStore, reconcile } from "solid-js/stores"const [data, setData] = createStore({  animals: ['cat', 'dog', 'bird', 'gorilla']})const newData = getNewData() // eg. contains ['cat', 'dog', 'bird', 'gorilla', 'koala']setData('animals', reconcile(newData))
```

In this example, the store will look for the differences between the existing and incoming data sets. Consequently, only `'koala'` - the new edition - will cause an update.

When there is a need for dealing with data outside of a reactive context, the `unwrap` utility offers a way to transform a store to a standard [object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object). This conversion serves several important purposes.

Firstly, it provides a snapshot of the current state without the processing overhead associated with reactivity. This can be useful in situations where an unaltered, non-reactive view of the data is needed. Additionally, `unwrap` provides a means to interface with third-party libraries or tools that anticipate regular JavaScript objects. This utility acts as a bridge to facilitate smooth integrations with external components and simplifies the incorporation of stores into various applications and workflows.

```
import { createStore, unwrap } from "solid-js/store"const [data, setData] = createStore({  animals: ["cat", "dog", "bird", "gorilla"],})const rawData = unwrap(data)
```

To learn more about how to use Stores in practice, visit the [guide on complex state management](https://docs.solidjs.com/guides/complex-state-management).
