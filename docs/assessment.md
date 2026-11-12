# Assessment walkthrough

This document converts the submitted **CYSE 425 – Lab 1** report into a public-facing assessment narrative. It describes only actions documented in the source; it intentionally omits executable exploit commands, live addresses, raw dumps, credentials, and payload details.

## 1. Exploitation — report pages 2–4

The assessment began with Metasploit in Kali Linux. The report identifies a Samba-associated Metasploit module for **CVE-2017-7494**, then documents configuring the authorized vulnerable target and executing the module. Screenshots and captions report that a command-shell session opened and `whoami` showed root-level access.

**Observed result:** The report documents privileged shell access to the lab target.

**Interpretation:** A service compromise capable of yielding privileged command execution can undermine confidentiality, integrity, and availability of the host.

## 2. Post-exploitation authentication testing — pages 5–9

The SSH server configuration was reviewed and temporarily modified to allow password authentication. The changed configuration was transferred to the target using a local HTTP service, then SSH was restarted. A temporary user was created with sudo privileges. The lab report describes successful SSH login and privileged command testing through that account.

**Observed result:** Authorized test-account SSH and sudo access were confirmed.

**Interpretation:** Password-enabled remote access and privileged accounts can increase exposure after initial compromise; lab changes must not be retained in a real environment.

## 3. Controlled account-file transfer — pages 10–11

The lab documentation describes making authorized copies of the target's account-information files and transferring test `passwd` and `shadow` files to Kali with Netcat.

**Observed result:** The report states the test files were received and verified.

**Interpretation:** Privileged account-file access enables offline password attacks if password hashes are disclosed. Raw account data is excluded from this public repository.

## 4. Password strength validation — pages 12–14

The report describes combining test account files with `unshadow`, then using **John the Ripper** to assess weak test-account passwords. The report documents recovered credentials, SSH login to a test account, and sudo command validation.

**Observed result:** Weak lab credentials were recovered and their usability was checked.

**Interpretation:** Credential compromise can extend the operational impact of server exploitation.

## 5. Remote shell test — page 15

A controlled Netcat reverse-shell connection from the target to Kali is shown, with root access to the lab host verified.

**Observed result:** Remote command execution continued to be observable within the authorized test setup.

## 6. Cleanup — page 16

The report states that the temporary lab account, modified SSH configuration files, and reverse-shell artifact were removed to restore the lab target.

**Observed result:** Cleanup actions were recorded. The report does not include a separate, independently verified post-cleanup audit.

## Evidence policy

The source PDF includes detailed terminal screenshots. Those screenshots may expose sensitive details and are therefore **not redistributed** as part of this public-ready starter. Add carefully reviewed/redacted screenshots later under `assets/evidence/` only when you can confirm that no credentials, hashes, personal data, IP addresses requiring confidentiality, or other secrets remain.
