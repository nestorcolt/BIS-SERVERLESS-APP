import gzip
import pathlib
import tarfile
import zipfile
from zipfile import ZipFile

import boto3
import io

##############################################################################################

codecommit = boto3.client('codecommit')
repository_name = "FlexSearchEngine"
response = codecommit.get_repository(repositoryName=repository_name)
branch = codecommit.get_branch(branchName="master", repositoryName=repository_name)
repo_url = response['repositoryMetadata']['cloneUrlHttp']


##############################################################################################


def get_differences(repository_name, branch="master"):
    response = codecommit.get_differences(
        repositoryName=repository_name,
        afterCommitSpecifier=branch,
    )
    differences = []
    while "nextToken" in response:
        response = codecommit.get_differences(
            repositoryName=repository_name,
            afterCommitSpecifier=branch,
            nextToken=response["nextToken"]
        )
        differences += response.get("differences", [])
    else:
        differences += response["differences"]
    return differences


##############################################################################################
#
# c_path = r"C:\Users\Sudo\Desktop\test\myfile.tar"
# repository_path = pathlib.Path(repository_name)
# buf = io.BytesIO()
# that = None
#
# with tarfile.open(mode="w:gz", fileobj=buf) as tar:
#     for difference in get_differences(repository_name):
#         blobid = difference["afterBlob"]["blobId"]
#         path = difference["afterBlob"]["path"]
#         mode = difference["afterBlob"]["mode"]  # noqa
#         blob = codecommit.get_blob(repositoryName=repository_name, blobId=blobid)
#         that = io.BytesIO(blob["content"])
#         tarinfo = tarfile.TarInfo()
#         tarinfo.size = len(blob["content"])
#         tar.addfile(tarinfo, that)
#
# tarobject = buf.getvalue()
#


c_path = r"C:\Users\Sudo\Desktop\test\myfile.ext"
repository_path = pathlib.Path(repository_name)
that = None

for difference in get_differences(repository_name):
    print(difference)
    blobid = difference["afterBlob"]["blobId"]
    path = difference["afterBlob"]["path"]
    mode = difference["afterBlob"]["mode"]  # noqa
    blob = codecommit.get_blob(repositoryName=repository_name, blobId=blobid)
    that = io.BytesIO(blob["content"])

##############################################################################################


# save to s3
# s3 = boto3.client('s3')
# s3.filename = str(repository_name)
# s3.bucket = 'bis-se-s3'
# response = s3.put_object(Body=that, Bucket=s3.bucket, Key="repo_001")
#
# s3.upload_fileobj(
#     Fileobj=gzip.GzipFile(None, 'rb',
#                           fileobj=io.BytesIO(s3.get_object(Bucket=s3.bucket, Key="my_repo")['Body'].read())),
#     Bucket=s3.bucket,
#     Key="my_repo")
