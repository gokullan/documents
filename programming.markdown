Stuff learned in CP

-   Area of triangle

    ![](Pictures/100000000000062D000000A85D00B07730CB7CC6.png "texmaths"){width="9.296cm"
    height="0.989cm"}

-   **

**

-   GCD-LCM: LCM(a,b) =

    -   Python: math.gcd(x,y) (import math)

    -   C++: \_\_gcd(x,y) (#include\<algorithm\>)

    -   Euclidean method:

        // x\<y

        gcd (x,y) {

        -   if (x==y) {

            -   return x;

            }

            else if (x==0) {

            -   return y;

            }

            else if (y==0) {

            -   return x;

            }

            else if (x\>y) {

            -   return gcd(y,x);

            }

            else {

            -   return gcd(x,y%x);

            }

        }

-   Counting the number of digits in a number:

-   Bit shifts

    -   <https://stackoverflow.com/questions/141525/what-are-bitwise-shift-bit-shift-operators-and-how-do-they-work>

    -   Left shift \<\<

        -   equivalent to multiplication by powers of 2
        -   Eg:
        -   meets needs of both logical and arithmetic left shift
            ***(how?)***

    -   Logical right shift \>\>\>

        -   for unsigned numbers
        -   equivalent to division by powers of 2
        -   Eg:

    -   Arithmetic right shift \>\>

        -   same as \>\>\>, but for signed numbers (sign-preserving)

-   mod of negative numbers

    -   <https://math.stackexchange.com/questions/2179579/how-can-i-find-a-mod-with-negative-number>

-   Inclusion-exclusion to find multiples

![](Pictures/100002010000017B000000A9498220A7C07C50C4.png){width="10.028cm"
height="4.471cm"}\

-   Pythagorean triplet (a + b + c = 1000) -
    <https://stackoverflow.com/questions/2817848/find-pythagorean-triplet-for-which-a-b-c-1000>

-   Even Fibonacci numbers

-   Non-decreasing sub array

-   Kadane's algorithm (maximum contiguous sum)

    -   sum = 0

    -   ans = INT_MIN

    -   for num in num_list:

        -   sum += num

        -   ans = max(ans, sum)

        -   if sum \< 0:

            -   sum = 0

-   Prefix sum

    -   prefix_sum = \[num_list\[0\]\]

    -   for i in range(len(num_list)):

        -   prefix_sum.append(prefix_sum\[i-1\] + num_list\[i\])

(OR)

-   -   prefix_sum(n+1,0)

        for i: 0 to len(num_list)-1:

        -   prefix_sum\[i+1\]=prefix_sum\[i\]+num_list\[i\]

    -   To find the sum between the indexes start and end:
        ***prefix_sum\[****end****+1\]-prefix_sum\[****start****\]***

    -   If the n+1 format is used, prefix_sum\[i\], represents the sum
        upto the (i-1)^th\ ^element.

        -   

    -   ***Marker array*** -- assume you given* q *queries and each
        query asks you to increment the elements from *l* to *r *by *k*.
        (*l, r* and *k* differ for each query) You need to print out the
        final array (num_list) -

    -   marker = \[0,0, \... (*n* times)\] (*n* is the array length)

    -   for each query:

        -   marker\[*l*\] += *k*
        -   marker\[*r+1*\] -= *k*, provided *r* \< *n -1*

    -   marker = find_prefix_sum(marker)

        -   // now *every element in marker* indicates, by how much
            *every element in the array* needs to be incremented

    -   for* i *in range(*n*):

        -   num_list\[*i*\] += marker\[*i*\]

-   -   Given 2 *lists of intervals *(every element in each list is of
        the form *(l,r) *which denotes that numbers from *l *to *r*, are
        contained in that interval), say X and Y. **For every interval
        in the list Y, you are required to find the count of
        *****number****s in X ****from Y***~***i***~***.****l ****to
        Y***~***i***~***.****r*****, whose frequencies are greater than
        some integer *****k*****.**

    -   Create an array, marker (initialized with 0) of size = \# of
        *numbers that X encompasses*

    -   For every interval in X:

        -   marker\[index representing X~i~.*l*\] += 1 **(check!)**
        -   marker\[index representing X~i~.*r + *1\] += -1

    -   Find_prefix_sum(marker_array)

        -   // now you know how many times each number in marker repeats

    -   Next, make a slight modification to the prefix_sum array, so
        that prefix_sum\[i\] represents the number of elements whose
        frequencies are greater than *k, *starting from *the element
        representing index 0* to *the element representing index i* (or
        i-1 if the n+1 format is used.)

    -   To find the count of numbers from* a *and* b* whose frequencies
        are greater than* k*, use the new prefix_sum array and compute
        **(# of elements upto b that have a frequency\>k) - (# of
        elements upto a-1 that have a frequency\>k) **= prefix\[index
        representing b\]-prefix\[index representing a-1\]

-   Difference Array -- <https://codeforces.com/blog/entry/78762>

-   Floyd's algorithm (repetition in N+1 numbers)

    -   *Important*: If elements that make up a list are from 1 to n
        (and the array size is n+1), then you can visit every element in
        this list (starting from index 0) by using each element as an
        index.

    -   slow = fast = num_list\[0\]

    -   do {

        -   slow = num_list\[slow\]
        -   fast = num_list\[num_list\[fast\]\]

        } while slow != fast

    -   fast = num_list\[0\]

    -   while slow != fast:

        -   fast = num_list\[fast\]
        -   slow = num_list\[slow\]

-   **Dutch National Flag algorithm**

    -   low = mid = 0

    -   high = n-1

    -   while mid \<= high:

        -   if mid == 0:

            -   swap(num_list\[low\], num_list\[mid\])
            -   mid++, low++

        -   else if mid == 1:

            -   mid++

        -   else: \# mid = 2

            -   swap(num_list\[high\], num_list\[mid\])
            -   mid ++, high\--

-   **2-sum problem**

    -   index_map\<int,int\> = {} // mapping from num_list\[i\] to i

    -   for i in range(n):

        -   if (target -- num_list\[i\]) in index_map:

            -   return \[index_map\[target -- num_list\[i\]\], i\]

        -   else:

            -   index_map\[num_list\[i\]\] = i

-   4-sum problem

    -   3-pointers + binary search

    -   2-pointers + 2 pointers

-   <https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640>

    -   

-   **Cycle Detection -- undirected -- BFS**

    -   visited = \[-1 for i in range(V)\]

    -   for i:1 to V

        // identifying components of the graph

        -   If visited\[i\]== -1:

            -   do cycle detection starting from i (Method 1 or 2)

                Note: visited is passed by reference for both methods

    -   Method 1:

        -   bfs_queue = \[\<start, -1\>\] *// \<node, parent\> form*

        -   while bfs_queue is not empty:

            -   current = bfs_queue.popfront() *// \<node, parent\>
                pair*

            -   visited\[current.node\] = 1

            -   for u in adj_list\[current.node\]:

                -   if visited\[u\] == -1:

                    -   bfs_queue.append(\<u, current.node\>)

                -   else if (u != current.parent):

                    -   return True *// cycle exists*

        -   return False

    -   Method 2:** **

        -   bfs_queue = \[\<start, -1\>\] *// \<node, parent\> form*

        -   visited\[start\]=0 \# -1 =\> unvisited; 0 =\> in-queue; 1
            =\> visited

        -   while bfs_queue is not empty:

            -   current = bfs_queue.popfront() *// \<node, parent\>
                pair*

            -   visited\[current.node\] = 1

            -   for u in adj_list\[current.node\]:

                -   if visited\[u\] == -1:

                    -   bfs_queue.append(\<u, current.node\>)
                    -   visited\[u\]=0

                -   else if visited\[u\]==0:

                    -   return True *// cycle exists*

        -   return False

-   Cycle Detection -- undirected -- DFS

    -   Similar to method 1 of undirected cycle detection using BFS

-   Cycle Detection -- directed -- BFS

    -   Using the idea of Khan's algorithm

-   Cycle Detection -- directed -- DFS

    -   Similar to method 2 of undirected cycle detection using BFS

-   Topological Sort -- BFS (Khan's algorithm)

    -   <https://practice.geeksforgeeks.org/problems/topological-sort/1>

        (log in through Google with SSN mail ID)

-   Topological Sort -- DFS

-   Bipartite Matching (Kuhn's algorithm)

    -   <https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html>

-   DFS Tree properties

    -   <https://codeforces.com/blog/entry/68138>

-   Rat in a maze using BFS

    -   <https://www.techiedelight.com/find-shortest-path-in-maze/>

-   

-   **Disjoint Sets**
-   Kruskal's Algorithm
-   Prim's Algorithm
-   Floyd-Warshal Algorithm
-   Ford-Fulkerson Algorithm

-   <https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/>
-   <https://stackoverflow.com/questions/29741691/maximum-flow-in-the-undirected-graph>

-   **Fractional Knapsack Problem (Greedy)**

    -   Input: W (knapsack capacity), array with elements of type (w~i~,
        v~i~), where w~i~ and v~i~ denote the weight and value of the
        i^th^ element in the knapsack

    -   Sort the items by decreasing order of their value to weight
        ratio

    -   Add elements

-   Job Sequencing (Greedy)

    -   <https://www.gatevidyalay.com/job-sequencing-with-deadlines/>

```{=html}
<!-- -->
```
-   

-   **Bitmasking DP **(suited for subset-type problems)

    for x from 0 to 2^n^:

// check which bits are set and do required processing

for k from 0 to size: // size refers to max of bit-string of x

if kth bit is set/unset in x:

// do required processing

-   Operations

1.  1.  To set the i^th^ bit in bit-string b: b \| (1 \<\< i)
    2.  To unset the i^th^ bit: b & !(1 \<\< i)
    3.  To check if i^th^ bit is set: b & (1 \<\< i) should be non-zero

-   <https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/>

-   Binary search

    -   Smallest character greater than a given target character --
        <https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/>
    -   Matrix median
    -   Aggressive cows

-   Backtracking

    -   <https://www.techiedelight.com/find-shortest-path-in-maze/>

-   Others:

    -   Understand "set matrix to zero"
    -   arr\[-1\] (merging overlapping subintervals)
    -   "repeat and missing number"
    -   "n-meetings in a room" -- Striver's algo
    -   

\-\--Python\-\--

-   File Handling-

```{=html}
<!-- -->
```
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

-   Numpy-

```{=html}
<!-- -->
```
-   -   inverse
    -   det -- np.linalg.det
    -   solve -- np.linalg.solve(mat1, mat2)
    -   dot

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

-   JSON (import json) --
    <https://www.programiz.com/python-programming/json>

    -   Loading JSON: person_dict = json.loads(personJSON)

    -   Pretty printing JSON: json.dumps(person_dict, indent=4,
        sort_keys=True)

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

\-\--C\-\--

-   qsort

    -   **void** qsort(**void** \*base, **size_t** total_count,
        **size_t** element_size, **int** (\*comparator) (**const**
        **void** \*, **const** **void**\*) );

    -   **int** **comparator** (**const** **void** \*p1, **const**
        **void** \*p2)

        {

        -   UserDefined \*x1 = (UserDefined \*) p1;

            UserDefined \*x2 = (UserDefined \*) p2;

            **return** (x1.(\...) - x2.(\...));

            // return value \> 0 =\> arg_1 should come after arg_2

        }

-   sprintf - sprintf(str, \"Value of Pi = %f\", M_PI); \[str is now =
    "Value of Pi = 3.14159\..."\]

-   itoa - *itoa(num, snum, 10); \[convert int to string\]*

-   strcat - char \*strcat(char \*s1, const char \*s2);

-   when using \<math.h\>, add -lm, (i.e.), gcc {filename.c} -lm

-   <https://stackoverflow.com/questions/3736210/how-to-execute-a-shell-script-from-c-in-linux>

-   Clearing input buffer -
    <https://www.geeksforgeeks.org/clearing-the-input-buffer-in-cc/>

-   getline() -- size_t getline (char \*\*string, size_t \*n, FILE
    \*stream);

-   THREADS

    -   #include*\<pthread.h\>*

        pthread_t thread_1;

        // thread creation

        pthread_create(&thread_1, NULL, void_ptr_returning_function,
        function_args_as_void_ptr); *// 2*^*nd*^* argument is thread
        attributes *

        // to ensure that the calling thread does not terminate before
        its created thread completes

        pthread_join(created_thread, NULL);

        // mutex lock

        pthread_mutex_t lock_thread_1 = PTHREAD_MUTEX_INITIALIZER

        // alternate

        pthread_mutex_t lock_thread_2;

        pthread_mutex_init(&thread2, NULL);

        // locking and unlocking

        pthread_mutex_lock(&lock_thread1);

        // code to protect

        pthread_mutex_unlock(&lock_thread1);

    -   Tutorial - <https://youtu.be/GXXE42bkqQk>

    -   "Locking a resource using mutex" -
        <https://stackoverflow.com/questions/40479316/what-does-it-mean-to-lock-a-resource-using-pthread-mutex-lock>
        (GOOD!)

    -   pthread_mutex_init vs. PTHREAD_MUTEX_INITIALIZER -
        <https://stackoverflow.com/questions/14320041/pthread-mutex-initializer-vs-pthread-mutex-init-mutex-param>

    -   Why wait and signal need to be atomic?

        -   <https://stackoverflow.com/questions/67046250/why-do-the-wait-and-signal-semaphore-operations-need-to-be-atomic>
        -   <https://www.quora.com/In-semaphores-are-wait-and-signal-operations-atomic-or-just-modification-of-S-semaphore-and-condition-S-0-atomic>

    -   local mutex locking -
        <https://stackoverflow.com/questions/20617095/how-to-lock-thread-by-using-mutex-variable-locally?rq=1>

    -   function inside pthread_mutex_lock(&lock_thread) -
        <https://stackoverflow.com/questions/60527669/can-i-insert-a-function-inside-a-pthread-mutex-lock-and-unlock-statements>

\-\--C++\-\--

-   <https://stackoverflow.com/questions/589985/vectors-structs-and-stdfind>
-   <https://stackoverflow.com/questions/31039900/bool-operator-in-c/46699996>
-   find_if -
    <https://www.geeksforgeeks.org/stdfind_if-stdfind_if_not-in-c/>

![](Pictures/100002010000031800000373BB3077F2822F38E8.png){width="17cm"
height="18.953cm"}

-   Unordered vs. Ordered maps

-   Priority Queue for user defined data types (refer
    \~/Documents/College/cpp/comparator.cpp)

-   const int vs int const --
    <https://stackoverflow.com/questions/162480/const-int-vs-int-const-as-function-parameters-in-c-and-c>

-   Compare (comparator)

    -   <https://en.cppreference.com/w/cpp/named_req/Compare>

    -   Operator overloading

        -   Function call
        -   \< operator

    -   Weak ordering

        -   <https://codeforces.com/blog/entry/72525>
        -   <https://stackoverflow.com/questions/979759/operator-and-strict-weak-ordering>

-   **STL containers **-
    <https://home.csulb.edu/~pnguyen/cecs282/lecnotes/stlcontainer.html>

-   Sorting 2-D lists

-   Initializing arrays and objects -
    <https://stackoverflow.com/questions/4118025/brace-enclosed-initializer-list-constructor>

    -   vector initialization

        -   constructor

            vector\<int\> vect1(n, -1); *// initializing n elements with
            -1*

            vector\<int\> vect2(vect1.begin(), vect1.end());

            vector\<int\> vect{1,2,3,4};

        -   other

            vector\<int\> vect1(n);

            fill(vect1.begin(), vect1.end(), 5); // initializing with 5

    -   pair

        -   constructor

            pair\<int, int\> p1(x,y);

            pair\<int, int\> p2(p1);

        -   other

            make_pair(x, y) or {x,y}

-   Strings

    -   s1.substr(start_index, length_of_substr);

-   Integer to string

    -   to_string(n);

-   char to int

    -   char a = '4';

        int x = a -- '0';

-   string to integer

    -   stringstream test(\"1234 5678 9101\");

        **while** (test.good())

        {

    int x;

    test \>\> x; *// stringstream automatically stops reading at blank
    space*

    cout \<\< \"**\\n**Number: \" \<\< x;

    -   }

-   Counting the number of words

    -   string word;

        int count = 0;

        while (test \>\> word)

        {

        -   count ++;

        }

-   Using boost::lexical_cast

    #include*\<boost/lexical_cast.hpp\>*

    \...

    int num = boost::lexical_cast\<int\>(s1); // string to integer

    (*sudo apt-get install libboost-dev*)

-   getline

    -   <https://www.javatpoint.com/cpp-getline> (3 synataxes)

    -   use cin.ignore() or cin.ignore(256, '\\n') if you have used cin
        before

    -   while(getline(\...)) to process until newline is encountered

-   PBDS - <https://codeforces.com/blog/entry/11080>

-   move_iterator, value_type

-   cout formatting

    -   <http://faculty.cs.niu.edu/~hutchins/csci241/output.htm>

    -   Eg: cout \<\< setw(n) \<\< "Some expression";

        Ensures that "Some expression" takes up at least (a minimum of)
        n characters (right justified) (use \<\< left for left
        justification)

-   for loop (since C++11) **for** (int **n**: num_array) { }

-   regex

    -   #include\<regex\>

        regex to_match(\"\<reg_expr\>\");

        return regex_match(string_to_match, to_match);

    -   regex_search -- to obtain information about matching(s)

        <https://www.cplusplus.com/reference/regex/match_results/position/>

        regex to_match(\"\<some-re\>\")

        smatch m;

        regex_search(string_to_check, m, to_match)

        for (int i=0; i\<m.size(); ++i)

        {

        -   cout \<\< m\[i\] \<\< m.position(i);

        }

    -   

-   Binary search

    -   bool **binary_search**(start_it, end_it, key) // array should be
        sorted

-   -   iterator\<\> **lower_bound**(start_it, end_it, key) // returns
        an iterator to key if it exists else returns an interator to the
        (immediate) next element greater than key

        -   

    -   iterator\<\> **upper_bound**(start_it, end_it, key) // returns
        an interator to the (immediate) next element greater than key

-   -   Note: Subtracting the result of lower_bound or upper_bound with
        the start iterator will give the index of that element

-   stringstream

-   Template function

    -   template\<typename T\> void print(vector\<vector\<T\>\> arr)

        {

        }

-   Iterators

    -   Reverse iterators -- to iterate from the end of the array to the
        beginning

        std::vector\<int\>::reverse_iterator it =
        vect_test.**rbegin**();

        std::vector\<int\>::reverse_iterator it = vect_test.**rend**();

    -   Get index of iterator

        -   it -- vec.begin()
        -   std::distance(vec.begin(), it)
        -   <https://stackoverflow.com/questions/2152986/what-is-the-most-effective-way-to-get-the-index-of-an-iterator-of-an-stdvector>

    -   

-   Bit manipulation

    -   Count the number of set bits: **\_\_builtin_popcount**(x)

    -   Get the parity: **\_\_builtin_parity**(x)

        -   1 if the number of set bits is odd; else even

    -   Count the number of leading zeros: **\_\_builtin_clz**(x) // for
        32-bit int

    -   Count the number of trailing zeros: **\_\_builtin_ctz**(x)

    -   Index (1-based) of least significant set bit:
        **\_\_builtin_ffs**(x) // Find First Set

    -   Index of highest set bit: **std::lg**(x)

    -   **Note**: The above are for integers. For long, add 'l'; for
        long long, add 'll' (eg: \_\_builtin_parityl(x),
        \_\_builtin_parityll(x))

    -   <https://codeforces.com/blog/entry/72437>

-   **Friend functions/classes** (/Documents/College/c-cpp-py)

    -   Friend function

        -   A non-member function that can access the private and
            protected members of a class
        -   Should be declared in the class as: *friend
            function_name(class_name &obj);*

    -   Friend class

        -   A class which can access the private and protected members
            of another class

        -   Should be declared in the class as: *friend class
            class_name;*

        -   The friend class should be defined *after* the class for
            which it is a friend.

-   Static data member/function (/Documents/College/c-cpp-py)

    -   Both are class level members (as opposed to object level) =\>
        they are common to all instaces (objects) of a class. In other
        words, a single copy of the member is accessed by all instances.

    -   They can be accessed (without instanting an object) using the
        scope resolution operator along with the class name

    -   Static data member

        -   Declared inside a class (under appropriate access-specifier)
            as: *static int count*
        -   Should be also be declared (and may be explicitly
            initialized) outside the class (using the scope resolution
            operator) as: *int class_name::count = 0*; (default
            initialization is 0 for int, float, \...) .

    -   Static member function

        -   static function_name() { }
        -   has access to only static variables, other static functions
            and functions declared outside the class.

-   Copy constructors

-   Priority Queue vs. Sets -
    <https://stackoverflow.com/questions/10141841/difference-between-stdset-and-stdpriority-queue>

    -   Priority queue updation --
        <https://stackoverflow.com/questions/649640/how-to-do-an-efficient-priority-update-in-stl-priority-queue>

-   Multisets and Multimaps

-   File Handling

    -   #include*\<fstream\>*

        \...

        fstream fileObj;

        fileObj.open("filename.txt");

        char data\[100\];

        fileObj \>\> data; *// reading from file*

        \...

        fileObj \<\< data; *// writing to file*

        fileObj.seekg(pos, ios::cur); *// to seek pos positions forward
        from the current position*

        fileObj.close();

    -   Use fileObj.clear() to seek to new positions in the file after
        reaching the end (clearing the flags set) --
        <https://stackoverflow.com/questions/5343173/returning-to-beginning-of-file-after-getline>

    -   Passing stream object as parameter -
        <https://stackoverflow.com/questions/27501160/pass-a-reference-to-stdifstream-as-parameter>

    -   Read specific amount of characters from a file:
        fileObj.read(buffer, n)

    -   Reading until EOF -
        <https://stackoverflow.com/questions/21647/reading-from-text-file-until-eof-repeats-last-line>

        while(1)

        {

        -   \...

            if (fileObj.eof())

            -   break;

\...

-   -   }
    -   

-   

Bitwise operators-

-   Precedence: \~, \<\<, \>\>, & , \^, \|
-   4 \<\< 1 =\> 100 \<\< (1 time) = 1000 = 8
-   4 \>\> 2 =\> 100 \>\> (1 time) = 010 = 2

Sorting

-   Stable

Regular expressions

-   Escape special characters (below) with \\

    -   . \[ { ( ) \\ \^ \$ \| ? \* +

-   Character matching

    -   . matches any character except newline

    -   word (\\w) character =\> a-z, A-Z, 0-9, \_

        -   \\W matches those which are NOT word characters (uppercase
            =\> negation of lowercase matching expr)

    -   whitespace (\\s) =\> space, tab, newline

-   Anchors

    -   \\b matches word boundaries
    -   \^ for beginning of string (string =\> 'line')
    -   \$ for end of string

-   Character set \[\<characters to match\>\] - matches one character
    from this list

    -   no need to escape characters like .
    -   \- when place at the ends means to match the literal .; else it
        is used to specify range. Eg: \[1-7\]
    -   \^ is used to negate the set \[\^\<some-expr\>\]

-   Quantifiers

    -   \* is 0 or more
    -   \+ is 1 or more
    -   ? is 0 or 1
    -   {3} denotes the exact number (3, in this case)
    -   {min#, max#}

-   Groups

-   Exercises

    -   match phone numbers
    -   match names (M(r\|s\|rs)\\.?\\s\[A-Z\]\\w\* (can space be used
        instead of \\s?)
    -   

Incomplete problems

-   Palindrome partitioning (leetcode)
-   Hamiltonian Circuit (HackerEarth -- bitmask)
-   Assignment Problem (HackerEarth -- bitmask)

Project Euler-

-   172 -- repeated digits (3 at most)
-   43 - Pandigital numbers (substring divisibility)
-   127 -- abc-hits
-   18, 67 -- maximum path I, II
    (<https://www.geeksforgeeks.org/maximum-cost-path-in-an-undirected-graph-such-that-no-edge-is-visited-twice-in-a-row/>)
-   65 -- convergents of e
-   121 -- disc game
-   k-smallest pairs --
    <https://www.geeksforgeeks.org/find-k-pairs-smallest-sums-two-arrays/>
-   least coins --
    <https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/>
-   maximal square (dp)

CodeChef

-   DP -- count subarrays

Swagger

-   Swagger editor

    -   <https://swagger.io/docs/specification/basic-structure/>
    -   <https://swagger.io/docs/specification/describing-parameters/>
    -   <https://inspector.swagger.io/builder>
    -   <https://swagger.io/docs/specification/data-models/data-types/>

-   Swagger Inspector
