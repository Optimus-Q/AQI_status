from streamlit.testing.v1 import AppTest
import pytest
from pathlib import Path
from app.app import add

def test_appui():
    app_path = Path(__file__).parents[1] / "app" / "app.py"
    print(app_path)
    app_ = AppTest.from_file(app_path).run()
    app_.number_input(key="First element").set_value(2).run()
    app_.number_input(key="Second element").set_value(2).run()
    app_.button(key="Add button").click().run()
    assert app_.markdown[0].value == "The result is: 4"

@pytest.fixture()
def numbers():
    return (10, 20)

def test_add(numbers):
    a, b = numbers
    result = add(a, b)
    assert result == 30