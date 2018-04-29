# -*- coding: utf-8 -*-

import json
import datetime as dt
import time

import logging

from kafka import KafkaClient, SimpleProducer

class DifcPipeline(object):
    def process_item(self, item, spider):
        return item



class KafkaPipeline(object):

    """Pushes serialized item to appropriate Kafka topics."""

    def __init__(self, producer, topic_prefix, aKafka):
        self.producer = producer
        self.topic_prefix = topic_prefix
        self.topic_list = []
        self.kafka = aKafka

    @classmethod
    def from_settings(cls, settings):
        kafka = KafkaClient(settings['KAFKA_HOSTS'])
        producer = SimpleProducer(kafka)
        topic_prefix = settings['KAFKA_TOPIC_PREFIX']
        return cls(producer, topic_prefix, kafka)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        # Construct the message
        datum = dict(item)
        datum["timestamp"] = dt.datetime.utcnow().isoformat()

        try:
            message = json.dumps(datum)
        except:
            message = 'json failed to parse'

        # Construct the topic
        prefix = self.topic_prefix
        appid_topic = "{prefix}.spout_{sourceId}".format(prefix=prefix, sourceId=datum["sourceId"])

        # Make sure topic exists
        self.checkTopic(appid_topic)

        # Send Message to kafka
        self.producer.send_messages(appid_topic, message)

        return item

    def checkTopic(self, topicName):
        if topicName not in self.topic_list:
            self.kafka.ensure_topic_exists(topicName)
            self.topic_list.append(topicName)
