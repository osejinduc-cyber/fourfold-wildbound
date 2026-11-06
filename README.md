# FOURFOLD: WILDBOUND · Version 0.6

An original 3D voxel open-world survival adventure prototype. Explore four procedural realms, gather resources, craft gear, build shelters, bond with wild creatures, defeat guardians, and expand your expedition with downloadable community content.

## Play locally
This is a static browser game using Three.js from jsDelivr. From the repository root, run:

```bash
python -m http.server 8000
```

Open **http://localhost:8000**. A network connection is needed to load Three.js and the community marketplace catalogue.

## Publish on GitHub Pages
1. Open repository **Settings → Pages**.
2. If Pages has not been enabled yet, choose **GitHub Actions** as the build and deployment source and save it. The workflow can deploy after this one-time setup.
3. Push to `main` or manually run the workflow under **Actions → Deploy FOURFOLD to GitHub Pages**.
4. Open the Pages URL shown by the successful workflow.

The workflow is in `.github/workflows/pages.yml`.

## The story
The Heart Loom once linked four dimensions. The Sundering shattered it into four Anchor Shards and broke the roads between worlds. You awaken as a Wayfarer beneath a Seed Beacon. Recover the shards from the realm guardians, discover the old ruins, then return to the Beacon to summon the Pale Cartographer—the architect of the catastrophe.

## Four playable realms
- **Verdantia** — forests, rootbound ruins, stone, heartwood and wild creatures.
- **Cinderdeep** — volcanic terrain, ember resources and heat pressure.
- **Skyreach** — elevated terrain, floating isles and cloudglass.
- **Umbral Wilds** — shrouded groves, glowing relics and stamina pressure.

Each realm is procedurally generated from its own terrain palette and height rules. The map in this prototype is a bounded expedition region rather than an infinite streamed world.

## Current 0.6 gameplay
- First-person 3D movement, mouse look, jump, sprint, pointer lock and crosshair.
- Procedural voxel terrain, trees, rocks, resource nodes, ruins, portals, Seed Beacons and Forgotten Vault entrances.
- Mine blocks and ore nodes, gather wood/fibre, collect realm resources, place building blocks and persist placed/mined block edits in browser saves.
- Survival health, hunger and stamina; hostile creatures can chase and attack; respawn returns the Wayfarer to the expedition start.
- Hotbar, inventory, selectable items, recipes and field crafting.
- Craftable mining tools, axe, blade, healing tonic, Resonance Cage, timber/stone blocks and a raft recipe.
- Capture creatures with **F**, command bonded companions with **Q**, and mount a bonded mountable creature with **R**.
- Community vehicles can be crafted and ridden for faster traversal; a simple visible vehicle rig follows the player.
- Realm guardian encounters with boss health UI. Each guardian can award its realm's Anchor Shard.
- Forgotten Vault combat encounter with three sentinels and a resource reward.
- Main quest progression: awaken at the Seed Beacon, craft a first tool, discover another realm, recover the first Anchor, collect all four shards and confront the Pale Cartographer.
- A village NPC encounter, local Chronicle/journal, level/XP and skill point rewards.
- Local save data in browser storage: player stats/location, inventory, quest progress, realm discoveries, Anchor Shards, bonded companions and block edits.
- Creative Mode toggle (**C**) for no-cost building and relaxed exploration.

### Controls
| Key / input | Action |
|---|---|
| WASD | Move |
| Mouse | Look around |
| Space | Jump |
| Shift | Sprint |
| Left click | Mine / attack |
| Right click | Place selected building block |
| 1–8 | Select hotbar slot |
| E | Interact with nearby beacon, gate, NPC, tree or vault |
| F | Attempt to bond with a nearby creature |
| Q | Toggle bonded companion follow |
| R | Mount / dismount or activate / park selected vehicle |
| V | Use selected food or vehicle |
| I | Inventory |
| K | Crafting |
| J | Chronicle / journal |
| M | Realm atlas |
| F2 | Mod marketplace |
| C | Toggle Creative Mode |
| Esc | Pause |

## Community Mod Marketplace
Open **Mod Marketplace** from the main menu, or press **F2** while exploring. The catalogue is stored at `marketplace/catalog.json`; downloadable JSON manifests live in `marketplace/packs/`.

Six sample downloads are included:
1. **Glimmerwood Kin** — three new creatures, including a rideable Brackenback.
2. **Shattered Meridian** — a fifth playable procedural realm and its Meridian Sentinel guardian.
3. **Astral Armory** — Starfall Glaive and Riftglass Saber, plus crafting recipes.
4. **Windbound Vehicles** — Wind Skiff and Umbral Strider traversal vehicles.
5. **The Cartographer's Lost Roads** — material-gathering side quests with XP and item rewards.
6. **Echoes of the Heart Loom** — a bundled expansion with a realm, creature, relic weapon, quest and lore.

### Install and manage packs
- Choose **Download +** on a marketplace card. The manifest is fetched from this repository and installed in the current browser profile.
- Open **My Mods** to enable, disable or remove installed content.
- Choose **Import File** to import a JSON manifest from your computer.
- Choose **Import URL** to install a direct HTTPS JSON manifest, such as a raw GitHub file.
- Installed packs are stored in browser local storage and are separate from the world save.
- Newly installed content is reloaded into the current realm. New dimensions appear in the in-game Atlas.

### What a pack can add
- `items` — inventory items and optional placeable blocks or consumables.
- `creatures` — custom palette, health, damage, speed and mountable companions.
- `dimensions` — new procedural realm palette, resource, hazard and guardian.
- `weapons` — craftable weapons with custom damage values.
- `vehicles` — craftable traversal upgrades with speed values.
- `quests` — resource requirements and item/XP rewards.
- `recipes` — craftable outputs and material costs.
- `lore` — journal discoveries.

Packs are data-only. The game does not run downloaded JavaScript, HTML, or executable scripts. Custom animation rigs, model files, hand-built maps and script-based AI behaviours are future modding API work.

See [marketplace/README.md](marketplace/README.md) and [marketplace/pack-schema.json](marketplace/pack-schema.json).

### Submit a community creation
This repository uses a curated static catalogue rather than an online account/download service. Community submissions are reviewed before being added:
- Open a [Community Pack Submission issue](https://github.com/osejinduc-cyber/fourfold-wildbound/issues/new?template=community_pack.yml), or
- Submit a pull request adding a JSON manifest under `marketplace/packs/` and an entry to `marketplace/catalog.json`.

Use unique IDs, describe required gameplay, and only submit content you have permission to share.

## Project scope — important
0.6 is an early single-player browser prototype and a foundation for a larger project. It is not a finished commercial-scale open-world game.

Not implemented yet: online multiplayer, persistent shared servers, streaming/infinite terrain chunks, advanced farming/fishing/cooking, complex building physics, detailed settlement populations, quest dialogue trees, multi-stage raid dungeons, full animation/rigging, custom 3D model import, script-based mods, paid marketplace transactions, creator accounts, ratings/reviews and automatic community publishing.

The marketplace does download and install the six JSON content packs above; it is not yet a global hosted marketplace service with accounts or community ratings. New pack submissions require repository review and catalogue updates.

## Credits and inspiration
FOURFOLD: WILDBOUND uses original names, lore, code and data. It takes broad genre inspiration from open-world survival, creature-collecting and voxel exploration games, without using proprietary game assets.
