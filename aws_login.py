import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from colorama import Fore, Style, init

init(autoreset=True)

aws_session = None
aws_region = None

def login_to_aws():
    global aws_session, aws_region
    try:
        aws_access_key_id = input(Fore.YELLOW + "Enter AWS Access Key ID: ")
        aws_secret_access_key = input(Fore.YELLOW + "Enter AWS Secret Access Key: ")
        aws_region = input(Fore.YELLOW + "Enter AWS Region: ")

        aws_session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

        aws_session.client('sts').get_caller_identity()
        print(Fore.GREEN + "Login successful!")
        return aws_session, aws_region
    except (NoCredentialsError, PartialCredentialsError):
        print(Fore.RED + "Login failed! Check your credentials and try again.")
        return None, None

def is_logged_in():
    return aws_session is not None

