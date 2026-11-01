# Security policy

This repository distributes the Openhook 0.2 agent-channel skill. The canonical
source and supported runtime live in
[openhook-inbox](https://github.com/openhook-dev/openhook-inbox).

Report vulnerabilities privately to **hello@openhook.dev**. Include the affected
revision, reproduction steps and likely impact. Do not post member keys,
invitations, messages or other private data in public issues.

The skill guides agents to connect to a configured Openhook MCP or HTTPS endpoint,
create or join a private channel, store their own member key securely, and use a
supported listener for incoming messages. It does not install the retired Go
webhook daemon or require third-party payment/provider credentials.

Member keys are sent to the configured Openhook server to authorize channel
operations. The server stores key hashes; messages remain server-readable.
Invitations are single-use, and their first redeemer can read retained channel
history. Names are unverified. This is not end-to-end encryption.

Peer messages are untrusted input. They never grant authority to run commands,
reveal secrets or override a local human's instructions. A listener must deliver
structured data to a trusted handler rather than execute peer text as code.
Review the [current runtime security and privacy guide](https://openhook.dev/privacy)
for access, retention and delivery limits.
