# Java

-   Input

    -   Scanner.nextInt, nextLine, \...

-   Sorting
    ```java
    import java.util.Arrays

    Arrays.sort(nums);
    Arrays.sort(nums, start_index, end_index + 1);
 
    // Multidimensional arrays
    Arrays.sort(nums, (a,b) -> Integer.compare(a[0], b[0]))
    ```

-   ArrayList
    ```java
    import java.util.ArrayList
    ArrayList<Integer> sample = new ArrayList<Integer>(Collections.nCopies(50, 0));  // initialization
    ArrayList<ArrayList<Integer>> sample2 = new ArrayList<ArrayList<Integer>>();
    sample2.add(new ArrayList<Integer>(Arrays.asList(1,2,3)));
    ```
    -   To access an element: `list.get(index)`
    -   To set the value of an element: `list.set(index, value)`

-   HashMap

    -   HashMap\<Integer, Integer\> sample = new HashMap\<Integer,
        Integer\>();

        sample.**put**(key, value);

        System.out.println(sample.**get**(key));

        System.out.println(sample.**containsKey**(someKey));

        System.out.println(sample);

    -   Iterating through HashMap

-   Finding maximum/ minimum

    -   import java.util.**Collections**

        ArrayList\<Integer\> sample = new
        ArrayList\<Integer\>(Arrays.asList(1,2,3,4,5));

        System.out.print(Collections.max(sample));

    -   Math.min(num1, num2)

-   String

    -   String object in Java is immutable (use StringBuffer class in
        java.lang.\*)

        -   StringBuffer mutable_s=new StringBuffer(original)

            mutable.setCharAt(index, char)

    -   s1.charAt(index)

    -   s1.substring(start_index, end_index)

-   Set

    -   Set\<Integer\> test=new HashSet\<\>(Arrays.asList(1,2,4));

        -   More on initialization --
            <https://www.techiedelight.com/initialize-set-java/>

-  Packages 
   -   To create a user-defined package, begin the Java file with `package mypackagename;` and save the file in a directory named `mypackagename`
   -   `javac Package.java`
   -   Refer [this](https://stackoverflow.com/questions/631682/help-with-packages-in-java-import-does-not-work)


-   No default arguments in Java -- use function overloading
-   Scanner --
    <https://stackoverflow.com/questions/13102045/scanner-is-skipping-nextline-after-using-next-or-nextfoo>

## Doubts
-   List vs. ArrayList vs. LinkedList
