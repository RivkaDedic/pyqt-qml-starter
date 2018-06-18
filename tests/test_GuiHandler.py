import pytest
from __main__ import GuiHandler

@pytest.fixture()
def gui_handler():
    yield GuiHandler()

def test_GuiHandler_instance(gui_handler):
    assert type(gui_handler) == GuiHandler