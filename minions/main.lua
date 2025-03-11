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

local function spawnMinion(name)
    local weaponData = game.GetWeaponData(CurrentRun.Hero, "WeaponDagger")
    weaponData.MaxSummons = 10
    CurrentRun.CurrentRoom.SummonEnemyName = name

    game.SpellSummon({ Charge = 100 }, weaponData)
end

rom.inputs.on_key_pressed({
    "Control X",
    Name = "Setup traits",
    function()
        removeCurrentTraits()

        game.AddTrait(CurrentRun.Hero, "SummonPermanenceTalent", "Rare")
    end
})

rom.inputs.on_key_pressed({
    "Control Q",
    Name = "Spawn minion 1",
    function()
        spawnMinion("Zombie")
    end
})

rom.inputs.on_key_pressed({
    "Control E",
    Name = "Spawn minion 2",
    function()
        spawnMinion("Mage2_Elite")
    end
})

rom.inputs.on_key_pressed({
    "Alt Q",
    Name = "Spawn minion leader",
    function()
        spawnMinion("Stalker")
    end
})

rom.inputs.on_key_pressed({
    "Alt E",
    Name = "Spawn minion 4",
    function()
        spawnMinion("Dragon")
    end
})

rom.inputs.on_key_pressed({
    "Alt K",
    Name = "Detonateeee",
    function()
        local oldestMinion = MapState.SpellSummons[1]

        if not oldestMinion then
            return
        end

        game.DetonateSummon(
            oldestMinion,
            {
                ProjectileName = "SummonDeathWeapon",
                DamageMultiplier = 1,
                ReportValues = { ReportedDamageMultiplier = "DamageMultiplier" }
            }
        )
    end
})
