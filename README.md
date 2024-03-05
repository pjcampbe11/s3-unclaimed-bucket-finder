# s3-unclaimed-bucket-finder

Example of how to use this script to target https://github.com/mlflow/mlflow

To run the s3huntr.py script targeting the mlflow/mlflow repository on GitHub, you would execute the script from your command line, passing the repository's name in the format user/repo as an argument. Here's how you would do it:


python s3huntr.py mlflow/mlflow

Make sure to replace python with python3 or the specific version of Python you're using if necessary (e.g., python3.11 as mentioned in your requirements), especially if you have multiple Python versions installed on your system.

Before running the script, ensure the following:

GitHub Token: Your script contains a placeholder for a GitHub token (GITHUB_TOKEN = 'your_github_access_token_here'). You need to replace 'your_github_access_token_here' with your actual GitHub Personal Access Token to authenticate your requests to the GitHub API.

Python Environment: Verify that Python 3.11 is installed and accessible from your command line. You can check your Python version by running python --version or python3 --version in your terminal.

Dependencies: If the script uses any external libraries (like requests), ensure they are installed in your Python environment. For this script, you might need to run pip install requests if you haven't already.

Script Location: Run the command from the directory where s3huntr.py is located, or provide the full path to the script in the command.

This example command line will initiate the script to search through the mlflow/mlflow repository for potential references to S3 buckets as specified by the search queries integrated into the script. The results will be printed to the console based on the current script configuration.

Example:

python3.11 s3huntr.py mlflow/mlflow

So what can you do if you find unclaimed S3 buckets?

https://huntr.com/bounties/6a69952f-a1ba-4dee-9d8c-e87f52508b58/
