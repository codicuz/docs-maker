import pytest
import docs_maker

class TestDocsMaker():
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        monkeypatch.setattr("sys.exit", lambda x: None)

    def test_version(self, capsys, monkeypatch):
        monkeypatch.setattr('sys.argv', ['docs-maker', '--version'])
        want = 'docs-maker Версия develop\n'
        docs_maker.cli()
        captured = capsys.readouterr()

        assert captured.out == want