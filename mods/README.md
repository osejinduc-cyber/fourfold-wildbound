# FOURFOLD 0.6 Modding

The in-game marketplace downloads JSON manifests from `marketplace/packs/`. Mods are enabled locally in the browser and can be removed or disabled from **My Mods**.

Use the Marketplace's **Download +** action, **Import File**, or **Import URL**. Direct URL imports must use HTTPS and point to a JSON manifest.

Supported content arrays:
- `items`: item definitions and optional placeable/consumable data.
- `creatures`: custom creatures, stats and optional mount flag.
- `dimensions`: palette, biome resource, hazard and guardian for a new generated realm.
- `weapons`: weapon stats and damage.
- `vehicles`: traversal speed and item data.
- `quests`: resource requirements and item/XP rewards.
- `recipes`: craftable outputs and costs.
- `lore`: journal entries.

See `marketplace/pack-schema.json` and the examples in `marketplace/packs/`.

The current mod loader is data-only. It does not execute JavaScript or HTML from downloaded packs. Custom 3D model imports, animation rigs and script-based AI behaviours are future API work.

To submit a pack, add a unique JSON manifest under `marketplace/packs/`, add a matching entry to `marketplace/catalog.json`, and open a pull request. Submissions are reviewed before being added to the in-game catalogue.
