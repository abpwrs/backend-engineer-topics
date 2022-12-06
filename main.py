import uvicorn
import os
from starlette.routing import Route
from starlette.requests import Request
from starlette.applications import Starlette
from starlette.responses import JSONResponse

import logging

# these are mocked to not actually interact w/ S3 for live interview purposes
from src.aws import s3, events

s3_bucket = os.environ["S3_BUCKET"]
s3_namespace = os.environ["S3_NAMESPACE"]

NEEDED_FILES = ["a", "b"]


def create_manifest(names: str):
    # This will save somewhere but for now
    return ["a", "b"]


def create_presigned_url(request: Request):
    name: str = request.path_params["name"]
    if name not in NEEDED_FILES:
        raise Exception("???")

    return JSONResponse(
        s3.generate_presigned_url("put_object", s3_bucket, s3_namespace + name, "PUT")
    )


def publishAllFilesUploadedEvent():
    pass  # What need to be here ????


def health(request: Request):
    return JSONResponse("OK")


routes = [
    Route("/healthz", health, methods=["GET"]),
    Route("/upload-url/{name:str}", create_presigned_url, methods=["GET"]),
]


def main():
    app = Starlette(debug=True, routes=routes)

    uvicorn.run(app, host="0.0.0.0", port=8010, log_level=logging.DEBUG)


if __name__ == "__main__":
    main()
