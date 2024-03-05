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

Searching for: amazonaws.com bucket
Searching for: "amazonaws.com" + "bucket" extension:json "s3://"
Searching for: "amazonaws.com" + "bucket" extension:yaml "s3://"
Searching for: extension:env "S3_BUCKET"
Searching for: extension:properties "s3.amazonaws.com"
Searching for: extension:tf "aws_s3_bucket"
Searching for: extension:sh "aws s3 cp"
Searching for: extension:py "boto3" "s3://"
Searching for: extension:js "AWS.S3"
Searching for: extension:json "s3://"
Error searching GitHub: 403
Searching for: extension:yaml "s3://"
Error searching GitHub: 403
Searching for: extension:txt "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:md "s3://"
Error searching GitHub: 403
Searching for: extension:ini "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:conf "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:cfg "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:xml "S3Bucket"
Error searching GitHub: 403
Searching for: extension:gradle "s3://"
Error searching GitHub: 403
Searching for: extension:rb "AWS::S3"
Error searching GitHub: 403
Searching for: extension:ps1 "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:ts "AWS.S3"
Error searching GitHub: 403
Searching for: extension:cs "Amazon.S3"
Error searching GitHub: 403
Searching for: extension:php "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:go "s3.amazonaws.com"
Error searching GitHub: 403
Searching for: extension:bat "aws s3 sync"
Error searching GitHub: 403
Repository: mlflow/mlflow
File Path: docs/source/tracking/artifacts-stores.rst
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/docs/source/tracking/artifacts-stores.rst

Repository: mlflow/mlflow
File Path: mlflow/sagemaker/__init__.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/mlflow/sagemaker/__init__.py

Repository: mlflow/mlflow
File Path: docs/source/tracking/tutorials/remote-server.rst
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/docs/source/tracking/tutorials/remote-server.rst

Repository: mlflow/mlflow
File Path: examples/llms/RAG/question_answer_source.csv
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/examples/llms/RAG/question_answer_source.csv

Repository: mlflow/mlflow
File Path: tests/store/artifact/test_gcs_artifact_repo.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/store/artifact/test_gcs_artifact_repo.py

Repository: mlflow/mlflow
File Path: tests/sagemaker/mock/test_sagemaker_service_mock.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/sagemaker/mock/test_sagemaker_service_mock.py

Repository: mlflow/mlflow
File Path: mlflow/sagemaker/__init__.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/mlflow/sagemaker/__init__.py

Repository: mlflow/mlflow
File Path: tests/sagemaker/test_batch_deployment.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/sagemaker/test_batch_deployment.py

Repository: mlflow/mlflow
File Path: tests/store/artifact/test_optimized_s3_artifact_repo.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/store/artifact/test_optimized_s3_artifact_repo.py

Repository: mlflow/mlflow
File Path: examples/sktime/test_sktime_model_export.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/examples/sktime/test_sktime_model_export.py

Repository: mlflow/mlflow
File Path: tests/store/_unity_catalog/model_registry/test_unity_catalog_rest_store.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/store/_unity_catalog/model_registry/test_unity_catalog_rest_store.py

Repository: mlflow/mlflow
File Path: tests/sagemaker/mock/test_sagemaker_service_mock.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/sagemaker/mock/test_sagemaker_service_mock.py

Repository: mlflow/mlflow
File Path: tests/store/artifact/test_s3_artifact_repo.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/store/artifact/test_s3_artifact_repo.py

Repository: mlflow/mlflow
File Path: tests/sagemaker/test_sagemaker_deployment_client.py
File URL: https://github.com/mlflow/mlflow/blob/75698e51af85719dcba4060a1f901b2f2ea984f3/tests/sagemaker/test_sagemaker_deployment_client.py

So what can you do if you find unclaimed S3 buckets?

https://huntr.com/bounties/6a69952f-a1ba-4dee-9d8c-e87f52508b58/
