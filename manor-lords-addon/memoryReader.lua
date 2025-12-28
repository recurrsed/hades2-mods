local ale = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 05461268] + F50] + 18] + 4D8] + 7A0] + 910] + 58] + 664")
local approval = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 0546B318] + C80] + B0] + 98] + A8] + 338] + 238] + 6DC")
local berries = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 056A3AC8] + A8] + 108] + C40] + 10] + 370] + 9F8] + 34")
local clay = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 057710D0] + 28] + B58] + 10] + 1D8] + 20] + 2F8] + 10C")
local eggs = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 056B08F8] + 10] + A8] + 108] + B28] + 10] + 678] + 64")
local firewood = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 057710D0] + 28] + B10] + 10] + 2A8] + 370] + 678] + 4")
local hides = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 056A3AC8] + A8] + 108] + B58] + 10] + 68] + 280] + 3F4")
local ironOre = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 05687270] + A8] + 108] + B58] + 10] + 68] + 280] + 49C")
local leather = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 056B08F0] + A8] + 108] + C40] + 10] + 358] + 2F8] + 4C")
local meat = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 05704850] + 510] + 68] + 108] + B20] + 10] + 2F8] + 4")
local planks = readInteger("[[[[[[ManorLords-Win64-Shipping.exe + 057948C0] + 68] + 28] + B18] + 10] + 2F8] + 1C")
local regionalWealth = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 058B4EB0] + A0] + B00] + C0] + 20] + 468] + 3B8] + 308")
local roofTiles = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 05704850] + 510] + 68] + 108] + B18] + 10] + 2F8] + 7C")
local stone = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 057710D0] + 28] + B28] + 10] + 3A8] + 30] + 678] + 34")
local timber = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 05687270] + A8] + 108] + C40] + 10] + 390] + 2F8] + 4")
local vegetables = readInteger("[[[[[[[ManorLords-Win64-Shipping.exe + 059068B0] + A8] + 108] + C40] + 10] + 330] + 678] + 1C")

local time = os.time(os.date("!*t"))

function updateData(path, content)
    local file = io.open(path, "a")
    
    if file then
        file:write(content)
        file:close()
    else
        return false
    end
end

Timer = createTimer(MainForm)
Timer.Interval(10000) -- 10s
Timer.OnTimer = function(timer)

updateData(
    'D:/Programming/manor-lords-addon/values.csv',
    'Ale,' .. ale .. ',' .. time .. '\n' ..
    'Approval,' .. approval .. ',' .. time .. '\n' ..
    'Berries,' .. berries .. ',' .. time .. '\n' ..
    'Clay,' .. clay .. ',' .. time .. '\n' ..
    'Eggs,' .. eggs .. ',' .. time .. '\n' ..
    'Firewood,' .. firewood .. ',' .. time .. '\n' ..
    'Hides,' .. hides .. ',' .. time .. '\n' ..
    'Iron Ore,' .. ironOre .. ',' .. time .. '\n' ..
    'Leather,' .. leather .. ',' .. time .. '\n' ..
    'Meat,' .. meat .. ',' .. time .. '\n' ..
    'Planks,' .. planks .. ',' .. time .. '\n' ..
    'Regional Wealth,' .. regionalWealth .. ',' .. time .. '\n' ..
    'Roof Tiles,' .. roofTiles .. ',' .. time .. '\n' ..
    'Stone,' .. stone .. ',' .. time .. '\n' ..
    'Timber,' .. timber .. ',' .. time .. '\n' ..
    'Vegetables,' .. vegetables .. ',' .. time .. '\n'
)
end