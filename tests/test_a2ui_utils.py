"""Unit tests for A2UI Utils callback and message extractor."""

import os
import sys
import json
import pytest

sys.path.insert(0, os.path.abspath("projects/agent-frontend-chat-ui"))
from a2ui_utils import (
    _extract_a2ui_messages,
    _sanitize_image_components,
    _surface_is_renderable,
    _iter_json_values,
    a2ui_callback
)


def test_extract_a2ui_messages_plain():
    raw = json.dumps({"beginRendering": {"root": "card1"}, "surfaceUpdate": {"components": []}})
    messages = _extract_a2ui_messages(raw)
    assert len(messages) == 1
    assert "beginRendering" in messages[0]


def test_extract_a2ui_messages_wrapped_envelope():
    envelope = {
        "kind": "data",
        "data": {
            "beginRendering": {"root": "main"},
            "surfaceUpdate": {"components": [{"id": "main", "component": {"Text": {"text": {"literalString": "Hello"}}}}]}
        }
    }
    raw = f"<a2a_datapart_json>{json.dumps(envelope)}</a2a_datapart_json>"
    messages = _extract_a2ui_messages(raw)
    assert len(messages) == 1
    assert messages[0]["beginRendering"]["root"] == "main"


def test_sanitize_image_components_non_http():
    messages = [{
        "surfaceUpdate": {
            "components": [
                {
                    "id": "img1",
                    "component": {
                        "Image": {
                            "url": {"literalString": "local_image.png"}
                        }
                    }
                }
            ]
        }
    }]
    _sanitize_image_components(messages)
    comp = messages[0]["surfaceUpdate"]["components"][0]["component"]
    assert "Text" in comp
    assert "Image generated" in comp["Text"]["text"]["literalString"]


def test_surface_is_renderable_valid():
    comp = {"id": "c1", "component": {"Text": {"text": {"literalString": "Test"}}}}
    messages = [
        {"beginRendering": {"root": "c1"}},
        {"surfaceUpdate": {"components": [comp]}}
    ]
    assert _surface_is_renderable(messages) is True


def test_surface_is_renderable_invalid_root():
    comp = {"id": "c1", "component": {"Text": {"text": {"literalString": "Test"}}}}
    messages = [
        {"beginRendering": {"root": "missing_id"}},
        {"surfaceUpdate": {"components": [comp]}}
    ]
    assert _surface_is_renderable(messages) is False
