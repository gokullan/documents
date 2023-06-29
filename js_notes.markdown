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

-   map

-   clipboard

    -   navigator.clipboard.writeText(content)

## String Manipulation
-   `stringName.toUpperCase()` (OR) `stringName.toLowerCase()`
-   `stringName.repeat(x)`
-   `number.toString(base)`
-   `stringName.includes(substring, start_idx)` - search for a substring (case-sensitive)
-   `stringName.indexOf()` -   returns the first occurence of specified substring; -1 if not found   
-   `replace`

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

    -   arrayName.filter((element)=\>{

        -   return this.element == something

        })


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

Doubts

-   document.write() vs writeln()
-   let vs. var
-   more on form validation (.value)
-   collections in JS
-   JS events
