import scrapy


class TeamBravo(scrapy.Spider):
    name = "Team_Bravo"
    allowed_domains = ['http://172.18.58.238/index.php']
    start_urls = ['http://172.18.58.238/headers.php']

    def website(self):
        # Use the Request library
        import requests
        # Set the target webpage
        url = "http://172.18.58.238/index.php"
        r = requests.get(url)
        # This will get the full page
        print("r.text= ..",r.text)
        # This will get the status code
        print("Status code:")
        print("\t *", r.status_code)
        # This will just get just the headers
        h = requests.head(url)
        print("Header:")
        print("**********")
        # To print line by line
        for x in h.headers:
            print("\t ", x, ":", h.headers[x])
        print("**********")
        # This will modify the headers user-agent
        #The HTTP headers User-Agent is a request header that allows a characteristic string that allows network
        # protocol peers to identify the Operating System and Browser of the  web-server. Your browser sends the user agent to every website you connect to.
        headers = {
            'User-Agent': 'Mobile'

        }
        # Test it on an external site
        url2 = 'http://172.18.58.238/headers.php'
        rh = requests.get(url2, headers=headers)
        print(rh.text)
        # Return status okay
        return print("OK")

ClassInstance = TeamBravo()
ClassInstance.website()

