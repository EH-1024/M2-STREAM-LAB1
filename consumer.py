"""
consumer.py
----------------
This file contains the logic for a Consumer that continuously reads messages
from the queue and processes them.

The Consumer runs forever, just like a streaming system.
"""

import time
from queue import Queue

class Consumer:
    def __init__(self, q, delay=0.5):
        """
        PARAMETERS:
        - q : the shared queue (simulated topic)
        - delay : time to wait while processing each event (float)

        TODO:
        - Store the queue.
        - Initialize any state variables you may want later,
          e.g. a running total for stateful computations.
        """
        self.q = q
        self.delay = delay
        self.running_total = 0


    def start(self):
        """
        Main loop of the consumer.

        TODO:
        - Continuously call q.get() to receive events.
        - Print the event received.
        - Pass it to the process() function.
        """
        while True:
            event = self.q.get()
            print(f"Received event: {event}")
            self.process(event)

    

    def process(self, event):
        """
        TODO:
        - Simulate some processing time using time.sleep().
        - Transform fields (e.g., convert amount to float).
        - Implement optional filtering conditions.
        - Update any state (example: running total).
        """
        time.sleep(self.delay)  # Simulate processing time
        amount = float(event.get("amount", 0))
        self.running_total += amount
        print(f"Processed event. Running total: {self.running_total}")
   

# Debugging test

if __name__ == "__main__":
    """
    Run this alone to see consumer behavior.

    Note: It will block waiting for messages since no producer is running.
    """
    q = Queue()
    consumer = Consumer(q)
    consumer.start()
