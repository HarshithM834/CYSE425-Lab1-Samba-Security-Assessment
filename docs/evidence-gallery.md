# Lab 1 evidence gallery

**26 redacted screenshots** from the original CYSE 425 Lab 1 report, in chronological order.

> **Publication policy:** test passwords, account-hash output and sensitive account records have been masked where present. Screenshots are evidence from the authorized educational lab, not proof of independent reproduction.

## Discovery and initial compromise

The assessment identifies the CVE-2017-7494 module, configures the authorized Samba target, and verifies a command shell and root privileges.

### 01. CVE-2017-7494 research and Kali lab environment

![01 - CVE-2017-7494 research and Kali lab environment](../assets/evidence/01.webp)

*Evidence 01: CVE-2017-7494 research and Kali lab environment.*

### 02. Metasploit database initialization and console launch

![02 - Metasploit database initialization and console launch](../assets/evidence/02.webp)

*Evidence 02: Metasploit database initialization and console launch.*

### 03. Identification of the Samba is_known_pipename module

![03 - Identification of the Samba is_known_pipename module](../assets/evidence/03.webp)

*Evidence 03: Identification of the Samba is_known_pipename module.*

### 04. Exploit configuration for the authorized lab target

![04 - Exploit configuration for the authorized lab target](../assets/evidence/04.webp)

*Evidence 04: Exploit configuration for the authorized lab target.*

### 05. Command-shell session established

![05 - Command-shell session established](../assets/evidence/05.webp)

*Evidence 05: Command-shell session established.*

### 06. Root identity verified from the shell

![06 - Root identity verified from the shell](../assets/evidence/06.webp)

*Evidence 06: Root identity verified from the shell.*

## SSH exposure analysis

The target's SSH settings are inspected to understand how authentication policy affects post-compromise risk.

### 07. Inspection of SSH server configuration

![07 - Inspection of SSH server configuration](../assets/evidence/07.webp)

*Evidence 07: Inspection of SSH server configuration.*

### 08. Password-authentication configuration review

![08 - Password-authentication configuration review](../assets/evidence/08.webp)

*Evidence 08: Password-authentication configuration review.*

### 09. SSH daemon directive inspection

![09 - SSH daemon directive inspection](../assets/evidence/09.webp)

*Evidence 09: SSH daemon directive inspection.*

### 10. Review of SSH service options and included configuration

![10 - Review of SSH service options and included configuration](../assets/evidence/10.webp)

*Evidence 10: Review of SSH service options and included configuration.*

## Controlled SSH access changes

A temporary SSH configuration change, test-account creation and remote-access checks illustrate the impact of privileged access in the isolated lab.

### 11. Preparing a lab-only SSH configuration override

![11 - Preparing a lab-only SSH configuration override](../assets/evidence/11.webp)

*Evidence 11: Preparing a lab-only SSH configuration override.*

### 12. Temporary HTTP server for configuration transfer

![12 - Temporary HTTP server for configuration transfer](../assets/evidence/12.webp)

*Evidence 12: Temporary HTTP server for configuration transfer.*

### 13. Applying lab SSH configuration and restarting SSH

![13 - Applying lab SSH configuration and restarting SSH](../assets/evidence/13.webp)

*Evidence 13: Applying lab SSH configuration and restarting SSH.*

### 14. Temporary lab account creation and privilege assignment

![14 - Temporary lab account creation and privilege assignment](../assets/evidence/14.webp)

*Evidence 14: Temporary lab account creation and privilege assignment.*

### 15. Successful SSH authentication for the test account

![15 - Successful SSH authentication for the test account](../assets/evidence/15.webp)

*Evidence 15: Successful SSH authentication for the test account.*

### 16. Sudo privilege testing through the SSH session

![16 - Sudo privilege testing through the SSH session](../assets/evidence/16.webp)

*Evidence 16: Sudo privilege testing through the SSH session.*

## Account-file exposure

Controlled transfers of test account files demonstrate why privileged access to password databases creates offline attack risk.

### 17. Authorized copies of account data

![17 - Authorized copies of account data](../assets/evidence/17.webp)

*Evidence 17: Authorized copies of account data.*

### 18. Controlled transfer of account files to Kali

![18 - Controlled transfer of account files to Kali](../assets/evidence/18.webp)

*Evidence 18: Controlled transfer of account files to Kali.*

### 19. Preparation of combined test password hashes

![19 - Preparation of combined test password hashes](../assets/evidence/19.webp)

*Evidence 19: Preparation of combined test password hashes.*

## Password recovery and access impact

John the Ripper identifies weak test credentials; selected recovery output is redacted, while the resulting SSH access and privilege checks are documented.

### 20. John the Ripper password-strength assessment

![20 - John the Ripper password-strength assessment](../assets/evidence/20.webp)

*Evidence 20: John the Ripper password-strength assessment.*

### 21. Verified password recovery results with sensitive values redacted

![21 - Verified password recovery results with sensitive values redacted](../assets/evidence/21.webp)

*Evidence 21: Verified password recovery results with sensitive values redacted.*

### 22. Recovered test-account SSH login

![22 - Recovered test-account SSH login](../assets/evidence/22.webp)

*Evidence 22: Recovered test-account SSH login.*

### 23. Recovered account privilege and identity validation

![23 - Recovered account privilege and identity validation](../assets/evidence/23.webp)

*Evidence 23: Recovered account privilege and identity validation.*

### 24. Follow-up SSH and administrative test

![24 - Follow-up SSH and administrative test](../assets/evidence/24.webp)

*Evidence 24: Follow-up SSH and administrative test.*

## Remote-shell validation and cleanup

A controlled reverse shell is demonstrated and temporary lab changes are removed.

### 25. Controlled Netcat reverse-shell validation

![25 - Controlled Netcat reverse-shell validation](../assets/evidence/25.webp)

*Evidence 25: Controlled Netcat reverse-shell validation.*

### 26. Post-test cleanup and restoration

![26 - Post-test cleanup and restoration](../assets/evidence/26.webp)

*Evidence 26: Post-test cleanup and restoration.*

---

**Source:** *CYSE 425 - Lab 1* (16-page course report). Screenshots were reorganized and redacted for portfolio publication. No standalone authentication artifacts, recovered plaintext passwords or hashes are included.
