# FOURFOLD: WILDBOUND

An original 3D voxel sandbox-action prototype for the browser, set across four imagined dimensions. The project is in an early playable-foundation stage.

## Current playable build

- A 3D voxel-style Verdantia landscape with block terrain, trees, rocks, a shoreline and a glowing Seed Beacon.
- First-person camera, WASD movement, mouse look, jumping and sprinting.
- Basic block mining and placement with simple wood and stone counters.
- A shader-inspired presentation pass using Three.js: directional lighting, shadow maps, fog, tone mapping and a stylized voxel environment.
- Opening story text introducing the Heart Loom, the Sundering, the four Anchor Shards and the Wayfarer.
- A GitHub Pages workflow for publishing the static prototype.

## The world and story vision

The Heart Loom once connected all four dimensions: Verdantia, Cinderdeep, Skyreach and the Umbral Wilds. The Sundering shattered it and scattered four Anchor Shards. The player awakens as a Wayfarer and must explore the realms, recover the shards, uncover the truth, and confront the Pale Cartographer.

Planned systems include a full campaign and side quests, dungeons and raids, dimension bosses, weapons and armor progression, skills and relics, farming, fishing, cooking, creature companions and mounts, settlements, machinery and automation, Creative Mode, and a safe mod ecosystem.

## Run locally

The game uses the Three.js browser module from jsDelivr. Run a local web server from the repository root:

```bash
python -m http.server 8000
```

Open http://localhost:8000 in a modern browser. A network connection is needed to load Three.js.

## GitHub Pages

1. In repository Settings → Pages, choose **GitHub Actions** as the deployment source.
2. Push to the `main` branch or manually run the Pages workflow.
3. Once the workflow succeeds, GitHub Pages will publish the site.

## Controls

- WASD: move
- Mouse: look around (click the world to lock pointer)
- Space: jump
- Shift: sprint
- Left mouse: mine a targeted block
- Right mouse: place a block on the targeted face
- E: interact with the Seed Beacon when nearby
- Esc: pause

## Modding status

The `mods/` folder contains a JSON manifest example and a guide for a future data-driven mod format. A working in-game mod manager and script sandbox are not part of this initial GitHub upload yet. The long-term direction is safe content packs for items, recipes, lore, creatures, structures and dimension content.

## Honest scope

This GitHub repository currently contains an early single-player prototype, not the full game described in the design vision. The current build does not yet implement the complete four-dimension campaign, full inventory/crafting/survival loop, NPC quests, creature capture, sailing, gliding, advanced automation, persistent world edits, multiplayer or a complete mod manager. These are future development goals.

All game names, story elements and code in this repository are original. The project takes broad genre inspiration from open-world survival and sandbox games without using their proprietary assets.
