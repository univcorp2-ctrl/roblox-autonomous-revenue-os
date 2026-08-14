# Autonomous Revenue OS architecture

The system deliberately separates AI creativity from deterministic release control.

`Market intelligence -> hypothesis queue -> builder -> Studio MCP -> playtest -> independent checks -> canary -> Open Cloud analytics -> keep/rollback`

## Agent boundaries

- Market agent: discovers successful and failing patterns. It may copy mechanics at the pattern level, never proprietary code, art, names, maps, audio, copy, or branding.
- Product agent: turns one pattern into the smallest sellable Creator Store feature or game experiment.
- Builder agent: edits Luau/UI/3D through Studio MCP.
- QA agent: runs playtests, simulated input, device checks, console inspection, and assertions.
- Revenue agent: reads analytics and ranks next experiments.
- Release controller: deterministic; rejects unsafe or low-confidence changes and owns rollback.

## Zero-human target

Normal operations should require no human input. Human gates remain only where platform identity, tax, legal/IP, account security, or new external spend makes automation inappropriate.

## Profit order

1. Creator Store paid plugin: shortest route to direct USD sales.
2. Adjacent paid models/plugins: reuse distribution, code and brand.
3. Creator-facing SaaS: recurring revenue after demand is demonstrated.
4. One evergreen social-learning experience: asymmetric upside, operated by the same analytics and QA loop.
