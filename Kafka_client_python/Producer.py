from confluent_kafka import Producer


# Install confluent_kafka
# pip3 install confluent_kafka==0.11.4
#1) Create Topic :
# docker exec kafka kafka-topics  --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic topic1
# 2) Liste Topics :
# docker exec -it kafka  kafka-topics  --list --zookeeper zookeeper:2181
#3) Send Message Topic kafka :
#docker exec --interactive --tty kafka  kafka-console-producer --bootstrap-server kafka:9092 --topic topic1
#) Read Message  from topic kafka :
#docker exec --interactive --tty kafka  kafka-console-consumer --bootstrap-server kafka:9092 --topic topic1 -- from-beginning

p = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
some_data_source = {"Phrase 1", "Phrase 2"}

for data in some_data_source:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('users', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()

