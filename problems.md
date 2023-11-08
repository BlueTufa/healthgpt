```
❯ curl 'https://api.twitter.com/1.1/search/tweets.json?q=health&result_type=popular' -H "Authorization: Bearer $TWITTER_API_TOKEN"
{"errors":[{"message":"You currently have access to a subset of Twitter API v2 endpoints and limited v1.1 endpoints (e.g. media post, oauth) only. If you need access to this endpoint, you may need a different access level. You can learn more here: https://developer.twitter.com/en/portal/product","code":453}]}

# Disabled openapi tests because of free account rate limiting
# FAILED tests/openai_test.py::test_openai - openai.RateLimitError: Error code: 429 - {'status': 'come back later'}
# FAILED tests/search_test.py::test_health_check - openai.RateLimitError: Error code: 429 - {'status': 'come back later'}
```
