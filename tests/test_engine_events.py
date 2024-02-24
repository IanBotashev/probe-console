import pytest
from engine.event import Event
from unittest.mock import Mock


@pytest.fixture
def event():
    """Fixture to provide an Event instance for each test."""
    return Event()


def test_event_trigger(event):
    """Tests if subscribers are properly ran when the event is triggered."""
    mock_subscriber = Mock()
    event.subscribe(mock_subscriber)

    event.trigger('data', key="value")

    mock_subscriber.assert_called_with('data', key="value")
