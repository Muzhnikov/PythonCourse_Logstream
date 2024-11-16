from maw import merge_and_write
import pytest

@pytest.fixture(autouse=True)
def my_fixture(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file2_path = tmp_path / "file2.txt"
    output_file_path = tmp_path / "output.txt"

    with open(file1_path, 'w') as file1:
        file1.write("Hello")
    with open(file2_path, 'w') as file2:
        file2.write("world")

    return file1_path, file2_path, output_file_path

def test_merge_and_write_good(my_fixture):
    file1, file2, output_file = my_fixture
    result = merge_and_write(file1, file2, output_file)
    assert result == "Hello world"

def test_merge_and_write_edited_files(my_fixture):
    file1, file2, output_file = my_fixture
    with open(file1, 'w') as f:
        f.write("")
    result = merge_and_write(file1, file2, output_file)
    assert result == " world"

def test_merge_and_write_not_found(my_fixture):
    file1, file2, output_file = my_fixture
    result = merge_and_write("unreal_file.txt", file2, output_file)
    assert result == "Один из файлов не найден"
