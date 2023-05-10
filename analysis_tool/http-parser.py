from urllib import parse
import pandas as pd

# set text file that you want to work
txt_file = input("Enter the text file name: ") + '.txt'

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
# more options will be added soon
df_netloc = pd.DataFrame(type_countlist(make_netloc_list(txt_file)).items(), columns=['netloc', 'count'])
df_path = pd.DataFrame(type_countlist(make_path_list(txt_file)).items(), columns=['path', 'count'])
print(df_netloc)
print(df_path)

df_netloc.to_csv(txt_file + '_netloc.csv', index=False)
df_path.to_csv(txt_file + '_path.csv', index=False)

