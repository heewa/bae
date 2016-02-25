import unittest
from os import path
from subprocess import check_output


REPO = path.dirname(path.realpath(__file__))
VAR_FILE = path.join(REPO, 'emoji_vars.sh')
GENERATE_SCRIPT = path.join(REPO, 'generate.py')


class TestGeneratedFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_vars = set(
            line.strip() for line in open(VAR_FILE).readlines())
        cls.generated_vars = set(
            line.strip() for line in check_output(
                ['/usr/bin/env', 'python', GENERATE_SCRIPT]).splitlines())

    def test_missing(self):
        missing_from_file = self.generated_vars - self.file_vars
        assert not missing_from_file, 'Missing %d emoji from file: %s' % (
            len(missing_from_file), ', '.join(missing_from_file))

    def test_extra(self):
        extra_in_file = self.file_vars - self.generated_vars
        assert not extra_in_file, '%d extra emoji in file: %s' % (
            len(extra_in_file), ', '.join(extra_in_file))


if __name__ == "__main__":
    unittest.main()
