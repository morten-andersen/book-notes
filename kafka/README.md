### Kafka - The Definitive Guide, ed. 2

[*Kafka: The Definitive Guide, Real-Time Data and Stream Processing at
Scale*](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)

#### Chapter 1. **Meet Kafka** - Components and Terms

#### Chapter 2. **Installing Kafka**

#### Chapter 3. **Kafka Producers** - Writing Messages to Kafka

High level producer overview (p.94)

![Kafka Producer](01-kafka-producer.png "Kafka Producer")

#### Chapter 4. **Kafka Consumers** - Reading Data from Kafka

##### Consumer groups

![Kafka Consumer Groups](02-kafka-consumer-groups.png "Kafka Consumer Groups")

If several applications subscribes to all the messages from the same *topic*, each application must have a *consumer group*.

Scaling of reading and processing of messages from the topics happen by adding consumers to an existing consumer group. Each additional consumer in a group will only get a subset of the messages.
