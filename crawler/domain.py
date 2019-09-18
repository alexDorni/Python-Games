from urllib.parse import urlparse
"""
    Some urls don't have a specified domain
    www
    name.com
    mail.gov.etc.
    name.example.com
"""


def get_sub_domain_name(url):
    # Working with internet must be in a try catch(Exception)
    try:
        # name.example.com but we want only example.com
        return urlparse(url).netloc
    except Exception as e:
        print("Domain error {}".format(e))
        return ''


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        print("String split error {}".format(e))
        return ''
