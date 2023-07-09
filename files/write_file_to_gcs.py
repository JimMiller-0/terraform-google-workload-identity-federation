import io
import os

from google.cloud import storage

def write_file_to_gcs(bucket_name, file_name, file_content):
    """Writes a file to Google Cloud Storage.

    Args:
        bucket_name (str): The name of the bucket.
        file_name (str): The name of the file.
        file_content (str): The content of the file.

    Returns:
        None.
    """

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    file_object = io.BytesIO(file_content.encode('utf-8'))
    blob = bucket.blob(file_name)
    blob.upload_from_file(file_object)

    print(f'File {file_name} successfully written to Google Cloud Storage.')

if __name__ == '__main__':
    bucket_name = 'my-bucket'
    file_name = 'my-file.txt'
    file_content = 'This is the content of my file.'

    write_file_to_gcs(bucket_name, file_name, file_content)
