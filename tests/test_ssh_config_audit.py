import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from ssh_config_audit import audit_config


class SSHConfigAuditTests(unittest.TestCase):
    def test_detects_risky_directives_case_insensitively(self):
        result = audit_config("passwordauthentication YES\nPermitRootLogin yes\n")
        self.assertEqual([n for n, _ in result], [1, 2])

    def test_ignores_comments_and_safe_values(self):
        self.assertEqual(audit_config("# PasswordAuthentication yes\nPasswordAuthentication no\nPermitRootLogin no\n"), [])

    def test_detects_empty_passwords(self):
        self.assertIn("PermitEmptyPasswords yes", audit_config("PermitEmptyPasswords yes")[0][1])

    def test_tracks_line_numbers(self):
        self.assertEqual(audit_config("\n# comment\nPermitRootLogin yes")[0][0], 3)


if __name__ == "__main__":
    unittest.main()
