from __future__ import annotations

import os
import sys
import random
import pathlib
import json
import argparse

from dataclasses import dataclass, asdict

random_hints: dict[int, str] = {1: "Random Hint: [Ctrl] + [F] is a handy-dandy key combination. You should use it more often. Please.",
                                2: "Random Hint: When necessary, make sure that crashes are consistent or repeatable, since in rare cases they aren't.",
                                3: "Random Hint: 20% of all crashes are caused by Classic Holstered Weapons mod. 80% of all statistics are made up.",
                                4: "Random Hint: No, I do not know why your game froze instead of crashed. But I know someone who might know: Google.",
                                5: "Random Hint: When posting crash logs, it's helpful that you mention the last thing were doing before the crash happened.",
                                6: "Random Hint: Have a crash log where Autoscanner couldn't find anything? Feel free to send it to me.",
                                7: "Random Hint: Patrolling the Buffout 4 Nexus Page almost makes you wish this joke was more overused.",
                                8: "Random Hint: Make sure to revisit both the Buffout 4 crash article and Auto-Scanner Nexus page from time to time for updates."}

print(
    """Hello World! | Crash Log Auto-Scanner | Version 2.00 | Fallout 4
    PERFORMING SCAN.........................................................."""
)
which_hint = random_hints[random.randrange(1, 8)]
parser = argparse.ArguementParser(
    description="Parser script for Buffout4 Crash Logs"
)
parser.add_argument(
    '--json',
    '-j',
    action="store_true",
    dest="json",
    help="Output the results as a JSON file instead of the classic text format."
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

@dataclass
class Data:
    counts: dict[str, int] | None
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
    json_counts: list[tuple[str, int]]

    

    def __post_init__(self, file: pathlib.Path):
        self.counts: dict[str, int] = {}
        with file.open("r", encoding="utf-8", errors="ignore") as crash_log:
            """Part 1"""
            self.counts["UnlimitedSurvivalMode"] = crash_log.count("UnlimitedSurvivalMode.dll")
            self.counts["B4Achivements"] = crash_log.count("Achievements: true")
            self.counts["B4MemoryManagement"] = crash_log.count("MemoryManager: true")
            self.counts["B4LMCompat"] = crash_log.count("F4EE: false")
            self.counts["LMPlugin"] = crash_log.count("f4ee.dll")
            self.counts["AchivementsDLL"] = crash_log.count("achievements.dll")
            self.counts["Baka"] = crash_log.count("BakaScrapHeap.dll")

            """Part 2"""
            self.counts["0x0"] = crash_log.count("0x000000000000")
            self.counts["Anim1"] = crash_log.count("hkbVariableBindingSet")
            self.counts["Anim2"] = crash_log.count("hkbHandIkControlsModifier")
            self.counts["Anim3"] = crash_log.count("hkbBehaviorGraph")
            self.counts["Anim4"] = crash_log.count("hkbModifierList")
            self.counts["Cathedral1"] = crash_log.count("DefaultTexture_Black")
            self.counts["Cathedral2"] = crash_log.count("NiAlphaProperty")
            self.counts["CBP"] = crash_log.count("cbp.dll")
            self.counts["Console1"] = crash_log.count("SysWindowCompileAndRun")
            self.counts["Console2"] = crash_log.count("BSResourceNiBinaryStream")
            self.counts["Console3"] = crash_log.count("ConsoleLogPrinter")
            self.counts["d3d11"] = crash_log.count("d3d11.dll")
            self.counts["DLCBanner01"] = crash_log.count("DLCBannerDLC01.dds")
            self.counts["DLCBanner05"] = crash_log.count("DLCBanner05.dds")
            self.counts["flexRelease_x64"] = crash_log.count("flexRelease_x64.dll")
            self.counts["Gamebryo"] = crash_log.count("GamebryoSequenceGenerator")
            self.counts["LooseFileAsync"] = crash_log.count("LooseFileAsyncStream")
            self.counts["LooseFileStream"] = crash_log.count("LooseFileStream")
            self.counts["MCM1"] = crash_log.count("FaderData")
            self.counts["MCM2"] = crash_log.count("FaderMenu")
            self.counts["MCM3"] = crash_log.count("UIMessage")
            self.counts["nvwgf2umx"] = crash_log.count("nvwgf2umx.dll")
            self.counts["Overflow"] = crash_log.count("EXCEPTION_STACK_OVERFLOW")
            self.counts["Papyrus1"] = crash_log.count("Papyrus")
            self.counts["Papyrus2"] = crash_log.count("VirtualMachine")
            self.counts["Particle"] = crash_log.count("ParticleSystem")
            self.counts["Pathing1"] = crash_log.count("PathingCell")
            self.counts["Pathing2"] = crash_log.count("BSPathBuilder")
            self.counts["Pathing3"] = crash_log.count("PathManagerServer")
            self.counts["Plugin1"] = crash_log.count("ObjectBindPolicy")
            self.counts["Plugin2"] = crash_log.count("BSMemStorage")
            self.counts["Plugin3"] = crash_log.count("DataFileHandleReaderWriter")
            self.counts["Power1"] = crash_log.count("GridAdjacencyMapNode")
            self.counts["Power2"] = crash_log.count("PowerUtils")
            self.counts["skeleton"] = crash_log.count("skeleton.nif")
            self.counts["tbbmalloc"] = crash_log.count("tbbmalloc.dll")
            self.counts["Texture1"] = crash_log.count("Create2DTexture")
            self.counts["Texture2"] = crash_log.count("DefaultTexture")
            self.counts["X3DAudio1_7"] = crash_log.count("X3DAudio1_7.dll")
            self.counts["XAudio2_7"] = crash_log.count("XAudio2_7.dll")

            """Part 3"""
            self.counts["LoadOrder"] = crash_log.count("[00]")
            self.counts["Unofficial"] = crash_log.count("Unofficial")
            self.counts["CHW"] = crash_log.count("ClassicHolsteredWeapons")
            self.counts["UniquePlayer"] = crash_log.count("UniquePlayer.esp")
            self.counts["BodyNIF"] = crash_log.count("Body.nif")
            self.counts["HighHeels"] = crash_log.count("HHS.dll")
            self.counts["FallSouls"] = crash_log.count("FallSouls.dll")
            self.counts["F4SE"] = crash_log.count("f4se_1_10_163.dll")

            self.lines = crash_log.readlines()
        
        self.log = file.read_text()
        
        if commandline.json:
            self.json_counts = list(zip(self.counts.keys(), self.counts.values(), strict=True))
            self.counts = None
    def is_bad_mod(self, line: str, modname: str) -> bool:
        if "FE:" in line and modname in line:
            return True
        elif "File:" not in line and modname in line:
            return True
        else:
            return False
        

if len(commandline.input) >= 1:
    inputfiles: list[pathlib.Path] = commandline.input
else:
    inputfiles: list[pathlib.Path] = pathlib.Path.cwd().glob("./crash-*.log")

for file in inputfiles:
    data = Data(file)
    
    b4_latest: str = "Buffout 4 v1.24.5"
    b4_ver: str = data.lines[1].strip()
    b4_error: str = data.lines[3].strip()

    if b4_ver.casefold() != b4_latest.casefold():
        print(f"Skipping {str(file.resolve())} because it was not generated with {b4_latest}")
        continue

    if commandline.json and file.suffix:
        outpath: pathlib.Path = file.with_suffix("-AUTOSCAN.json")
    else:
        outpath: pathlib.Path = file.with_suffix("-AUTOSCAN.txt")

    if outpath.exists() and outpath.stat().st_size > 0:
        print("Output file already exists, delete the output file if you want it rescanned.")
        continue   
    
    data = Data(file)