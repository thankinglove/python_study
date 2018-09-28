#!/usr/bin/env python3
# _*_coding:utf-8_*_


__author__ = 'Alex Li'
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.20.199'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("---->", ch, method, properties)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='hello',
                      #no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()