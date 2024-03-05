import argparse
import requests
import json
import re

# GitHub API settings
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
API_URL_TEMPLATE = 'https://api.github.com/search/code?q={query}+repo:{repository}'

# Enhanced Search Queries
SEARCH_QUERIES = [
    'amazonaws.com bucket',
    '"amazonaws.com" + "bucket" extension:json "s3://"',
    '"amazonaws.com" + "bucket" extension:yaml "s3://"',
    'extension:env "S3_BUCKET"',
    'extension:properties "s3.amazonaws.com"',
    'extension:tf "aws_s3_bucket"',
    'extension:sh "aws s3 cp"',
    'extension:py "boto3" "s3://"',
    'extension:js "AWS.S3"',
    'extension:json "s3://"',
    'extension:yaml "s3://"',
    'extension:txt "s3.amazonaws.com"',
    'extension:md "s3://"',
    'extension:ini "s3.amazonaws.com"',
    'extension:conf "s3.amazonaws.com"',
    'extension:cfg "s3.amazonaws.com"',
    'extension:xml "S3Bucket"',
    'extension:gradle "s3://"',
    'extension:rb "AWS::S3"',
    'extension:ps1 "s3.amazonaws.com"',
    'extension:ts "AWS.S3"',
    'extension:cs "Amazon.S3"',
    'extension:php "s3.amazonaws.com"',
    'extension:go "s3.amazonaws.com"',
    'extension:bat "aws s3 sync"',
]

# Initialize parser
parser = argparse.ArgumentParser(description='Search for S3 bucket references in a GitHub repository.')
parser.add_argument('repository', type=str, help='Name of the GitHub repository (format: user/repo)')
args = parser.parse_args()

# Headers for GitHub API authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def search_repository(repository, query):
    """Search the repository for a query and return the results."""
    url = API_URL_TEMPLATE.format(query=query.replace(' ', '+'), repository=repository)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error searching GitHub: {response.status_code}")
        return []

def main():
    findings = []

    for query in SEARCH_QUERIES:
        print(f"Searching for: {query}")
        items = search_repository(args.repository, query)
        findings.extend(items)

    # Simple output of findings to console. Modify as needed for file output.
    for item in findings:
        print(f"Repository: {item['repository']['full_name']}")
        print(f"File Path: {item['path']}")
        print(f"File URL: {item['html_url']}\n")

if __name__ == '__main__':
    main()
