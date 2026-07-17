from datetime import datetime
from fastapi.responses import JSONResponse


def success_response(status_code: int, message: str, data, path: str):
    return JSONResponse(
        status_code=status_code,
        content={
            "statusCode": status_code,
            "message": message,
            "error": None,
            "data": data,
            "path": path,
            "timestamp": datetime.now().isoformat(),
        },
    )


def error_response(status_code: int, message: str, error_code: str, path: str):
    return JSONResponse(
        status_code=status_code,
        content={
            "statusCode": status_code,
            "message": message,
            "error": error_code,
            "data": None,
            "path": path,
            "timestamp": datetime.now().isoformat(),
        },
    )