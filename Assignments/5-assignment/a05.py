# Your code for get_companies_names goes here
def get_companies_names(companies):
    b_list = []
    for company in companies:
        b_list.append(company['Company Name'])
    return b_list






# Your code for get_countries goes here

def get_countries(companies):
    mydict = {}
    for company in companies:
        country = company['Country']
        if country in mydict:
            mydict[country] =country+1
        else:
            mydict[country] = 1
    return mydict




# Your code for get_companies goes here

def get_companies(companies, location):
    c_list = []
    for company in companies:
        if location['city'] == company['City'] :
            c_list.append(company['Company Name'])
    if len(c_list) == 0:
        return None
    else:
        return c_list
