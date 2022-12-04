import logging

logger = logging.getLogger()

# what goes in and out
def publish_event(*args, **kwargs):
    # what happens here?
    ...
    # does this log correctly?
    logger.info(f"publishing: {args}, {kwargs}")
