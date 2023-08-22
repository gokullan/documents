# React
-   `npm install` to install dependencies (from package.json)
-   `index.js` kick-starts the application and injects React components into DOM 
-   React components are written in JSX. Babel converts JSX into HTML
-   A component is a function that (usually) returns a JSX template. It should be exported to be used in other places.
-   Dynamic inline styling: `<h1 style={{propertyInCamelCase: "stringValue"}}>Something</h1>`
-   Responding to events: If arguments need to be passed to the event handler function, wrap it inside an anonymous function.
    
    ```
    ... onClick={ () => {
                funcWithArg(a1, a2);
            }
        }
    ```
-   Event object is automatically captured as the first parameter to the event handling function.
-   State of a component is the data being used by that component at a given instance of time.
-   Hooks are special types of functions in React
-   Use Array.map to iterate through a list and display its elements. Be sure to attach the `key` attribute in the template. Refer [here](https://bobbyhadz.com/blog/react-loop-through-array-of-objects)
-   Props
    -   Used to pass data from parent component to child component
    ```javascript
    <ChildComponent propertyName={variable} />
    ...
    // Inside ChildComponent.js
    const ChildComponent = (props) => {
        // access the parent-component data as props.propertyName
    }

    ```
    -   Updating states from child component
        -   Define update function in parent component (since that is where the state resides) and pass the function as props
        -   Now, use this function inside the child component
    -   Using JSON sever
        -   Each top-level property in a JSON server(file?) is considered a resource that can be accessed using endpoints(?)
        -   `npx json-server --watch <path-to-json-file> --port 8000`
        -   Use `useEffect` to load this data into a state
        ```javascript
        useEffect(() => {
            fetch(URL)
            .then(res => res.json())  // convert response to JS object
            .then(data => {
                setVar(data);
            })
        })
        ```
    -   Conditional template
        `{varName && <SomeTag>}`

## Hooks
-   `useState`
    -   Used to create reactive variables, i.e., whenever changes to the variable occur (via `setState`), React re-renderes the template corresponding to the component.
    ```javascript
    import { useState } from 'react'
    const [varName, setVarName] = useState("some initial value");
    ...
    setVarname("new value")
    ```
-   `useEffect`
    -   This hook runs the specified function every time the component (re-)renders to the browser, (i.e.), initially when the application loads and everytime a state changes
    -   Use a dependency array (2nd argument to `useEffect`) to trigger the function only for certain state changes
    -   &#10071; If `setState` is used inside `useEffect`, it will lead to an infinite loop UNLESS the dependency array is empty.
    ```javascript
    import { useEffect } from 'react';
    useEffect(() => {
        // function
    }, [variablesToWatch]) 
    // above function runs only when the values of `variablesToWatch` changes
    ```

## Some useful JS functions
-   Array API
    -   map
    -   filter
    ```javascript
    filteredArray = myArray.filter((arrayItem) => {
        // if item needs to be kept in array, return true; else false
    })
    ```
    -   `setTimeout(() => {}, 1000)`

## Doubts
-   How does SPA work in the context of React?
-   What is webpack?
-   What is a transpiler (Babel)?
-   What is `npx`?
-   Why do we need to 'watch' the JSON file (in the context of using JSON server)?
-   Passing function as props (`handleDelete` in The Net Ninja series)
