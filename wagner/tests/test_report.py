import boto3
import os
import pytest

from moto import mock_s3

from wagner import main


def test_upper_string():
    assert main.upper_string("Sample Message") == "SAMPLE MESSAGE"


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture(scope="function")
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")


def test_create_bucket(s3):
    # s3 is a fixture defined above that yields a boto3 s3 client.
    s3.create_bucket(Bucket="test-bucket")

    result = s3.list_buckets()
    assert len(result["Buckets"]) == 1
    assert result["Buckets"][0]["Name"] == "test-bucket"
