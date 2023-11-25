\-\--Python\-\--

-   File Handling-

-   -   with open("filepath/filename.txt", "r") as fp

        -   Exceptions -- FileNotFoundError

    -   csv

    -   fp.readlines

    -   fp.readline

    -   fp.read(n) (n: number of characters to be read)

    -   fp.seek(offset, from_what)

        -   from_what = 0 (beginning), 1 (current position), 2 (end of
            file)

    -   EOF: if whatever_read == "" -
        <https://stackoverflow.com/questions/10140281/how-to-find-out-whether-a-file-is-at-its-eof>

    -   Reading/ writing objects to file (pickle) --
        <https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence>

-   Deep and shallow copy

    -   <https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/>
    -   Assigning 2d lists: new_list = copy.deepcopy(old_list) \# import
        copy

-   Sorting 2d lists: sorted_list = sorted(old_list, key=lambda x:
    x\[i\]) (i = 0 or 1)

-   Sorting files using iter() -
    <https://stackoverflow.com/questions/37145734/python-sorting-a-file-with-names-and-scores>

-   Heaps (import heapq)

    It is minheap by default. For maxheap, negate all elements and
    heapify.

```{=html}
<!-- -->
```
-   -   heapq.heapify(iterable)

    -   heapq.heappush(heap, ele)

    -   heapq.heappop(heap)

    -   heap.nlargest(n, iterable, key) \[return the n largest elements
        in the iterable\]

    -   User defined heap invariants (example)

        **class** **myList**(list):

        -   **def** \_\_lt\_\_(self, other):

            -   **return** self\[1\] \< other\[1\] *\# for min-heap
                based on 2*^*nd*^* list elements*

    -   Heap updation

        heap_dict = {key:\[element_1, element_2, \...\], \...}

        \# note that one of the elements would be the key itself

        heap = \[\[element_1, element_2, \...\], \...\]

        **def** heapupdate(to_update, new_value, heap, heap_dict):

        -   old_entry = heap_dict.pop(to_update)

            old_entry\[-1\] = 1

            \# note that old_entry would still be in the heap

            \# the last element in each entry needs to be an indicator
            if the entry is old/updated

            new_entry = new_value

            \# both the heap and the dictionary should have the same
            reference

            heapq.heappush(heap, new_entry)

            heap_dict\[to_update\] = new_entry

    -   see **functools.total_ordering** for more details on \_\_lt\_\_

-   Sets (unordered collection of unique elements -- ***see time
    complexity of every operation***)

```{=html}
<!-- -->
```
-   -   x = set(()) (OR) x = {1,2,3}

    -   x.add(n)

-   Dictionaries

    -   dict_name.pop(key) -- deletes and returns the value for
        dict_name\[key\]
    -   if key\_ in dict_name -- to check if a key exists
    -   dict_name.fromkeys(keys, value=None) - returns a dictionary with
        specified keys and the specified value (singular)

-   float("inf") -- for infinity

-   Queue implementations

    -   list

        -   list_name = \[\]
        -   list_name.append(value) -- to add at the end
        -   list_name.pop(index)

    -   **deque** *(from collections import deque)*

        -   q = deque()
        -   q.append(value)
        -   q.appendleft(value)
        -   q.pop()
        -   q.popleft()

    -   Queue *(from queue import Queue)*

-   Removing duplicates *(from collections import OrderedDict)*

    list(OrderedDict.fromkeys(list_name,val=None))

-   How to pass by reference (IMPORTANT!)

    <https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference>

-   Default arguments

    -   Do not pass mutable data types as default

    ![](Pictures/10000201000002120000015BB8C43CA32DB8564C.png){width="14.023cm"
    height="6.897cm"}

![](Pictures/100002010000021C0000011C9C1EF2EB39A2EADD.png){width="14.288cm"
height="7.514cm"}

-   Regex

    import re

    txt = 'This is the input string'

    re.search("\^.\$", txt)

    \# re.search returns a Match object

    \# other functions -- re.findall, re.split, re.sub

    <https://developers.google.com/edu/python/regular-expressions>

-   repr vs. str

    -   repr is used to be unambiguous (mainly intended for developers)

        -   repr returns a string that can be executed in Python

    -   str is used for readability

## JSON (`import json`)
-   Loading JSON: person_dict = json.loads(personJSON)
-   Pretty printing JSON: json.dumps(person_dict, indent=4,
        sort_keys=True)
-   Reading and writing to files
```python
# read
f = open("file_1", "r")
data = json.load(f)
# write
f = open("file_2", "w")
json.dump(data, f)
```
- [Reference](https://www.programiz.com/python-programming/json)

-   Object Oriented Programming

    -   Class -- A blueprint for a real-world entity

    -   Object -- an instance of a class

    -   Class = attributes (data) + methods (functions)

    -   Abstraction vs. Encapsulation --
        <https://stackoverflow.com/questions/15176356/difference-between-encapsulation-and-abstraction>

        <https://stackoverflow.com/questions/742341/difference-between-abstraction-and-encapsulation>

        -   **Encapsulation** -- **Information hiding** -- internal
            representation of a class is hidden (division of class
            members into those that can be manipluated outside and those
            that cannot, (i.e.), insulation of a part of the class from
            the rest)

        -   **Abstraction** -- **Implementation hiding** -- mechanics of
            how something works is hidden. Abstraction can be thought of
            as a generalization of a particular functionality. Eg: qsort
            is an abstration because one can use this function for any
            data type.

            -   Why is this a thing in OOPs? Doesn't it offer the same
                functionality as function calls?

        -   Eg: Car brake pedal and internal circuitry, calculator
            button and internal circuitry

    -   Inheritance

        -   

    -   Polymorphism

        -   Compile time

            -   Function Overloading, Operator Overloading

        -   Run time

            -   How can parent class variable store child class object
                (Java) (OR) how can parent class pointer variable point
                to child class objects? (in terms of memory) (OR) why
                can a variable's object type not be determined at
                compile time?
            -   Eg: Function Overriding (same function signature, but
                should the function of the parent class be called or the
                overriden function in the current(child) object be
                called?)
            -   Virtual functions

**VARIABLES**

-   -   Instance variables

        -   Data that is unique to each instance
        -   These are set using self.variableName

    -   Class variables

        -   Variables that are shared among all instances of a class

        -   Can be accessed through instance as well as class name

        -   When accessing a class variable through instance name --

            -   the namespace of the instance (objectName.\_\_dict\_\_)
                is checked first and if it is unavailable, it moves on
                to check the class variable
            -   However, when making an assignment, a new variable is
                created in the namespace of the object

        -   Using self.classVariableName in methods --

            -   This is better if you want to override the variable for
                a specific instance
            -   It also allows sub-class to override

**METHODS**

-   -   Instance methods

        -   When creating methods within class, they receive the first
            argument (*self* is used by convention when defining
            methods) as the class instance (which is passed
            automatically when the method is invoked).
        -   *\_\_init\_\_(self, args)* method will be run automatically
            when a class is created
        -   methods can also be run using the class name --
            Employee.fullname(emp1), where emp1 is an instance of class
            Employee

    -   Class methods

        -   Automatically take class name (conventially, *cls*) as the
            first argument

        -   use **\@classmethod** (this decorator is used to alter the
            functionality of the method to where we now receive the
            class as the first argument)

        -   Rarely invoked using objects

        -   Alternate constructors (eg: datetime module in python)

            -   method name usually starts with 'from\_'

            -   Eg: say we already have a constructor (\_\_init\_\_)
                that takes in 3 arguments, but the data that is given to
                us is in the form of a single string that can be parsed
                to extract the 3 arguments

            -   \@classmethod

                def from_string(cls, given_string):

                -   arg1, arg2, arg3 = function_to_parse()

                    return cls(arg1, arg2, arg3)

    -   Static methods

        -   Do not pass anything automatically
        -   They behave like normal functions; they are included in the
            classs because they have some logical connection
        -   Use** \@staticmethod **decorator
        -   If a function does not need access to the instance or the
            class, but it has some logical connection with that class,
            declare it as static
        -   Invoke as cls.staticMethodName()

    -   Virtual methods --
        <https://stackoverflow.com/questions/4714136/how-to-implement-virtual-methods-in-python>

**INHERITANCE**

-   -   class childClass(\<classes_to_inherit\>)

    -   Python walks up the chain of inheritance until it finds out what
        it is looking for -- AKA ***method resolution order ***(see
        help(childClass))

    -   To execute a function from the parent class

        -   super().funcToExecute(args) (OR)
        -   parentClassName.funcToExecute(self, args)

    -   issubclass(classToCheck, parentClass); isinstance(object, class)

    -   Eg: Python exception class (HTTPException)

    SPECIAL METHODS (Eg: datetime module)

    -   \_\_ (double underscores) is called dunder
    -   dunder methods allow classes to perform language operator
        overloading
    -   Eg: **\_\_repr\_\_(self)**, **\_\_str\_\_(self) **(if not
        defined, falls back to \_\_repr\_\_(); overloads print),
        **\_\_add\_\_(self, other)**,** \_\_len\_\_(self, other)**
    -   1+2 is the same as int.\_\_add\_\_(1, 2)
    -   <https://docs.python.org/3/reference/datamodel.html#special-method-names>

PROPERTY DECORATOR

-   Allows to define method that can be accessed like an attribute

-   Say, we have an attribute that is currently in need of a change --
    to correct this, a method can be created which returns the required
    attribute value. But those who are currently using our class will
    need to change that attribute syntax to a method syntax

-   To avoid this, a property decorator can be used

    \@property

    **def** email(self): *\# this can be invoked as objName.email
    (delete the self.email attribute)*

    -   **return** \<required_value\>

-   Let's say we want to set other attributes using another "attribute"

-   Say, we have the function fullname() -

    **\@property**

    **def** fullname(self):

    -   **return** \<fullname\>

    **@fullname**.setter

    **def** fullname(self, name): *\# objName.fullname = 'hello world'*

    -   first, last = fullname.split()

        self.first = first

        self.last = last

-   To delete an attribute -- del obj.someAttribute (deleter for that
    attribute will be called)

    **\@fullname**.deleter *\# provided \@property is defined for
    fullname*

    **def** fullname(self): *\# no more arguments*

    -   \<some cleanup code\>

-   To delete an object, use del object (internally,
    className.\_\_del\_\_(object) will be called)
-   Defining methods outside classes --
    <https://stackoverflow.com/questions/9455111/define-a-method-outside-of-class-definition>
-   Importing classes --
    <https://docs.python.org/3/tutorial/modules.html#packages> (from
    package.module import className)
-   Practice --
    <https://pynative.com/python-object-oriented-programming-oop-exercise/>
-   Usage of ***if \_\_name\_\_ == "\_\_main\_\_" *** - acts as a guard
    code to prevent the python file from running when imported in
    another file

EXCEPTION HANDLING

-   try:

    -   \<code that may raise an exception\>

        \<custom exception can also be raised\>

        raise Exception (more on the Exception class!)

-   except FileNotFoundError as e:

    -   print(e)

-   except Exception:

    -   print("Some custom error message")

-   else:

    -   \<gets executed if try block throws no exceptions\>

-   finally:

    -   \<gets executed irrespective of whether an exception is thrown
        or not\>

-   Use `global varname` if the global variable `varname` is being assigned inside a function. 
    Refer [here](https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment) for explanation.

## Encoding-decoding
```python
import base64

s = "my string"
# convert to 'bytes' class
s_bytes = s.encode("utf-8")
# encode to base64
encoded_bytes = base64.b64encode(s_bytes)
decoded_bytes = base64.b64decode(encoded_bytes)
decoded_str = decoded_bytes.decode("utf-8")
```
