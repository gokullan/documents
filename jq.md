# `jq`

- `.[] | (select EXPR)`: To perform a specific filtering operation on every element in an array of objects 
- `.[] | { message: ._source.service.message } | .message |= gsub(".*id: "; "") | .message`
