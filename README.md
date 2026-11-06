# FOURFOLD: WILDBOUND

An original 3D voxel open-world survival adventure across four dimensions. This is a browser-playable prototype designed to be extended into a larger game.

## What is in this build

- Four independently generated realms: Verdantia, Cinderdeep, Skyreach, and the Umbral Wilds.
- First-person exploration, mining, block placement, hotbar, inventory, crafting, hunger, stamina, health, weather, day/night, and browser saves.
- Shader-inspired voxel presentation with directional lighting, soft shadows, ambient occlusion-style shading, atmospheric fog, reflective-looking water, emissive crystals, and realm-specific sky colors.
- Main campaign built around the Heart Loom, the Sundering, four Anchor Shards, four realm guardians, and the Pale Cartographer finale.
- Four Forgotten Vault encounters, each with two enemy waves and a vault guardian; vaults award relics, alloy, crystals, and skill points.
- A small Green Road village with a trader, plus realm outposts and NPCs. Side quests for Mira, Korr, Sella, and Ilyr build relationships and grant unique rewards, lore discoveries, and skill points.
- Wayfarer skill tree: Vitality, Warden’s Discipline, Wild Forager, and Living Craft.
- Seed-Beacon settlement claim and upgrades with nearby recovery benefits.
- Farming: craft and place Garden Beds, plant Wildseed, wait for crops to grow, and harvest Sungrain and Sunberries.
- Fishing: craft a Tidecaller Rod, reach the outer shoreline, cast with T, wait for a bite, then reel in Silverfin.
- Cooking: interact with a campfire to turn Wild Meat + Sunberry into Wayfarer Stew, or Silverfin + Wild Fiber into Smoked Silverfin.
- Creature companions: capture with Resonance Cages; command them to follow or gather; ride a tamed Mossback.
- Sailing raft and a Wayfarer Glider for traversal.
- Craftable weapons, protective wraps, Cinderplate heat armor, Cloudweave shroud/glide protection, relics, rare resources, Loomsteel Alloy, and upgrade materials.
- Settlement engineering: craft conduits, switches, dynamos, processors, and powered gates. Dynamos and switches toggle nearby gates directly or through a conduit link; processors refine Ember Ore and Lumen Shards into alloy. Select any owned build item from the Inventory panel by clicking it, then use right-click to place it.
- Creative mode for free building and relaxed exploration.
- Fully redesigned multi-page main menu with Expedition, Mods, Settings and Chronicle sections.
- Mod manager with starter packs, safe JSON import/export, enable/disable controls and a documented data-registration API.
- Three bundled starter mod packs: Builder’s Atelier, Astral Reliquary and Wildskeeper’s Compendium.
- Extra graphics controls for quality presets, camera sensitivity, field of view and accessibility options.

## Story premise

The Heart Loom once connected all four dimensions. When the Sundering shattered it, four Anchor Shards were scattered and the roads between worlds collapsed. The player awakens as a Wayfarer beneath a Seed Beacon and sets out to recover the shards. The ruins reveal that the disaster was engineered by the Pale Cartographer, a former Wayfarer who wanted every path and future to obey a single design. The campaign culminates in a confrontation at the Seed Beacon after all four realm guardians have fallen.

## Run locally

Because the project uses native browser modules and an import map, it needs to be served from a local web server rather than opened as a `file://` URL. From this folder, run one of:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

Or use any static server / editor live-preview extension.

## Publish with GitHub Pages

1. Create a new GitHub repository named `fourfold-wildbound` (or another name you prefer).
2. Upload the contents of this folder to the repository root, including `.github/workflows/pages.yml`.
3. Set the repository's default branch to `main`.
4. In **Settings → Pages**, choose **GitHub Actions** as the build/deploy source.
5. Push to `main`. The included workflow publishes the static game to GitHub Pages.

The game loads Three.js from jsDelivr, so a network connection is required when playing the published build.

## Controls

- `W A S D`: move
- Mouse: look around (click the world to lock the pointer)
- `Space`: jump
- `Shift`: sprint
- `Left click`: mine / attack
- `Right click`: place the selected building block
- `1–8`: select hotbar slot
- `E`: talk / activate nearby portal or beacon
- `F`: capture a nearby creature with a Resonance Cage
- `Q`: order your companion to follow / gather
- `R`: launch or dock the raft near the shoreline
- `G`: deploy / fold the glider after unlocking it
- `Z`: mount / dismount a nearby tamed Mossback
- `V`: use the selected consumable (Sunberry, Wild Tonic, or Glider)
- `I`: inventory, `K`: crafting, `J`: journal, `M`: map, `F2`: mod manager, `Esc`: pause
- `C`: toggle creative mode

## Project scope

This prototype is intentionally transparent: local single-player is implemented; online multiplayer, persistent shared servers, a streamed persistent open world, fully simulated town populations, online multiplayer, and large handcrafted multi-floor dungeons remain future development. It is an original project and does not include Minecraft, Valheim, Palworld, or Enshrouded assets.

## Design inspirations, re-imagined

The game takes broad genre inspiration from expedition survival games: a boss-and-biome expedition loop, a buildable home base and raft travel, recruitable creature companions that can gather materials, rideable mounts, ancient ruins, a dangerous mist region, and a glider for vertical exploration. All names, world lore, characters, and assets in this prototype are original.

## Prototype limitations

This is a real-time browser prototype, not a finished commercial-scale game. It is local single-player only. Multiplayer, shared servers, a full settlement population simulation, large multi-stage dungeons, advanced animation systems, and deep crafting tiers are future work. Manual saves retain player location, health, inventory, main and side quests, relationships, settlement level, skill ranks and points, relic collection, conquered vaults, discoveries, unlocked glider, and companion roster. Placed structures, crop plots, and mined terrain edits are not yet stored in the save.

## Mods and add-ons

Open **Mods & add-ons** from the main menu or pause menu. The mod manager includes starter content packs and supports importing/exporting JSON manifests. Mods can add items, crafting recipes and lore. Modded items can optionally become placeable blocks or food consumables. This preview intentionally does not execute arbitrary scripts. See `mods/README.md` and `mods/examples/` for the format.

## Menu redesign

The main menu now uses a responsive sidebar, campaign dashboard, dimension expedition cards, mod manager entry point, settings page, and story chronicle. The interface is designed to remain legible across desktop and smaller screens. Settings include High/Balanced/Performance graphics presets, camera sensitivity, field of view, reduced motion, control hint visibility, and three survival challenge levels: Story, Wayfarer, and Wildbound. Challenge level changes incoming enemy damage and hunger drain and is saved with the expedition.

## Latest update: menu, modding and survival options

The main menu has been rebuilt as a multi-page command centre. The mod manager opens from the main menu, the pause menu, or `F2` during play. The starter library contains Builder’s Atelier (placeable Runed Brick, Sun Glass and Hearth Lantern blocks), Astral Reliquary (Starsteel, Rift Compass and Comet Flares), and Wildskeeper’s Compendium (including a food-and-healing Companion Biscuit). Modded placeable blocks can be mined to recover them. Imported mods and enabled packs are retained in browser storage independently of the world save.

To use a modded placeable block, enable its pack, craft the item, assign it to a hotbar slot from Inventory, and right-click to place it. To use a modded food item, select it and press `V`. Open the Journal’s Discoveries tab to read lore supplied by enabled packs.
