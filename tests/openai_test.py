import pytest
from model.timeline import Timeline
from integrations.openai import send_to_chatgpt


@pytest.mark.skip(reason="Disabled because of free account rate limiting")
def test_openai():
    timeline = Timeline(title="Ketamine can rapidly reduce symptoms of PTSD and depression, new study finds", text="")
    message = send_to_chatgpt(timeline)
    assert len(message) > 0
