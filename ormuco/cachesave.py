'''
 09/26/2018 by Author May

 This is pseudo codes
 1. When router gets the request, the application should check whether the cache exists in the local server
 2. If cache exists in the local server response immediately
 3. If cache does not exist, check the nearest server and fetch the data
 4. If cache does not exist any servers, send request to the remote one and update the cache
 5. If any error occurs because of network issue, application response to the client with the proper message and exit

'''


import urllib2


class MyCache:

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10

    #----------------------------------------------------------------------
    def update(self, data):
        """
        Update the cache
        """
    #----------------------------------------------------------------------
    def remove(self):
        """
        Remove the cash data
        """
    #----------------------------------------------------------------------
    def fetch_data(self):
        """
        Remove the cash data
        """

    #----------------------------------------------------------------------

    def get_size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)
    #----------------------------------------------------------------------
    # Check the current time and
    def isExpired(self):
        """
        Return True or False
        """
        return True/False
    #----------------------------------------------------------------------
    def isExist(data):
        """
        Return True or False
        """
        return True/False


######################################################################

if __name__ == '__main__':

    url = 'https://ormuco.com/'
    if !cache.isExist(url): # if cache doesn't exist

        data = check_data_servers(url) #check other closely located servers

        if data is not empty:
            return data
        else: # Creat cache
            response = urllib2.urlopen(url)
            html = response.read()

            cache = MyCache()
            cache.update(html)
    else:

        cache.fetch_data() # if cache exists get the data from cache
