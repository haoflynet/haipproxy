from haipproxy.config.settings import (
    TEMP_TMALL_QUEUE, VALIDATED_TMALL_QUEUE,
    TTL_TMALL_QUEUE, SPEED_TMALL_QUEUE
)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class TmallValidator(BaseValidator, ValidatorRedisSpider):
    name = 'tmall'
    urls = [
        'https://rate.tmall.com/list_detail_rate.htm?itemId=538232353890&sellerId=1862759827&order=3&currentPage=1&callback=jsonp'
    ]
    task_queue = TEMP_TMALL_QUEUE
    score_queue = VALIDATED_TMALL_QUEUE
    ttl_queue = TTL_TMALL_QUEUE
    speed_queue = SPEED_TMALL_QUEUE
    success_key = 'rateContent'