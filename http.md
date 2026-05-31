# HTTP Guide

## [CORS - Cross Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
- Origin: `(Scheme, domain, port)`
- `access-control-allow-origin`
  - This response-header specifies the (request) origins for which the server can respond
  - The server checks the `origin` header sent in the request (this header is added by the browser and cannot be removed)
- `access-control-allow-credentials`
  - When `credentials` is set to `include` on the client-side, then 
    - `access-control-allow-origin` must include the requesting origin
    - This response-header must be set to `true`
    - Does this indicate that the client is allowed to send credentials or the server is allowed to respond with credentials (`set-cookie`)?
  - See also [CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)
- Simple request?
- Preflight request: An `OPTIONS` request used to validate if CORS is configured correctly for the request before actually making that request
- cURL vs browser-requests?
