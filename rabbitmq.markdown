# RabbitMQ

-   RabbitMQ is a distributed message broker
    -   A message broker is software that allows applications to communicate
        with each other
    -   Messages could be something like "User added a new item to cart" or
        "User logged in from another device", ...
    -   Allows for loose-coupling
-   Uses AMQP - Advanced Message Queuing Protocol
-   Asynchronous communication (as opposed to synchronous in case of API GET
    requests)

## Terminology
-   Analogy - Postal service
-   Producer - publishes messages into RabbitMQ
-   Message broker - forwards message to final destination
-   Consumer - listens to messages that come off message broker
-   Exchange - (the "brains")
    -   A message broker may have multiple exchanges
    -   Producer pushes messages to exchange
-   Queue ("letter box")
    -   Exchange pushes messages into one or more queues
-   Binding
    -   An exchange can be tied to many queues and vice-versa
-   Connection/ channel
    -   A connection can have multiple channels; each channel uses a different
        thread (so the messages are independent)
    -   Using multiple channels (as opposed to multiple connections) saves a
        lot of resources.

## Resources
- [ByteByteGo E-commerce
    example](https://blog.bytebytego.com/p/why-do-we-need-a-message-queue)
- [Ready vs. Unacked](https://stackoverflow.com/questions/31915773/rabbitmq-what-are-ready-and-unacked-types-of-messages)
