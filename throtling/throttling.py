from rest_framework.throttling import UserRateThrottle

class CustomRateThrottle(UserRateThrottle):
    scope='customrate'
    #now go to settings.py to set rate and use this class as your throttle class for throttling different views.