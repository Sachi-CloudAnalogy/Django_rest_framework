from rest_framework.throttling import UserRateThrottle

# we can create class for different users
class JackRateThrottle(UserRateThrottle):
    scope = 'jack'