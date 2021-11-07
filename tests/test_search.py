from brep import Search
import pytest

tests = [
    {
        "file": "tests/small.txt",
        "prefix": "key_1",
        "results": ['key_1   Lorem', 'key_1   Ipsum']
    },
    {
        "file": "tests/large.gz",
        "prefix": "77777",
        "results": [
            '7777720972104115   4576946181861782',
            '7777734576998869   2529253557699727'
        ]
    },
]


@pytest.mark.parametrize("test", tests)
def test_search(test):
    results = list(Search(test.get('prefix'), test.get('file')))
    if not all(result in results for result in test.get('results')):
        raise Exception(f"Failed test {test.get('file')}")
