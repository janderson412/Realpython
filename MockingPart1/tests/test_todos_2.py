from unittest.mock import patch
from nose.tools import assert_is_not_none
from MockingPart1.services import get_todos

def test_getting_todos():
    with patch('MockingPart1.services.requests.get') as mock_get:
        mock_get.return_value.ok = True

        response = get_todos()

    assert_is_not_none(response)