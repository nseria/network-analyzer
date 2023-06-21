from urllib import parse
import pandas as pd

# read text file and make it a list
def read_textfile(txt_file):
    txt_list = txt_file.readlines()
    i = 0

    for i in range(len(txt_list)):
        txt_list[i] = txt_list[i].split()
    
    return txt_list

# make url-only list
def parse_url(list):
    url_list = []
    i = 0

    for i in range(len(list)):
        url_list.append(parse.urlparse(list[i][2]))
    
    return url_list

# new list for netloc
def netloc_list(url_list):
    netloc_list = []
    i = 0

    for i in range(len(url_list)):
        netloc_list.append(url_list[i].netloc)
    
    return netloc_list

# new list for path
def path_list(url_list):
    path_list = []
    i = 0

    for i in range(len(url_list)):
        path_list.append(url_list[i].path)
    
    return path_list

def type_countlist(url_list):
    count_list = dict()
    for keyword in url_list:
        try: count_list[keyword] += 1
        except: count_list[keyword] = 1
    
    return count_list

# bundle of functions
# easy to categorize the url by netloc and path
def make_netloc_list(txt_file):
    # return value is "simple list"
    return netloc_list(parse_url(read_textfile(open(txt_file))))

def make_path_list(txt_file):
    # return value is "simple list"
    return path_list(parse_url(read_textfile(open(txt_file))))


# make dataframe of netloc and path
def http_parser(txt_file_name):
    txt_file = "./../txt_storage/" + txt_file_name + ".txt"

    df_netloc = pd.DataFrame(type_countlist(make_netloc_list(txt_file)).items(), columns=['netloc', 'count'])
    df_path = pd.DataFrame(type_countlist(make_path_list(txt_file)).items(), columns=['path', 'count'])

    df_netloc.to_csv('./../csv_storage/' + txt_file_name + '_netloc.csv', index=False)
    df_path.to_csv('./../csv_storage/' + txt_file_name + '_path.csv', index=False)

    print("----------------------------------------")
    print("Http parsing to get [netloc] and [path] for" + txt_file_name + " is done.")
    print("csv files are saved in ./../csv_storage/" + txt_file_name + "_netloc.csv and " + txt_file_name + "_path.csv")
    print("----------------------------------------")

def main():
    http_parser("login-email")
    http_parser("login-google")
    http_parser("login-apple")
    http_parser("login-status")
    http_parser("using_ai")
    http_parser("upload_pdf")
    http_parser("download_pdf")
    http_parser("export_pdf")
    http_parser("integration_googlemap")
    http_parser("integration_googledrive")
    http_parser("integration_onedrive")
    http_parser("integration_zoom")

main()
