---@meta _
-- grabbing our dependencies,
-- these funky (---@) comments are just there
--	 to help VS Code find the definitions of things

---@diagnostic disable-next-line: undefined-global
local mods = rom.mods

---@module 'SGG_Modding-ENVY-auto'
mods['SGG_Modding-ENVY'].auto()
-- ^ this gives us `public` and `import`, among others
--	and makes all globals we define private to this plugin.
---@diagnostic disable: lowercase-global

---@diagnostic disable-next-line: undefined-global
rom = rom
---@diagnostic disable-next-line: undefined-global
_PLUGIN = _PLUGIN

json = import "jsonParser.lua"

-- get definitions for the game's globals
---@module 'game'
game = rom.game
---@module 'game-import'
import_as_fallback(game)

---@module 'SGG_Modding-Chalk'
chalk = mods["SGG_Modding-Chalk"]
---@module 'SGG_Modding-ReLoad'
reload = mods['SGG_Modding-ReLoad']

---@module 'config'
config = chalk.auto 'config.lua'
-- ^ this updates our `.cfg` file in the config folder!
public.config = config -- so other mods can access our config

local function removeCurrentTraits()
    for _, val in pairs(game.CurrentRun.Hero.Traits) do
        game.RemoveTrait(game.CurrentRun.Hero, val)
    end
    
end

local function setupLoadout(loadoutData)
    removeCurrentTraits()

    for key, value in pairs(loadoutData) do
        if key == "keepsake" then
            if value ~= nil and value ~= "" then
                game.EquipKeepsake(CurrentRun.Hero, value)
            end
        elseif key == "traits" then
            for _, traitItem in pairs(loadoutData.traits) do
                if game.HeroHasTrait(traitItem.id) == false then
                    game.AddTrait(CurrentRun.Hero, traitItem.id, traitItem.rarity)
                end
            end
        elseif key == "weapon" then
            local weaponData = game.WeaponData[value]

            if weaponData ~= nil then
                game.UseWeaponKit(weaponData)
            else
                print("Weapon data not found")
            end
        end
    end

	-- This applies traits/upgrades
	game.EquipWeaponUpgrade(CurrentRun.Hero, { SkipNewTraitHighlight = true })
	game.EquipMetaUpgrades( CurrentRun.Hero, { SkipNewTraitHighlight = true })
	game.UpdateRunHistoryCache(CurrentRun)
	game.BuildMetaupgradeCache()
end

rom.inputs.on_key_pressed({
    "Control X",
    Name = "Use Loadout",
    function()
        local file = io.open("./Content/Mods/MyMod2/plugin_data/loadout.json", "r" )

        if file then
            -- read all contents of file into a string
            local contents = file:read("*a")
            io.close( file )

            local loadout = json.parse(contents)
            thread(setupLoadout, loadout)
        else
            print("Loadout file not found")
        end
    end
})
