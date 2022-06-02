from __future__ import annotations

import os
import sys
import random
import pathlib
import json
import argparse

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

if len(commandline.input) > 1:
    inputfiles: list[pathlib.Path] = commandline.input
else:
    inputfiles: list[pathlib.Path] = pathlib.Path.cwd().glob("./crash-*.log")

for file in inputfiles:
    all_lines: list = f.readlines()
    crash_log: str = file.read_text(encoding="utf-8", errors="ignore")
    with file.open("r", encoding="utf-8", errors="ignore") as f:
        b4_latest: str = "Buffout 4 v1.24.5"
        b4_ver: str = all_lines[1].strip()
        b4_error: str = all_lines[3].strip()

        if b4_ver.casefold() != b4_latest.casefold():
            print(f"Skipping {str(file.resolve())} because it was not generated with {b4_latest}")
            continue
    
    if commandline.json:
        outpath: pathlib.Path = pathlib.Path(str(file).replace(file.suffix, ".json"))
    else:
        outpath: pathlib.Path = pathlib.Path(str(file).replace(file.suffix, "-AUTOSCAN.txt"))

    if outpath.exists():
        print("Output file already exists, delete the output file if you want it rescanned.")
        continue
    
    datadict: dict[str, int] = {}
    """Part 1"""
    datadict["UnlimitedSurvivalMode"] = crash_log.count("UnlimitedSurvivalMode.dll")
    datadict["B4Achivements"] = crash_log.count("Achievements: true")
    datadict["B4MemoryManagement"] = crash_log.count("MemoryManager: true")
    datadict["B4LMCompat"] = crash_log.count("F4EE: false")
    datadict["LMPlugin"] = crash_log.count("f4ee.dll")
    datadict["AchivementsDLL"] = crash_log.count("achievements.dll")
    datadict["Baka"] = crash_log.count("BakaScrapHeap.dll")

    """Part 2"""
    datadict["0x0"] = crash_log.count("0x000000000000")
    datadict["Anim1"] = crash_log.count("hkbVariableBindingSet")
    datadict["Anim2"] = crash_log.count("hkbHandIkControlsModifier")
    datadict["Anim3"] = crash_log.count("hkbBehaviorGraph")
    datadict["Anim4"] = crash_log.count("hkbModifierList")
    datadict["Cathedral1"] = crash_log.count("DefaultTexture_Black")
    datadict["Cathedral2"] = crash_log.count("NiAlphaProperty")
    datadict["CBP"] = crash_log.count("cbp.dll")
    datadict["Console1"] = crash_log.count("SysWindowCompileAndRun")
    datadict["Console2"] = crash_log.count("BSResourceNiBinaryStream")
    datadict["Console3"] = crash_log.count("ConsoleLogPrinter")
    datadict["d3d11"] = crash_log.count("d3d11.dll")
    datadict["DLCBanner01"] = crash_log.count("DLCBannerDLC01.dds")
    datadict["DLCBanner05"] = crash_log.count("DLCBanner05.dds")
    datadict["flexRelease_x64"] = crash_log.count("flexRelease_x64.dll")
    datadict["Gamebryo"] = crash_log.count("GamebryoSequenceGenerator")
    datadict["LooseFileAsync"] = crash_log.count("LooseFileAsyncStream")
    datadict["LooseFileStream"] = crash_log.count("LooseFileStream")
    datadict["MCM1"] = crash_log.count("FaderData")
    datadict["MCM2"] = crash_log.count("FaderMenu")
    datadict["MCM3"] = crash_log.count("UIMessage")
    datadict["nvwgf2umx"] = crash_log.count("nvwgf2umx.dll")
    datadict["Overflow"] = crash_log.count("EXCEPTION_STACK_OVERFLOW")
    datadict["Papyrus1"] = crash_log.count("Papyrus")
    datadict["Papyrus2"] = crash_log.count("VirtualMachine")
    datadict["Particle"] = crash_log.count("ParticleSystem")
    datadict["Pathing1"] = crash_log.count("PathingCell")
    datadict["Pathing2"] = crash_log.count("BSPathBuilder")
    datadict["Pathing3"] = crash_log.count("PathManagerServer")
    datadict["Plugin1"] = crash_log.count("ObjectBindPolicy")
    datadict["Plugin2"] = crash_log.count("BSMemStorage")
    datadict["Plugin3"] = crash_log.count("DataFileHandleReaderWriter")
    datadict["Power1"] = crash_log.count("GridAdjacencyMapNode")
    datadict["Power2"] = crash_log.count("PowerUtils")
    datadict["skeleton"] = crash_log.count("skeleton.nif")
    datadict["tbbmalloc"] = crash_log.count("tbbmalloc.dll")
    datadict["Texture1"] = crash_log.count("Create2DTexture")
    datadict["Texture2"] = crash_log.count("DefaultTexture")
    datadict["X3DAudio1_7"] = crash_log.count("X3DAudio1_7.dll")
    datadict["XAudio2_7"] = crash_log.count("XAudio2_7.dll")

    """Part 3"""
    datadict["LoadOrder"] = crash_log.count("[00]")
    datadict["Unofficial"] = crash_log.count("Unofficial")
    datadict["CHW"] = crash_log.count("ClassicHolsteredWeapons")
    datadict["UniquePlayer"] = crash_log.count("UniquePlayer.esp")
    datadict["BodyNIF"] = crash_log.count("Body.nif")
    datadict["HighHeels"] = crash_log.count("HHS.dll")
    datadict["FallSouls"] = crash_log.count("FallSouls.dll")
    datadict["F4SE"] = crash_log.count("f4se_1_10_163.dll")


    if not commandline.json:

        with outpath.open("a", encoding="utf-8", errors="ignore") as w:
            w.write(f"""{file.name}
This crash log was automatically scanned.
VER Ion-1.0 | MIGHT CONTAIN FALSE POSITIVES.
===================================================="""
                    )
            """Config File Checks"""
            if (datadict["B4Achievements"] and datadict["AchivementsDLL"] >= 1) or (datadict["B4Achivements"] and datadict["UnlimitedSurvivalMode"] >= 1):
                w.write("""Achievements Mod and/or Unlimited Survival Mode is installed, but Achievements parameter is set to TRUE"
 Open Buffout4.toml and change Achievements parameter to FALSE, this prevents conflicts with Buffout 4.
 -----""")
            else:
                w.write("""Achievements parameter is correctly configured.
-----""")
            if datadict["B4MemoryManagement"] and datadict["Baka"] >= 1:
                w.write("""Baka ScrapHeap is installed, but MemoryManager parameter is set to TRUE
Open Buffout4.toml and change MemoryManager parameter to FALSE, this prevents conflicts with Buffout 4.
You should also open BakaScrapHeap.toml with a text editor and change ScrapHeapMult parameter to 4.
-----""")
            else:
                w.write("""Memory Manager parameter is correctly configured.
-----""")
            if datadict["B4LMCompat"] and datadict["LMPlugin"] >= 1:
                w.write("""Looks Menu is installed, but F4EE parameter under [Compatibility] is set to FALSE"
Open Buffout4.toml and change F4EE parameter to TRUE, this prevents bugs and crashes from Looks Menu.)
-----""")
            else:
                w.write("""Looks Menu (F4EE) parameter is correctly configured."
-----""")

            """It's a Trap!!! Part 1 (Known Crash Messages)"""
            ItsATrap1 = False

            if datadict["Overflow"] >= 1:
                w.write("""Checking for Stack Overflow Crash..........CULPRIT FOUND!
> Priority Level: [4]""")
                ItsATrap1 = True
            else:
                w.write("Checking for Stack Overflow Crash..........All Clear")

            if datadict["nvwgf2umx"] >= 3:
                w.write(f'''Checking for Nvidia Driver Crash..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of nvwgf2umx.dll : {datadict["nvgf2umx"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Nvidia Driver Crash..........All Clear")

            if datadict["flexRelease_x64"] > 2:
                w.write(f'''Checking for Weapon Debris Crash..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of flexRelease_x64.dll : {datadict["flexRelease_x64"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Weapon Debris Crash..........All Clear")

            if datadict["d3d11"] >= 3:
                w.write(f'''Checking for Render Driver Crash..........CULPRIT FOUND!
> Priority Level: [4] | Detected number of d3d11.dll : {datadict["d3d11"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Render Driver Crash..........All Clear")

            if datadict["X3DAudio1_7"] or datadict["XAudio2_7"] >= 2:
                w.write(f'''Checking for Audio Driver Crash..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of X3DAudio1_7.dll | XAudio2_7.dll : {datadict["X3DAudio1_7"]} | {datadict["XAudio2_7"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Audio Driver Crash..........All Clear")

            if datadict["CBP"] >= 3 or datadict["skeleton"] >= 1:
                w.write(f'''Checking for Body Physics Crash..........CULPRIT FOUND!
> Priority Level: [4] | Detected number of cbp.dll | skeleton.nif : {datadict["CBP"]} | {datadict["skeleton"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Body Physics Crash..........All Clear")

            if datadict["DLCBanner05"] >= 1:
                w.write(f'''Checking for Invalidation Crash..........CULPRIT FOUND!
                    > Priority Level: [5] | Detected number of DLCBanner05.dds : {datadict["DLCBanner05"]}''')
                ItsATrap1 = True
            else:
                w.write("Checking for Invalidation Crash..........All Clear")

            if datadict["Power1"] or datadict["Power2"] >= 1:
                w.write(f"""Checking for Grid Scrap Crash..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of GridAdjacencyMapNode | PowerUtils : {datadict["Power1"]} | {datadict["Power2"]}""")
                ItsATrap1 = True
            else:
                w.write("Checking for Grid Scrap Crash..........All Clear")

            if datadict["Gamebryo"] >= 1:
                w.write(f"""Checking for Load Order Crash..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of GamebryoSequenceGenerator : {datadict["Gamebryo"]}""")
                ItsATrap1 = True
            else:
                w.write("Checking for Load Order Crash..........All Clear")

            if datadict["DLCBanner01"] >= 1:
                w.write(f"""Checking for DLCBannerDLC01.dds..........CULPRIT FOUND!
> Priority Level: [5] | Detected number of DLCBannerDLC01.dds : {datadict["DLCBanner01"]}
PLEASE POST THE ORIGINAL FULL CRASH LOG FILE
IN THE COMMENTS SECTION AT ONE OF THESE SITES:
https://www.nexusmods.com/fallout4/articles/3115
https://www.nexusmods.com/fallout4/mods/56255"""
                        )
                ItsATrap1 = True
            else:
                w.write("Checking for DLCBannerDLC01.dds..........All Clear")

            if datadict["0x0"]:
                w.write(f"""Checking for 0x0 (Zero Crash)..........CULPRIT FOUND!
> Priority Level: [3] | Detected number of 0x000000000000 : {datadict['0x0']}
PLEASE POST THE ORIGINAL FULL CRASH LOG FILE
IN THE COMMENTS SECTION AT ONE OF THESE SITES:
https://www.nexusmods.com/fallout4/articles/3115
https://www.nexusmods.com/fallout4/mods/56255""")
                ItsATrap1 = True
            else:
                w.write("Checking for 0x0 (Zero Crash)..........All Clear")

            if datadict["Cathedral1"] or datadict["Cathedral2"] >= 1:
                w.write(f"""Checking for CAO Crash..........CULPRIT FOUND!
> Priority Level: [3] | Detected number of DefaultTexture_Black | NiAlphaProperty : {datadict['Cathedral1']} | {datadict['Cathedral2']}""")
                ItsATrap1 = True
            else:
                w.write("Checking for CAO Crash..........All Clear")

            if datadict["MCM1"] or datadict["MCM2"] or datadict["MCM3"] >= 1:
                w.write(f"""Checking for MCM Crash..........CULPRIT FOUND!
> Priority Level: [3] | Detected number of FaderData | FaderMenu | UIMessage : {datadict['MCM1']} | {datadict['MCM2']} | {datadict['MCM3']}""")
                ItsATrap1 = True
            else:
                w.write("Checking for MCM Crash..........All Clear")

            if datadict["tbbmalloc"] >= 2:
                w.write(f"""Checking for Generic Crash..........CULPRIT FOUND!
> Priority Level: [2] | Detected number of tbbmalloc.dll : {datadict['tbbmalloc']}""")
                ItsATrap1 = True
            elif datadict["tbbmalloc"] == 0:
                w.write("""Checking for Generic Crash..........DLL MISSING?
Autoscan cannot find tbbmalloc.dll! Make sure that TBB Redists are installed!
Get them from Buffout 4: https://www.nexusmods.com/fallout4/mods/47359""")
                ItsATrap1 = True
            else:
                w.write("Checking for Generic Crash..........All Clear")

            if datadict["Papyrus1"] or datadict["Papyrus2"] == 1:
                w.write(f"""Checking for Papyrus Crash..........POSSIBLE CULPRIT?
> Priority Level: [2] | Detected number of Papyrus | VirtualMachine : {datadict['Papyrus1']} | {datadict['Papyrus2']}""")
                ItsATrap1 = True
            elif datadict["Papyrus1"] or datadict["Papyrus2"] >= 2:
                w.write(f"""Checking for Papyrus Crash..........CULPRIT FOUND!
> Priority Level: [3] | Detected number of Papyrus | VirtualMachine : {datadict["Papyrus1"]} | {datadict["Papyrus2"]}""")
                ItsATrap1 = True
            else:
                w.write("Checking for Papyrus Crash..........All Clear")

            if datadict["LooseFileAsync"] >= 1:
                w.write(f"""Checking for BA2 Limit Crash..............CULPRIT FOUND!
> Priority Level: [5] | Detected number of LooseFileAsyncStream : {datadict['LooseFileAsync']}""")
                ItsATrap1 = True
            else:
                w.write("Checking for BA2 Limit Crash..............All Clear")

            if datadict["Pathing1"] or datadict["Pathing2"] or datadict["Pathing3"] >= 1:
                w.write(f"""Checking for NPC Pathing Crash............CULPRIT FOUND!
> Priority Level: [3] | Detected number of PathingCell | BSPathBuilder | PathManagerServer : {datadict["Pathing1"]} | {datadict["Pathing2"]} | {datadict["Pathing3"]}""")
                ItsATrap1 = True
            else:
                w.write("Checking for NPC Pathing Crash............All Clear")
