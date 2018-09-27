from urllib.parse import urlparse

#####-ISSUE-#####
#The following favours country specific domains (example.co.ke)

#Get domain name (example.co.ke)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
        #For single level domain suffix (example.com);
        #return results[-2] + '.' + results[-1]
    except:
        return ''
        

#Get sub domain name (sub.example.co.ke)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
