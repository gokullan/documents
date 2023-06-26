# CodeIgniter

-   PHP application framework
-   MVC design
    -   Controller
        -   receives request and contains response logic
        -   requests data from the model
    -   Model
        -   database manipulation
        -   returns data to the contoller
    -   View
        -   To render data in browser (HTML + PHP)
        -   recieves data from controller and sends to the user

## Folder structure
-   Starting point: `public/index.php` ?
-   Setup `.env` file
    -   CI_ENVIRONMENT
    -   baseURL (='http//localhost' ?)
-   `vendor`
    -   dependencies for codeigniter
    -   never edit these files
-   `app`
    -  `Config`: Contains configuration files for libraries used by CodeIgniter
        -   `Routes.php`:
            -   Used for navigation inside website
            -   `setDefaultController` sets the controller for the default (home) page. (`http://localhost/controllerName` loads the index method inside the controller).
            -   `view('page_name')` loads `page_name.php` from the `views` directory.
