# Golang

- "Fast, statically-typed, compiled programming language"

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
var ages = [3]int{1, 2, 3}
fmt.Println(ages, len(ages))

// slices (use arrays under the hood)
var scores = []{1, 2, 3}
// add new element
scores = append(scores, 4)

// slice ranges
fmt.Print(scores[1:3])
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
```

## Structs
```go
type Test struct {
	name string
	age uint
}
// receiver function
func (Test t) someFunc() string {
    return "Hello, World!!!"
}

func main() {
    t := Test{name: "Hi", age: 29,}
    fmt.Println(t)
    fmt.Println(t.someFunc())
}
```

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
  "github.com/user-1/my-module-name/my-package"
)
```
![fileStructure](./images/goFileStructure.png)
- Red: `.go` source file
- Purple: package
- Green: module
- Orange: main file

## References
- Standard Library -> [builtin](https://pkg.go.dev/builtin@go1.21.3)
- [Specs](https://go.dev/ref/spec#Numeric_types)
