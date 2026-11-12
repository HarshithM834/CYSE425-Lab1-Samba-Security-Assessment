# Defensive lessons & remediation

These are recommended controls derived from the risks illustrated by the class exercise. They were **not verified as applied** to the lab target.

## Samba hardening

- Identify installed Samba versions and applicable vendor security updates; patch affected deployments.
- Restrict SMB service access to explicitly authorized internal networks and hosts.
- Disable unneeded services and shares, and limit write access to Samba-exposed locations.
- Avoid running network-facing services with unnecessary privileges.

## Privileged access and SSH

- Prefer SSH key-based authentication and disable password-based login where operationally feasible.
- Do not permit direct root SSH login unless a tightly controlled exception is required.
- Remove temporary privileged users after testing, review sudo rules, and monitor authorization logs.
- Validate effective SSH daemon settings with system-native tools; static file inspection alone is insufficient.

## Credential protection

- Keep `shadow` and other sensitive authentication artifacts restricted to the smallest possible set of privileged processes and administrators.
- Use strong, unique credentials, modern password hashing, and a documented rotation procedure.
- Treat disclosure of credential hashes as a security incident requiring investigation, even if plaintext passwords are not immediately known.

## Detection and recovery

- Monitor unexpected service child processes, privileged sessions, network egress, new accounts, and SSH configuration changes.
- After an authorized exercise, compare configuration to its known-good baseline and review logs for leftover artifacts.
- Confirm remediation with fresh testing under a separate, approved scope.
