mock_s3: set[str] = set()


def generate_presigned_url(
    s3_action: str, bucket_name: str, key_name: str, http_method: str
):
    # this is made up, but similar to the real presigned url generation function
    presigned_url = f"http://aws.region.s3.{s3_action}/{bucket_name}/{key_name}?some_token=abc?allowed_method={http_method}"

    # what does this mock assume?
    # is it okay to assume this?
    mock_s3.add(f"s3://{bucket_name}/{key_name}")

    return presigned_url


def file_exists(bucket_name: str, key_name: str) -> bool:
    return f"s3://{bucket_name}/{key_name}" in mock_s3
