# Rust

## Misc

- `const` is used to declare *compile-time* constants
- Is one file = one "module"?
- How to import modules whose file names contain "-", begin with a number, etc.?

## "References" and "Pointers"

- Pointers (`*Type`) are simply memory-addresses (the same as what they mean in C++)
- *Creating* a pointer is safe, but reading / writing to them can be done only within an `unsafe` block
- References (`&Type`) are special-types which get translated to the same actions of a pointer, but the Rust-compiler enforces several checks on the reference-variable. They can be thought of as "wrappers on pointers"
- Among the several checks made by the compiler, the noteworthy ones are ...
  - Null-checks (a reference must always point to a valid value)
  - Lifetime-checks (the value being pointed to must last longer than the reference pointing to it.)
- To obtain the value the reference-variable points to, use the `*` (de-reference) operator
- Auto de-referencing
  - When you pass a struct by reference, you don't need to use `*` to access its methods
- Deref-coersion?
- "Fat" pointer is one which consists of metadata apart from memory address (see `&str`)

### Comparison with C++

## Strings

```rs
const s: String = "abcd"
```

- Strings cannot be indexed as in other languages
- `str` is a DST (Dynamic Sized Type) => it's size cannot be known at compile-time; thus `let s: &str = "Hello!"` is its usage
- `&str` is a "fat" pointer which consists of the memory-address and the metadata (length of the string)

## Arrays and Slices

- An array is a contiguous set of data whose size is known at compile-time
- A slice, `str`, `[char]`, ... is the underlying data a "fat" pointer points to
- Slices are almost always interacted with via references

## Mutability

## Iterators

## Vectors

```rs
let vec1 = vec![0; 5];  // initializes a vector of length 5 with all zeros
let vec2 = Vec<i32>::new();
```

- `vec1` is a pointer to a struct in the following manner (?)
- `for x in vec1` &rarr; this implicitly calls `into_iter` which takes ownership of the vector; this means that `vec1` cannot be used anymore

## Hash Maps

```rs
let mut my_map: HashMap<char, i32> = HashMap::new()
my_map.entry('x')  // the Entry-enum is cost-effective when you need to check for existence, then update
  .and_modify(|val| => *val += 1)  // the argument is a "lambda" which takes a reference
  .or_insert(0);
```

## How can one use "classes" in Rust

- In Rust, there are no classes - `struct` is the closest representative to a class

```rs
pub struct Person {  // use pub to use this in other files (AKA "modules")
  // The member-fields in the struct should be owned by it => references are not allowed (see "Lifetimes")
  name: String,
  age: i32
}

impl Person {
  // No variable declaration allowed except for "RO associated constants"

  // the conventional way to define a "constructor" (Person::new())
  pub fn new() -> Self {  // "Self" is an alias for the current struct's type 
    return Person {
      name: "Gokulakrishnan S",
      age: 25
    }
  }
}
```

- "RO Associated constants" : These are defined within `impl`
- "Associated functions": These are functions within `impl` that take the instance (`&self`) as the first argument

## Traits

TBD

## Borrowing and Moving

- To "borrow" a variable means to temporarily transfer ownership to another variable (meaning that initial variable can be used later); to "move" a variable is to permanently transfer ownership
- When de-referencing a reference-variable, the ownership is transferred to the new variable unless the data-type referenced by the reference implements the "Copy" trait

## Lifetimes

TBD

## Comprehensive Rust

- Benefits of Rust
  - Type safety
  - No garbage collection
  - Double-frees?
- How is overflow defined?
- What is the "width of a pointer"?
- Scope: "... \[deallocated\] even if their data on the stack is still there"
