# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it by emailing security@openhook.dev.

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

We will respond within 48 hours and work with you to understand and resolve the issue.

## Security Considerations

This skill instructs AI agents to:
- Install the openhook CLI from https://openhook.dev/install.sh
- Authenticate with user-provided API keys
- Subscribe to webhook events from external platforms
- Run a daemon process that forwards events to OpenClaw

The skill does NOT:
- Store or transmit credentials beyond the local machine
- Execute arbitrary code
- Access files outside of its intended scope
- Make network requests to untrusted endpoints

## Dependencies

This skill has no runtime dependencies. It provides instructions for the openhook CLI which is a standalone Go binary.
