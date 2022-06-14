from __future__ import annotations

import os
import sys
import random
import pathlib
import argparse

from dataclasses import dataclass, asdict, InitVar
from tkinter.tix import Tree

random_hints: dict[int, str] = {1: "Random Hint: [Ctrl] + [F] is a handy-dandy key combination. You should use it more often. Please.",
                                2: "Random Hint: When necessary, make sure that crashes are consistent or repeatable, since in rare cases they aren't.",
                                3: "Random Hint: 20% of all crashes are caused by Classic Holstered Weapons mod. 80% of all statistics are made up.",
                                4: "Random Hint: No, I do not know why your game froze instead of crashed. But I know someone who might know: Google.",
                                5: "Random Hint: When posting crash logs, it's helpful that you mention the last thing were doing before the crash happened.",
                                6: "Random Hint: Have a crash log where Autoscanner couldn't find anything? Feel free to send it to me.",
                                7: "Random Hint: Patrolling the Buffout 4 Nexus Page almost makes you wish this joke was more overused.",
                                8: "Random Hint: Make sure to revisit both the Buffout 4 crash article and Auto-Scanner Nexus page from time to time for updates."}

print("Hello World! | Crash Log Auto-Scanner | Version 2.00 | Fallout 4")
print("PERFORMING SCAN..........................................................")

which_hint = random_hints[random.randrange(1, 8)]

parser = argparse.ArguementParser(
    description="Parser script for Buffout4 Crash Logs"
)
parser.add_argument(
    '--inputfile',
    '-i',
    dest="input",
    nargs="?",
    type=pathlib.Path,
    action="append",
    help="Specify a specific file to parse (optional), use multiple times for multiple files, will scan all unscanned log files in current directory otherwise."
)

commandline: argparse.Namespace = parser.parse_args()
b4_latest: str = "Buffout 4 v1.26.2"

"""Using Data Classes instead of variables"""
@dataclass
class Counts:
    unlimitedsurvivalmode: int
    b4achievements: int
    b4memorymanagement: int
    b4looksmenucompat: int
    looksmenuplugin: int
    achievementsdll: int
    baka: int
    zeroxzero: int
    anim1: int
    anim2: int
    anim3: int
    anim4: int
    cathedrial1: int
    cathedrial2: int
    cbpdll: int
    console1: int
    console2: int
    console3: int
    d3d11: int
    dlcbanner01: int
    dlcbanner05: int
    flexrelease_x64: int
    gamebryo: int
    loosefileasync: int
    loosefilestream: int
    mcm1: int
    mcm2: int
    mcm3: int
    nvwgf2umx: int
    overflow: int
    papyrus1: int
    papyrus2: int
    particle: int
    pathing1: int
    pathing2: int
    pathing3: int
    plugin1: int
    plugin2: int
    plugin3: int
    power1: int
    power2: int
    skeleton: int
    texture1: int
    texture2: int
    x3daudio1_7: int
    xaudio2_7: int
    loadorder: int
    unofficialpatch: int
    classicholsteredweapons: int
    uniqueplayer: int
    bodynif: int
    highheels: int
    fallsouls: int
    f4se: int


@dataclass
class Data:
    counts: Counts
    lines: list[str]
    log: str
    achievementsconfig: bool
    memorymanagement: bool
    looksmenucompat: bool
    overflow: bool
    nvidiadriver: bool
    weapondebris: bool
    renderdriver: bool
    audiodriver: bool
    bodyphysics: bool
    invalidation: bool
    gridscrap: bool
    loadorder: bool
    dlcbanner01: bool
    zerocrash: bool
    cao_crash: bool
    mcm_crash: bool
    tbbmalloc_missing: bool
    generic_crash: bool
    papyrus: str | bool
    archivelimit: bool
    pathing: bool
    objectmodel: bool
    pluginlimit: bool
    consolecommand: bool
    particles: bool
    weapon_animations: bool
    corrupted_texture: bool
    no_plugin_list: bool
    no_unofficial_patch: bool
    detectedplugins: list[str]
    detectedformids: list[str]
    allplugins: list[str]
    onlyids: list[str]
    logfile: InitVar[pathlib.Path] = None
    """"""
    def __post_init__(self):
        self.counts: Counts = Counts()
        with self.file.open("r", encoding="utf-8", errors="ignore") as crash_log:
            """Part 1"""
            self.counts.unlimitedsurvivalmode = crash_log.count("UnlimitedSurvivalMode.dll")
            self.counts.b4achievements = crash_log.count("Achievements: true")
            self.counts.b4memorymanagement = crash_log.count("MemoryManager: true")
            self.counts.b4looksmenucompat = crash_log.count("F4EE: false")
            self.counts.looksmenuplugin = crash_log.count("f4ee.dll")
            self.counts.achievementsdll = crash_log.count("achievements.dll")
            self.counts.baka = crash_log.count("BakaScrapHeap.dll")

            """Part 2"""
            self.counts.zeroxzero = crash_log.count("0x000000000000")
            self.counts.anim1 = crash_log.count("hkbVariableBindingSet")
            self.counts.anim2 = crash_log.count("hkbHandIkControlsModifier")
            self.counts.anim3 = crash_log.count("hkbBehaviorGraph")
            self.counts.anim4 = crash_log.count("hkbModifierList")
            self.counts.cathedrial1 = crash_log.count("DefaultTexture_Black")
            self.counts.cathedrial2 = crash_log.count("NiAlphaProperty")
            self.counts.cbpdll = crash_log.count("cbp.dll")
            self.counts.console1 = crash_log.count("SysWindowCompileAndRun")
            self.counts.console2 = crash_log.count("BSResourceNiBinaryStream")
            self.counts.console3 = crash_log.count("ConsoleLogPrinter")
            self.counts.d3d11 = crash_log.count("d3d11.dll")
            self.counts.dlcbanner01 = crash_log.count("DLCBannerDLC01.dds")
            self.counts.dlcbanner05 = crash_log.count("DLCBanner05.dds")
            self.counts.flexrelease_x64 = crash_log.count("flexRelease_x64.dll")
            self.counts.gamebryo = crash_log.count("GamebryoSequenceGenerator")
            self.counts.loosefileasync = crash_log.count("LooseFileAsyncStream")
            self.counts.loosefilestream = crash_log.count("LooseFileStream")
            self.counts.mcm1 = crash_log.count("FaderData")
            self.counts.mcm2 = crash_log.count("FaderMenu")
            self.counts.mcm3 = crash_log.count("UIMessage")
            self.counts.nvwgf2umx = crash_log.count("nvwgf2umx.dll")
            self.counts.overflow = crash_log.count("EXCEPTION_STACK_OVERFLOW")
            self.counts.papyrus1 = crash_log.count("Papyrus")
            self.counts.papyrus2 = crash_log.count("VirtualMachine")
            self.counts.particle = crash_log.count("ParticleSystem")
            self.counts.pathing1 = crash_log.count("PathingCell")
            self.counts.pathing2 = crash_log.count("BSPathBuilder")
            self.counts.pathing3 = crash_log.count("PathManagerServer")
            self.counts.plugin1 = crash_log.count("ObjectBindPolicy")
            self.counts.plugin2 = crash_log.count("BSMemStorage")
            self.counts.plugin3 = crash_log.count("DataFileHandleReaderWriter")
            self.counts.power1 = crash_log.count("GridAdjacencyMapNode")
            self.counts.power2 = crash_log.count("PowerUtils")
            self.counts.skeleton = crash_log.count("skeleton.nif")
            self.counts.texture1 = crash_log.count("Create2DTexture")
            self.counts.texture2 = crash_log.count("DefaultTexture")
            self.counts.x3daudio1_7 = crash_log.count("X3DAudio1_7.dll")
            self.counts.xaudio2_7 = crash_log.count("XAudio2_7.dll")

            """Part 3"""
            self.counts.loadorder = crash_log.count("[00]")
            self.counts.unofficialpatch = crash_log.count("Unofficial")
            self.counts.classicholsteredweapons = crash_log.count("ClassicHolsteredWeapons")
            self.counts.uniqueplayer = crash_log.count("UniquePlayer.esp")
            self.counts.bodynif = crash_log.count("Body.nif")
            self.counts.highheels = crash_log.count("HHS.dll")
            self.counts.fallsouls = crash_log.count("FallSouls.dll")
            self.counts.f4se = crash_log.count("f4se_1_10_163.dll")

            self.lines = crash_log.readlines()
        
        self.log = file.read_text()

    def is_bad_mod(self, line: str, modname: str) -> bool:
        if "FE:" in line and modname in line:
            return True
        elif "File:" not in line and modname in line:
            return True
        else:
            return False

    def write_bad_mod(self, line: str, modshortname: str, modname: str) -> str:
        if "FE:" in line and modshortname in line:
            return f"FOUND {line[0:9]} {modname.capitalize()}!"
        elif "File:" not in line and modshortname in line:
            return f"FOUND {line[0:5]} {modname.capitalize()}!"
    
    def write_bad_mod_opc(self, line: str, modname: str) -> str:
        if "FE:" in line and modname in line:
            return f"FOUND {line[0:9]} {modname}!"
        elif "File:" not in line and modname in line:
            return f"FOUND {line[0:5]} {modname}!"
        

if len(commandline.input) >= 1:
    inputfiles: list[pathlib.Path] = commandline.input
else:
    inputfiles: list[pathlib.Path] = pathlib.Path.cwd().glob("./crash-*.log")

for file in inputfiles:
    data = Data(logfile=file)
    if not data.counts.unofficialpatch and not data.counts.loadorder:
        print("Could not load the plugin list for this log file, skipping this file.")
        continue
    b4_ver: str = data.lines[1].strip()
    b4_error: str = data.lines[3].strip()

    if b4_ver.casefold() != b4_latest.casefold():
        print(f"This crashdump was generated with an older version of Buffout 4: {b4_ver}.")
        print(f"This script is designed to scan crashdumps generated by: {b4_latest}")
        print("Please go to https://www.nexusmods.com/fallout4/mods/47359 to get the latest version and then rescan the file.")
        continue

    outpath: pathlib.Path = file.with_suffix("-AUTOSCAN.txt")

    if outpath.exists() and outpath.stat().st_size > 0:
        print("The output file for this crashdump already exists and is not empty, delete the existing file if you want this log to be scanned.")
        continue

    with file.open("a", encoding="utf-8", errors="ignore") as w:
        w.write("This crash log was automatically scanned.")
        w.write("VER 1.0-Ion Beta | MIGHT CONTAIN FALSE POSITIVES.")
        w.write("====================================================")
        w.write(f"Main Error: {b4_error}")
        w.write("====================================================")
        
        w.write("====================================================")
        w.write("CHECKING IF BUFFOUT4.TOML PARAMETERS ARE CORRECT...")
        w.write("====================================================")

        if (data.counts.achievementsdll and data.counts.b4achievements) or (data.counts.b4achievements and data.counts.unlimitedsurvivalmode):
            w.write("Achievements Mod and/or Unlimited Survival Mode is installed, but Achievements parameter is set to TRUE")
            w.write("Open Buffout4.toml and change Achievements parameter to FALSE, this prevents conflicts with Buffout 4.")
            w.write("-----")
        else:
            w.write("Achievements parameter is correctly configured.")
            w.write("-----")
        
        if data.counts.b4memorymanagement and data.counts.baka:
            w.write("Baka ScrapHeap is installed, but MemoryManager parameter is set to TRUE")
            w.write("Open Buffout4.toml and change MemoryManager parameter to FALSE, this prevents conflicts with Buffout 4.")
            w.write("You should also open BakaScrapHeap.toml with a text editor and change ScrapHeapMult parameter to 4.")
            w.write("-----")
        else:
            w.write("Memory Manager parameter is correctly configured.")
            w.write("-----")
        
        if data.counts.looksmenuplugin and data.counts.b4looksmenucompat:
            w.write("Looks Menu is installed, but F4EE parameter under [Compatibility] is set to FALSE")
            w.write("Open Buffout4.toml and change F4EE parameter to TRUE, this prevents bugs and crashes from Looks Menu.")
            w.write("-----")
        else:
            w.write("Looks Menu (F4EE) parameter is correctly configured.")
            w.write("-----")
        
        w.write("====================================================")
        w.write("CHECKING IF LOG MATCHES ANY KNOWN CRASH MESSAGES...")
        w.write("====================================================")

        ItsATrap1: bool = False
        if data.counts.overflow:
            w.write("Checking for Stack Overflow Crash.........CULPRIT FOUND!")
            w.write("> Priority Level: [4]")
            ItsATrap1 = True
        else:
            w.write("Checking for Stack Overflow Crash.........All Clear")
        
        if data.counts.nvwgf2umx >= 3:
            w.write("Checking for Nvidia Driver Crash..........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of nvwgf2umx.dll : {data.counts.nvwgf2umx}")
            ItsATrap1 = True
        else:
            w.write("Checking for Nvidia Driver Crash..........All Clear")

        if data.counts.flexrelease_x64 >= 2:
            w.write("Checking for Weapon Debris Crash..........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of flexRelease_x64.dll : {data.counts.flexrelease_x64}")
            ItsATrap1 = True
        else:
            w.write("Checking for Weapon Debris Crash..........All Clear")
        
        if data.counts.d3d11 >= 3:
            w.write("Checking for Render Driver Crash..........CULPRIT FOUND!")
            w.write(f"> Priority Level: [4] | Detected number of d3d11.dll : {data.counts.d3d11}")
            ItsATrap1 = True
        else:
            w.write("Checking for Render Driver Crash..........All Clear")

        if data.counts.x3daudio1_7 >= 2 or data.counts.xaudio2_7 >= 2:
            w.write("Checking for Audio Driver Crash...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of X3DAudio1_7.dll | XAudio2_7.dll: {data.counts.x3daudio1_7} | {data.counts.xaudio2_7}")
            ItsATrap1 = True
        else:
            w.write("Checking for Audio Driver Crash...........All Clear")
        
        if data.counts.cbpdll >= 3 or data.counts.skeleton:
            w.write("Checking for Body Physics Crash...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [4] | Detected number of cbp.dll | skeleton.nif : {data.counts.cbpdll} | {data.counts.skeleton}")
            ItsATrap1 = True
        else:
            w.write("Checking for Body Physics Crash...........All Clear")
        
        if data.counts.dlcbanner05:
            w.write("Checking for Invalidation Crash...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of DLCBanner05.dds : {data.counts.dlcbanner05}")
            ItsATrap1 = True
        else:
            w.write("Checking for Invalidation Crash...........All Clear")
        
        if data.counts.power1 or data.counts.power2:
            w.write("Checking for Grid Scrap Crash.............CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of GridAdjacencyMapNode | PowerUtils : {data.counts.power1} | {data.counts.power2}")
            ItsATrap1 = True
        else:
            w.write("Checking for Grid Scrap Crash.............All Clear")
        
        if data.counts.gamebryo:
            w.write("Checking for Load Order Crash.............CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of GamebryoSequenceGenerator : {data.counts.gamebryo}")
            ItsATrap1 = True
        else:
            w.write("Checking for Load Order Crash.............All Clear")

        if data.counts.dlcbanner01:
            w.write("Checking for DLCBannerDLC01.dds...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of DLCBannerDLC01.dds : {data.counts.dlcbanner01}")
            w.write("PLEASE POST THE ORIGINAL FULL CRASH LOG FILE")
            w.write("IN THE COMMENTS SECTION AT ONE OF THESE SITES:")
            w.write("https://www.nexusmods.com/fallout4/articles/3115")
            w.write("https://www.nexusmods.com/fallout4/mods/56255")
            ItsATrap1 = True
        else:
            w.write("Checking for DLCBannerDLC01.dds...........All Clear")

        if data.counts.zeroxzero:
            w.write("Checking for 0x0 (Zero Crash).............CULPRIT FOUND!")
            w.write(f"> Priority Level: [3] | Detected number of 0x000000000000 : {data.counts.zeroxzero}")
            print("PLEASE POST THE ORIGINAL FULL CRASH LOG FILE")
            print("IN THE COMMENTS SECTION AT ONE OF THESE SITES:")
            print("https://www.nexusmods.com/fallout4/articles/3115")
            print("https://www.nexusmods.com/fallout4/mods/56255")
            ItsATrap1 = True
        else:
            w.write("Checking for 0x0 (Zero Crash).............All Clear")
        
        if data.counts.cathedrial1 or data.counts.cathedrial2:
            w.write("Checking for CAO Crash....................CULPRIT FOUND!")
            w.write(f"> Priority Level: [3] | Detected number of DefaultTexture_Black | NiAlphaProperty : {data.counts.cathedrial1} | {data.counts.cathedrial2}")
            ItsATrap1 = True
        else:
            w.write("Checking for CAO Crash....................All Clear")

        if data.counts.mcm1 or data.counts.mcm2 or data.counts.mcm3:
            w.write("Checking for MCM Crash....................CULPRIT FOUND!")
            w.write(f"> Priority Level: [3] | Detected number of FaderData | FaderMenu | UIMessage : {data.counts.mcm1} | {data.counts.mcm2} | {data.counts.mcm3}")
            ItsATrap1 = True
        else:
            w.write("Checking for MCM Crash....................All Clear")
        
        w.write("Generic Crash test removed because Buffout 4 no longer uses tbbmalloc.dll")

        if data.counts.papyrus1 or data.counts.papyrus2:
            if data.counts.papyrus1 or data.counts.papyrus2 == 1:
                w.write("Checking for Papyrus Crash................POSSIBLE CULPRIT?")
                w.write(f"> Priority Level: [2] | Detected number of Papyrus | VirtualMachine : {data.counts.papyrus1} | {data.counts.papyrus2}")
            elif data.counts.papyrus1 or data.counts.papyrus2 >= 2:
                w.write("Checking for Papyrus Crash................CULPRIT FOUND!")
                w.write(f"> Priority Level: [3] | Detected number of Papyrus | VirtualMachine : {data.counts.papyrus1} | {data.counts.papyrus2}")
            ItsATrap1 = True
        else:
            w.write("Checking for Papyrus Crash................All Clear")

        if data.counts.loosefileasync:
            w.write("Checking for BA2 Limit Crash..............CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of LooseFileAsyncStream : {data.counts.loosefileasync}")
            ItsATrap1 = True
        else:
            w.write("Checking for BA2 Limit Crash..............All Clear")
        
        if data.counts.pathing1 or data.counts.pathing2 or data.counts.pathing3:
            w.write("Checking for NPC Pathing Crash............CULPRIT FOUND!")
            w.write(f"> Priority Level: [3] | Detected number of PathingCell | BSPathBuilder | PathManagerServer : {data.counts.pathing1} | {data.counts.pathing2} | {data.counts.pathing3}")
            ItsATrap1 = True
        else:
            w.write("Checking for NPC Pathing Crash............All Clear")
        
        if data.counts.loosefilestream:
            w.write("Checking for Object Model Crash...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [4] | Detected number of LooseFileStream : {data.counts.loosefilestream}")
            ItsATrap1 = True
        else:
            w.write("Checking for Object Model Crash...........All Clear")
        
        if data.counts.plugin1 or data.counts.plugin2 or data.counts.plugin3:
            w.write("Checking for Plugin Limit Crash...........CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of ObjectBindPolicy | BSMemStorage | DataFileHandleReaderWriter : {data.counts.plugin1} | {data.counts.plugin2} | {data.counts.plugin3}")
            ItsATrap1 = True
        else:
            w.write("Checking for Plugin Limit Crash...........All Clear")
        
        if data.counts.console1 or data.counts.console2 or data.counts.console3:
            w.write("Checking for Console Command Crash........CULPRIT FOUND!")
            w.write(f"> Priority Level: [1] | Detected number of SysWindowCompileAndRun | BSResourceNiBinaryStream | ConsoleLogPrinter : {data.counts.console1} | {data.counts.console2} | {data.counts.console3}")
            ItsATrap1 = True
        else:
            w.writable("Checking for Console Command Crash........All Clear")
        
        if data.counts.particle:
            w.write("Checking for Particle Effects Crash.......CULPRIT FOUND!")
            w.write(f"> Priority Level: [4] | Detected number of ParticleSystem : {data.counts.particle}")
            ItsATrap1 = True
        else:
            w.write("Checking for Particle Effects Crash.......All Clear")
        
        if data.counts.anim1 or data.counts.anim2 or data.counts.anim3 or data.counts.anim4:
            w.write("Checking for Weapon Animation Crash.......CULPRIT FOUND!")
            w.write(f"> Priority Level: [5] | Detected number of hkbVariableBindingSet | hkbHandIkControlsModifier | hkbBehaviorGraph | hkbModifierList : {data.counts.anim1} | {data.counts.anim2} | {data.counts.anim3} | {data.counts.anim4}")
            ItsATrap1 = True
        else:
            w.write("Checking for Weapon Animation Crash.......All Clear")
        
        if data.counts.texture1 or data.counts.texture2:
            w.write("Checking for Corrupted Textures Crash.....CULPRIT FOUND!")
            w.write(f"> Priority Level: [3] | Detected number of Create2DTexture | DefaultTexture : {data.counts.texture1} | {data.counts.texture2}")
            ItsATrap1 = True
        else:
            w.write("Checking for Corrupted Textures Crash.....All Clear")
        
        """Did anything trigger the trap?"""
        w.write("-----")
        if ItsATrap1:
            w.write("FOR DETAILED DESCRIPTIONS AND POSSIBLE SOLUTIONS TO ANY ABOVE DETECTED CULPRITS,")
            w.write("VISIT THE BUFFOUT 4 CRASH ARTICLE: https://www.nexusmods.com/fallout4/articles/3115")
        else:
            w.write("AUTOSCAN FOUND NO CRASH MESSAGES THAT MATCH THE CURRENT DATABASE.")
            w.write("Check below for mods that can cause frequent crashes and other problems.")

        ItsATrap2 = False

        w.write("====================================================")
        w.write("CHECKING FOR MODS THAT CAN CAUSE FREQUENT CRASHES...")
        w.write("====================================================")

        w.write("IF YOU'RE USING DYNAMIC PERFORMANCE TUNER AND/OR LOAD ACCELERATOR,")
        w.write("remove these mods completely and switch to High FPS Physics Fix!")
        w.write("Link: https://www.nexusmods.com/fallout4/mods/44798?tab=files")
        w.write("-----")

        if not data.counts.unofficialpatch and data.counts.loadorder:
            w.write("UNOFFICIAL FALLOUT 4 PATCH ISN'T INSTALLED OR AUTOSCAN CANNOT DETECT IT!")
            w.write("If you own all DLCs, make sure that the Unofficial Patch is installed.")
            w.write("Link: https://www.nexusmods.com/fallout4/mods/4598?tab=files")
            w.write("-----")
            ItsATrap2 = True

        for line in data.lines:
            if data.is_bad_mod(line, "DamageThresholdFramework.esm"):
                w.write(data.write_bad_mod(line, "DamageThresholdFramework.esm", "DAMAGE THRESHOLD FRAMEWORK"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "EPO"):
                w.write(data.write_bad_mod(line, "EPO", "EXTREME PARTICLES OVERHAUL"))
                w.write("-----")
                ItsATrap2 = True

            if data.is_bad_mod(line, "SakhalinWasteland"):
                w.write(data.write_bad_mod(line, "SakhalinWasteland", "FALLOUT SAKHALIN"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "76HUD"):
                w.write(data.write_bad_mod(line, "76HUD", "HUD76 HUD REPLACER"))
                w.write("-----")
                ItsATrap2 = True

            if data.is_bad_mod(line, "Scrap Everything"):
                w.write(data.write_bad_mod(line, "Scrap Everything", "SCRAP EVERYTHING"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "SOTS"):
                w.write(data.write_bad_mod(line, "SOTS", "SOUTH OF THE SEA"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "(STO) NO"):
                w.write(data.write_bad_mod(line, "(STO) NO", "STALKER TEXTURE OVERHAUL"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "TacticalReload.esm"):
                w.write(data.write_bad_mod(line, "TacticalReload.esm", "TACTICAL RELOAD"))
                w.write("-----")
                ItsATrap2 = True

            if data.is_bad_mod(line, "TacticalTablet.esp"):
                w.write(data.write_bad_mod(line, "TacticalTablet.esp", "TACTICAL TABLET"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "True Nights"):
                w.write(data.write_bad_mod(line, "True Nights", "TRUE NIGHTS"))
                w.write("-----")
                ItsATrap2 = True
            
            if data.is_bad_mod(line, "WeaponsFramework"):
                w.write(data.write_bad_mod(line, "WeaponsFramework", "WEAPONS FRAMEWORK BETA"))
                w.write("-----")
                ItsATrap2 = True
            
        if data.counts.classicholsteredweapons in range(1,2) and not (data.counts.uniqueplayer or data.counts.highheels or data.counts.cbpdll or data.counts.bodynif):
            w.write("FOUND CLASSIC HOLSTERED WEAPONS, BUT...")
            w.write("AUTOSCAN CANNOT ACCURATELY DETERMINE IF CHW CAUSED THIS CRASH OR NOT.")
            w.write("You should open CHW's ini file and change IsHolsterVisibleOnNPCs to 0.")
            w.write("This usually prevents most common crashes with Classic Holstered Weapons.")
            w.write("-----")
            ItsATrap2 = True
        elif data.counts.classicholsteredweapons and data.counts.uniqueplayer or data.counts.highheels or data.counts.cbpdll or data.counts.bodynif:
            w.write("FOUND CLASSIC HOLSTERED WEAPONS!")
            w.write("AUTOSCAN ALSO DETECTED ONE OR SEVERAL MODS THAT ARE GUARANTEED TO CRASH WITH CHW.")
            w.write("CHW is not compatible with mods that modify NPC/Player body, including but not limited to:")
            w.write("- ZaZ Extended Skeleton")
            w.write("- High Heels System")
            w.write("- Unique Player (Body)")
            w.write("- Some CBBE / Body Mods")
            w.write("- CBP / OCBP / 3BBB Physics")
            w.write("YOU CAN DISABLE CHW TO CONFIRM IT CAUSED THIS CRASH.")
            w.write("-----")
            ItsATrap2 = True
        elif data.counts.classicholsteredweapons >= 3:
            w.write("FOUND CLASSIC HOLSTERED WEAPONS!")
            w.write("AUTOSCAN IS PRETTY CERTAIN THAT CHW CAUSED THIS CRASH!")
            w.write("You should disable CHW to further confirm this.")
            w.write("-----")
            ItsATrap2 = True
        
        if ItsATrap2:
            w.write("CAUTION: ANY ABOVE DETECTED MODS HAVE A MUCH HIGHER CHANCE TO CRASH YOUR GAME!")
            w.write("You can disable any/all of them temporarily to confirm they caused this crash.")
            w.write("-----")
        elif not ItsATrap2:
            w.write("AUTOSCAN FOUND NO PROBLEMATIC MODS THAT MATCH THE CURRENT DATABASE FOR THIS LOG.")
            w.write("THAT DOESN'T MEAN THERE AREN'T ANY! HINT: RUN THE PLUGIN CHECKER IN WRYE BASH!")
            w.write("-----")

        ItsATrap3 = False
        
        for line in data.lines:
            if data.is_bad_mod(line, "ArmorKeywords.esm"):
                w.write(data.write_bad_mod(line, "ArmorKeywords.esm", "ARMOR AND WEAPON KEYWORDS"))
                w.write("If you don't rely on AWKCR, you should switch to Equipment and Crafting Overhaul")
                w.write("Better Alternative: https://www.nexusmods.com/fallout4/mods/55503?tab=files")
                w.write("-----")
                ItsATrap3 = True

            if data.is_bad_mod(line, "BTInteriors_Project"):
                w.write(data.write_bad_mod(line, "BTInteriors_Project", "BEANTOWN INTERIORS PROJECT"))
                w.write("Usually causes fps drops, stuttering, crashing and culling issues in multiple locations.")
                w.write("Recommended Patch: https://www.nexusmods.com/fallout4/mods/53894?tab=files")
                w.write("-----")
                ItsATrap3 = True

            if data.is_bad_mod(line, "D.E.C.A.Y"):
                w.write(data.write_bad_mod(line, "D.E.C.A.Y", "DECAY BETTER GHOULS"))
                w.write("You have to unpack / repack the D.E.C.A.Y - Main.ba2 archive by removing the Sound folder.")
                w.write("You can also install the main file from link below, it contains a patched DECAY plugin.")
                w.write("Recommended Patch: https://www.nexusmods.com/fallout4/mods/48637?tab=files")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "M8r_Item_Tags"):
                w.write(data.write_bad_mod(line, "M8r_Item_Tags", "FallUI Item Sorter"))
                w.write("This is a premade item tagging / sorting patch that will crash or conflict in all kinds of situations.")
                w.write("I strongly recommend generating your own sorting patch instead. Place it last in your load order.")
                w.write("That way, you won't experience any conflicts / crashes and even modded items will be sorted.")
                w.write("Link: https://www.nexusmods.com/fallout4/mods/48826?tab=files")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "Fo4FI_FPS_fix") or data.is_bad_mod(line, "BostonFPSFix"):
                if data.is_bad_mod(line, "Fo4FI_FPS_fix"):
                    w.write(data.write_bad_mod(line, "Fo4FI_FPS_fix", "FO4FI FPS FIX"))
                elif data.is_bad_mod(line, "BostonFPSFix"):
                    w.write(data.write_bad_mod(line, "BostonFPSFix", "Boston FPS Fix"))
                w.write("This mod is severely outdated and will cause crashes even with compatibility patches.")
                w.write("Better Alternative: https://www.nexusmods.com/fallout4/mods/46403?tab=files")
                w.write("-----")
                ItsATrap3 = True

            if data.is_bad_mod(line, "FunctionalDisplays.esp"):
                w.write(data.write_bad_mod(line, "FunctionalDisplays.esp", "Functional Displays"))
                w.write("Frequently causes object model (nif) related crashes and this needs to be manually corrected.")
                w.write("Advised Fix: Open its Meshes folder and delete everything inside EXCEPT for the Functional Displays folder.")
                w.write("-----")
                ItsATrap3 = True

            if data.is_bad_mod(line, "skeletonmaleplayer") or data.is_bad_mod(line, "skeletonfemaleplayer"):
                if data.is_bad_mod(line, "skeletonmaleplayer"):
                    w.write(data.write_bad_mod(line, "skeletonmaleplayer", "Gender Specific Skeletons"))
                elif data.is_bad_mod(line, "skeletonfemaleplayer"):
                    w.write(data.write_bad_mod(line, "skeletonfemaleplayer", "Gender Specific Skeletons"))
                w.write("High chance to cause a crash when starting a new game or during intro sequence.")
                w.write("Advised Fix: Enable the mod only after leaving Vault 111. Existing saves shouldn't be affected.")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "CapsWidget"):
                w.write(data.write_bad_mod(line, "CapsWidget", "Hud Caps"))
                w.write("Often breaks the Save / Quicksave function due to poor script implementation.")
                w.write("Advised Fix: Either remove HUD Caps or try saving the game through ingame console commands.")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "LegendaryModification.esp"):
                w.write(data.write_bad_mod(line, "LegendaryModification.esp", "Legendary Modification"))
                w.write("This is an old mod that's plagued with all kinds of bugs and crashes.")
                w.write("Better Alternative: https://www.nexusmods.com/fallout4/mods/55503?tab=files")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "MoreUniques"):
                w.write(data.write_bad_mod(line, "MoreUniques", "More Uniques Expansion"))
                w.write("Causes crashes due to broken precombines and compatibility issues with other weapon mods.")
                w.write("Recommended Patch: https://www.nexusmods.com/fallout4/mods/54848?tab=files")
                w.write("-----")
                ItsATrap3 = True

            if data.is_bad_mod(line, "SKKCraftableWeaponsAmmo") and data.is_bad_mod(line, "ArmorKeywords.esm"):
                w.write(f'Found {"SKK Craft Weapons and Ammo".capitalize()} and ARMOR AND WEAPON KEYWORDS')
                w.write("Version 008 is incompatible with AWKCR and will cause crashes while saving the game.")
                w.write("Advised Fix: Use Version 007 or remove AWKCR and switch to Equipment and Crafting Overhaul.")
                w.write("-----")
                ItsATrap3 = True
            
            if data.is_bad_mod(line, "walkers"):
                w.write(data.write_bad_mod(line, "walkers", "Zombie Walkers"))
                w.write("Version 2.6.3 contains a resurrection script that will regularly crash the game.")
                w.write("Advised Fix: Use one of the 3.0 Beta versions instead. A new game might be required.")
                w.write("-----")
                ItsATrap3 = True
        
        if data.counts.fallsouls:
            w.write("FOUND FALLSOULS UNPAUSED GAME MENUS!")
            w.write("Occasionally breaks the Quests menu, can crash while changing MCM settings.")
            w.write("Advised Fix: Toggle PipboyMenu in FallSouls MCM settings or completely reinstall the mod.")
            w.write("-----")
            ItsATrap3 = True
        
        if not ItsATrap3:
            w.write("Autoscan found no problematic mods with alternatives and solutions.")
            w.write("-----")

        w.write("====================================================")
        w.write("CHECKING FOR MODS PATCHED THROUGH OPC INSTALLER...")
        w.write("====================================================")
        ItsATrap4 = False

        for line in data.lines:
            if data.is_bad_mod(line, "Beyond the Borders"):
                w.write(data.write_bad_mod_opc(line, "Beyond the Borders"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Deadly Commonwealth Expansion"):
                w.write(data.write_bad_mod_opc(line, "Deadly Commonwealth Expansion"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Dogmeat and Strong Armor"):
                w.write(data.write_bad_mod_opc(line, "Dogmeat and Strong Armor"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "DoYourDamnJobCodsworth"):
                w.write(data.write_bad_mod_opc(line, "Do Your Damn Job Codsworth"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "ConcordEXPANDED"):
                w.write(data.write_bad_mod_opc(line, "Concord Expanded"))
                ItsATrap4 = True

            if data.is_bad_mod(line, "HagenEXPANDED"):
                w.write(data.write_bad_mod_opc(line, "Fort Hagen Expanded"))
                ItsATrap4 = True

            if data.is_bad_mod(line, "GlowingSeaEXPANDED"):
                w.write(data.write_bad_mod_opc(line, "Glowing Sea Expanded"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "SalemEXPANDED"):
                w.write(data.write_bad_mod_opc(line, "Salem Expanded"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "SwampsEXPANDED"):
                w.write(data.write_bad_mod_opc(line, "Swamps Expanded"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "_hod"):
                w.write(data.write_bad_mod_opc(line, "Hearts of Darkness"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "ImmersiveBeantown"):
                w.write(data.write_bad_mod_opc(line, "Immersive Beantown Brewery"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "CovenantComplex"):
                w.write(data.write_bad_mod_opc(line, "Immersive Covenant Compound"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "GunnersPlazaInterior"):
                w.write(data.write_bad_mod_opc(line, "Immersive Gunners Plaza"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "ImmersiveHubCity"):
                w.write(data.write_bad_mod_opc(line, "Immersive Hub City"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Immersive_Lexington"):
                w.write(data.write_bad_mod_opc(line, "Immersive & Extended Lexington"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Immersive Nahant"):
                w.write(data.write_bad_mod_opc(line, "Immersive & Extended Nahant"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Immersive S Boston"):
                w.write(data.write_bad_mod_opc(line, "Immersive Military Checkpoint"))
                ItsATrap4 = True

            if data.is_bad_mod(line, "MutilatedDeadBodies"):
                w.write(data.write_bad_mod_opc(line, "Mutilated Dead Bodies"))
                ItsATrap4 = True

            if data.is_bad_mod(line, "Vault4"):
                w.write("------")
                w.write(data.write_bad_mod_opc(line, "Fourville (Vault 4)"))
                w.write("Note: I've read that some people are having trouble with the OPC version of Fourville, the residents of Fourville just can't catch a break :(")
                w.write("I will update when a new version comes out.")
                w.write("------")
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "atlanticofficesf23"):
                w.write(data.write_bad_mod_opc(line, "Lost Building of Atlantic"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Minutemen Supply Caches"):
                w.write(data.write_bad_mod_opc(line, "Minutemen Supply Caches"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "moreXplore"):
                w.write(data.write_bad_mod_opc(line, "MoreXplore"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "NEST_BUNKER_PROJECT"):
                w.write(data.write_bad_mod_opc(line, "NEST Survival Bunkers"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Raider Children"):
                w.write(data.write_bad_mod_opc(line, "Raider Children and Other Horrors"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "sectorv"):
                w.write(data.write_bad_mod_opc(line, "Sector Five - Rise and Fall"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "SettlementShelters"):
                w.write(data.write_bad_mod_opc(line, "Settlement Shelters"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "subwayrunnnerdynamiclighting"):
                w.write(data.write_bad_mod_opc(line, "Subway Runner"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "3DNPC_FO4Settler.esp"):
                w.write(data.write_bad_mod_opc(line, "Settlers of the Commonwealth"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "3DNPC_FO4.esp"):
                w.write(data.write_bad_mod_opc(line, "Tales of the Commonwealth"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "The Hollow"):
                w.write(data.write_bad_mod_opc(line, "The Hollow"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "nvvault1080"):
                w.write(data.write_bad_mod_opc(line, "Vault 1080"))
                ItsATrap4 = True

            if data.is_bad_mod(line, "Vertibird Faction Paint Schemes"):
                w.write(data.write_bad_mod_opc(line, "Vertibird Faction Paint Schemes"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "MojaveImports"):
                w.write(data.write_bad_mod_opc(line, "Wasteland Imports"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "Firelance2.5"):
                w.write(data.write_bad_mod_opc(line, "Xander's Aid"))
                ItsATrap4 = True
            
            if data.is_bad_mod(line, "zxcMicroAdditions"):
                w.write(data.write_bad_mod_opc(line, "ZXC Micro Additions"))
                ItsATrap4 = True
        if ItsATrap4:
            w.write("-----")
            w.write("FOR COMPLETE PATCH REPOSITORY THAT PREVENTS CRASHES AND FIXES PROBLEMS IN THESE AND OTHER MODS,")
            w.write("VISIT THE OPTIMIZATION PATCHES COLLECTION: https://www.nexusmods.com/fallout4/mods/54872")
            w.write("-----")
        else:
            w.write("Autoscan found no problematic mods that are already patched through OPC Installer.")
            w.write("-----")

        w.write("====================================================")
        w.write("SCANNING THE LOG FOR SPECIFIC (POSSIBLE) CUPLRITS...")
        w.write("====================================================")
        ItsATrap5 = False

        if not data.counts.f4se:
            w.write("AUTOSCAN CANNOT FIND FALLOUT 4 SCRIPT EXTENDER DLL!")
            w.write("MAKE SURE THAT F4SE IS CORRECTLY INSTALLED!")
            w.write("Link: https://f4se.silverlock.org/")
            w.write("-----")
        
        for line in data.lines:
            if len(line) >= 6 and "]" in line[4]:
                #line = line[6:]
                data.allplugins.append(line.strip())
            if len(line) >= 7 and "]" in line[5]:
                #line = line[7:]
                data.allplugins.append(line.strip())
            if len(line) >= 10 and "]" in line[8]:
                #line = line[10:]
                data.allplugins.append(line.strip())
            if len(line) >= 11 and "]" in line[9]:
                #line = line[11:]
                data.allplugins.append(line.strip())
        
        w.write("LIST OF (POSSIBLE) PLUGIN CULRIPTS:")

        for line in data.lines:
            if "File: " in line:
                line = line.replace("File: ", "")
                line = line.replace('"', '')
                data.detectedplugins.append(line.strip())
        
        data.detectedplugins = list(dict.fromkeys(data.detectedplugins)) 
        if "Fallout4.esm" in data.detectedplugins:
            data.detectedplugins.remove("Fallout4.esm")
        if "DLCCoast.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCCoast.esm")
        if "DLCNukaWorld.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCNukaWorld.esm")
        if "DLCRobot.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCRobot.esm")
        if "DLCworkshop01.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCworkshop01.esm")
        if "DLCworkshop02.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCworkshop02.esm")
        if "DLCworkshop03.esm" in data.detectedplugins:
            data.detectedplugins.remove("DLCworkshop03.esm")
        if '' in data.detectedplugins:
            data.detectedplugins.remove('')
        if "" in data.detectedplugins:
            data.detectedplugins.remove("")

        PL_strings = data.allplugins
        PL_substrings = data.detectedplugins
        PL_result = []
        
        for string in PL_strings:
            PL_matches = []
            for substring in PL_substrings:
                if substring in string:
                    PL_matches.append(string)
            if PL_matches:
                PL_result.append(PL_matches)
                w.write(f"- {' '.join(PL_matches)}")
        
        if not PL_result:
            w.write("AUTOSCAN COULDN'T FIND ANY PLUGIN CULRIPTS")
            w.write("-----")
        else:
            w.write("-----")
            w.write("These Plugins were caught by Buffout 4 and some of them might be responsible for this crash.")
            w.write("You can try disabling any listed plugins and recheck your game, though this method is unreliable.")
            w.write("-----")
        
        for line in data.lines:
            if 'Form ID: ' in line:
                line = line.replace("0x", "")
                data.detectedformids.append(line.strip())
                line = line.replace("Form ID: ", "")
                line = line[:5].strip()
                data.onlyids.append(line)

        data.detectedformids = list(dict.fromkeys(data.detectedformids))
        data.onlyids = list(dict.fromkeys(data.onlyids))
        for elem in data.detectedformids:
            w.write(elem)

        if not data.detectedformids:
            w.write("AUTOSCAN COULDN'T FIND ANY FORM ID CULRIPTS")
            w.write("-----")
        else:
            w.write("-----")
            w.write("These Form IDs were caught by Buffout 4 and some of them might be related to this crash.")
            w.write("You can try searching any listed Form IDs in FO4Edit and see if they lead to relevant records.")
            w.write("-----")

print("SCAN COMPLETE!!! IT MIGHT TAKE SEVERAL SECONDS FOR SCAN RESULTS TO APPEAR")
print("SCAN RESULTS ARE AVAILABE IN FILES NAMED crash-date-and-time-AUTOSCAN.txt")
print("===============================================================================")
print("FOR FULL LIST OF MODS THAT MAY CAUSE PROBLEMS, THEIR ALTERNATIVES AND DETAILED SOLUTIONS,")
print("VISIT THE BUFFOUT 4 CRASH ARTICLE: https://www.nexusmods.com/fallout4/articles/3115")
print("-----")
print(random_hints[random.randrange(1, 8)])
print("-----")

print("===============================================================================")
print("END OF AUTOSCAN | Author/Made By: Poet#9800 | 251221")
print("https://www.nexusmods.com/fallout4/mods/56255")

os.system("pause")