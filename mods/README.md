# FOURFOLD: WILDBOUND Mod Packs

This prototype uses safe JSON data manifests. Packs can add item definitions, recipes, and journal lore. Some items may be marked as placeable blocks or consumables. The current format does not execute arbitrary JavaScript.

## Install
1. Open Mods & Add-ons in the game.
2. Choose Import JSON Mod and select a manifest.
3. Enable the imported pack.
4. Open Crafting to discover its recipes.

See examples/example-celestial-tools.json for a starter manifest. IDs must be unique lowercase identifiers. Recipes may refer only to base-game items or items supplied by enabled packs.

Future mod API goals include custom creatures, dimension content, structures, scripted behaviours in a sandbox, and custom 3D assets. These advanced extension points are not implemented in this prototype.
