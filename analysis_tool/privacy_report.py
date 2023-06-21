import tag_collector
import sys

def print_cleanlist(list):
    converted_list = []
    converted_list = '    '.join(list)
    print(converted_list)

def main():
    sys.stdout = open('./../txt_storage/privacy_report.md', 'w')

    print("Privacy report")
    print("==============")
    print("This is a privacy report of your Notion usage.")
    print("Intercepted network traffic by Playwright for Python.")
    print("You can check the analysis by the actions you set.")
    print("## List of works")
    print("This is a list of works you have done.")
    print("")
    print_cleanlist(tag_collector.work_list)
    print("")

    print("## Number of Notion API used")
    print("> If you want look further, please check the Notion API lists for each work below.")
    print("")
    notion_api_report = tag_collector.report_notion_api()
    for work, notion_apis in notion_api_report:
        print("* " + work + ": " + str(len(notion_apis)))

    print("## List of Notion URLs (Domains)")
    print("This is a list of Notion URLs (Domains) that are detected during the Network interception.")
    print("> Each domains are related with specific functions. If you want look further, please check the database below.")
    print("")

    print("## aif.notion.so Notion domain")
    print("Several Notion domains are detected during the Network interception.")
    print("> If you want look further, please check the database below.")
    print("")
    print("One of them is aif.notion.so, which is related with the external trackers.")
    print("Here is the list of the trackers related with aif.notion.so.")
    print("")
    print_cleanlist(tag_collector.aif_notion_list)
    print("")

    print("## Trackers and External functional APIs (fn_api)")

    print("During the following tasks, the list of service companies that performed tracking and the number of tracking occurrences during each task, counted based on HTTP response and request, are as follows...")
    print("### List of detected company that use trackers")
    print_cleanlist(tag_collector.merge_tracker())
    print("### # of trackers")
    for work, counts in tag_collector.report_tracker_count():
        print("* " + work + ": " + str(counts))

    
    print("")
    print("There are various external functional APIs (fn_api) that are used by Notion.")
    print("These APIs are used for various purposes, such as analytics, big data, customer services, etc.")
    print("During the following tasks, the list of service companies that added functional APIs and the number of fn_api used during each task, counted based on HTTP response and request, are as follows...")
    print("### List of detected company that use fn_api")
    print_cleanlist(tag_collector.merge_fn_api())
    print("### How fn_apis are used")
    print_cleanlist(tag_collector.merge_fn_api_data())

    print("> For further information, please check the database below.")
    print("```")
    print(tag_collector.netloc_dict_to_df())
    print("```")

    print("## End of the report")
    print("This brief report is for reference purposes and may not be entirely accurate.")
    print("It is intended to provide a simple overview of the traffic flowing through Notion while using it on the web.")
    print("Thank you!!")

    sys.stdout.close()

main()
