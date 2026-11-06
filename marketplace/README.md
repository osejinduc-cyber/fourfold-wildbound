# FOURFOLD 0.7 Community Mod Packs

The in-game marketplace downloads JSON manifests from `marketplace/packs/`. Installed packs are enabled locally in the browser and can be disabled or removed from **My Mods**.

## Install
Use the in-game Marketplace's **Download +** action, **Import File**, or **Import URL**. Direct URL imports must use HTTPS and point to a JSON manifest.

## Supported content arrays
- `items`: inventory item definitions; optional `type`, `icon`, `color`, `placeable`, `heal`, `hunger`, `thirst`, `warmth`.
- `creatures`: `id`, `name`, `color`, `face`, `hp`, `damage`, `speed`, optional `mount`.
- `dimensions`: `id`, `name`, `description`, integer colour values `sky`, `fog`, `ground`, `top`, `soil`, `rock`, `water`, `accent`, and optional `resource`, `hazard`, `guardian`, `icon`.
- `weapons`: `id`, `name`, `icon`, `damage`, `description`.
- `vehicles`: `id`, `name`, `icon`, `speed`, `description`.
- `quests`: `id`, `name`, `description`, `requirement.item`, `requirement.count`, `reward.xp`, optional `reward.items`.
- `recipes`: `id`, `label`, `desc`, `cost`, `out`.
- `lore`: `title`, `text`.

See the bundled examples in `marketplace/packs/`.

## Safety
The current mod loader is data-only. It does not execute JavaScript or HTML from downloaded packs. Do not include script, code or HTML fields. The client validates pack IDs, names and supported array types and caps content array sizes. Marketplace catalogue validation also verifies category names and confirms that every download path points to an existing local manifest. Marketplace entries are manually curated in this repository.

## Submit
Create a pull request with:
1. A unique JSON file in `marketplace/packs/`.
2. A matching entry in `marketplace/catalog.json` with category `creature`, `dimension`, `weapon`, `vehicle`, `quest`, `expansion`, `settlement`, `dungeon` or `survival`.
3. A short description, version and creator credit.
4. Confirmation that you created the content or have permission to share it.

Community submissions can also start through the Community Pack Submission issue template. Curated additions are reviewed before appearing in the in-game catalogue.
