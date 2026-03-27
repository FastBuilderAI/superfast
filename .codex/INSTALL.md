# Installing Superfast for Codex

Enable superfast skills in Codex via native skill discovery. Just clone and symlink.

## Prerequisites

- Git

## Installation

1. **Clone the superfast repository:**
   ```bash
   git clone https://github.com/obra/superfast.git ~/.codex/superfast
   ```

2. **Create the skills symlink:**
   ```bash
   mkdir -p ~/.agents/skills
   ln -s ~/.codex/superfast/skills ~/.agents/skills/superfast
   ```

   **Windows (PowerShell):**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
   cmd /c mklink /J "$env:USERPROFILE\.agents\skills\superfast" "$env:USERPROFILE\.codex\superfast\skills"
   ```

3. **Restart Codex** (quit and relaunch the CLI) to discover the skills.

## Migrating from old bootstrap

If you installed superfast before native skill discovery, you need to:

1. **Update the repo:**
   ```bash
   cd ~/.codex/superfast && git pull
   ```

2. **Create the skills symlink** (step 2 above) — this is the new discovery mechanism.

3. **Remove the old bootstrap block** from `~/.codex/AGENTS.md` — any block referencing `superfast-codex bootstrap` is no longer needed.

4. **Restart Codex.**

## Verify

```bash
ls -la ~/.agents/skills/superfast
```

You should see a symlink (or junction on Windows) pointing to your superfast skills directory.

## Updating

```bash
cd ~/.codex/superfast && git pull
```

Skills update instantly through the symlink.

## Uninstalling

```bash
rm ~/.agents/skills/superfast
```

Optionally delete the clone: `rm -rf ~/.codex/superfast`.
