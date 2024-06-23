### Architectural Resources

#### API Design

* **Joshua Bloch, 2006** [How to design a good API and why it matters](./how-to-design-a-good-api.pdf)

#### Evolving a Microservice Architecture

*.. think of evolving a microservice architecture like “trimming a hedge” so that it eventually grows correctly, rather than a top-down or one-time architecture (or re-architecture) effort. It’s a dynamic and progressive process.* -- [Uber - blog post](https://www.uber.com/en-NL/blog/microservice-architecture/)

#### Domain-Oriented Microservice Architecture

* **Uber's blog post** [Introducing Domain-Oriented Microservice Architecture](https://www.uber.com/en-NL/blog/microservice-architecture/)
  * grouping of microservices into ***domains***, which is a logical grouping of functionality. The example given in the blog post is the *map search* service which is one domain.
  * collections of ***domains*** into ***layers***. Each ***layer*** can only depend on ***layers*** below it. Uber has established 5 layers
    * *edge layer* - exposing external APIs
    * *presentation layer* - API for clients (e.g. for mobile and web)
    * *product layer*  - functionality for a specific line of the business - based on the names it sounds to be 'verbs' (i.e. services)
    * *business layer* - general functionality used by all product domains - based on the names it sounds to be 'nouns' (i.e. data containers)
    * *infrastructure layer* - storage and networking
  * each ***domain*** exposes a ***gateway*** with a clean interface. No microservices can be accessed directly.
  [![Domain Gateway](domain-oriented-gateways.png "Domain Gateway")](domain-oriented-gateways.png)

#### Distributed Systems

* **Waldo, J., Wyant, G., Wollrath, A. & Kendall, S., 1994** [A Note on Distributed Computing](https://scholar.harvard.edu/files/waldo/files/waldo-94.pdf)
  * see also the [fallacies of distributed computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)
* **Saltzer, J.H., Reed, D.P. & Clark, D.D., 1981** [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf)
  * [End-to-end principle](https://en.wikipedia.org/wiki/End-to-end_principle)

#### Authorization

* **John Mikael Lindbakk** [Authorisation Patterns for Monoliths and Microservices](https://lindbakk.com/blog/authorisation-patterns-for-monoliths-and-microservices)
  * different patterns
    * *Native Authorization Pattern* building the authorization in pure code. Hard to verify the company policy.
    * *Internal Non-Native Authorization Pattern* enforced in the code, but written in a different policy language. Easier to report.
    * *Proxy Pattern / Gateway Pattern* authorization on the gateway. All internal traffic is trusted. No defense in depth.
    * *Gloabal Authorization Service Pattern* authorization by calling a central authorization service from every service.
    * *Infrastructure-Aware Policy Pattern* authorization in e.g. a service mesh or in AWS IAM. Vendor lock in.
    * *Local Authorization Service Pattern* authorization using e.g. [OPA - Open Policy Agent](https://www.openpolicyagent.org/) using an external policy language.
      * see e.g. the [OPA Guide on authorization for the HTTP APIs of a service](https://www.openpolicyagent.org/docs/latest/http-api-authorization/)
  * further information in **Ekaterina Shmeleva**'s master thesis [How Microservices are Changing the
Security Landscape](https://aaltodoc.aalto.fi/server/api/core/bitstreams/a0bc2320-95e1-49e4-a55e-374243839efc/content)
