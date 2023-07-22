# Angular

## CLI
-   `ng new project-name`
-   `ng serve`
-   `ng generate component component_name`
    -   `ng g c parent/child --flat`: generates component `child` under (the existing) component parent

-   Typescript

    -   Declaring types

        -   myVar: any

        -   myVar: number\[\]

        -   Type of a variable cannot be changed once defined or
            declared

    -   Classes

        -   class Car {

            constructor() { }

            \<properties and methods\> }

        -   car: Car = new Car()
        -   Constructor shorthand
        ```typescript
        class Sample {
            constructor(
                private prop1: string,
                // ...
            ) {}
        }
        ```

    -   Application is written is TypeScript and converted to JavaScript
        (and outputs it in the distribution folder)

        -   Browsers cannot understand TypeScript

-   When importing TypeScript files, no need to put '.ts' at the end
-   Interfaces
    -   Dynamic fields
    ```typescript
    interface Example {
        [prop : string] : string
        // expects a string as key and string as value
    }
    ```

## Modules
-   An angular application consists of many modules
-   Every application has at least one (root) module - `app.module.ts`
-   Each module is made up of components and services

## Components

-   `main.ts` is the entry point for the angular application (followed by `app.module.ts`)
-   Application is built out of various components
-   Each components controls a portion of the view on the browser

-   app.component is the root component

-   app.module.ts bootstraps the app component

-   Each component consists of 3 parts

    -   componentName.component.ts (logic)

    -   componentName.component.html (view/template)

    -   componentName.component.css (styles)

-   It also has some metadata attached to it by means of the `@Component` decorator (which differentiates a normal class from a component class); a decorator is a function that attaches information to the class right below it.
    ```typescript
    @Component({
        selector: 'tag-name'
        templateUrl: './name.component.html',
        // template: `HTML code`
        styleUrls: ['./name.component.css']
        // styles: [`CSS code`]
    })
    ```
-   Everytime a new component is created, the module needs to be made aware of this - this is done through import and declaration in `@NgModule` (`ng g` does this automatically)
-   `selector` can be specified in 2 other ways - `'.class-name'` (to use as HTML class) and `'[attribute]'` (to use as HTML attribute) 
-   Nested components

    -   import { ComponentClassName } from './\<path\>/index'
        (inside the parent component)

        -   The index.ts exports everything in
            ./\<path\>/something.component.ts

    -   Add 'directives: \[ComponentClassName\]' in the \@Component
        decorator of the parent component

-   CSS files (for the entire application, if any) should be put inside
    the 'public' directory and can be referenced in the index.html file
    as "/styles.css"

## Data Flow
-   **Into the view** (component class -> component template)
    -   Interpolation (evaluate content inside curly braces)
        -   cannot contain assignments
        -   cannot access global JS variables (like `window`)

    -   Property binding
        -   Attribute (HTML) vs. Property (DOM)
            -   Attributes initialize DOM properties
            -   Once attribute is initialized, it cannot be changed
            -   `HTMLElement.getAttribute('value')` is different from `HTMLElement.value`. The former will show the initial value even after the value is changed. See [this](https://stackoverflow.com/questions/11973678/difference-between-element-value-and-element-getattributevalue) for more details

        -   ```html
            <!-- interpolation -->
            <input id="{{someVar}}">

            <!-- property-binding -->
            <input [id]="someVar">  <!-- or <input bind-id="someVar"> -->
            <input [disabled]="false">  <!-- interpolation cannot be used for this -->
            ```

        -   <https://stackoverflow.com/questions/18487480/angular-expression-in-attribute>

    -   Class binding

        -   Regular class attribute becomes a dummy in the presence of class binding
        ```html
        <!-- only the class (value) of class_variable is applied -->
        <div class='class-1' [class]='class_variable'>  

        <!-- applying classes conditionally -->

        <!-- single class -->
        <div [class.class-1]="expression_that_evals_to_bool">

        <!-- multiple classes -->
        <div [ngClass]="object">
        <!--
        where object is of the format
        {
            "class-1": true;
            "class-2": false;
            ...
        }
        -->
        ```

    -   Style binding
        ```html
        <h2 [style.propertyName]="expression_returing_suitable_string"> Hello </h2>

        <h3 [ngStyle]="styleObj"> World </h3>
        <!--
        where styleObj is an object of the form,
        {
            property: "value" 
        }
        -->
        ```

-   **Out of the view** (template -> class)

    -   Event binding
    ```html
    <button (eventName) = "func($event)"></button>
    <!--
    $event is a special variable that provides
    information about the DOM event that was raised
    -->
    <button (eventName) = "someVar='Hello, World!'"></button>
    ```

    -   Template reference variables
        -   to easily pass an HTML element into the class
        ```html
        <input #myInput... >
        <button (click)=someFunc(myInput.value)></button>
        ```
        -   `myInput` can be passed as an argument (to a function)
            from the HTML page
        -   All DOM properties of this element can be accessed using
            `myInput`

-   **2-way data binding**
    -   Data in the model and view (if bound, as in the case of form inputs) need to be consistent, (i.e.), if there is a change in the model (class property), it should be reflected in the view and vice-versa.
    -   To use `ngModel`, go to `app.module.ts`:
        -   import forms module
        -   add FormsModule to the imports array

    ```html
    <input [(ngModel)]="varName">
    ``` 
    where `varName` is a property defined in the component class

## Pipes 
-   {{ expr | pipe}} -- to transform data in the view

-   String pipes
    -   lowercase
    -   uppercase
    -   titlecase
    -   slice:start:end-1 (0-based indexing)

-   JSON pipe `{{ object_var | json }}`

-   Number pipe
    ```html
    {{ 5.678 | number:'3.2-3' }}
    <!-- number:'min-int-digits.min-digits-max-digits' -->
    ```

-   Percent pipe `{{ 0.25 | percent }}`

-   Currency pipe `{{ 25 | currency:'GBP':'code'}}`
    -   If 'code' is specified, output is GBP25; else the currency symbol is displayed before the number (GBP stands for Great Britain Pound)

-   Date pipe

    -   `{{ date | date:short }}` (where the 1st `date` is a Date
        object)

    -   Other args to date pipe   
        -   shortDate
        -   shortTime
        -   *short* can be replaced with *medium* or *long*

## Directives
-   Custom HTML attributes provided by Angular
-   Some useful directives
    -   `ngClass` (see class binding)
    -   `ngStyle` (see style binding)
    -   `ngModel` (see 2-way data binding)
    -   `ngIf`
        -   **Note**: `ng-template` tag is a container for elements that can be used by `ngIf`
    ```html
    <h2 *ngIf="exp_returning_true_or_false; else spanish">Hello!</h2>
    <ng-tempate>
        <h2 #spanish>Hola!</h2>
    </ng-tempate>

    <!-- alternate syntax -->
    <div *ngIf="boolean_exp; then trueBlock; else falseBlock"></div>
    <!-- where trueBlock and falseBlock are template references to elements defined using ng-template -->
    ```
    -   `ngSwitch`
    ```html
    <div [ngSwitch]="myVar">
        <div *ngSwitchCase="value1"> Hi! </div>
        <div *ngSwitchCase="value2"> Hola! </div>
        <div *ngSwitchDefault="value3"> Hello! </div>
    </div>
    ```
    -   `ngFor`
    ```html
    <!-- elementList is an array defined in the component class -->
    <ul *ngFor="let element of elementList; index as i">
        <li>{{ i }} - {{ element }}</li>
    </ul>
    <!--
    other keywords to use in ngFor (keyword as k)
    Boolean return-type (couple with ngIf):
    -   first 
    -   last
    -   odd
    -   even
    -->
    ```

## Component Interaction

-   @Input and @Output decorators ([Refer](https://angular.io/guide/inputs-outputs))
    -   @Input
        -   (For child) To accept input from parent
        ```html
        <!-- inside parent component template -->
        <child-comp [parentData]="variable_from_parent_class"><child-comp>
        ```
        ```typescript
        // inside child component class
        import { Input, ... } from '@angular/core'
        
        Class ChildComp {
            @Input() public parentData = someAppropriateInitialization;
            // @Input('parentData') public newName = ... ;
            // use parentData (or newName) as needed inside the template
        }
        ```
    -   @Output
        -   For child to send out events to parent
        ```typescript
        // emit event from child
        @Output() public childEvent = new EventEmitter();
        ...
        childEvent.emit(message_to_send);
        ```
        ```html
        <!-- Catch the event in the place where the child component is used -->
        <child-comp (childEvent)="message_from_child=$event"></child-comp>
        ```

    -   [Using subjects](https://angular.io/guide/component-interaction#parent-and-children-communicate-using-a-service)
    ```typescript
    sampleSubject = new Subject<string>(); 
    // create Observable stream
    sampleSubject$ = this.sampleSubject.asObservable();
    // set value
    this.sampleSubject.next("Hello!");

    // subscribe wherever required
    // to see the new changes
    this.sampleSubject$.subscribe(
        data => {
            // do whatever required ...
        }
    )
    ```

-   Asynchronous functions
    ```typescript
    // using `lastValueFrom`
    asyc sampleFunction() {
        let response = await lastValueFrom(anotherAsyncFunction());
    }
    ```

-   2-way binding --
    <https://stackoverflow.com/questions/41464871/update-parent-component-property-from-child-component-in-angular-2>

-   Comprehensive --
    <https://stackoverflow.com/questions/37587732/how-to-call-another-components-function-in-angular2>

-   Change Detection --
    <https://www.sitepoint.com/change-detection-angular/>

## Service 
-   Principle/s used
    -   Do not Repeat Yourself (DRY)
    -   Single Responsibility Principle

-   a class with a specific task (filename.service.ts;
    class: filenameService)

-   Creating and using a service
    -   `ng g s service-name`
        -   `@Injectable` decorator is present inside `serviceName.service.ts` to indicate that the service itself might have injectable dependencies.
    -   Register service with injector
        -   Better to register in `AppModule` in the `providers` property (metadata)
    -   Declare as dependency in required component
    ```typescript
    constructor(private _myService: myService) {}
    // vs-code automatically does an import (?)

    ngOnInit() {
        // use _myService to populate any component property
    }
    ```

-   Applications

    -   To share data

    -   Implement application logic (which can be used by various
        components)

    -   External interaction (connecting to DB)

-   Dependency Injection

    -   Assume we have 3 classes -- Engine, Tyre and Car. Car
        depends on Engine and Tyre classes

    -   Code without DI

        -   The Car class creates instances of Engine and Tyre in
            its constructor

        -   Code is not flexible

            -   If the parameters to the constructors of Engine
                and/or Tyre change, the change has to be made in the
                code of the Car class as well
            ```python
            class Car:
                def __init__(self)
                    self.engine = new Engine();
                    self.tyre = new Tyre();
            ```

        -   Testing is difficult

    -   DI as a design pattern

        -   Pass dependencies (from external sources) as parameters to a class rather than creating them itself.
            ```python
            class Car:
                def __init__(self, engine, tyre)
                    self.engine = engine;
                    self.tyre = tyre;
            ```

        -   Disadvantage: We need to manually create all
            dependencies for a class(?) as they need to be passed as
            parameters. This is difficult if the number of
            dependencies are large (and recursive, (i.e.), a dependency itself has dependencies)

    -   DI as a framework (provided by Angular)

        -   Regsiter dependencies in an Injector
            (Injectore is like a container for (of?) dependencies)

        -   **Define service class** (use \@Injectable decorator
            since a service may have another service as dependency)
            **-\>** **register with injector** (Provider metadata (injector 'provides' services to required components))
            **-\> declare service as dependency wherever required**

-   Lifecycle Hooks

    -   ngOnChanges --
        <https://www.tektutorialshub.com/angular/angular-ngonchanges-life-cycle-hook/>

    -   All

        -   <https://indepth.dev/posts/1494/complete-guide-angular-lifecycle-hooks>

        -   <https://blog.logrocket.com/angular-lifecycle-hooks/>

## Interface
```typescript
export interface Test {
    id: number,
    name: string,
    // ...
}
```

## HTTP and Observables (Observable =\> HTTP response)

-   Observable: A sequence of items that arrive asynchronously over time
-   `RxJS` is the library used to work with Observables
-   Inside `app.module.ts`, `import { HTTPClientModule } ...` and include HTTPClientModule in the imports property
-   Steps
    -   In the service, provide the HTTPClient class in the constructor
        and make a HTTP get request

    -   Cast observable into suitable format
    ```typescript
    // inside the service class
    // import statements ...
    import 'rxjs/add/operator/catch'
    import 'rxjs/add/operator/throw'
    export class MyService() {
        constructor(private http: HttpClientModule) {};
        // ...
        // Test is an interface
        getData() : Observable<Test[]> {
            // cast Observable into appropriate type
            return this.http.get<Test[]>(url)
                        .catch(this.errorHandler);
        }

        errorHandler(error: HttpErrorResponse) {
            Observable.throw(error.message || "Server Error");
        }
    }
    ```
    -   Subscribe to observable (observable doesn't provide data unless subscribed)
    ```typescript
    // inside component class
    ngOnInit() {
        this._myService.getData()
            .subscribe(data => {
                // do something with data
            },
            error => {
                // error handler
            });
    }
    ```
-   Using promises --
    <https://stackoverflow.com/questions/50303033/how-to-return-a-promise-from-subscribe-in-angular-5>

-   Subscribe or use service object directly? (See 
    [here](https://stackoverflow.com/questions/45296967/using-service-data-in-components-template-is-it-a-good-practice))

-   Constructor vs. `ngOnInit` for subscribing?  

Doubts

-   ngModel

-   Sharing data between siblings --
    <https://stackoverflow.com/questions/43940351/how-do-i-share-data-between-sibling-components-in-angular>

-   Dependency injection - injecting services inside root component creates only one service instance?
    (Even if that service is used as dependency for other services?)
