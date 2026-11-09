# Changelog

## 0.7.2 — Workbench, First-Person Equipment & Building

- Replaced the plain recipe list with a redesigned workbench: All, Tools, Weapons, Survival, Building, Travel and Community filters; live recipe search; selected design details; ingredient counts; output previews; and batch craft ×5.
- Changed crafting to consume and grant materials in one saved transaction, with Creative Mode bypassing ingredient costs.
- Added a camera-mounted low-poly forearm, cuff, hand and item silhouettes. Tools, weapons, blocks, food and vehicles display different held models, and the model refreshes when the selected hotbar slot changes.
- Added Build Mode (G), a snapped wireframe placement preview, blocked-space feedback, and 90-degree rotation (Z).
- Added a build catalogue (H) that assigns structural pieces to the selected hotbar slot.
- Added craftable structural pieces: timber floors, beams, stairs, fences, doors, Cloudglass panes, roof tiles, stone paths and lanterns.
- Saved building-piece identity and rotation in terrain edits and restored the correct piece when its chunk streams back in.
- Added five expedition presets: Wayfarer, Pathfinder, Ranger, Warden and Architect, each with gameplay modifiers.
- Added crafting, held equipment, building and play-style controls to the HUD; updated the responsive workbench and selection-card styling.

## 0.7.1 — The Field Journal Visual Pass

- Reworked the main menu as a quieter, editorial field journal with numbered navigation, clearer hierarchy, improved realm/marketplace cards and a four-part world facts strip.
- Replaced glow-heavy gradients with a restrained pine, stone and aged-brass palette, squared card edges and more consistent spacing.
- Updated pause, HUD, inventory, crafting and modal styling to share the same visual language.
- Removed the remote Google Fonts import and introduced system-font fallbacks.
- Reduced scene exposure, ambient light and emissive intensity to make the low-poly world less glossy and synthetic.
- Added a GitHub Actions workflow that vendors the Three.js build and produces a self-contained offline ZIP with all nine marketplace packs and Windows/macOS/Linux launch instructions.

## 0.7.0 — The Living Worlds Update

### Expanding worlds
- Expanded the active world window to a seven-by-seven grid of 16×16 chunks around the Wayfarer.
- Extended the finite procedural travel boundary and kept chunk creation deterministic from the world seed and realm.
- Fixed instance-aware terrain mining so a single terrain cube is removed instead of deleting its entire instanced batch.
- Persisted mined terrain, harvested trees and ore nodes across chunk unload/reload, with realm-specific depletion IDs.
- Kept campfire warmth local to the realm where the campfire was placed.

### Wildlife and companions
- Added patrol, forage, flee, hunt, group-alert and low-health retreat behaviours to the lightweight creature AI.
- Added companion field roles: Follow, Guard and Forager, with a companion role panel.
- Guard companions periodically damage nearby threats; Forager companions periodically return a small fibre supply.

### Dungeons and combat progression
- Rebuilt the Forgotten Vault entrance with more substantial stonework and a rune seal.
- Turned vault combat into three escalating depths, ending with a Vaultheart Custodian.
- Added repeat-run records that raise later vault enemy durability and damage, with improved completion rewards.
- Kept the vault boss separate from the four core realm guardians and their Anchor Shard progression.

### Settlement and survival
- Added a Verdant settlement ledger at the Seed Beacon and a B-key shortcut.
- Added buildable homesteads, Sunberry farms, workshops and watchtowers, with residents, settlement population, reputation and five Beacon levels.
- Farms produce a small berry harvest over time while the expedition is active.
- Expanded survival from health/hunger/stamina to health, hunger, thirst, warmth and stamina.
- Added craftable waterskins, warming stew, campfires and reusable bedroll rest.
- Added thirst and warmth meters to the HUD and realm-specific environmental pressure.

### Community marketplace
- Expanded the catalogue from six to nine downloadable data packs.
- Added Settler's Toolkit, Deepvault Expeditions and Wilds Survival Provisions.
- Added Settlement, Dungeon and Survival marketplace filters and validator category support.
- Kept the marketplace data-only; no downloaded JavaScript or HTML is executed.

### Save compatibility
- Versioned new world saves as 0.7 and migrated existing 0.6 saves forward in the browser.
- Added persistence for settlement structures/residents, companion roles, dungeon records, depleted resources and campfire locations.

## 0.6.0 — Fourfold Frontier

### Core game
- Replaced the minimal scene with a 0.6 menu, HUD, pause, Chronicle, realm atlas, settings and local-save flow.
- Added procedural expedition terrain for Verdantia, Cinderdeep, Skyreach and the Umbral Wilds, each with different palettes, resources and guardian identities.
- Expanded realm maps, resource nodes, trees, ruin structures, a Seed Beacon, Realm Gate and Forgotten Vault entrance.
- Added first-person movement, pointer-lock mouse look, jump, sprint, raycast mining/attacking and block placement.
- Added health, hunger and stamina, hostile creature pursuit/attacks, respawn, inventory, hotbar and crafting.
- Added bonded creature companions, follow commands, mountable wildlife and visible community vehicle rigs.
- Added guardian health display, four Anchor Shard rewards, Forgotten Vault sentinel encounter and Pale Cartographer final boss trigger.
- Added campaign journal, NPC encounter, XP and skill point rewards.
- Added persistence for inventory, stats, quests, discovered realms, companions, Anchor Shards and placed/mined block edits.

### Community mod marketplace
- Added GitHub-hosted static catalogue and six downloadable data packs.
- Added safe JSON manifest validation, local-file import, HTTPS URL import, enable/disable/remove, installed-pack library and local storage persistence.
- Added content registration for custom creatures, dimensions, weapons, vehicles, quests, recipes, lore and items.
- Added creator submission flow, pack schema and contribution documentation.
- Packs do not execute third-party scripts.

### Known limitations
- This remains a bounded single-player browser prototype. Online multiplayer, shared servers, chunk streaming, complex physics, advanced AI, custom model/animation importing, full settlement simulation and a server-backed marketplace are future development.
