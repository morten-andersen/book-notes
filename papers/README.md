### Software Development Papers

* 🔗 [Spotlight on ACM A.M. Turing Laureates](https://www.acm.org/turing-award-50/spotlight-on-turing-laureates)

#### Classical Papers

* **Leslie Lamport, 1978** [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
* **Ken Thomson, 1984** [Reflections on Trusting Trust](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf)
* **James Hamilton, 2007** [On Designing and Deploying Internet-Scale Services](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton.pdf)

#### Cryptography

* **Whitfield Diffie and Martin E. Hellman, 1976** [New Directions in Cryptography](https://www.cs.jhu.edu/~rubin/courses/sp03/papers/diffie.hellman.pdf)
* [EPC342-08 - Guidelines on cryptographic algorithms usage and key management](https://www.europeanpaymentscouncil.eu/document-library/guidance-documents/yearly-update-guidelines-cryptographic-algorithms-usage-and-0)
  * rev. 13 in 2024
  * contains recommendations on algorithms and key sizes
* **Alex Biryukov, Daniel Dinu, and Dmitry Khovratovich** [Argon2: the memory-hard function for password hashing and other applications](./argon2-specs-1.3.pdf)
  * winner of the [*Password Hashing Competition*](https://www.password-hashing.net/) in 2015
  * [GitHub repository](https://github.com/p-h-c/phc-winner-argon2)
* **European Union Agency for Cybersecurity (ENISA)** [Pseudonymisation techniques and best practices](https://www.enisa.europa.eu/publications/pseudonymisation-techniques-and-best-practices)
  * EU advices on how personal data should be handled
* **Jim Waldo, 2019** [A Hitchhiker's Guide to the Blockchain Universe](https://queue.acm.org/detail.cfm?id=3305265)
* **Thomas Wu, 2002** [SRP-6: Improvements and Refinements to the Secure Remote Password Prototol](http://srp.stanford.edu/doc.html)
  * Proton blog post on [Improved Authentication for Email Encryption and Security](https://proton.me/blog/encrypted-email-authentication) which covers some interesting implementation details of their usage of SRP. They also have an excerpt from an old paper covering there SRP usage in more details[ProtonMail Security Features and Infrastructure](./ProtonMail_Authentication_excerpt_30992d07f9.pdf)
  * [Secure Remote Password protocol](https://en.wikipedia.org/wiki/Secure_Remote_Password_protocol)

#### Streaming Algorithms

* **Robert Morris, 1977** [Counting large numbers of events in small registers](https://www.inf.ed.ac.uk/teaching/courses/exc/reading/morris.pdf) - approximate counting, the math in the paper is explained in
  * [Approximate Counting with Morris's Algorithm](https://gregorygundersen.com/blog/2019/11/11/morris-algorithm/)
  * [Morris's Algorithm for Approximate Counting](https://arpitbhayani.me/blogs/morris-counter)
  * **Philippe Flajolet, 1985** [Approximate Counting: A Detailed Analysis](http://algo.inria.fr/flajolet/Publications/Flajolet85c.pdf)
* **Ted Dunning, 2019** [Computing Extremely Accurate Quantiles Using *t*-digest](https://arxiv.org/pdf/1902.04023.pdf)
  * algorithm for computing percentiles with very little space
  * https://github.com/tdunning/t-digest

#### Memory Models and Synchronization

* [JSR-133: Java Memory Model and Thread Specification, 2004](https://www.cs.umd.edu/~pugh/java/memoryModel/jsr133.pdf)

#### Quantum Computing

* [Assessing the Quantum-Computing Landscape](https://cacm.acm.org/magazines/2022/10/264854-assessing-the-quantum-computing-landscape/fulltext) (*Communications of the ACM, October 2022, Vol. 65 No. 10, Pages 57-65*) Overview article of the state of Quantum Computing in 2022.
  * currently most advanced quantum computers has less than 100 qubits. A general purpose computer would require approximately one million qubits to be useful. That is at least a decade away.
  * the different cloud computing platforms are beginning to offer access to quantum computers - one of these is [AWS Braket](https://aws.amazon.com/braket/). Most of these are programmed using tools based on Python.

#### Collections of Papers

* 🔗 [Reading List for the mindful Software Engineer](https://gerlacdt.github.io/posts/classic-papers/)
* 🔗 [Papers We Love](https://github.com/papers-we-love/papers-we-love)

#### Other

* [Personnummeret i CPR-systemet](https://www.cpr.dk/media/17534/personnummeret-i-cpr.pdf)
