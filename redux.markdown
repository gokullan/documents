# Redux

"A predictable state container for JavaScript applications"
-   Redux is framework-agnostic
-   Redux-toolkit (also framework-agnostid) is the preferred way for writing
    Redux code to overcome the latter's limitions
-   `redux-react` is the package used to bind React with Redux (toolkit?)

## 3 core concepts
-   Store
-   Action
    -   An object that contains the property `type` (a description of what needs
        to be done)
    -   Action-creater: The function that creates this object
-   Reducer
    -   A function that returns the next state given the previous state and
        current context

## 3 principles
-   There is only 1 state object that is shared by all components
-   Updation of states can only be done by the components dispatching actions
-   States changes are made with pure reducers

<img src="./images/redux_3_principles.png" width="500px">

## Code
