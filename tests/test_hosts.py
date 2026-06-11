import pytest
from ows_gde_mcp.hosts import host_of


@pytest.mark.parametrize("url,expected", [
    ("https://1057-sg.teleows.com", "1057-sg.teleows.com"),
    ("https://1057-sg-studio.teleows.com/", "1057-sg-studio.teleows.com"),
    ("https://1057-sg.teleows.com:443/path?q=1", "1057-sg.teleows.com:443"),
    ("https://A.Example.COM/x", "a.example.com"),
])
def test_host_of(url, expected):
    assert host_of(url) == expected


def test_host_of_rejects_relative():
    with pytest.raises(ValueError):
        host_of("/portal/web/rest")
