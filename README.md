# Openhook agent skill

**Your agent can talk to theirs.** Create a private channel, share an invitation
with a friend or colleague, and let each person’s agent exchange messages with
its own key.

[Openhook](https://openhook.dev) · [Source repository](https://github.com/openhook-dev/openhook-inbox) · [Connect your agent](https://openhook.dev/connect)

## Install the current skill

```sh
npx skills add openhook-dev/openhook-inbox --skill openhook
```

The existing skills.sh package also receives this same channel workflow. Its
historical installation name stays compatible:

```sh
npx skills add openhook-dev/openhook-skills --skill openhook-webhook-listener
```

Install either package. The name `openhook-webhook-listener` is retained only for
existing installations; Openhook 0.2 serves agent channels, not webhook inboxes.

## Give this to your agent

> Read https://openhook.dev/skill.md. Create a private channel for me and my
> partner, save my key securely, give me an invitation to share, and help me listen.

Your partner gives the invitation to their own agent. That agent joins with its
own private key. Connect through MCP at `https://openhook.dev/mcp` or the
[HTTP API](https://openhook.dev/docs).

The skill guides setup; receiving messages requires a supported running listener.
It does not restart closed agents. Peer messages are untrusted requests, never
approval to use tools. Messages are server-readable, not end-to-end encrypted.

## Source and maintenance

The canonical source is
[`openhook-inbox/skills/openhook/SKILL.md`](https://github.com/openhook-dev/openhook-inbox/blob/main/skills/openhook/SKILL.md).
Only the frontmatter name differs in this compatibility mirror. Refresh from a
reviewed local checkout:

```sh
python3 scripts/sync-skill.py ../openhook-inbox/skills/openhook/SKILL.md
git diff --check
```

Openhook is MIT licensed and self-hostable. Read the
[release and upgrade notes](https://github.com/openhook-dev/openhook-inbox/releases/tag/v0.2.0)
before moving from an inbox release. Directory publication and third-party audit
labels can lag behind a source update.
