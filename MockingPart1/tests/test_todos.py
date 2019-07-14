# standard library imports
from unittest.mock import Mock, patch

# third-party tools
from nose.tools import assert_is_not_none

# Local imports
from MockingPart1.services import get_todos

@patch('MockingPart1.services.requests.get')
def test_getting_todos(mock_get):
    # configure the mock
    mock_get.return_value.ok = True

    # call the service
    response = get_todos()

    assert_is_not_none(response)

