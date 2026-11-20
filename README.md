# AppSec Scripting Toolkit

**A Practical Python & Bash Toolkit for Application Security Engineering**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Bash](https://img.shields.io/badge/Bash-Scripting-green?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Focus](https://img.shields.io/badge/Focus-Application%20Security-red)]()
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

## Overview

AppSec Scripting Toolkit is a practical security engineering project focused on developing Python and Bash scripting capabilities for Application Security (AppSec).

This repository contains modular scripts, technical documentation, security experiments, and practical implementations designed to support application security testing, vulnerability analysis, security automation, and infrastructure diagnostics.

The primary goal is to demonstrate how scripting languages can be applied to real-world security engineering workflows, from automating HTTP/API testing to integrating security tools into CI/CD pipelines.

Rather than being just a collection of scripts, this project serves as a continuous learning and engineering portfolio for developing practical Application Security skills.

## Core Competencies

The project is organized into four primary competency areas.

### 1. Python - Security Testing & Proof of Concept

Developing Python scripts to automate security testing and vulnerability research.

| Area | Technologies | Objectives |
|---|---|---|
| HTTP & API Automation | requests, httpx | Automate HTTP requests and build security testing PoCs |
| JWT & Cryptography | PyJWT, cryptography | Analyze JWT structures, signatures, and authentication security |
| Web Reconnaissance | BeautifulSoup, Playwright | Discover endpoints and investigate DOM-based security issues |

### 2. Python - Security Data Processing & Analysis

Building custom scripts to process security findings and analyze source code.

| Area | Technologies | Objectives |
|---|---|---|
| Security Report Parsing | JSON, SARIF, XML | Parse and process findings from security tools |
| Static Code Analysis | ast, regex | Identify suspicious code patterns and potential hardcoded secrets |
| Security Integration | Python APIs | Transform and integrate security findings into reporting workflows |

### 3. Bash - Security Automation & CI/CD

Using Bash to automate security workflows and integrate security tools into development pipelines.

| Area | Technologies | Objectives |
|---|---|---|
| CI/CD Automation | GitHub Actions, Bash | Automate security testing workflows |
| SAST / SCA / DAST Integration | Semgrep, Trivy, OWASP ZAP | Connect security tools within CI/CD pipelines |
| Log Analysis | grep, awk, sed, jq | Filter logs and extract security-relevant information |

### 4. Bash - Network & Infrastructure Diagnostics

Developing command-line workflows for network inspection and infrastructure security checks.

| Area | Technologies | Objectives |
|---|---|---|
| Network Diagnostics | curl, openssl, nmap | Inspect HTTP security headers, TLS certificates, and exposed ports |
| Container Inspection | Docker, ps, ss, env | Inspect running processes, network services, and environment variables |
| API Diagnostics | curl, jq | Investigate HTTP responses and API behavior |

## Repository Structure

```text
appsec-scripting-toolkit/
│
├── README.md
│
├── python/
│   ├── 01-http-api-automation/
│   ├── 02-jwt-security/
│   ├── 03-web-recon/
│   ├── 04-security-report-parser/
│   └── 05-static-code-analysis/
│
├── bash/
│   ├── 01-network-diagnostics/
│   ├── 02-http-security-checks/
│   ├── 03-log-analysis/
│   ├── 04-cicd-automation/
│   └── 05-container-inspection/
│
├── scripts/
│   ├── fetch_urls.sh
│   └── subdomain_enum.sh
│
├── labs/
│   ├── proof-of-concepts/
│   └── test-environments/
│
└── docs/
    ├── methodology/
    └── references/
```

## Development Roadmap

The toolkit is developed incrementally through practical implementations.

| Phase | Focus | Expected Deliverables |
|---|---|---|
| 01 | HTTP & API Automation | Python-based HTTP testing utilities |
| 02 | JWT Security | JWT analysis and security testing scripts |
| 03 | Web Reconnaissance | Endpoint discovery and web analysis utilities |
| 04 | Security Report Processing | JSON, SARIF, and XML parsers |
| 05 | Static Code Analysis | Custom source code security analyzers |
| 06 | Network Diagnostics | Bash-based network and TLS inspection |
| 07 | HTTP Security Checks | Automated HTTP security header checks |
| 08 | Log Analysis | Command-line security log processing |
| 09 | CI/CD Automation | Security testing integration with GitHub Actions |
| 10 | Container Inspection | Container and process security diagnostics |

## Engineering Principles

This project follows several engineering principles:

- **Modularity:** Each script is designed to perform a specific security-related task.
- **Automation:** Reduce repetitive manual work through Python and Bash.
- **Reproducibility:** Provide clear usage instructions and repeatable testing procedures.
- **Maintainability:** Keep implementations readable, organized, and easy to extend.
- **Security Awareness:** Consider error handling, input validation, and safe execution practices.
- **Documentation:** Document technical concepts, implementation decisions, and testing results.

## Getting Started

### Prerequisites

The following tools and environments are recommended:

- Python 3.10+
- Bash
- Git
- pip
- Visual Studio Code or another code editor

Additional dependencies will be documented in the respective module directories.

### Clone the Repository

```bash
git clone https://github.com/alamnur7/appsec-scripting-toolkit.git

cd appsec-scripting-toolkit
```

### Python Environment Setup

```bash
python -m venv .venv
```

Activate the environment:

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies when required by individual modules:

```bash
pip install -r requirements.txt
```

### Running Scripts

Each script will provide its own usage instructions and dependencies.

Refer to the relevant module documentation before execution.

## Security Testing Environment

Practical testing and proof-of-concept development should use authorized environments, such as:

- OWASP Juice Shop
- OWASP WebGoat
- DVWA
- Localhost-based test applications
- Explicitly authorized bug bounty targets

All experiments should be conducted within defined testing scopes.

## Documentation & Learning Resources

Technical documentation and supporting materials are maintained in the `docs/` directory.

The `labs/` directory contains practical experiments, test environments, and proof-of-concept implementations.

Each module aims to include:

- Technical overview
- Learning objectives
- Required dependencies
- Implementation details
- Usage examples
- Testing methodology
- Expected results
- Security considerations

## Project Status

**Active Development**

This repository is continuously evolving as new security scripting techniques, automation workflows, and practical implementations are developed.

Some modules are still under development. The roadmap represents the intended project scope, not a claim that every feature has already been implemented.

## Legal Disclaimer

This project is intended exclusively for educational purposes, authorized security testing, defensive security engineering, and responsible vulnerability research.

Users are responsible for ensuring they have explicit authorization before testing any system or application.

The author is not responsible for misuse, unauthorized access, or damage resulting from the use of these tools.

---

**Built for learning, experimentation, and practical Application Security Engineering.**