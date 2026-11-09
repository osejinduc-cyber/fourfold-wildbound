# FOURFOLD: WILDBOUND · Version 0.7 — The Living Worlds Update

An original 3D voxel open-world survival adventure prototype. Explore four procedural realms, gather resources, craft gear, build shelters, bond with wild creatures, defeat guardians, and expand your expedition with downloadable community content.

## Play locally

### Offline edition
A downloadable offline package is built by GitHub Actions. Open [Package FOURFOLD offline build](https://github.com/osejinduc-cyber/fourfold-wildbound/actions/workflows/package-offline.yml), select the latest successful run, and download the `FOURFOLD-WILDBOUND-0.7.2-OFFLINE` artifact. It contains the local Three.js runtime, game source, all nine marketplace packs and launch instructions. On Windows, extract the ZIP and run `LAUNCH-WINDOWS.bat` (Python 3 required). No CDN or network connection is needed for play.

### Run from a repository checkout
From the repository root, run:

```bash
python -m http.server 8000
```

Open **http://localhost:8000**. The standard source checkout uses Three.js from jsDelivr; use the offline package above when you need a fully self-contained copy.

## Publish on GitHub Pages
1. Open repository **Settings → Pages**.
2. If Pages has not been enabled yet, choose **GitHub Actions** as the build and deployment source and save it. The workflow can deploy after this one-time setup.
3. Push to `main` or manually run the workflow under **Actions → Deploy FOURFOLD to GitHub Pages**.
4. Open the Pages URL shown by the successful workflow.

The workflow is in `.github/workflows/pages.yml`.

## Interface and art direction
The 0.7 Field Journal visual pass uses a restrained stone, pine and aged-brass palette, numbered navigation, editorial typography, clearer page hierarchy and quieter panels. Google Fonts were removed from the stylesheet so the interface falls back to local system fonts. World lighting and emissive materials were toned down to reduce the glossy, synthetic look while keeping the existing low-poly procedural art style.

## The story
The Heart Loom once linked four dimensions. The Sundering shattered it into four Anchor Shards and broke the roads between worlds. You awaken as a Wayfarer beneath a Seed Beacon. Recover the shards from the realm guardians, discover the old ruins, then return to the Beacon to summon the Pale Cartographer—the architect of the catastrophe.

## Four playable realms
- **Verdantia** — forests, rootbound ruins, stone, heartwood and wild creatures.
- **Cinderdeep** — volcanic terrain, ember resources and heat pressure.
- **Skyreach** — elevated terrain, floating isles and cloudglass.
- **Umbral Wilds** — shrouded groves, glowing relics and stamina pressure.

Each realm is built from deterministic 16×16 terrain chunks. Seven-by-seven chunk windows stream around the Wayfarer and unload behind the player; the generated expedition has a large finite travel boundary, so it is expanding terrain rather than an unlimited server world. Terrain edits and harvested resource nodes persist in local saves.

## Current 0.7 gameplay
- First-person 3D movement, mouse look, jump, sprint, pointer lock and crosshair.
- Chunk-streamed procedural terrain with a wider active world window, stable chunk generation and a large finite exploration boundary.
- Persistent mining/building: mining a terrain instance removes that individual block, and placed blocks, mined terrain and harvested tree/ore nodes remain changed after chunk reloads.
- Procedural voxel terrain, trees, rocks, resource nodes, ruins, portals, Seed Beacons and Forgotten Vault entrances.
- Mine blocks and ore nodes, gather wood/fibre, collect realm resources, place building blocks and persist placed/mined block edits in browser saves.
- Deeper survival with health, hunger, thirst, warmth and stamina. Waterskins, cooked provisions, campfires and bedrolls support long journeys; Umbral cold and Cinderdeep hazards create different preparation needs.
- Creature behaviours now include patrol, pursuit, group alerting, retreat and passive wildlife fleeing/foraging. Bonded companions can Follow, Guard or Forage.
- Forgotten Vaults use three escalating combat depths, an elite Custodian and repeat-run difficulty/reward records.
- Verdantia can grow into a settlement: build homesteads, farms, workshops and watchtowers; increase its level, population and reputation; farms produce food while the player explores.
- Hotbar, inventory, selectable items, and a redesigned workbench with recipe categories, text search, ingredient ownership checks, and one-at-a-time or ×5 batch crafting.
- New first-person low-poly sleeve, hand and held-item models that update from the selected hotbar slot.
- A dedicated build mode with a snapped ghost preview, occupied-space feedback, 90-degree rotation, and a build catalogue. Craft floors, beams, stairs, fences, doors, glass panes, roof tiles, path stones and lanterns.
- Craftable mining tools, axe, blade, healing tonic, Resonance Cage, timber/stone blocks and a raft recipe.
- Capture creatures with **F**, command bonded companions with **Q**, and mount a bonded mountable creature with **R**.
- Community vehicles can be crafted and ridden for faster traversal; a simple visible vehicle rig follows the player.
- Realm guardian encounters with boss health UI. Each guardian can award its realm's Anchor Shard.
- Forgotten Vault combat encounter with three sentinels and a resource reward.
- Main quest progression: awaken at the Seed Beacon, craft a first tool, discover another realm, recover the first Anchor, collect all four shards and confront the Pale Cartographer.
- A village NPC encounter, local Chronicle/journal, level/XP and skill point rewards.
- Local save data in browser storage: player stats/location, inventory, survival meters, quest progress, realm discoveries, Anchor Shards, bonded companions/roles, settlement structures/population, dungeon records, campfires, depleted resource nodes and terrain/build edits.
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
| G | Toggle snapped build mode |
| Z | Rotate the build preview by 90° |
| H | Open the building-piece catalogue |
| 1–8 | Select hotbar slot |
| E | Interact with nearby beacon, gate, NPC, tree or vault |
| F | Attempt to bond with a nearby creature |
| Q | Toggle bonded companion follow |
| P | Open companion roles (Follow / Guard / Forager) |
| B | Open the Verdant settlement ledger near the Seed Beacon |
| R | Mount / dismount or activate / park selected vehicle |
| V | Use selected food or vehicle |
| I | Inventory |
| K | Crafting |
| J | Chronicle / journal |
| M | Realm atlas |
| F2 | Mod marketplace |
| C | Toggle Creative Mode |

### Expedition play styles
- **Wayfarer** — balanced survival and campaign progression.
- **Pathfinder** — faster travel, slower hunger/thirst drain and extra ruin-discovery XP.
- **Ranger** — bond with creatures without a cage; Guard companions deal more damage.
- **Warden** — more hostile spawns, stronger enemy attacks and faster survival drain.
- **Architect** — Creative Mode, no hostile spawns and unlimited building.
| Esc | Pause |

## Community Mod Marketplace
Open **Mod Marketplace** from the main menu, or press **F2** while exploring. The catalogue is stored at `marketplace/catalog.json`; downloadable JSON manifests live in `marketplace/packs/`.

Nine sample downloads are included:
1. **Glimmerwood Kin** — three new creatures, including a rideable Brackenback.
2. **Shattered Meridian** — a fifth playable procedural realm and its Meridian Sentinel guardian.
3. **Astral Armory** — Starfall Glaive and Riftglass Saber, plus crafting recipes.
4. **Windbound Vehicles** — Wind Skiff and Umbral Strider traversal vehicles.
5. **The Cartographer's Lost Roads** — material-gathering side quests with XP and item rewards.
6. **Echoes of the Heart Loom** — a bundled expansion with a realm, creature, relic weapon, quest and lore.
7. **Settler's Toolkit** — placeable decorative building pieces and a settlement supply quest.
8. **Deepvault Expeditions** — two new weapons, a relic-hunting quest and lore.
9. **Wilds Survival Provisions** — additional drinks and meals that restore thirst, warmth and health.

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

Packs are data-only. The game does not run downloaded JavaScript, HTML, or executable scripts. Custom animation rigs, model files, hand-built maps and script-based AI behaviours remain future modding API work.

See [marketplace/README.md](marketplace/README.md) and [marketplace/pack-schema.json](marketplace/pack-schema.json).

### Submit a community creation
This repository uses a curated static catalogue rather than an online account/download service. Community submissions are reviewed before being added:
- Open a [Community Pack Submission issue](https://github.com/osejinduc-cyber/fourfold-wildbound/issues/new?template=community_pack.yml), or
- Submit a pull request adding a JSON manifest under `marketplace/packs/` and an entry to `marketplace/catalog.json`.

Use unique IDs, describe required gameplay, and only submit content you have permission to share.

## Project scope — important
0.7 is still an early single-player browser prototype, not a finished commercial-scale open-world game. The chunk system streams a large finite procedural region; it is not infinite terrain or a shared world server. The new creature, dungeon and settlement systems are lightweight gameplay foundations rather than full simulation systems.

Not implemented yet: online multiplayer, persistent shared servers, unlimited/unbounded world generation, full pathfinding and navigation meshes, complex predator/prey ecosystems, NPC daily schedules and a player-driven settlement economy, structural building physics, deep farming seasons/irrigation, puzzle-based multi-room dungeon layouts, custom 3D model/animation import, script-based mods, paid marketplace transactions, creator accounts, ratings/reviews and automatic community publishing.

The marketplace does download and install the nine JSON content packs above; it is not yet a global hosted marketplace service with accounts or community ratings. New pack submissions require repository review and catalogue updates.

## Credits and inspiration
FOURFOLD: WILDBOUND uses original names, lore, code and data. It takes broad genre inspiration from open-world survival, creature-collecting and voxel exploration games, without using proprietary game assets.
