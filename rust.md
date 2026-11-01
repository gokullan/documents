# Rust

## Misc

- `const` is used to declare *compile-time* constants

## Strings

```rs
const s: String = "abcd"
```

- Strings cannot be indexed as in other languages
- `String` vs. `slice`

## Vectors

```rs
let vec1 = vec![0; 5];  // initializes a vector of length 5 with all zeros
let vec2 = Vec<i32>::new();
```

- `vec1` is a pointer to a struct in the following manner (?)

## Hash Maps

```rs
let mut my_map: HashMap<String, i32> = HashMap::new()
```

## Comprehensive Rust

- Benefits of Rust
  - Type safety
  - No garbage collection
  - Double-frees?
- How is overflow defined?
- What is the "width of a pointer"?
- Scope: "... \[deallocated\] even if their data on the stack is still there"
