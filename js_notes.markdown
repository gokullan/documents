JS Notes

-   Case-sensitive

-   Statements end with ';'

-   Comments

    -   multi-line: /\* \*/
    -   single-line: //

-   Not sensitive to white-space

-   Weakly-typed language; dynamic types

    -   var myVariable = 10;
    -   myVariable = "Hi!"
    -   variables must not start with number, but can contain letters,
        \_ , \$

-   Looping through an array --
    <https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript>

-   To add CSS in JS

    -   element.style.backgroundColor = "#333"

-   3 dot (...) syntax (Read more [here](https://codeburst.io/what-are-three-dots-in-javascript-6f09476b03e1))
```js
array2 = [...array1];
// array2 is independent of array1 
// (assignment operator will copy array1 by reference)
```

-   DOM traversal

    -   document.getElementById("")
    -   getElementByClassName("") - returns multiple elements
    -   querySelector("\<cssSelector\>") - returns only one element (the
        1^st^ one if there are multiple)
    -   querySelectorAll("") - returns all elements that match the given
        selector
    -   element.children
    -   className.querySelector('') ?
    -   element.parentElement (or) element.ParentNode
    -   element.closest('') - selects the closest selector moving
        upwards (like querySelector, but upwards)
    -   element.nextElementSibling (or) element.nextSibling
    -   element.previousElementSibling

-   arrayName.forEach(\<functionName\>)

-   **Array.from**(document.getElementByClass("\<className\>")) - to
    convert to an array

-   DOM manipulation

```{=html}
<!-- -->
```
-   forEach

    -   arrayName.forEach(someFunction)
    -   arrayName.forEach(element =\> {

> \<\< write function here \>\>

});

-   JS regex

    -   pattern.test("someString")

-   Arrow function

-   clipboard

    -   navigator.clipboard.writeText(content)

-   UTF-8 encoding
    -   Uses 1 to 4 bytes for character encoding
    -   [Reference](https://stackoverflow.com/questions/10229156/how-many-characters-can-utf-8-encode) 

-   `encodeURIComponent`
    -   Used to encode data sent from the user's side
        -   Needed to ensure characters like `&` are not interpreted incorrectly
    -   The encoding is done based on UTF-8 encoding

## String Manipulation
-   `stringName.toUpperCase()` (OR) `stringName.toLowerCase()`
-   `stringName.repeat(x)`
-   `number.toString(base)`
-   `stringName.includes(substring, start_idx)` - search for a substring (case-sensitive)
-   `stringName.indexOf()` -   returns the first occurence of specified substring; -1 if not found   
-   `replace`
-   `stringName.trim()` - removes whitespace from both ends of the string

## Array
-   array.findIndex(function(element) { /\* \... \*/ }) OR
    array.findIndex(element =\> { /\* \... \*/ })

-   Deletion of elements from an array

    -   arrName.splice(startIndex, n)
    -   

-   Function()

-   **slice**()

    -   stringName.slice(beginIndex)
    -   stringName.slice(beginIndex, endIndex)

-   sort

-   filter() - to return a filtered array
```js
arrayName.filter((element)=> {
    return this.element == something
})
```

-   map: To execute a function on every element of an array
```js
arr = [1, 2, 3]
new_arr = arr.map((e) => e + 1);
// new_arr = [2, 3, 4]
```

-   [map vs. forEach vs. every](https://stackoverflow.com/questions/7340893/what-is-the-difference-between-map-every-and-foreach)

-   reduce

-   setTimeOut(function(), \<time_in_ms\>)

-   setTimeInterval

-   clearInterval

-   Form validation

    -   Refer regex assignment docx
    -   <https://stackoverflow.com/questions/16134733/html-javascript-simple-form-validation-on-submit>
    -   <https://stackoverflow.com/questions/5195933/with-form-validation-why-onsubmit-return-functionname-instead-of-onsubmit>

## JSON
-   JSON.parse(jsonObj) returns a Javascript object
-   JSON.stringify(jsObj);

## Object
-   Object.keys(obj) returns the property names of the specified object as an array

-   Get all form data using FormData() --
    <https://stackoverflow.com/questions/588263/how-can-i-get-all-a-forms-values-that-would-be-submitted-without-submitting>

-   Capturing events in \<select\> -
    <https://stackoverflow.com/questions/14651955/capture-events-in-select-list>

-   Blob, localStorage and fileReader --
    <https://hacks.mozilla.org/2012/02/saving-images-and-files-in-localstorage/>

-   **Promises** --
    <https://www.freecodecamp.org/news/how-to-write-a-javascript-promise-4ed8d44292b8/>

## URL encoding-decoding
-   `decodeURI`
-   `decodeURIComponent`

## Cookies
-   [js-cookie documentation](https://www.npmjs.com/package/js-cookie/v/3.0.5)

## Scopes
-   Note: Functions are actually objects in JavaScript
    -   The function name is a variable that is bound to the function object
-   Scope dictates the portion of the program where a given variable is accessible
-   How to restrict scope?
    -   Enclosing code in curly braces does not create a scope in JS (like it does in C++, Java, ...)
    -   To create a local variable, declare it inside a function
    ```js
    if (1) {
        var a = 10;  // global
    }
    function test() {
        var b = 10;  // local
        console.log(a)  // 10
        a = 20;
    }
    test();
    console.log(a)  // 20
    console.log(b)  // runtime error
    ```
-   JS has functional scoping - any variable created within a function is available only inside that function
    -   Method args create (new) locally scoped variables (write operation)
        (clarify &#x2753;)
    -   If you use a variable without declaring, it is okay to do a write operation, but not a read
-   Why global vars are an issue?
    -   All JS scripts of a given webpage have the same namespace. This means that:
    1.   One (malicious?) script can modify a global variable used by another
    2.   Unintended changes due to clash of variable names result.
-   IIFE - Immediately Invoked Function Execution
    -   Simply enclosing a variable inside a function alone is not sufficient to eliminate the above issue.
    -   Since a function is an object, the function name also becomes a global variable and we are back to $1^2$
    -   Here is a workaround
    ```js
    (function () {
        // function body
    })()  // this is immediately invoked after the script is loaded
    ```
-   Block scope can be obtained using `let`
-   [Ref. Book](https://github.com/getify/You-Dont-Know-JS) by Kyle Simpson

## JS Compilation and Interpretation
-   JS is both compiled and interpreted
    -   Compilation step happens just before interpretation
    -   Compilation entails "making notes" from the source code to ensure it has
        everything for execution (not creating an intermediary code as in case
of other compilers)
-   Global object depends on the runtime (`window` for browser, `global` for
    node)

### Compilation
-   The "compiler" makes note of all variables and their scopes
    -   Looks at `var`, function declarations and arguments
-   Creates a "scope chain"
-   Global variables (properties of the global object) are super-scoped and all others are function-scoped.
### Interpretation
-   Resolves variable references from the scope chain and executes the code
-   If a variable is not found in the currently executing scope, it keeps going one level up in the scope chain until 
    that variable is resolved
-   If the global scope search is negative, then it means that the variable has not been declared. But - 
    -   If that variable is used in a write operation, then JS creates that variable in the global scope
        (irrespective of which scope the corresponding piece of code is in)!
    -   Else (for a read operation), an error is thrown

<img src="./images/js_compilation_interpretation.png">

```js
// example
console.log(a);  // `undefined`, no error
var a = 10;
```
-   Hoisting
    -   Due to the 2-step process, it feels as if the variable declarations are
        hoisted (pushed to the top) and then the code executes
    -   This addtionally has implications for 2 (or more) functions calling each
        other
    ```js
    function fn1() {
        fn2();
    } 

    function fn2() {
        fn1();
    }
    ```
    -   Note that the above does not work for function expressions since
        assignments are made by the interpreter (a function
        declaration results in a function object being created in the
compilation step itself).
-   Strict mode: Place `"use strict";` at the top of the JS file. (can also be
    applied to just a function) (Why is strict mode needed &#x2753;)

## Closures
-   For a JS function expression, the scope information* is also attached to the
    variable (in addition to the function definition itself)
-   \*scope information => Pointer to actual variables (at the time the function
    was declared?)
    -   This means that the scope a function is executing in need not contain
        the actual variables.
-   In simple terms, a closure is a function that remembers its scope
-   In depth
    -   Variables declared in a function are created each time that function is
        called
```js
var a = 10;  // global

function outer() {
    var b = 20;  // created every time `outer` is executed
    var inner = function() {
        a++;
        b++;
        console.log(a);
        console.log(b);
    }
    return inner;
}

var inner1 = outer()  // global `a` and `b` attached to inner1
inner1();
// 11
// 21

var inner2 = outer() // global `a` and new `b` attached to inner2
inner2();
// 12
// 21
```

-   `setTimeout(fn, 1000)` is a practical example of closures being used.

### The Module Pattern
-   A workaround to have getters and setters (make properties of an object
    private)
```js
function createObj() {
    var somePrivateVar = 10;
    var objToReturn = {
        "getPrivateVar": function() {
            return somePrivateVar;
        }
    }
    return objToReturn;
}

var obj = createObj();
console.log(obj.getPrivateVar()); // 10
console.log(obj.somePrivateVar);  // undefined
```
-   This works because of the concept of closures - the getters and setters
    remember the variables used inside them.

### Closures and Async functions
```js
var i;
for(i = 0; i < 10; ++i) {
    setTimeout(
        function() {
            console.log(i);  // 10 is printed 10 times
        }, 1000
    )
}
```
-   The problem with the above snippet is that all the setTimeout calls point to
    the *same* variable `i` (the one in the global scope).
-   Because all these calls get executed after the `for` loop completes, all
    calls print the final value of `i` which is 10
-   To solve this problem, we need each calls to point to a  different variable.
```js
for(i = 0; i < 10; ++i) {
    (function() {
        var currValue = i;
        setTimeout(
            function() {
                console.log(currValue); // expected behaviour
            }, 1000
        )
    }
    )();
}
```
-   **Note:** "The argument-function of the method setTimeout is always executed
    last: once the entire code of the file has been executed." (Refer comment
[here](https://youtu.be/RU-QXuhOSy0))

-   [Load scripts asynchronously](https://stackoverflow.com/questions/7718935/load-scripts-asynchronously)
-   Autoscroll to end of `div`
```js
if (condition) {
    divNode.scrollTop = divNode.scrollHeight;
}
```

### Datetime stuff
-   HH:MM:SS to seconds - [source](https://stackoverflow.com/questions/9640266/convert-hhmmss-string-to-seconds-only-in-javascript)
```js
'01:02:03'.split(':').reduce((acc,time) => (60 * acc) + +time);
```
-   Sort data by time
```js
data.sort(function (a, b) {
    return a.time.localeCompare(b.time);
});
```

### JS Under the Hood
- Thread of execution
  - JS is single threaded and synchronous (but with asynchronous capabilities)
  - A thread has a call stack and memory
  ```js
  // check the call stack
  function first() {
    console.log("First");
    second();
  }
  function second() {
    console.log("Second");
    second();
  }
  function third() {
    console.log("Third");
    second();
  }
  first();
  ```
  - Call stack manages execution context (Global Execution Context is at the
    bottom of the call stack)
- Execution context
  - A special environment for transformation and execution of JS code
  - 2 types: global and functional
  - 2 phases:
    - Memory Creation
      - Creates global object
      - Creates `this` and binds to the global object
      - Stores functions and sets variables to `undefined`
    - Execution
      - Executes code line by line
      - Creates new EC for every function call
  - ![Global EC creation example](./images/globalContextExample.jpg)
    - During this phase, `x` and `y` are created in the global scope and set to
      `undefined`
  - ![Functional EC](./images/functionContextExample.jpg)
- `let` vs. `var`
  - ![Scope of let](./images/letScope.jpg)
  - ![let vs. var](./images/varLet.jpg)

Doubts

-   document.write() vs writeln()
-   let vs. var
-   How do 2 async calls get executed in JavaScript (will the 2nd call return if
    it can complete in a shorter time?)
