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

## `npm` package management
- To automatically update package version, use `npm verison <major|minor|patch>`
- [Use of `package-lock`](https://stackoverflow.com/questions/44297803/what-is-the-role-of-the-package-lock-json)
- [`npm --package-lock-only`](https://stackoverflow.com/questions/55599356/what-does-npm-i-package-lock-only-do?rq=3)
- [`overrides`](https://stackoverflow.com/questions/15806152/how-do-i-override-nested-npm-dependency-versions)
- [dependency vs. dev vs. peer](https://stackoverflow.com/questions/18875674/whats-the-difference-between-dependencies-devdependencies-and-peerdependencie)

## Cases
### Case 1
- Do initial commits
- `npm i <package> [--save-peer]`
- Same error if only `node_modules` is deleted / both `package-lock.json` and `node_modules` are deleted
### Case 2
- Is it of no use if `package.json` is updated, but the corresponding update of `package-lock.json` (assuming it exists) is not done?
- Leave `package-lock.json` as it is; update only `package.json` (change version and do some updates); delete `node_modules`
- Same error as above
- Inference: If `package-lock.json` exists, the versions of the downloaded packages will be in accordance with that;
  at the same time, a check is also done with `package.json` to ensure both `package` and `package-lock` are on the same page

## Remove unintended `peer: "true"`
- Commit to B1 with `peer: "true"` itself
- On B2: `git diff B1 package* > ./package-patch.patch`
- On B1: 
  - `git reset --soft HEAD~1`
  - `git restore --staged .`
  - `git apply -3 ./package-patch.patch`

## Modules

## Misc
- Command-line arguments: Accessed using `process.agrv`
  - First element is (usually) node-runtime path; second is file-name (?)
