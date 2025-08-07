from calculator import add
import pytest

def test_add_two_numbers():
   assert add(2, 3) == 5
   with pytest.raises(TypeError):
      add(2, "3")