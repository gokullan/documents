# NodeJS

## File handling
### Using `async/await`
```js
const fs = require('fs/promises');
// reading
const contents = await fs.readFile(file, encoding);
// writing
await fs.writeFile(filePath, data);
```

## Modules

## Misc
- Command-line arguments: Accessed using `process.agrv`
  - First element is (usually) node-runtime path; second is file-name (?)
