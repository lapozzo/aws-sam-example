import json
import pytest
#importing layer
import sys
sys.path.append('../calculation-layer/calculation_services/python/')
import calculation
from sum import app

@pytest.fixture()
def event():
    """ Generates Sum Event"""

    return {
        "n1": "2",
        "n2": "1"
    }

@pytest.fixture()
def event_error():
    """ Generates Sum Error Event"""

    return {
    }



def test_lambda_handler(event, mocker):

    ret = app.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "sum result:3"

def test_lambda_handler(event_error, mocker):

    ret = app.lambda_handler(event_error, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 400
    assert "message" in ret["body"]
    assert data["message"] == "invalid numbers n1 and n2"
