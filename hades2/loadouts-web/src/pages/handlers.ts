import { type WData } from '../components/WeaponList.astro';
import { type BoonProps } from '../components/BoonItems.astro';

export type LoadoutData = {
    keepsake: string;
    weapon: WData[number]["Id"]
    traits: { "id": BoonProps["Id"], "rarity": BoonProps["Rarities"][number] }[];
}

const finalData: LoadoutData = {
    weapon: "",
    traits: [],
    keepsake: ""
}

// Weapon logic
function onWeaponSelect(weapon: WData[number]["Id"]) {
    finalData.weapon = weapon
}

const weaponEls = document.querySelectorAll('[data-weapon-item]');

weaponEls.forEach((weaponEl) => {
    const weaponElVal = weaponEl.getAttribute('data-weapon-item') as WData[number]["Id"]
    weaponEl.addEventListener('click', () => {
        const isActive =weaponEl.classList.contains('active') 

        // Reset classes
        weaponEls.forEach((el) => el.classList.remove('active'))

        if (isActive) {
            weaponEl.classList.remove("active")
            onWeaponSelect("")
            return;
        }

        weaponEl.classList.add("active")
        onWeaponSelect(weaponElVal)
    });
});

// Boon logic
function onBoonSelect(boonId: BoonProps["Id"], rarity?: BoonProps["Rarities"][number]) {
    const alreadyAddedIdx = finalData.traits.findIndex(({ id }) => id === boonId)
    const itemEl = document.querySelector(`[data-boon-item=${boonId}]`)

    if (alreadyAddedIdx > -1 && !rarity) {
        finalData.traits.splice(alreadyAddedIdx, 1)
        itemEl?.classList.remove('active')
    } else if (alreadyAddedIdx > -1 && rarity) {
        finalData.traits[alreadyAddedIdx].rarity = rarity
        itemEl?.classList.add('active')
    } else {
        finalData.traits.push({
            id: boonId,
            rarity: rarity ?? 'Common'
        })
        itemEl?.classList.add('active')
    }
}

const boonEls = document.querySelectorAll('[data-boon-item]');

boonEls.forEach((boonEl) => {
    const boonElVal = boonEl.getAttribute('data-boon-item') as BoonProps["Id"]

    boonEl.addEventListener('click', () => onBoonSelect(boonElVal));
});

// Rarity logic
const rarityEls = document.querySelectorAll('[data-boon-rarity-item]');

rarityEls.forEach((rarityEl) => {
    const rarityElVal = rarityEl.getAttribute('data-boon-rarity-item') as BoonProps["Rarities"][number]

    rarityEl.addEventListener('click', (event) => {
        event.stopPropagation();

        const parentBoonEl = rarityEl.closest("[data-boon-item]")
        const parentElVal = parentBoonEl?.getAttribute('data-boon-item') as BoonProps["Id"]

        if (!parentElVal) {
            console.error("Could not find parent")
            return
        }

        const deezRarities = parentBoonEl?.querySelectorAll("[data-boon-rarity-item]")

        // Reset classes
        deezRarities?.forEach((el) => el.classList.remove('active-rarity'))
        rarityEl.classList.add("active-rarity")
        
        onBoonSelect(parentElVal, rarityElVal)
    });
});

// Save/Export logic
const saveBtn = document.getElementById('save-build')
const exportBtn = document.getElementById('export-build')

function onSave() {
    const storageData = (JSON.parse(localStorage.getItem("loadout-data") || "[]") || []) as LoadoutData[]

    storageData.push(finalData)
    localStorage.setItem("loadout-data", JSON.stringify(storageData))
}

function onExport() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(finalData));
    const dlAnchorElem = document.getElementById('download-file');
    
    dlAnchorElem?.setAttribute("href", dataStr);
    dlAnchorElem?.setAttribute("download", "loadout.json");
    dlAnchorElem?.click();
}

saveBtn?.addEventListener('click', onSave)
exportBtn?.addEventListener('click', onExport)
