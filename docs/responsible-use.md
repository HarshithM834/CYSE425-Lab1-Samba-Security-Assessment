# Responsible use and publication policy

This project summarizes a controlled university laboratory activity. Only reproduce security tests in isolated environments you own or for which you have documented authorization.

For public GitHub publication:

1. Do not commit `passwd`, `shadow`, unshadowed hash files, recovered passwords, private keys, access tokens or reverse-shell binaries.
2. Review screenshots for credential output, private host addresses, names, IDs, and any other identifiable network metadata before publishing.
3. Keep targets and networks fictional or clearly documented as authorized test assets.
4. Do not publish classroom-provided VM images or third-party lab materials without permission.
5. Revert test users and configuration changes; describe limitations without asserting unverified cleanup.

This starter repo intentionally contains **no attack payloads or recovered authentication material**.
