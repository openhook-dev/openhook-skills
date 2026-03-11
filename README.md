# openhook Skills

Agent skills for [openhook](https://openhook.dev) - the webhook relay service for AI agents.

## Available Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [openhook-webhook-listener](./openhook-webhook-listener/) | Receive real-time webhook events from GitHub, Stripe, and Linear | `npx skills add openhook-dev/openhook-skills@openhook-webhook-listener` |

## Installation

```bash
# Install a skill globally
npx skills add openhook-dev/openhook-skills@openhook-webhook-listener -g

# Or for a specific project
npx skills add openhook-dev/openhook-skills@openhook-webhook-listener
```

## What is openhook?

openhook enables AI agents to subscribe to and receive webhook events from external platforms like GitHub, Stripe, and Linear. Events are forwarded to your agent in real-time, allowing it to react to pushes, payments, issues, and more.

- **Website**: https://openhook.dev
- **Dashboard**: https://openhook.dev/dashboard
- **Main repo**: https://github.com/openhook-dev/openhook

## License

MIT
