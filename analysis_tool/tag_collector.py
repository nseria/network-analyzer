import pandas as pd
import numpy as np

work_list = [
    "login-email", "login-google", "login-apple", "login-status",
    "using_ai",
    "upload_pdf", "download_pdf", "export_pdf",
    "integration_googlemap", "integration_googledrive", "integration_onedrive", "integration_zoom"
]

### -------------------------------------------------------------------------------- ###
### This categorization may not be correct. This project is for just practice. ----- ###
### I do not related to specific company or service. I have no conflict of interest. ###
### The functions below can be compressed, sorry!!. -------------------------------- ###
### -------------------------------------------------------------------------------- ###

# netloc to company, service dictionary
# tracker, notion_api, fn_api, domain -> [company or service, type, data]
# company: what company is using this domain
# type: tracker, notion_api, fn_api, domain
# data: what kind of data is collected, what is the purpose of this domain

netloc_dict = {
    "connect.facebook.net": ["facebook", "tracker", "ad"],
    "public.profitwell.com" : ["profitwell", "tracker", "analytics"],
    "googleads.g.doubleclick.net": ["google", "tracker", "ad"],
    "stats.g.doubleclick.net": ["google", "tracker", "ad"],
    "11762090.fls.doubleclick.net": ["google", "tracker", "ad"],
    "www.google.com/pagead": ["googleads", "tracker", "ad"],
    "analytics.tiktok.com": ["tiktok", "tracker", "ad"],
    "cdn.linkedin.oribi.io": ["linkedin", "tracker", "ad"],
    "px.ads.linkedin.com": ["linkedin", "tracker", "ad"],
    "googletagmanager.com": ["google", "tracker", "analytics"],
    "analytics.google.com": ["google", "tracker", "analytics"],
    "x.clearbitjs.com": ["clearbit", "tracker", "ad"],
    "app.clearbit.com": ["clearbit", "tracker", "ad"],
    "vitals.vercel-insights.com": ["vercel", "tracker", "analytics"],
    "js.partnerstack.com": ["partnerstack", "tracker", "analytics"],
    "grsm.io": ["partnerstack", "tracker", "analytics"],
    "http-inputs-notion.splunkcloud.com": ["splunk", "fn_api", "big-data"],
    "cdn.contentful.com": ["contentful", "fn_api", "knowledge"],
    "cdn.transcend.io": ["transcend", "fn_api", "privacy"],
    "telemetry.transcend.io": ["transcend", "fn_api", "privacy"],
    "munchkin.marketo.net": ["adobe", "tracker", "ad"],
    "cdn.metadata.io": ["metadata", "tracker", "analytics"],
    "api-iam.intercom.io": ["intercom", "fn_api", "customer-support"],
    "js.intercomcdn.com": ["intercom", "fn_api", "customer-support"],
    "widget.intercom.io": ["intercom", "fn_api", "customer-support"],
    "segment.prod.bidr.io": ["beeswax", "tracker", "ad"],
    "ib.adnxs.com": ["appnexus", "tracker", "ad"],
    "acdn.adnxs.com": ["appnexus", "tracker", "ad"],
    "www.linkedin.com": ["linkedin", "tracker", "ad"],
    "snap.licdn.com": ["linkedin", "tracker", "ad"],
    ".cloudfront.net": ["cloudfront", "tracker", "analytics"],
    ".mktoresp.com": ["adobe", "tracker", "ad"],
    ".notion.so": ["notion", "notion_domain", "default"], # counting the number of notion.so subdomains roughly
    "msgstore.www.notion.so": ["notion", "notion_domain", "primus"],
    "aif.notion.so": ["notion", "notion_domain", "tracker"],
    "analytics.pgncs.notion.so": ["notion", "notion_domain", "analytics"],
    "exp.notion.so": ["notion", "notion_domain", "server-interaction"],
    "file.notion.so": ["notion", "notion_domain", "file"],
    ".ingest.sentry.io": ["sentry", "fn_api", "error-tracking"],
    ".gist.build": ["gist", "tracker", "analytics"],
    ".customer.io": ["customer.io", "tracker", "analytics"],
    ".googleapis.com": ["google", "fn_api", "integration-google"],
    "maps.googleapis.com": ["google", "fn_api", "integration-google"],
    ".gstatic.com": ["google", "tracker", "analytics"],
    ".apple.com": ["apple", "fn_api", "integration-apple"],
    ".mzstatic.com": ["apple", "fn_api", "integration-apple"],
    "partnerlinks.io": ["partnerlink", "tracker", "analytics"],
    "www.googleadservices.com": ["google", "tracker", "ad"],
    "www.google.co.kr": ["google", "tracker", "ad"],
    "s3-us-west-2.amazonaws.com": ["amazon", "fn_api", "cloud-storage"],
}

aif_notion_list = [
    "ib.adnxs.com", "px.ads.linkedin.com", "414-xmy-838.mktoresp.com",
    "cdn.linkedin.oribi.io", "analytics.google.com", "www.linkedin.com",
    "www.facebook.com"
]

# get notion api list of each work from csv_storage, /api/v3/~
# if path contains /api/v3/, append the word after /api/v3/ to notion_api_list
def get_notion_api_list(work):
    notion_api_list = []
    path_df = pd.read_csv('./../csv_storage/' + work + '_path.csv')
    for path in path_df['path']:
        if isinstance(path, float):
            path = str(path)
        if "/api/v3/" in path:
            notion_api_list.append(path.split("/api/v3/")[1])
    return notion_api_list

def report_notion_api():
    result = []
    for work in work_list:
        result.append((work, get_notion_api_list(work)))
    return result

# get notion sub domain list from csv_storage
# if netloc contains notion.so, append the netloc to notion_subdomain_list
def get_notion_subdomain_list(work):
    notion_subdomain_list = []
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        if "notion.so" in netloc:
            notion_subdomain_list.append(netloc)
    return notion_subdomain_list

def report_notion_subdomain():
    result = []
    for work in work_list:
        result.append((work, get_notion_subdomain_list(work)))
    return result

# make a list of the services that are revealed as tracker in the netloc_dict
# just use netloc_dict, and append the service name to tracker_list
# if service name is already in the tracker_list, do not append
def total_tracking_service_list():
    tracker_list = []
    for netloc_word in netloc_dict.keys():
        if netloc_dict[netloc_word][1] == "tracker":
            service = netloc_dict[netloc_word][0]
            if service not in tracker_list:
                tracker_list.append(service)
    return tracker_list

# count the number of trackers in each work
# first, we need to check if the netloc from the csv_storage contains the netloc words in the netloc_dict
# then if type in the netloc_dict is tracker, add the count value of netloc from netloc_df that contains the netloc_word of tracker, to the count
def count_tracker(work):
    count = 0
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        for netloc_word in netloc_dict.keys():
            if netloc_word in netloc:
                if netloc_dict[netloc_word][1] == "tracker":
                    # get the value right next to the netloc that satisfies the condition
                    count += netloc_df.loc[netloc_df['netloc'] == netloc, 'count'].values[0]
    return count

def report_tracker_count():
    result = []
    for work in work_list:
        result.append((work, count_tracker(work)))
    return result

# make a list of the service that are revealed as fn_api in the netloc_dict
# first, we need to check if the netloc from the csv_storage contains the netloc words in the netloc_dict
# then if type in the netloc_dict is fn_api, append service name to fn_api_list
# if service name is already in the fn_api_list, do not append
def get_fn_api_list(work):
    fn_api_list = []
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        for netloc_word in netloc_dict.keys():
            if netloc_word in netloc:
                if netloc_dict[netloc_word][1] == "fn_api":
                    service = netloc_dict[netloc_word][0]
                    if service not in fn_api_list:
                        fn_api_list.append(service)
    # sort the list in alphabetical order
    fn_api_list.sort()
    return fn_api_list

def report_fn_api():
    result = []
    for work in work_list:
        result.append((work, get_fn_api_list(work)))
    return result

def merge_fn_api():
    fn_api_list = []
    for work in work_list:
        fn_api_list = list(set(fn_api_list + get_fn_api_list(work)))
    # sort the list in alphabetical order
    fn_api_list.sort()
    return fn_api_list


# make a list of the service that are revealed as tracker in the netloc_dict
# first, we need to check if the netloc from the csv_storage contains the netloc words in the netloc_dict
# then if type in the netloc_dict is tracker, append service name to tracker_list
# if service name is already in the tracker_list, do not append
def get_tracker_list(work):
    tracker_list = []
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        for netloc_word in netloc_dict.keys():
            if netloc_word in netloc:
                if netloc_dict[netloc_word][1] == "tracker":
                    service = netloc_dict[netloc_word][0]
                    if service not in tracker_list:
                        tracker_list.append(service)
    # sort the tracker_list in alphabetical order
    tracker_list.sort()
    return tracker_list

def report_tracker():
    result = []
    for work in work_list:
        result.append((work, get_tracker_list(work)))
    return result

# merge the tracker_list using get_tracker_list(work) and make a single list
# compare each list and merge them without duplication
def merge_tracker():
    tracker_list = []
    for work in work_list:
        tracker_list = list(set(tracker_list + get_tracker_list(work)))
    # sort the tracker_list in alphabetical order
    tracker_list.sort()
    return tracker_list


# make a list of the data that tracker collects : tracked_data_list
# first, we need to check if the netloc from the csv_storage contains the netloc words in the netloc_dict
# then if type in the netloc_dict is tracker, append data to tracked_data_list
# if data is already in the tracked_data_list, do not append
def get_tracked_data_list(work):
    tracked_data_list = []
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        for netloc_word in netloc_dict.keys():
            if netloc_word in netloc:
                if netloc_dict[netloc_word][1] == "tracker":
                    data = netloc_dict[netloc_word][2]
                    if data not in tracked_data_list:
                        tracked_data_list.append(data)
    # sort the tracked_data_list in alphabetical order
    tracked_data_list.sort()
    return tracked_data_list

def report_tracked_data():
    result = []
    for work in work_list:
        result.append((work, get_tracked_data_list(work)))
    return result

# make a list of the data that fn_api collects : fn_api_data_list
# first, we need to check if the netloc from the csv_storage contains the netloc words in the netloc_dict
# then if type in the netloc_dict is fn_api, append data to fn_api_data_list
# if data is already in the fn_api_data_list, do not append
def get_fn_api_data_list(work):
    fn_api_data_list = []
    netloc_df = pd.read_csv('./../csv_storage/' + work + '_netloc.csv')
    for netloc in netloc_df['netloc']:
        if isinstance(netloc, float):
            netloc = str(netloc)
        for netloc_word in netloc_dict.keys():
            if netloc_word in netloc:
                if netloc_dict[netloc_word][1] == "fn_api":
                    data = netloc_dict[netloc_word][2]
                    if data not in fn_api_data_list:
                        fn_api_data_list.append(data)
    # sort the fn_api_data_list in alphabetical order
    fn_api_data_list.sort()
    return fn_api_data_list

def report_fn_api_data():
    result = []
    for work in work_list:
        result.append((work, get_fn_api_data_list(work)))
    return result

def merge_fn_api_data():
    fn_api_data_list = []
    for work in work_list:
        fn_api_data_list = list(set(fn_api_data_list + get_fn_api_data_list(work)))
    # sort the fn_api_data_list in alphabetical order
    fn_api_data_list.sort()
    return fn_api_data_list

# just using the netloc_dict, convert the netloc_dict into a database
# keys are go into the first colum, and values are going into the 2nd, 3rd, 4th columns
# indexs are the numbers
def netloc_dict_to_df():
    netloc_dict_df = pd.DataFrame.from_dict(netloc_dict, orient='index')
    netloc_dict_df = netloc_dict_df.reset_index()
    netloc_dict_df.columns = ['netloc', 'service', 'type', 'data']
    netloc_dict_df.index = np.arange(1, len(netloc_dict_df) + 1)
    # sort the dataframe according to the type name
    netloc_dict_df = netloc_dict_df.sort_values(by=['type'])
    # rearrange the index of the dataframe
    netloc_dict_df.index = np.arange(1, len(netloc_dict_df) + 1)
    return netloc_dict_df

# print the dataframe without lossing any information
# do not print None at the end of the dataframe
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

    
def main():
    print(netloc_dict_to_df())

if __name__ == "__main__":
    main()
