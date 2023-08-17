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
-   (js-cookie documentation)[https://www.npmjs.com/package/js-cookie/v/3.0.5]

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
    (function test() {
        // function body
    })()  // this is immediately invoked after the script is loaded
    ```
-   Block scope can be obtained using `let`
-   [Ref. Book](https://github.com/getify/You-Dont-Know-JS) by Kyle Simpson

## JS Compilation and Interpretation
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

## Closures

Doubts

-   document.write() vs writeln()
-   let vs. var
-   more on form validation (.value)
-   collections in JS
-   JS events
