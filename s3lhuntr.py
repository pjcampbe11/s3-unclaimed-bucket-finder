import argparse
import os
import re

# Simplified and adapted search patterns for regex matching in local files
SEARCH_PATTERNS = [
    r'amazonaws\.com/bucket',
    r'amazonaws\.com.*bucket.*s3://',
    r'S3_BUCKET',
    r's3\.amazonaws\.com',
    r'aws_s3_bucket',
    r'aws s3 cp',
    r'boto3.*s3://',
    r'AWS\.S3',
    r's3://',
    r's3\.amazonaws\.com',
    # The following are simplified to broadly match potential occurrences within files
    r'\.env',
    r'\.properties',
    r'\.tf',
    r'\.sh',
    r'\.py',
    r'\.js',
    r'\.json',
    r'\.yaml',
    r'\.txt',
    r'\.md',
    r'\.ini',
    r'\.conf',
    r'\.cfg',
    r'\.xml',
    r'\.gradle',
    r'\.rb',
    r'\.ps1',
    r'\.ts',
    r'\.cs',
    r'\.php',
    r'\.go',
    r'\.bat'
]

# Initialize parser
parser = argparse.ArgumentParser(description='Search for S3 bucket references in a downloaded GitHub repository.')
parser.add_argument('directory', type=str, help='Path to the local repository directory')
args = parser.parse_args()

def search_files(directory, pattern):
    """Recursively search through files in a directory for a given regex pattern."""
    findings = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    if re.search(pattern, f.read(), re.MULTILINE):
                        findings.append(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return findings

def main():
    findings = []

    for pattern in SEARCH_PATTERNS:
        print(f"Searching for pattern: {pattern}")
        matches = search_files(args.directory, pattern)
        findings.extend(matches)

    # Output findings
    for file_path in set(findings):  # Using set to remove potential duplicate paths
        print(f"Match found in: {file_path}")

if __name__ == '__main__':
    main()
