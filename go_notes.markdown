# Golang

- "Fast, statically-typed, compiled programming language"

## Creating a module
TODO

## Functions
- Only one `main` function should be present inside the application
```go
func main() {
    // do something
}
```

## Variables
- Refer `builtin` package and language specs for more details
```go
var varOne string = "Hello, World!" // note the double quotes!
// the below cannot be used outside a function
varTwo := 3 // `:=` is shorthand for 'both declaring and initializing'
```

## `fmt` package
- `Print`
- `Println`
- `Printf`
- `Sprintf` - save result in variable instead of printing
```go
var myString = fmt.Sprintf("Hello, %v", varName);
```
- Format operators
  - Can be used only with `Printf` or `Sprintf`
  - `%v`: default formatting
  - `%25v`: to allow for minimum of 25 characters. Remaining characters are
    replaced by ' 's (on the right) 
  - `%q`: quote (for int or float variables, '#' is displayed)
  - `%0.2f`: to display up to 2 decimal points
  - [Reference](https://pkg.go.dev/fmt)

## Arrays and Slices
```go
// creates an integer array of size 3
// array length cannot be changed once declared
// IMPORTANT: The length of the array is considered part of the data-type
var ages = [3]int{1, 2, 3}
fmt.Println(ages, len(ages))

// slices (use arrays under the hood)
var scores = []{1, 2, 3}
// add new element
scores = append(scores, 4)

// slice ranges
fmt.Print(scores[1:3])
```
- Arrays are value-types; slices are reference types
- Slices can be created using `make` keyword - `slice1 := make([]string, length, capacity)`.
  (Length vs. capacity ?)
```go
func exploringArraysAndSlices() {
  arr := [...]int{1, 2, 3} // `...` is alternate to specifying the exact length
  // variadism - https://go.dev/ref/spec#Passing_arguments_to_..._parameters
  slice1 := []int{1, 2, 3}
  slice2 := make([]int, 3, 5) // make(type, length, capacity)
  // slice2[4] = 2 // ERROR!
  fmt.Println("arr ", arr)
  fmt.Println("slice1 ", slice1)
  fmt.Println("slice2 ", slice2)
  fmt.Printf("arr-type: %T; slice1-type: %T\n", arr, slice1)
  fmt.Printf("slice1 - Length: %d; Capacity: %d\n", len(slice1), cap(slice1))
  fmt.Printf("cap(arr[1:]) = %d, cap(arr[0:1]) = %d, cap(arr[2:]) = %d\n", cap(arr[1:]), cap(arr[0:1]), cap(arr[2:]))
  // copying (only for slices)
  // SYNTAX: copy(destn, src)
  slice3 := []int{10}
  fmt.Println("slice3 ", slice3)
  fmt.Printf("%d element(s) copied from slice1 to slice3\n", copy(slice3, slice1)) // returns no. of elements copied
  fmt.Println("slice3 ", slice3)
}
```

## Standard Library
- `strings`
  - `Contains`
  - `ReplaceAll`
  - `ToUpper`
  - `Index`
  - `Split`
- `sort`
  - `Ints`, `Strings`, ...
  - `SearchInts`, `SearchStrings`, ...

## Loops
```go
scores := []int{1, 2, 3}
// 'while' loop
i := 0
for i < len(scores) {
	fmt.Print(scores[i], ", ")
	i += 1
}
fmt.Print("\n");
// typical 'for'
for j := 0; j < len(scores); j++ {
	fmt.Print(scores[j], ", ")
}
fmt.Print("\n");
// 'for in'
for _, value := range scores {
	fmt.Print(value, ", ");
}
```
## Functions
```go
// passing a function as an argument
func test(arg1 string, f func(string)) string {
    f("Hello")
    // do something
    return "Done!"
}

// multiple return values
func test2() (int, string) {
    return 1, "Hi!"
}
```

## Maps
```go
menu := map[string]float {
    "candy": 50.0,
}
// iteration
for key, val := range menu {
    fmt.Printf("%v : %0.2f", key, val);
}
// if a key does not exist, a new one is created with default zero-value
fmt.Println(map["savoury"])
// checking if a key exists
value, ok := map["chocolate"]
if !ok {
  fmt.Println("Key does not exist")
}
// delete a key - no return value; no error if key does not exist
delete(menu, candy)
```
- Runtime error when trying to add new key to a `nil` map (eg: `var nilMap map[string]int`) ?

## Structs
```go
type Test struct {
	name string
	age uint
}

// receiver function
// SYNTAX: func (receiverArg T) funcName (returnType1, returnType2)
func (Test t) someFunc() string {
    return "Hello, World!!!"
}

func main() {
  t := Test{name: "Hi", age: 29,}
  // Other methods of INITIALIZATION
  t1 := Test{"Hi", 29}  // implicit initialization
  t2 := Test{} // initialized with default zero-values
  t3 : Test{"Hi"} // ERROR! For implicit initialization, all values need to be provided

  fmt.Println(t)
  fmt.Println(t.someFunc())
}
```
- Structs are value-types
- Properties and methods of structs can be accessed using "." 
  irrespective of whether it is done so with the struct element or with its pointer
```go
func someFunc() {
  t := Test{"Hi", 29}
  ptr := &t
  fmt.Println((*ptr).name == ptr.name)
}
```
- Embedding vs. Composition
```go
type embedTest struct {
  Test // all properties of Test become part of those of embedTest
  anotherProperty string
}

type CompositionTest struct {
  tester Test
  anotherProperty string
}
```
### Struct Tags
```go
type Animal struct {
	Name    string `key:"value1"`
	Age     int    `key:"value2"`
}
```

## Interfaces
```go
type myInterface interface {
  myMethod()
}

func (t *Test) myMethod() {
  fmt.Println("Hello, World!!!")
}

func exploringInterfaces() {
  testStruct := Test{"gokula-s", 23}
  fmt.Println("testStruct: ", testStruct)
  // explicit interface type
  // note that *Test (not Test) is the one that implements myMethod
  var myInterfaceInstance myInterface = &testStruct
  fmt.Printf("myInterfaceInstance type: %T\n", myInterfaceInstance)
  fmt.Println("myInterfaceInstance: ", myInterfaceInstance)
  fmt.Println()

  // empty interface
  fmt.Println("Creating empty interface ...")
  var myInterface2 interface{}
  myInterface2 = &testStruct // properties of myInterface2 cannot be accessed directly
  // Type-assertion: To get value of interface
  v1, ok1 := myInterface2.(*Test)
  if ok1 {
    fmt.Println("Type assertion succeeded! Value(s) is ", v1.name, v1.age)
  }
  v2, ok2 := myInterface2.(int)
  if !ok2 {
    fmt.Println("Type assertion failed! Value is ", v2) // default 0-value
  }
  // NOTE: if `ok` (return value) is not present, panic occurs if assertion fails
  // Type-switching
  switch v := myInterface2.(type) {
  case string:
    fmt.Printf("Value is %s\n", v)
  case *Test:
    fmt.Println("Value(s) is: ", v.name, v.age)
  default:
    fmt.Println("NOTA")
  }
}
```
- [Interfaces and pointer-receiver error](https://stackoverflow.com/questions/40823315/x-does-not-implement-y-method-has-a-pointer-receiver)

## Pass by Value
- The 2 groups
![groups](./images/goGroups.jpg)
- Group I
![non-pointer-groups](./images/goGroupA.jpg)
- Group II
![pointer-groups](./images/goGroupB.jpg)

## File structure
- Package
  - Can be thought of as directories (?)
  - Multiple `.go` source files can fall within the scope of a package; but a single file cannot belong to more than 1 package
  - A package can be defined recursively as follows: Stand-alone `.go` files + other packages 
```go
package "some-name"  // all files belonging to this package has to start with this
// some functions
```
- Modules - Each go project has a `go.mod` file which looks something like this:
```go
module "github.com/user-1/my-module-name"

require (
  "github.com/user-2/some-other-module"
)
```
- Using packages
```go
import (
  "my-module/my-package/dir-name"
)
// assuming dir-name defines a package `mine`
mine.DoSomething()
```
![fileStructure](./images/goFileStructure.png)
- Red: `.go` source file
- Purple: package
- Green: module
- Orange: main file

## Channels
- Goroutines
- Internal structure (circular queue)
- Reading/ writing
  - Acquire lock
  - Memory copy
  - Release lock
- Scheduling : `m:n` Scheduling
- Close channel in sender if using `range` (to read from channel) in receiver
```go
func main() {
  ch := make(chan bool);
  for _, val := range ch {
    <- ch
  }
  // OR
  // for {
  //   val, open := <- ch
  //   if !open {
  //     break
  //   }
  // }
}

func send(chan bool ch) {
  total = getTotal()
  for i := 0; i < total; ++i {
    ch <- true
  }
  close(channel)
}
```
### Select
- To select a channel randomly when listening to (receiving from) multiple channels
- If an unbuffered, closed channel is read from, it will return the zero value
```go
ch1, ch2 := make(chan bool), make(chan bool)
close(ch1)
close(ch2)
select {
  case result := <-ch1: {
    fmt.Println("Channel 1", result)
  }
  case result := <-ch2: {
    fmt.Println("Channel 2", result)
  }
}
```
- Behaviour of `default` - If no channels are immediately available at the time of execution of the `select` statements, this is chosen?
### WaitGroup
```go
var wg sync.WaitGroup
// wg.Add(100) // COMMENT THIS ...
for i := 0; i < 100; i++ {
  wg.Add(1) // ... OR THIS
  go func() {
    wg.Done() 
  }()
}
wg.Wait()
```
- Correlating WaitGroup with channel
- [Where to put wg.Add()](https://stackoverflow.com/questions/65213707/where-to-put-wg-add)

### Mutex
- Regular Mutex vs. RWMutex
- [Mutex vs. channels](https://go.dev/wiki/MutexOrChannel)

### Deadlocks
- For an unbuffered channel
  - If the main go-routine has a send/ receive-channel action and if there are no subroutines at that point of time, it is a deadlock
  - Though the capacity is 0, one can still send unlimited messages as long as is a reciever to process them (at the time of publishing the messages)
- [Why deadlocks happen?](https://stackoverflow.com/questions/54157836/a-simple-example-about-go-channel-with-deadlock-and-why)
- [Leaving channels open?](https://stackoverflow.com/questions/8593645/is-it-ok-to-leave-a-channel-open)

## `iota`
- To define auto-incremental constants
```go
const (
  Red int iota // value is 0
  Blue // value is 1
  Green // value is 2
)
```
- [Reference](https://www.gopherguides.com/articles/how-to-use-iota-in-golang)

## Unsafe Pointers
- A key capability of the “unsafe” package is the generation of pointers to non-pointer data types like integers and structs
- Casting a Go pointer to “unsafe.Pointer” and then passing it to C methods that anticipate a void pointer might be helpful when interacting with C code that makes use of void pointers.
- Low-level memory manipulation:
```go
 p := &myStruct{}
p1 := (*int32)(unsafe.Pointer(p))
*p1 = 10
```

## `logrus`
```go
import (
  log "github.com/sirupsen/logrus"
)

func ExploringLogger() {
  fmt.Println("Hi, Logger!")
  log.WithField("name", "gokulas").Info("Using `WithField`")
  dataToLog := log.Fields{
    "chocolate": 30,
    "sweet": 20,
  }
  log.WithFields(dataToLog).Info("Using `WithFields`")
}
```
- `withField` and `withFields` do not log until you call Debug, Print, Info, Warn, Fatal or Panic on the Entry it returns.
- Both of the above return a value of type `Entry`
- Logging with panic and error handling:
```go
func someMethod(a int, b int) error {
  if b % 2 == 0 {
   panic("Oops")
  }
  return fmt.Errorf("E1")
}

func ExploringLogger() {
  err := new(error)
  defer func() {
    logFields := log.Fields{}
    if r := recover(); r != nil {
      logFields["msg1"] = "Handling panic"
      switch t := r.(type) {
      case string: {
        logFields["msg2"] = fmt.Sprintf("Panic arg is string %s", t)
        *err = errors.New("E2")  // No effect
      }
      case error: {
        logFields["msg2"] = fmt.Sprint("Panic arg is error ", t)
      }
      default: {
        fmt.Println("Unknown panic")
      }
      }
    } else {
      logFields["msg1"] = "Handling error"
      *err = errors.New("E2")  // No effect
    }
    log.WithFields(logFields).Debug("Debug title")
  }()
  *err = someMethod(4, 2) // below statements not executed if `someMethod` panics
  log.WithError(*err).Warn()
  fmt.Println("Done!!!")
}
```
- Chaining methods

## `reflect`
- `Type`
- `Value`
  - `Kind` gives the "kind of value" (for `Value`)

## `net/http`

## `age`
- [Docs](https://pkg.go.dev/filippo.io/age)
```
// generate key-pair
// encrypt data with (public-key) receiver; save in *.age file
// decrypt using identifier (file with private key)
```

## References
- Standard Library -> [builtin](https://pkg.go.dev/builtin@go1.21.3)
- [Specs](https://go.dev/ref/spec#Numeric_types)
- [Complete Tutorial - Karan Pratap Singh](https://github.com/karanpratapsingh/learn-go)
- [GopherCon Channels](https://youtu.be/KBZlN0izeiY?si=crky_yXPoe159xbj) & accompanying [Textual Tutorial](https://www.velotio.com/engineering-blog/understanding-golang-channels)
- [JSON](https://go.dev/blog/json)
- [json.Marshal and race-condition](https://stackoverflow.com/questions/69074539/go-json-marshaller-panics-with-call-of-reflect-value-int-on-zero-value)
- [Reflection](https://golangbot.com/reflection/)
### To read later
- [Unsafe pointers](https://blog.devgenius.io/unsafe-pointers-in-go-should-i-ever-i-bothered-about-it-9d1d9db1a97c)
- [Understanding uintptr](https://golangbyexample.com/understanding-uintptr-golang/)
- [Unidirectional channels](https://hyperskill.org/learn/step/24709)
