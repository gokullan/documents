# Hapi

-   Developed by Walmart
```js
server.route({
    path: '/',
    method: 'GET',
    handler: (request, h) => {
        return "Hello World!!!";
    }
})
```
-   For variations on `path` values, check [here](https://hapi.dev/tutorials/routing/?lang=en_US#path)
    -   `/path/{user}` (eg: `public/hapi` => `hapi` can be accessed via
        `request.params.user`)
    -   `/path/{user*}` (eg: `public/john/doe` => `john/doe` is accessed via
        `request.params.user`)
-   Register plugins as follows: `server.register(require('@hapi/inert'))`
-   Relative paths
    -   To respond with files using a relative path, use the `Path` module
```js
var Path = require('path');
// ...
Hapi.server({
    // ...
    routes: {
        files: {
           relativeTo: Path.join(__dirname, 'someDir'); 
        }
    }
});
```
-   [Handling CORS](https://stackoverflow.com/questions/57653272/how-to-allow-cors-in-hapi-js)   
```js
Hapi.Server({
    // ...
    "routes": {
        "cors": true,
    }
})
```
-   [Handling `multipart/form-data`](https://stackoverflow.com/questions/61957031/hapijs-not-accepting-form-data-requests)
```js
server.route({
    // ...
    options: {
        payload: {
            multipart: true,
            maxBytes: 2000000,
        }
    }
})
```
-   Handlers as objects
    -   The object must  contain one of the following: file (requires
        @hapi/inert plugin),  directory (requires @hapi/inert plugin), proxy
        (requires @hapi/h2o2  plugin), or view (requires @hapi/vision plugin).
-   Static file handling
    -   Use `@hapi/inert` (Adds `h.file(filename)` method to `h`)
    ```js
    // static file serving with inert
    handler: {
        file: "/path/file.html"
    }
    ```
    -   To server URLs of the form `/path/{filename}`, where `filename` is
        dynamic and all such `filename`s need to be served from the same
        directory, use the `directory` property in the handler object.

## Views
```js
// register the `vision` package
await server.register(require('@hapi/vision'));

server.views({
    engines: {
        html: require('handlebars'),
    },
    relativeTo: __dirname,
    path: './templates',  // all template files will be searched for in
    __dirname/templates
    helpersPath: './helpers',  // references to variables used in the templates
});

// rendering
server.route({
    // ...
    handler: {
        view: {
            template: 'file.html',
            context: {
                varName: value,
            }
        }
    }
    // another way
    handler: (request, h) => {
        return h.view('file.html', { // context obj }, {// layout override});
    }
});
```
## `hapi-swagger`
-   [Example](https://github.com/hapi-swagger/hapi-swagger/blob/master/examples/options.js)
    for `options`
-   [Authorization
    example](https://medium.com/@arpanmajibally/hapi-js-authentication-with-swagger-documentation-3fe916e24280)
    -   Use `securityDefinitions`

## Doubts
-   Absolute paths should be provided while serving files?
