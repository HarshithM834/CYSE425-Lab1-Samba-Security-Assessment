# CYSE 425 — Lab 1: Samba Security Assessment: CVE-2017-7494

![Security](https://img.shields.io/badge/domain-offensive%20security-202b3b) ![Environment](https://img.shields.io/badge/environment-authorized%20lab-20835c)

An authorized penetration-testing lab documenting the exploitation of a vulnerable **Samba service (CVE-2017-7494)**, validation of root-level access, SSH authentication changes, controlled account-file transfer, password recovery testing, and post-assessment cleanup using Kali Linux.

**Tools:** Metasploit Framework · Kali Linux · SSH · Netcat · John the Ripper  
**Lab report:** [View the 16-page redacted PDF](docs/CYSE425_Lab1_Report_Redacted.pdf)

## At a glance

| Item | Details |
|---|---|
| Assessment focus | Samba vulnerability **CVE-2017-7494**, post-exploitation exposure, credential hygiene |
| Environment | Kali Linux and a deliberately vulnerable Linux/Samba lab target |
| Tools used in the documented exercise | Metasploit Framework, SSH, Netcat, John the Ripper |
| Outcome documented | A command shell and root privileges; authorized SSH access testing; test-account password recovery; cleanup |

## Assessment Workflow

![Samba vulnerability assessment workflow](assets/assessment-flow.svg)

## Evidence Screenshots

All **26 screenshots** from the authorized Lab 1 report are shown below, in chronological order. Sensitive password and account-data regions are redacted.

### Discovery and initial compromise

**01. CVE-2017-7494 research and Kali lab environment**

![01 — CVE-2017-7494 research and Kali lab environment](assets/evidence/01.webp)

**02. Metasploit database initialization and console launch**

![02 — Metasploit database initialization and console launch](assets/evidence/02.webp)

**03. Identification of the Samba is_known_pipename module**

![03 — Identification of the Samba is_known_pipename module](assets/evidence/03.webp)

**04. Exploit configuration for the authorized lab target**

![04 — Exploit configuration for the authorized lab target](assets/evidence/04.webp)

**05. Command-shell session established**

![05 — Command-shell session established](assets/evidence/05.webp)

**06. Root identity verified from the shell**

![06 — Root identity verified from the shell](assets/evidence/06.webp)

### SSH exposure analysis

**07. Inspection of SSH server configuration**

![07 — Inspection of SSH server configuration](assets/evidence/07.webp)

**08. Password-authentication configuration review**

![08 — Password-authentication configuration review](assets/evidence/08.webp)

**09. SSH daemon directive inspection**

![09 — SSH daemon directive inspection](assets/evidence/09.webp)

**10. Review of SSH service options and included configuration**

![10 — Review of SSH service options and included configuration](assets/evidence/10.webp)

### Controlled SSH access changes

**11. Preparing a lab-only SSH configuration override**

![11 — Preparing a lab-only SSH configuration override](assets/evidence/11.webp)

**12. Temporary HTTP server for configuration transfer**

![12 — Temporary HTTP server for configuration transfer](assets/evidence/12.webp)

**13. Applying lab SSH configuration and restarting SSH**

![13 — Applying lab SSH configuration and restarting SSH](assets/evidence/13.webp)

**14. Temporary lab account creation and privilege assignment**

![14 — Temporary lab account creation and privilege assignment](assets/evidence/14.webp)

**15. Successful SSH authentication for the test account**

![15 — Successful SSH authentication for the test account](assets/evidence/15.webp)

**16. Sudo privilege testing through the SSH session**

![16 — Sudo privilege testing through the SSH session](assets/evidence/16.webp)

### Account-file exposure

**17. Authorized copies of account data**

![17 — Authorized copies of account data](assets/evidence/17.webp)

**18. Controlled transfer of account files to Kali**

![18 — Controlled transfer of account files to Kali](assets/evidence/18.webp)

**19. Preparation of combined test password hashes**

![19 — Preparation of combined test password hashes](assets/evidence/19.webp)

### Password recovery and access impact

**20. John the Ripper password-strength assessment**

![20 — John the Ripper password-strength assessment](assets/evidence/20.webp)

**21. Verified password recovery results with sensitive values redacted**

![21 — Verified password recovery results with sensitive values redacted](assets/evidence/21.webp)

**22. Recovered test-account SSH login**

![22 — Recovered test-account SSH login](assets/evidence/22.webp)

**23. Recovered account privilege and identity validation**

![23 — Recovered account privilege and identity validation](assets/evidence/23.webp)

**24. Follow-up SSH and administrative test**

![24 — Follow-up SSH and administrative test](assets/evidence/24.webp)

### Remote-shell validation and cleanup

**25. Controlled Netcat reverse-shell validation**

![25 — Controlled Netcat reverse-shell validation](assets/evidence/25.webp)

**26. Post-test cleanup and restoration**

![26 — Post-test cleanup and restoration](assets/evidence/26.webp)

## Findings and evidence

| Finding | Evidence from lab write-up | Security impact | Recommended control |
|---|---|---|---|
| Vulnerable Samba service | A Metasploit module associated with **CVE-2017-7494** was selected and used against the authorized target | Remote code execution on a vulnerable, reachable server | Upgrade to a patched Samba release; limit SMB reachability |
| Privilege exposure | The resulting session was verified with `whoami` as root | Compromise of privileged operations and local data | Reduce service privileges and isolate vulnerable services |
| SSH configuration risk | Password authentication was temporarily enabled during testing | Broader password-based access surface | Restore hardened SSH settings and prefer key authentication |
| Account-file exposure | Lab copies of `passwd` and `shadow` were transferred to Kali for testing | Offline password-guessing risk if privileged files are exposed | Restrict privileged file access, use strong unique passwords and strong hashing |
| Weak test passwords | John the Ripper recovered test-account credentials | Weak credentials can magnify a host compromise | Strengthen password policy and rotate affected credentials |
| Remote access validation | A controlled reverse-shell connection was demonstrated | Evidence of ability to operate remotely from compromised host | Outbound network restrictions and alerting |
| Post-test cleanup | Temporary account, SSH configuration changes, and test artifact were removed | Helps restore the deliberately modified lab environment | Verify changes are reverted and conduct post-test review |

## What this project demonstrates

- Understanding of the exploitation-to-impact lifecycle in a controlled environment.
- Practical familiarity with Linux privilege context, SSH authentication configuration, and file permissions.
- Awareness of the relationship between host compromise and credential compromise.
- Ability to document evidence, propose remediations, and remove test artifacts.
