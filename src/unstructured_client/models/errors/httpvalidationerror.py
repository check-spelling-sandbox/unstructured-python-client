"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional, Union
from unstructured_client.models.shared import validationerror as shared_validationerror
from unstructured_client.types import BaseModel
import unstructured_client.utils as utils

class HTTPValidationErrorData(BaseModel):
    detail: Optional[Detail] = None
    


class HTTPValidationError(Exception):
    data: HTTPValidationErrorData

    def __init__(self, data: HTTPValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, HTTPValidationErrorData)


DetailTypedDict = Union[List[shared_validationerror.ValidationErrorTypedDict], str]


Detail = Union[List[shared_validationerror.ValidationError], str]

