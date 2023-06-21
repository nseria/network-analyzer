# Network analyzer for Notion

This is a simple code for gathering network traffics from the actions done in using Notion service.

# Before start

Make three folders:
./txt_storage
./pdf_storage
./csv_storage

# Tools for analysis

Analysis is done in three steps:

1. Analyze request and response data and sort them → http_parser.py
2. Collect tags and categorize them according to the attributes → tag_collector.py
3. Make a privacy report of your actions done in Notion →privacy_report

You can check **how** Notion collects your data and **what** data Notion collects through this simple test.

### http_parser.py

Parse the HTTP request and response data. Extract netloc and path data.

### tag_collector.py

Analysis of the parsed data and organize it.

You can check how I contruct the codes just by reading the simple python codes.

### privacy_report.py

Generate a simple report in markdown style.

# Example report

demo_privacy_report.md is the example report for my case.

# How to use

Check the individual .py analyzer file.

I wrote everything inside codes so that everyone can use easily.
