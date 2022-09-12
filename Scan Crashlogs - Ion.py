import glob
import os
import random
import string
import subprocess
import sys
import time

# > auto update pip and install packages:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
#subprocess.check_call([sys.executable, '-m','pip','install','<package>'])
# > list all installed packages:
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print("List of all installed packages:", installed_packages)
print("-----")
# import <package>

Sneaky_Tips = ["\nRandom Hint: [Ctrl] + [F] is a handy-dandy key combination. You should use it more often. Please.\n",
               "\nRandom Hint: Patrolling the Buffout 4 Nexus Page almost makes you wish this joke was more overused.\n",
               "\nRandom Hint: You have a crash log where Autoscanner couldn't find anything? Feel free to send it to me.\n",
               "\nRandom Hint: You can add comments and suggestions to the online version of 'How To Read Crash Logs' document.\n",
               "\nRandom Hint: 20% of all crashes are caused by Classic Holstered Weapons mod. 80% of all statistics are made up.\n",
               "\nRandom Hint: No, I don't know why your game froze instead of crashed. But I know someone who might know; Google.\n",
               "\nRandom Hint: When posting crash logs, it's helpful to mention the last thing were doing before the crash happened.\n",
               "\nRandom Hint: When necessary, make sure that crashes are consistent or repeatable, since in rare cases they aren't.\n",
               "\nRandom Hint: Be sure to revisit both Buffout 4 Crash Crticle and Auto-Scanner Nexus Page from time to time for updates.\n"]

# SUSSY MOVE (Move unsolved logs to special folder.)
# if not os.path.exists("CL-UNSOLVED"):
#   os.mkdir("CL-UNSOLVED")
# =================== STATISTICS LOGGING ===================
# MAIN
statL = {"scanned": 0, "incomplete": 0, "failed": 0, "veryold": 0}
# BUFFOUT SETTINGS
statB = {"Achieve": 0, "Memory": 0, "F4EE": 0, "F4SE": 0, "NoMessage": 0}
# KNOWN CRASH MESSAGES
statC = {"ActiveEffect": 0, "AnimationPhysics": 0, "Audio": 0, "BA2Limit": 0, "BGSM": 0, "BitDefender": 0, "BodyPhysics": 0, "ConsoleCommands": 0, "CorruptedTex": 0,
         "NVDriver": 0, "Null": 0, "OverFlow": 0, "Papyrus": 0, "Particles": 0, "PluginLimit": 0, "Rendering": 0, "Texture": 0, "CorruptedAudio": 0, "LOD": 0,
         "Decal": 0, "MO2Unp": 0, "VulkamMem": 0, "VulkanSet": 0, "DLL": 0, "Equip": 0, "Generic": 0, "GridScrap": 0, "NIF": 0, "NPCPathing": 0, "Overflow": 0, "BadMath": 0, "MCM": 0,
         "LoadOrder": "0", "NVDebris": 0, "NVDriver": 0, "Invalidation": 0}
# UNSOLVED CRASH MESSAGES
statU = {"Precomb": 0, "Player": 0, "Save": 0, "HUDAmmo": 0, "Patrol": 0, "Projectile": 0, "Item": 0, "Input": 0, "INI": 0}
# KNOWN CRASH CONDITIONS
statM_CHW = 0

# SteamAPI_OG = 206760 | Fallout4_OG = 65503104
# ==========================================================

print("Hello World! | Crash Log Auto-Scanner | Version 1.0-Ion (based on Poet's version 4.10) | Fallout 4")
print("CRASH LOGS MUST BE .log AND IN THE SAME FOLDER WITH THIS SCRIPT!")
print("===============================================================================")
print("You should place this script into your Documents\My Games\Fallout4\F4SE folder.")
print("(This is where Buffout 4 crash log files are generated after the game crashes.)")
print("===============================================================================")
print("CAUTION: Crash Log Auto-Scanner will probably not work correctly with Win 7 and will not work with Python 2.")
print("Unfortunately, I have no systems with Windows 7, so I can't help in case of problems.")
print("===============================================================================")
# Check 5 most likely drives to see where Documents\My Games\Fallout4 exists.
User_Path = os.getenv('HOMEPATH')
drives = list(i for i in string.ascii_uppercase[2:])
for drive in drives:
    if os.path.exists(f"{drive}:\{User_Path}\Documents\My Games\Fallout4"):
        FO4_Custom_Path = f"{drive}:\{User_Path}\Documents\My Games\Fallout4\Fallout4Custom.ini"
        FO4_INI_Path = f"{drive}:\{User_Path}\Documents\My Games\Fallout4\Fallout4.ini"

# Create/Open Fallout4Custom.ini and check Archive Invalidaton & other settings.
# DO NOT USE a+ WHEN SEARCHING STRINGS BECAUSE IT FUCKS UP STRING SEARCHING!
"""with open(FO4_Custom_Path, "r+") as FO4_Custom:
    INI_Fix = FO4_Custom.read()
    INI_Fix = INI_Fix.replace("bInvalidateOlderFiles=0", "bInvalidateOlderFiles=1")
    if not "[Archive]" in INI_Fix:
        INI_Fix += "\n[Archive]\nbInvalidateOlderFiles=1\nsResourceDataDirsFinal="
with open(FO4_Custom_Path, "w+") as FO4_Custom:
    FO4_Custom.write(INI_Fix)"""

# Find INI/File that uses game path, format its line until it matches game path.
if not os.path.exists(FO4_INI_Path):
    print("\nERROR: AUTO-SCANNER CANNOT FIND FALLOUT4.INI!")
    print("RUN THE GAME AT LEAST ONCE WITH Fallout4Launcher.exe")
    print("EXIT AFTER MAIN MENU AND RUN THE AUTO-SCANNER AGAIN!\n")
else:
    with open(FO4_INI_Path, "r+") as FO4_INI:
        INI_Read = FO4_INI.readlines()
        for line in INI_Read:
            if "sScreenShotBaseName" in line:
                INI_Game_Path = line
                INI_Path_START = INI_Game_Path.index("=") + 1
                INI_Path_END = INI_Game_Path.index("4") + 1
                Game_Path = INI_Game_Path[INI_Path_START:INI_Path_END]
            else:
                pass
    # If there is no INI/File that uses game path, prompt user to manually input.
    with open(FO4_INI_Path, "r+") as FO4_INI:
        INI_Read = FO4_INI.read()
        if not "sScreenShotBaseName" in INI_Read:
            Game_Path = input("PLEASE COPY-PASTE THE FULL DIRECTORY PATH WHERE YOUR FALLOUT 4 IS INSTALLED \n(Press ENTER to confirm. Example: C:\Steam\steamapps\common\Fallout 4) \n-> ")
            print(f"You entered: {Game_Path}")

print("\n PERFORMING SCAN... \n")
start_time = time.time()
orig_stdout = sys.stdout

logs = glob.glob("crash-*.log") + glob.glob("crash-*.log.txt")  # second is for a hypothetical edge case where a browser insists on adding a .txt extension


for file in logs:  # This if statement only exists so that I don't have to re-indent hundreds of lines of code.
    logname = str(file)[:len(str(file)) - 4]
    sys.stdout = open(f"{logname}-AUTOSCAN.md", "w", encoding='utf-8-sig', errors="ignore")
    crashlog = str(f"{logname}.log")
    print(f"{logname}.log")
    print("This crash log was automatically scanned.")
    print("VER 1.0-Ion (based on Poet's version 4.10) | MIGHT CONTAIN FALSE POSITIVES.")
    print("====================================================")

    # OPEN FILE TO CHECK INDEXES AND EVERYTHING ELSE.
    crash_version = open(crashlog, "r", errors="ignore")
    # INDEXES FOR ALL LINE ROWS ARE DEFINED HERE.
    all_lines = crash_version.readlines()
    buff_ver = str(all_lines[1].strip())
    buff_error = str(all_lines[3].strip())

    # BUFFOUT VERSION CHECK
    buff_latest = "Buffout 4 v1.26.2"
    print("Main Error:", buff_error)
    print("====================================================")
    print("Detected Buffout Version:", buff_ver.strip())
    print("Latest Buffout Version:", buff_latest.strip())

    if buff_ver.casefold() == buff_latest.casefold():
        print("You have the lastest version of Buffout 4!")
    else:
        print("REPORTED BUFFOUT VERSION DOES NOT MATCH THE BUFFOUT VERSION USED BY AUTOSCAN")
        print("UPDATE BUFFOUT 4 IF NECESSARY: https://www.nexusmods.com/fallout4/mods/47359")

    if "v1." not in buff_ver:
        statL["veryold"] += 1
        statL["scanned"] -= 1

    # ===========================================================
    # CLOSE CURRENT INDEX CHECK
    crash_version.close()
    # OPEN FILE AGAIN FOR A DIFFERENT CHECK
    crash_log = open(crashlog, "r", errors="ignore")
    # READ CONTENTS OF FILE AND CONVERT TO STRINGS
    crash_message = crash_log.read()

    # ===========================================================
    # 1.) CHECK FOR CORRECT BUFFOUT SETTINGS
    print("====================================================")
    print("CHECKING IF BUFFOUT 4 FILES/SETTINGS ARE CORRECT...")
    print("====================================================")
    counts = {}
    # Writing to TOML files in Python makes me gauge my eyes out.
    counts["Survival_Mod"] = crash_message.count("UnlimitedSurvivalMode.dll")
    counts["Achievements"] = crash_message.count("Achievements: true")
    counts["Achievementmod"] = crash_message.count("achievements.dll")
    counts["Buffout_MemoryManager"] = crash_message.count("MemoryManager: true")
    counts["Baka"] = crash_message.count("BakaScrapHeap.dll")
    counts["LooksMenuCompat"] = crash_message.count("F4EE: false")
    counts["F4EE"] = crash_message.count("f4ee.dll")

    """if F4SE_Loader.is_file() and F4SE_DLL.is_file() and F4SE_SDLL.is_file():
            print("REQUIRED: Fallout 4 Script Extender (F4SE) is correctly (manually) installed.")
            print("NOTICE: Auto-Scanner must be run by original user for correct detection.")
            print("-----")
        else:
            print("CAUTION: Auto-Scanner cannot find required Script Extender (F4SE) files inside your Fallout 4 game folder!")
            print("FIX: Extract all files inside *f4se_0_06_21* folder into your Fallout 4 game folder.")
            print("FALLOUT 4 SCRIPT EXTENDER: (Download Build 0.6.23) https://f4se.silverlock.org/")
            print("-----")
            
        if Address_Library.is_file():
            print("REQUIRED: Address Library is correctly (manually) installed.")
            print("NOTICE: Auto-Scanner must be run by original user for correct detection.")
            print("-----")
        else:
            print("CAUTION: Auto-Scanner cannot find required Adress Library file inside Fallout 4\Data\F4SE\Plugins folder!")
            print("FIX: Place the *version-1-10-163-0.bin* file manually into Fallout 4\Data\F4SE\Plugins folder.")
            print("ADDRESS LIBRARY: (Use Manual Download Option ONLY) https://www.nexusmods.com/fallout4/mods/47327?tab=files")
            print("-----")

        if Buffout_DLL.is_file() and Buffout_TOML.is_file():
            print("REQUIRED: Buffout 4 is correctly (manually) installed.")
            print("NOTICE: Auto-Scanner must be run by original user for correct detection.")
            print("-----")
        else:
            print("CAUTION: Auto-Scanner cannot find required Buffout 4 files inside Fallout 4\Data\F4SE\Plugins folder!")
            print("FIX: Place Buffout4.dll, Buffout4.toml and Buffout4_preload.txt manually into Fallout 4\Data\F4SE\Plugins folder.")
            print("BUFFOUT 4: (Use Manual Download Option ONLY) https://www.nexusmods.com/fallout4/mods/47359?tab=files")
            print("-----")

        if Preloader_XML.is_file() and Preloader_DLL.is_file():
            print('OPTIONAL: Plugin Preloader is correctly (manually) installed.')
            print('NOTICE: If you cannot run the game after installing Plugin Preloader, open xSE PluginPreloader.xml with any text editor and')
            print('CHANGE: <LoadMethod Name="ImportAddressHook"> TO <LoadMethod Name="OnThreadAttach"> OR <LoadMethod Name="OnProcessAttach">')
            print('IF THE GAME STILL REFUSES TO START, COMPLETELY REMOVE xSE PluginPreloader.xml AND IpHlpAPI.dll FROM YOUR FO4 GAME FOLDER')
            print("-----")
        else:
            print('OPTIONAL: Plugin Preloader is not (manually) installed.')
            print("NOTICE: Auto-Scanner must be run by original user for correct detection.")
            print("-----")
"""
    if (counts["Achievements"] and counts["Achievementmod"]) >= 1 or (counts["Achievementmod"] and counts["Survival_Mod"]) >= 1:
        print("CAUTION: Achievements Mod and/or Unlimited Survival Mode is installed, but Achievements parameter is set to TRUE")
        print("FIX: Open Buffout4.toml and change Achievements parameter to FALSE, this prevents conflicts with Buffout 4.")
        print("-----")
        statB["Achieve"] += 1
    else:
        print("Achievements parameter is correctly configured.")
        print("-----")

    if (counts["Buffout_MemoryManager"] and counts["Baka"]) >= 1:
        print("CAUTION: Baka ScrapHeap is installed, but MemoryManager parameter is set to TRUE")
        print("FIX: Open Buffout4.toml and change MemoryManager parameter to FALSE, this prevents conflicts with Buffout 4.")
        print("You should also open BakaScrapHeap.toml with a text editor and change the ScrapHeapMult parameter to 4.")
        print("-----")
        statB["Memory"] += 1
    else:
        print("Memory Manager parameter is correctly configured.")
        print("-----")

    if (counts["F4EE"] and counts["LooksMenuCompat"]) >= 1:
        print("CAUTION: Looks Menu is installed, but F4EE parameter under [Compatibility] is set to FALSE")
        print("FIX: Open Buffout4.toml and change F4EE parameter to TRUE, this prevents bugs and crashes from Looks Menu.")
        print("-----")
        statB["F4EE"] += 1
    else:
        print("Looks Menu (F4EE) parameter is correctly configured.")
        print("-----")

    # ===========================================================
    # 2.) CHECK FOR KNOWN CRASH MESSAGES - BUFFOUT TRAP 1
    print("====================================================")
    print("CHECKING IF LOG MATCHES ANY KNOWN CRASH MESSAGES...")
    print("====================================================")
    Buffout_Trap = 1

    # ====================== HEADER ERRORS ======================
    if ".dll" in buff_error and "tbbmalloc" not in buff_error:
        print("MAIN ERROR REPORTS A DLL WAS INVLOVED IN THIS CRASH!")
        print("-----")

    # Stack Overflow Crash
    counts["Overflow"] = crash_message.count("EXCEPTION_STACK_OVERFLOW")
    # Active Effect Crash
    counts["ActiveEffect"] = crash_message.count("0x000100000000")
    # Bad Math Crash
    counts["BadMath"] = crash_message.count("EXCEPTION_INT_DIVIDE_BY_ZERO")
    # Null Crash
    counts["Null"] = crash_message.count("0x000000000000")

    # ======================= MAIN ERRORS =======================
    # SPECIAL - Uneducated Shooter (56789)
    counts["InvalidArg"] = crash_message.count("std::invalid_argument")
    #GENERIC - DLL
    counts["KERNELBASE"] = crash_message.count("KERNELBASE.dll")
    counts["MSVCP140"] = crash_message.count("MSVCP140.dll")
    counts["MSVCR110"] = crash_message.count("MSVCR110.dll")
    # CBP Crash
    counts["CBP"] = crash_message.count("cbp.dll")
    counts["skeleton"] = crash_message.count("skeleton.nif")
    # DLL Crash
    counts["DLCBanner01"] = crash_message.count("DLCBannerDLC01.dds")
    # LOD Crash
    counts["BGSLocation"] = crash_message.count("BGSLocation")
    counts["BGSQueued"] = crash_message.count("BGSQueuedTerrainInitialLoad")
    # MCM Crash
    counts["FaderData"] = crash_message.count("FaderData")
    counts["FaderMenu"] = crash_message.count("FaderMenu")
    counts["UIMessage"] = crash_message.count("UIMessage")
    # Decal Crash
    counts["BGSDecal"] = crash_message.count("BGSDecalManager")
    counts["BSTempEffect"] = crash_message.count("BSTempEffectGeometryDecal")
    # Equip Crash
    counts["PipboyMapData"] = crash_message.count("PipboyMapData")
    # Script Crash
    counts["Papyrus"] = crash_message.count("Papyrus")
    counts["VirtualMachine"] = crash_message.count("VirtualMachine")
    # Console Crash
    counts["CompileAndRun"] = crash_message.count("SysWindowCompileAndRun")
    counts["NiBinaryStream"] = crash_message.count("BSResourceNiBinaryStream")
    counts["ConsoleLogPrinter"] = crash_message.count("ConsoleLogPrinter")
    # Generic Crash
    counts["tbbmalloc"] = crash_message.count("tbbmalloc.dll")
    # Particle Crash
    counts["ParticleSystem"] = crash_message.count("ParticleSystem")
    # BA2 Limit Crash
    counts["LooseFileAsync"] = crash_message.count("LooseFileAsyncStream")
    # Rendering Crash
    counts["d3d11"] = crash_message.count("d3d11.dll")
    # Grid Scrap Crash
    counts["GridAdjacency"] = crash_message.count("GridAdjacencyMapNode")
    counts["PowerUtils"] = crash_message.count("PowerUtils")
    # Mesh (NIF) Crash
    counts["LooseFileStream"] = crash_message.count("LooseFileStream")
    counts["BSMulti"] = crash_message.count("BSMultiBoundNode")
    counts["BSFade"] = crash_message.count("BSFadeNode")
    # Texture (DDS) Crash
    counts["Create2DTexture"] = crash_message.count("Create2DTexture")
    counts["DefaultTexture"] = crash_message.count("DefaultTexture")
    # Material (BGSM) Crash
    counts["TextureBlack"] = crash_message.count("DefaultTexture_Black")
    counts["NiAlphaProperty"] = crash_message.count("NiAlphaProperty")
    # NPC Pathing Crash - Static
    counts["PathingCell"] = crash_message.count("PathingCell")
    counts["BSPathBuilder"] = crash_message.count("BSPathBuilder")
    counts["PathManagerServer"] = crash_message.count("PathManagerServer")
    # NPC Pathing Crash - Dynamic
    counts["NavMesh"] = crash_message.count("NavMesh")
    counts["NavMeshObstacle"] = crash_message.count("BSNavmeshObstacleData")
    counts["NavMeshDynamic"] = crash_message.count("DynamicNavmesh")
    # BitDefender Crash
    counts["bdhkm64"] = crash_message.count("bdhkm64.dll")
    counts["DeleteFileW"] = crash_message.count("usvfs::hook_DeleteFileW")
    # Audio Driver Crash
    counts["X3DAudio1_7"] = crash_message.count("X3DAudio1_7.dll")
    counts["XAudio2_7"] = crash_message.count("XAudio2_7.dll")
    # Plugin Limit Crash
    counts["BSMemStorage"] = crash_message.count("BSMemStorage")
    counts["ReaderWriter"] = crash_message.count("DataFileHandleReaderWriter")
    # Plugin Order Crash
    counts["Gamebryo"] = crash_message.count("GamebryoSequenceGenerator")
    # MO2 Extractor Crash
    counts["BSD3D"] = crash_message.count("BSD3DResourceCreator")
    # Nvidia Debris Crash
    counts["flexRelease_x64"] = crash_message.count("flexRelease_x64.dll")
    # Nvidia Driver Crash
    counts["nvwgf2umx"] = crash_message.count("nvwgf2umx.dll")
    # Vulkan Memory Crash
    counts["SubmissionQueue"] = crash_message.count("DxvkSubmissionQueue")
    # Vulkan Settings Crash
    counts["DXGIAdapter"] = crash_message.count("dxvk::DXGIAdapter")
    counts["DXGIFactory"] = crash_message.count("dxvk::DXGIFactory")
    # Corrupted Audio Crash
    counts["BSXAudio2Data"] = crash_message.count("BSXAudio2DataSrc")
    counts["BSXAudio2Game"] = crash_message.count("BSXAudio2GameSound")
    # Animation / Physics Crash
    counts["Anim1"] = crash_message.count("hkbVariableBindingSet")
    counts["Anim2"] = crash_message.count("hkbHandIkControlsModifier")
    counts["Anim3"] = crash_message.count("hkbBehaviorGraph")
    counts["Anim4"] = crash_message.count("hkbModifierList")
    # Archive Invalidation Crash
    counts["DLCBanner05"] = crash_message.count("DLCBanner05.dds")
    # *[Item Crash]
    counts["BGSAttachment"] = crash_message.count("BGSMod::Attachment")
    counts["BGSTemplate"] = crash_message.count("BGSMod::Template")
    counts["BGSTemplateItem"] = crash_message.count("BGSMod::Template::Item")
    # *[Save Crash] <?> *[Bad INI Crash]
    counts["BGSSaveBuffer"] = crash_message.count("BGSSaveFormBuffer")
    # *[Input Crash]
    counts["ButtonEvent"] = crash_message.count("ButtonEvent")
    counts["MenuControls"] = crash_message.count("MenuControls")
    counts["MenuOpenClose"] = crash_message.count("MenuOpenCloseHandler")
    counts["PlayerControls"] = crash_message.count("PlayerControls")
    counts["DXGISwapChain"] = crash_message.count("DXGISwapChain")
    # *[Bad INI Crash] <?> *[Save Crash]
    counts["BGSSaveManager"] = crash_message.count("BGSSaveLoadManager")
    counts["BGSSaveThread"] = crash_message.count("BGSSaveLoadThread")
    counts["INIMem1"] = crash_message.count("+0CDAD30")
    counts["INIMem2"] = crash_message.count("+0D09AB7")
    # *[NPC Patrol Crash]
    counts["Patrol"] = crash_message.count("BGSProcedurePatrol")
    counts["PatrolExec"] = crash_message.count("BGSProcedurePatrolExecState")
    counts["PatrolActor"] = crash_message.count("PatrolActorPackageData")
    # *[Precombines Crash]
    counts["TESObjectCELL"] = crash_message.count("TESObjectCELL")
    counts["BGSStatic"] = crash_message.count("BGSStaticCollection")
    counts["BGSCombined"] = crash_message.count("BGSCombinedCellGeometryDB")
    counts["BSPacked"] = crash_message.count("BSPackedCombinedGeomDataExtra")
    # *[Ammo Counter Crash]
    counts["HUDAmmo"] = crash_message.count("HUDAmmoCounter")
    # *[NPC Projectile Crash]
    counts["BGSProjectile"] = crash_message.count("BGSProjectile")
    counts["CombatProjectile"] = crash_message.count("CombatProjectileAimController")
    # *[Player Character Crash]
    counts["Player"] = crash_message.count("PlayerCharacter")
    counts["0x7"] = crash_message.count("0x00000007")
    counts["0x8"] = crash_message.count("0x00000008")
    counts["0x14"] = crash_message.count("0x00000014")
    # *OTHER
    # counts["ObjectBindPolicy] = crash_message.count("ObjectBindPolicy")

    # ===========================================================

    if counts["Overflow"] >= 1:
        print("Checking for Stack Overflow Crash.........CULPRIT FOUND!")
        print("> Priority Level: [5]")
        Buffout_Trap = 0
        statC["Overflow"] += 1
    if counts["ActiveEffect"] >= 1:
        print("Checking for Active Effects Crash.........CULPRIT FOUND!")
        print("> Priority Level: [5]")
        Buffout_Trap = 0
        statC["ActiveEffect"] += 1

    if counts["BadMath"] >= 1:
        print("Checking for Bad Math Crash...............CULPRIT FOUND!")
        print("> Priority Level: [5]")
        Buffout_Trap = 0
        statC["BadMath"] += 1

    if counts["Null"] >= 1:
        print("Checking for Null Crash...................CULPRIT FOUND!")
        print("> Priority Level: [5]")
        Buffout_Trap = 0
        statC["Null"] += 1

    # ===========================================================
    #print("> Priority Level: [X] | X01 : ",count_Y01," | X02 : ",count_Y02," | X03 : ",count_Y03," | X04 : ",count_Y04)

    if counts["DLCBanner01"] >= 1:
        print("Checking for DLL Crash....................CULPRIT FOUND!")
        print(f'> Priority Level: [5] | DLCBannerDLC01.dds : {counts["DLCBanner01"]}')
        Buffout_Trap = 0
        statC["DLL"] += 1
    # ===========================================================
    if (counts["BGSLocation"] >= 1 and counts["BGSQueued"] >= 1):
        print("Checking for LOD Crash....................CULPRIT FOUND!")
        print(f'> Priority Level: [5] | BGSLocation : {counts["BGSLocation"]} | BGSQueuedTerrainInitialLoad : {counts["BGSQueued"]}')
        Buffout_Trap = 0
        statC["LOD"] += 1
    # ===========================================================
    if (counts["FaderData"] or counts["FaderMenu"] or counts["UIMessage"]) >= 1:
        print("Checking for MCM Crash....................CULPRIT FOUND!")
        print(f'> Priority Level: [3] | FaderData : {counts["FaderMenu"]} | UIMessage : {counts["UIMessage"]}')
        Buffout_Trap = 0
        statC["MCM"] += 1
    # ===========================================================
    if (counts["BGSDecal"] or counts["BSTempEffect"]) >= 1:
        print("Checking for Decal Crash..................CULPRIT FOUND!")
        print(f'> Priority Level: [5] | BGSDecalManager : {counts["BGSDecal"]} | BSTempEffectGeometryDecal : {counts["BSTempEffect"]}')
        Buffout_Trap = 0
        statC["Decal"] += 1
    # ===========================================================
    if counts["PipboyMapData"] >= 2:
        print("Checking for Equip Crash..................CULPRIT FOUND!")
        print(f'> Priority Level: [2] | PipboyMapData : {counts["PipboyMapData"]}')
        Buffout_Trap = 0
        statC["Equip"] += 1
    # ===========================================================
    if (counts["Papyrus"] or counts["VirtualMachine"]) >= 2:
        print("Checking for Script Crash.................CULPRIT FOUND!")
        print(f'> Priority Level: [3] | Papyrus : {counts["Papyrus"]} | VirtualMachine : {counts["VirtualMachine"]}')
        Buffout_Trap = 0
        statC["Papyrus"] += 1
    # ===========================================================
    if counts["tbbmalloc"] >= 3 or "tbbmalloc" in buff_error:
        print("Checking for Generic Crash................CULPRIT FOUND!")
        print(f'> Priority Level: [2] | tbbmalloc.dll : {counts["tbbmalloc"]}')
        Buffout_Trap = 0
        statC["Generic"] += 1
    # ===========================================================
    if counts["LooseFileAsync"] >= 1:
        print("Checking for BA2 Limit Crash..............CULPRIT FOUND!")
        print(f'> Priority Level: [5] | LooseFileAsyncStream : {counts["LooseFileAsync"]}')
        Buffout_Trap = 0
        statC["BA2Limit"] += 1
    # ===========================================================
    if counts["d3d11"] >= 3 or "d3d11" in buff_error:
        print("Checking for Rendering Crash..............CULPRIT FOUND!")
        print(f'> Priority Level: [4] | d3d11.dll : {counts["d3d11"]}')
        Buffout_Trap = 0
        statC["Rendering"] += 1
    # ===========================================================
    if (counts["GridAdjacency"] or counts["PowerUtils"]) >= 1:
        print("Checking for Grid Scrap Crash.............CULPRIT FOUND!")
        print(f'> Priority Level: [5] | GridAdjacencyMapNode : {counts["GridAdjacency"]} | PowerUtils : {counts["PowerUtils"]}')
        Buffout_Trap = 0
        statC["GridScrap"] += 1
    # ===========================================================
    if (counts["LooseFileStream"] or counts["BSFade"] or counts["BSMulti"]) >= 1 and counts["LooseFileAsync"] == 0:
        print("Checking for Mesh (NIF) Crash.............CULPRIT FOUND!")
        print(f'> Priority Level: [4] | LooseFileStream : {counts["LooseFileStream"]} | BSFadeNode : {counts["BSFade"]} | BSMultiBoundNode : {counts["BSMulti"]}')
        Buffout_Trap = 0
        statC["NIF"] += 1
    # ===========================================================
    if (counts["Create2DTexture"] or counts["DefaultTexture"]) >= 1:
        print("Checking for Texture (DDS) Crash..........CULPRIT FOUND!")
        print(f'> Priority Level: [3] | Create2DTexture : {counts["Create2DTexture"]} | DefaultTexture : {counts["DefaultTexture"]}')
        Buffout_Trap = 0
        statC["Texture"] += 1
    # ===========================================================
    if (counts["TextureBlack"] or counts["NiAlphaProperty"]) >= 1:
        print("Checking for Material (BGSM) Crash........CULPRIT FOUND!")
        print(f'> Priority Level: [3] | DefaultTexture_Black : {counts["TextureBlack"]} | NiAlphaProperty : {counts["NiAlphaProperty"]}')
        Buffout_Trap = 0
        statC["BGSM"] += 1
    # ===========================================================
    if (counts["bdhkm64"] or counts["DeleteFileW"]) >= 2:
        print("Checking for BitDefender Crash............CULPRIT FOUND!")
        print(f'> Priority Level: [5] | bdhkm64.dll : {counts["bdhkm64"]} | usvfs::hook_DeleteFileW : {counts["DeleteFileW"]}')
        Buffout_Trap = 0
        statC["BitDefender"] += 1
    # ===========================================================
    if (counts["PathingCell"] or counts["BSPathBuilder"] or counts["PathManagerServer"]) >= 1:
        print("Checking for NPC Pathing Crash............CULPRIT FOUND!")
        print(f'> Priority Level: [3] | PathingCell : {counts["PathingCell"]} | BSPathBuilder : {counts["BSPathBuilder"]} | PathManagerServer : {counts["PathManagerServer"]}')
        Buffout_Trap = 0
        statC["NPCPathing"] += 1
    elif (counts["NavMesh"] or counts["NavMeshObstacle"] or counts["NavMeshDynamic"]) >= 1:
        print("Checking for NPC Pathing Crash............CULPRIT FOUND!")
        print(f'> Priority Level: [3] | NavMesh : {counts["NavMesh"]} | BSNavmeshObstacleData : {counts["NavMeshObstacle"]} | DynamicNavmesh : {counts["NavMeshDynamic"]}')
        Buffout_Trap = 0
        statC["NPCPathing"] += 1
    # ===========================================================
    if counts["X3DAudio1_7"] >= 3 or counts["XAudio2_7"] >= 2 or "X3DAudio1_7" in buff_error or "XAudio2_7" in buff_error:
        print("Checking for Audio Driver Crash...........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | X3DAudio1_7.dll : {counts["X3DAudio1_7"]} | XAudio2_7.dll : {counts["XAudio2_7"]}')
        Buffout_Trap = 0
        statC["Audio"] += 1
    # ===========================================================
    if counts["CBP"] >= 3 or counts["skeleton"] >= 1 or "cbp" in buff_error:
        print("Checking for Body Physics Crash...........CULPRIT FOUND!")
        print(f'> Priority Level: [4] | cbp.dll : {counts["CBP"]} | skeleton.nif : {counts["skeleton"]}')
        Buffout_Trap = 0
        statC["BodyPhysics"] += 1
    # ===========================================================
    if (counts["BSMemStorage"] or counts["ReaderWriter"]) >= 1:
        print("Checking for Plugin Limit Crash...........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | BSMemStorage : {counts["BSMemStorage"]} | DataFileHandleReaderWriter : {counts["ReaderWriter"]}')
        Buffout_Trap = 0
        statC["PluginLimit"] += 1
    # ===========================================================
    if counts["Gamebryo"] >= 1:
        print("Checking for Plugin Order Crash...........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | GamebryoSequenceGenerator : {counts["Gamebryo"]}')
        Buffout_Trap = 0
        statC["LoadOrder"] += 1
    # ===========================================================
    if counts["BSD3D"] == 3 or counts["BSD3D"] == 6:
        print("Checking for MO2 Extractor Crash..........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | BSD3DResourceCreator : {counts["BSD3D"]}')
        Buffout_Trap = 0
        statC["MO2Unp"] += 1
    # ===========================================================
    if counts["flexRelease_x64"] >= 2 or "flexRelease_x64" in buff_error:
        print("Checking for Nvidia Debris Crash..........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | flexRelease_x64.dll : {counts["flexRelease_x64"]}')
        Buffout_Trap = 0
        statC["NVDebris"] += 1
    # ===========================================================
    if counts["nvwgf2umx"] >= 10 or "nvwgf2umx" in buff_error:
        print("Checking for Nvidia Driver Crash..........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | nvwgf2umx.dll : {counts["nvwgf2umx"]}')
        Buffout_Trap = 0
        statC["NVDriver"] += 1
    # ===========================================================
    if (counts["KERNELBASE"] or counts["MSVCP140"]) >= 3 and counts["SubmissionQueue"] >= 1:
        print("Checking for Vulkan Memory Crash..........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | KERNELBASE.dll : {counts["KERNELBASE"]} | MSVCP140.dll : {counts["MSVCP140"]} | DxvkSubmissionQueue : {counts["SubmissionQueue"]}')
        Buffout_Trap = 0
        statC["VulkamMem"] += 1
    # ===========================================================
    if (counts["DXGIAdapter"] or counts["DXGIFactory"] >= 1):
        print("Checking for Vulkan Settings Crash........CULPRIT FOUND!")
        print(f'> Priority Level: [5] | dxvk::DXGIAdapter : {counts["DXGIAdapter"]} | dxvk::DXGIFactory : {counts["DXGIFactory"]}')
        Buffout_Trap = 0
        statC["VulkanSet"] += 1
    # ===========================================================
    if (counts["BSXAudio2Data"] or counts["BSXAudio2Game"]) >= 1:
        print("Checking for Corrupted Audio Crash........CULPRIT FOUND!")
        print(f'> Priority Level: [4] | BSXAudio2DataSrc : {counts["BSXAudio2Data"]} | BSXAudio2GameSound : {counts["BSXAudio2Game"]}')
        Buffout_Trap = 0
        statC["CorruptedAudio"] += 1
    # ===========================================================
    if (counts["CompileAndRun"] or counts["NiBinaryStream"] or counts["ConsoleLogPrinter"]) >= 1:
        print("Checking for Console Command Crash........CULPRIT FOUND!")
        print(f'> Priority Level: [1] | SysWindowCompileAndRun : {counts["CompileAndRun"]} | BSResourceNiBinaryStream : {counts["NiBinaryStream"]} | ConsoleLogPrinter : {counts["ConsoleLogPrinter"]}')
        Buffout_Trap = 0
        statC["ConsoleCommands"] += 1
    # ===========================================================
    if counts["ParticleSystem"] >= 1:
        print("Checking for Particle Effects Crash.......CULPRIT FOUND!")
        print(f'> Priority Level: [4] | ParticleSystem : {counts["ParticleSystem"]}')
        Buffout_Trap = 0
        statC["Particles"] += 1
    # ===========================================================
    if int(counts["Anim1"]) or int(counts["Anim2"]) or int(counts["Anim3"]) or int(counts["Anim4"]) >= 1:
        print("Checking for Animation / Physics Crash....CULPRIT FOUND!")
        print(f'> Priority Level: [5] | hkbVariableBindingSet : {counts["Anim1"]}  | hkbHandIkControlsModifier : {counts["Anim2"]}')
        print(f'                        hkbBehaviorGraph : {counts["Anim3"]} | hkbModifierList : {counts["Anim4"]}')
        Buffout_Trap = 0
        statC["AnimationPhysics"] += 1
    # ===========================================================
    if int(counts["DLCBanner05"]) >= 1:
        print("Checking for Archive Invalidation Crash...CULPRIT FOUND!")
        print(f'> Priority Level: [5] | DLCBanner05.dds : {counts["DLCBanner05"]}')
        Buffout_Trap = 0
        statC["Invalidation"] += 1
    # ===========================================================
    print("---------- Unsolved Crash Messages Below ----------")

    if (counts["BGSAttachment"] or counts["BGSTemplate"] or counts["BGSTemplateItem"]) >= 1:
        print("Checking for *[Item Crash]................DETECTED!")
        print(f'> Priority Level: [5] | BGSMod::Attachment : {counts["BGSAttachment"]} | BGSMod::Template : {counts["BGSTemplate"]} | BGSMod::Template::Item : {counts["BGSTemplateItem"]}')
        Buffout_Trap = 0
        statU["Item"] += 1
    # ===========================================================
    if counts["BGSSaveBuffer"] >= 2:
        print("Checking for *[Save Crash]................DETECTED!")
        print(f'> Priority Level: [5] | BGSSaveFormBuffer : {counts["BGSSaveBuffer"]}')
        Buffout_Trap = 0
        statU["Save"] += 1
    # ===========================================================
    if (counts["ButtonEvent"] or counts["MenuControls"] or counts["MenuOpenClose"] or counts["PlayerControls"] or counts["DXGISwapChain"]) >= 1:
        print("Checking for *[Input Crash]...............DETECTED!")
        print(f'> Priority Level: [5] | ButtonEvent : {counts["ButtonEvent"]} | MenuControls : {counts["MenuControls"]}')
        print(f'                        MenuOpenCloseHandler : {counts["MenuOpenClose"]} | PlayerControls : {counts["PlayerControls"]} | DXGISwapChain : {counts["DXGISwapChain"]}')
        Buffout_Trap = 0
        statU["Input"] += 1
    # ===========================================================
    if (counts["BGSSaveManager"] or counts["BGSSaveThread"] or counts["BGSSaveBuffer"] or counts["INIMem1"] or counts["INIMem2"]) >= 1:
        print("Checking for *[Bad INI Crash].............DETECTED!")
        print(f'> Priority Level: [5] | BGSSaveLoadManager : {counts["BGSSaveManager"]} | BGSSaveLoadThread : {counts["BGSSaveThread"]} | BGSSaveFormBuffer : {counts["BGSSaveBuffer"]}')
        Buffout_Trap = 0
        statU["INI"] += 1
    # ===========================================================
    if (counts["Patrol"] or counts["PatrolExec"] or counts["PatrolActor"]) >= 1:
        print("Checking for *[NPC Patrol Crash]..........DETECTED!")
        print(f'> Priority Level: [5] | BGSProcedurePatrol : {counts["Patrol"]} | BGSProcedurePatrolExecStatel : {counts["PatrolExec"]} | PatrolActorPackageData : {counts["PatrolActor"]}')
        Buffout_Trap = 0
        statU["Patrol"] += 1
    # ===========================================================
    if (counts["BSPacked"] or counts["BGSCombined"] or counts["BGSStatic"] or counts["TESObjectCELL"]) >= 1:
        print("Checking for *[Precombines Crash].........DETECTED!")
        print(f'> Priority Level: [5] | BGSStaticCollection : {counts["BSPacked"]} | BGSCombinedCellGeometryDB : {counts["BGSCombined"]}')
        print(f'                        BSPackedCombinedGeomDataExtra : {counts["BGSStatic"]} | TESObjectCELL : {counts["TESObjectCELL"]}')
        Buffout_Trap = 0
        statU["Precomb"] += 1
    # ===========================================================
    if counts["HUDAmmo"] >= 1:
        print("Checking for *[Ammo Counter Crash]........DETECTED!")
        print(f'> Priority Level: [5] | HUDAmmoCounter : {counts["HUDAmmo"]}')
        Buffout_Trap = 0
        statU["HUDAmmo"] += 1
    # ===========================================================
    if (counts["BGSProjectile"] or counts["CombatProjectile"]) >= 1:
        print("Checking for *[NPC Projectile Crash].....DETECTED!")
        print(f'> Priority Level: [5] | BGSProjectile : {counts["BGSProjectile"]} | CombatProjectileAimController : {counts["CombatProjectile"]}')
        Buffout_Trap = 0
    # ===========================================================
    if (counts["Player"] and counts["0x7"]) >= 2 and (counts["0x14"] or counts["0x8"]) >= 2:
        print("Checking for *[Player Character Crash]....DETECTED!")
        print(f'> Priority Level: [5] | PlayerCharacter : {counts["Player"]} | 0x00000007 : {counts["0x7"]}')
        print(f'                        0x00000008 : {counts["0x8"]} | 0x000000014 : {counts["0x14"]}')
        Buffout_Trap = 0
        statU["Player"] += 1
    # ===========================================================

    # DEFINE CHECK IF NOTHING TRIGGERED BUFFOUT TRAP
    if Buffout_Trap == 1:
        print("-----")
        print("AUTOSCAN FOUND NO CRASH MESSAGES THAT MATCH THE CURRENT DATABASE.")
        print("Check below for mods that can cause frequent crashes and other problems.")
        statB["NoMessage"] += 1
    else:
        print("-----")
        print("FOR DETAILED DESCRIPTIONS AND POSSIBLE SOLUTIONS TO ANY ABOVE DETECTED CULPRITS,")
        print("CHECK THE 'HOW TO READ CRASH LOGS' PDF DOCUMENT INCLUDED WITH THE AUTO-SCANNER!")

    # MOD TRAP 1
    print("====================================================")
    print("CHECKING FOR MODS THAT CAN CAUSE FREQUENT CRASHES...")
    print("====================================================")
    Mod_Trap1 = 1

    counts["LoadOrder"] = crash_message.count("[00]")
    counts["Unofficial"] = crash_message.count("Unofficial Fallout 4 Patch.esp")
    counts["CHW"] = crash_message.count("ClassicHolsteredWeapons")
    counts["BSShadow"] = crash_message.count("BSShadowParabolicLight")
    counts["BSShader"] = crash_message.count("BSShaderAccumulator")
    counts["BSDFLight"] = crash_message.count("BSDFLightShader")
    counts["UniquePlayer"] = crash_message.count("UniquePlayer.esp")
    counts["BodyNIF"] = crash_message.count("Body.nif")
    counts["HighHeels"] = crash_message.count("HHS.dll")

    print("IF YOU'RE USING DYNAMIC PERFORMANCE TUNER AND/OR LOAD ACCELERATOR,")
    print("remove these mods completely and switch to High FPS Physics Fix!")
    print("Link: https://www.nexusmods.com/fallout4/mods/44798?tab=files")
    print("-----")

    # CHECK IF PLUGIN LIST WASN'T LOADED - TRAP X
    Mod_TrapX = 1
    no_repeat2 = 1

    # Needs 1 empty space as prefix to prevent duplicates.
    List_Mods1 = [" DamageThresholdFramework.esm",
                  " Endless Warfare.esm",
                  " ExtendedWeaponSystem.esm",
                  " EPO",
                  " SakhalinWasteland",
                  " 76HUD",
                  " NCRenegade",
                  " Respawnable Legendary Bosses",
                  " Scrap Everything",
                  " Shade Girl Leather Outfits",
                  " SpringCleaning.esm",
                  " (STO) NO",
                  " TacticalTablet.esp",
                  " True Nights",
                  " WeaponsFramework",
                  " WOTC.esp"]

    List_Warn1 = ["DAMAGE THRESHOLD FRAMEWORK \n"
                  "- Can cause crashes in combat on some occasions due to how damage calculations are done.",

                  "ENDLESS WARFARE \n"
                  "- Some enemy spawn points could be bugged or crash the game due to scripts or pathfinding.",

                  "EXTENDED WEAPON SYSTEMS \n"
                  "- Alternative to Tactical Reload that suffers from similar weapon related problems and crashes.",

                  "EXTREME PARTICLES OVERHAUL \n"
                  "- Can cause particle effects related crashes, its INI file raises particle count to 500000. \n"
                  "  Consider switching to Burst Impact Blast FX: https://www.nexusmods.com/fallout4/mods/57789",

                  "FALLOUT SAKHALIN \n"
                  "- Breaks the precombine system all across Far Harbor which will randomly crash your game.",

                  "HUD76 HUD REPLACER \n"
                  "- Can sometimes cause interface and pip-boy related bugs, glitches and crashes.",

                  "NCR RENEGADE ARMOR \n"
                  "- Broken outfit mesh that crashes the game in 3rd person or when NPCs wearing it are hit.",

                  "RESPAWNABLE LEGENDARY BOSSES \n"
                  "- Can sometimes cause Deathclaw \ Behmoth boulder projectile crashes for unknown reasons.",

                  "SCRAP EVERYTHING \n"
                  "- Weird crashes and issues due to multiple unknown problems. This mod must be always last in your load order.",

                  "SHADE GIRL LEATHER OUTFITS \n"
                  "- Outfits can crash the game while browsing the armor workbench or upon starting a new game due to bad meshes.",

                  "SPRING CLEANING \n"
                  "- Abandoned and severely outdated mod that breaks precombines and could potentially even break your save file.",

                  "STALKER TEXTURE OVERHAUL \n"
                  "- Doesn't work due to incorrect folder structure and has a corrupted dds file that causes Create2DTexture crashes.",

                  "TACTICAL TABLET \n"
                  "- Can cause flickering with certain scopes or crashes while browsing workbenches, most commonly with ECO.",

                  "TRUE NIGHTS \n"
                  "- Has an invalid Image Space Adapter (IMAD) Record that will corrupt your save memory and has to be manually fixed.",

                  "WEAPONS FRAMEWORK BETA \n"
                  "- Will randomly cause crashes when used with Tactical Reload and possibly other weapon or combat related mods. \n"
                  "  Visit Important Patches List article for possible solutions: https://www.nexusmods.com/fallout4/articles/3769",

                  "WAR OF THE COMMONWEALTH \n"
                  "- Seems responsible for consistent crashes with specific spawn points or randomly during settlement attacks."]

    for line in all_lines:
        for elem in List_Mods1:
            if str("File:") not in line and str("[FE") not in line and elem in line:
                order_elem = List_Mods1.index(elem)
                print("[!] Found:", line[0:5].strip(), List_Warn1[order_elem])
                print("-----")
                Mod_Trap1 = 0
            elif str("File:") not in line and str("[FE") in line and elem in line:
                order_elem = List_Mods1.index(elem)
                print("[!] Found:", line[0:9].strip(), List_Warn1[order_elem])
                print("-----")
                Mod_Trap1 = 0

    if counts["CHW"] >= 2 and (counts["BSShadow"] or counts["BSShader"] or counts["BSDFLight"]) >= 1 or "ClassicHolsteredWeapons" in buff_error:
        print("[!] Found: CLASSIC HOLSTERED WEAPONS")
        print("AUTOSCAN IS PRETTY CERTAIN THAT CHW CAUSED THIS CRASH!")
        print("You should disable CHW to further confirm this.")
        print("Visit the main crash logs article for additional solutions.")
        print("-----")
        statM_CHW += 1
        Mod_Trap1 = 0
        Buffout_Trap = 0
    elif counts["CHW"] >= 2 and (counts["UniquePlayer"] or counts["HighHeels"] or counts["CBP"] or counts["BodyNIF"]) >= 1:
        print("[!] Found: CLASSIC HOLSTERED WEAPONS")
        print("AUTOSCAN ALSO DETECTED ONE OR SEVERAL MODS THAT WILL CRASH WITH CHW.")
        print("You should disable CHW to further confirm it caused this crash.")
        print("Visit the main crash logs article for additional solutions.")
        print("-----")
        statM_CHW += 1
        Mod_Trap1 = 0
        Buffout_Trap = 0
    elif counts["CHW"] == 1 and "d3d11" in buff_error:
        print("[!] Found: CLASSIC HOLSTERED WEAPONS, BUT...")
        print("AUTOSCAN CANNOT ACCURATELY DETERMINE IF CHW CAUSED THIS CRASH OR NOT.")
        print("You should open CHW's ini file and change IsHolsterVisibleOnNPCs to 0.")
        print("This usually prevents most common crashes with Classic Holstered Weapons.")
        print("-----")
        Mod_Trap1 = 0

    # ===========================================================
    # DEFINE CHECKS IF NOTHING TRIGGERED MOD TRAP 1 & NO PLUGINS

    if Mod_Trap1 == 0:
        print("CAUTION: ANY ABOVE DETECTED MODS HAVE A MUCH HIGHER CHANCE TO CRASH YOUR GAME!")
        print("You can disable any/all of them temporarily to confirm they caused this crash.")
        print("-----")
        statL["scanned"] += 1
    elif Mod_TrapX == 0:
        print("BUFFOUT 4 COULDN'T LOAD THE PLUGIN LIST FOR THIS CRASH LOG!")
        print("Autoscan cannot continue. Try scanning a different crash log.")
        print("-----")
        statL["incomplete"] += 1
        statL["scanned"] -= 1
    elif Mod_Trap1 == 1:
        print("AUTOSCAN FOUND NO PROBLEMATIC MODS THAT MATCH THE CURRENT DATABASE FOR THIS LOG.")
        print("THAT DOESN'T MEAN THERE AREN'T ANY! YOU SHOULD RUN PLUGIN CHECKER IN WRYE BASH.")
        print("Wrye Bash Link: https://www.nexusmods.com/fallout4/mods/20032?tab=files")
        print("-----")
        statL["scanned"] += 1

    # MOD TRAP 2 | ESL PLUGINS NEED 8 SPACES FOR [FE:XXX]
    print("====================================================")
    print("CHECKING FOR MODS WITH SOLUTIONS & COMMUNITY PATCHES")
    print("====================================================")
    Mod_Trap2 = 1
    no_repeat1 = 1

    counts["FallSouls"] = crash_message.count("FallSouls.dll")

    if counts["Unofficial"] == 0 and counts["LoadOrder"] == 0:
        Mod_TrapX = 0
    elif counts["Unofficial"] == 0 and counts["LoadOrder"] >= 1:
        print("UNOFFICIAL FALLOUT 4 PATCH ISN'T INSTALLED OR AUTOSCAN CANNOT DETECT IT!")
        print("If you own all DLCs, make sure that the Unofficial Patch is installed.")
        print("Link: https://www.nexusmods.com/fallout4/mods/4598?tab=files")
        print("-----")

    # Needs 1 empty space as prefix to prevent duplicates.
    List_Mods2 = [" DLCUltraHighResolution.esm",
                  " AAF.esm",
                  " ArmorKeywords.esm",
                  " BTInteriors_Project.esp",
                  " CombatZoneRestored",
                  " D.E.C.A.Y.esp",
                  " EveryonesBestFriend",
                  " M8r_Item_Tags",
                  " Fo4FI_FPS_fix",
                  " BostonFPSFix",
                  " FunctionalDisplays.esp",
                  " skeletonmaleplayer",
                  " skeletonfemaleplayer",
                  " CapsWidget",
                  " Homemaker.esm",
                  " LegendaryModification.esp",
                  " MilitarizedMinutemen.esp",
                  " MoreUniques",
                  " RaiderOverhaul.esp",
                  " SKKCraftableWeaponsAmmo",
                  " SOTS.esp",
                  " StartMeUp.esp",
                  " SuperMutantRedux.esp",
                  " TacticalReload.esm",
                  " Creatures and Monsters.esp",
                  " ZombieWalkers"]

    List_Warn2 = ["HIGH RESOLUTION DLC. I STRONGLY ADVISE NOT USING IT! \n"
                  "Right click on Fallout 4 in your Steam Library folder, then select Properties \n"
                  "Switch to the DLC tab and uncheck / disable the High Resolution Texture Pack",
                  #
                  "ADVANCED ANIMATION FRAMEWORK \n"
                  "Looks Menu versions 1.6.20 & 1.6.19 can frequently break adult mod related (erection) morphs. \n"
                  "If you notice any AAF realted problems, uninstall latest version of Looks Menu and switch to 1.6.18!",
                  #
                  "ARMOR AND WEAPON KEYWORDS \n"
                  "If you don't rely on AWKCR, you should switch to Equipment and Crafting Overhaul \n"
                  "Better Alternative: https://www.nexusmods.com/fallout4/mods/55503?tab=files",
                  #
                  "BEANTOWN INTERIORS PROJECT \n"
                  "Usually causes fps drops, stuttering, crashing and culling issues in multiple locations. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/53894?tab=files",
                  #
                  "COMBAT ZONE RESTORED \n"
                  "Contains few small issues and NPCs usually have trouble navigating the interior space. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/59329?tab=files",
                  #
                  "DECAY BETTER GHOULS \n"
                  "You have to install DECAY Redux patch to prevent its audio files from crashing the game. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/59025?tab=files",
                  #
                  "EVERYONE'S BEST FRIEND \n"
                  "This mod needs a compatibility patch to properly work with the Unofficial Patch (UFO4P). \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/43409?tab=files",
                  #
                  "FALLUI ITEM SORTER (OLD) \n"
                  "This is an outdated item tagging / sorting patch that can cause crashes or conflicts in all kinds of situations. \n"
                  "I strongly recommend to instead generate your own sorting patch and place it last in your load order. \n"
                  "That way, you won't experience any conflicts / crashes and even modded items will be sorted. \n"
                  "Generate Sorting Patch With This: https://www.nexusmods.com/fallout4/mods/48826?tab=files",
                  #
                  "FO4FI FPS FIX \n"
                  "This mod is severely outdated and will cause crashes even with compatibility patches. \n"
                  "Better Alternative: https://www.nexusmods.com/fallout4/mods/46403?tab=files",
                  #
                  "BOSTON FPS FIX \n"
                  "This mod is severely outdated and will cause crashes even with compatibility patches. \n"
                  "Better Alternative: https://www.nexusmods.com/fallout4/mods/46403?tab=files",
                  #
                  "FUNCTIONAL DISPLAYS \n"
                  "Frequently causes object model (nif) related crashes and this needs to be manually corrected. \n"
                  "Advised Fix: Open its Meshes folder and delete everything inside EXCEPT for the Functional Displays folder.",
                  #
                  "GENDER SPECIFIC SKELETONS (MALE) \n"
                  "High chance to cause a crash when starting a new game or during the game intro sequence. \n"
                  "Advised Fix: Enable the mod only after leaving Vault 111. Existing saves shouldn't be affected.",
                  #
                  "GENDER SPECIFIC SKELETONS (FEMALE) \n"
                  "High chance to cause a crash when starting a new game or during the game intro sequence. \n"
                  "Advised Fix: Enable the mod only after leaving Vault 111. Existing saves shouldn't be affected.",
                  #
                  "HUD CAPS \n"
                  "Often breaks the Save / Quicksave function due to poor script implementation. \n"
                  "Advised Fix: Download fixed pex file and place it into HUDCaps/Scripts folder. \n"
                  "Fix Link: https://drive.google.com/file/d/1egmtKVR7mSbjRgo106UbXv_ySKBg5az2/view",
                  #
                  "HOMEMAKER \n"
                  "Causes a crash while scrolling over Military / BoS fences in the Settlement Menu. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/41434?tab=files",
                  #
                  "LEGENDARY MODIFICATION \n"
                  "Old mod plagued with all kinds of bugs and crashes, can conflict with some modded weapons. \n"
                  "Better Alternative: https://www.nexusmods.com/fallout4/mods/55503?tab=files",
                  #
                  "MILITARIZED MINUTEMEN \n"
                  "Can occasionally crash the game due to a broken mesh on some minutemen outfits. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/55301?tab=files",
                  #
                  "MORE UNIQUE WEAPONS EXPANSION \n"
                  "Causes crashes due to broken precombines and compatibility issues with other weapon mods. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/54848?tab=files",
                  #
                  "RAIDER OVERHAUL \n"
                  "Old mod that requires several patches to function as intended. Use ONE Version instead. \n"
                  "Upated ONE Version: https://www.nexusmods.com/fallout4/mods/51658?tab=files",
                  #
                  "SKK CRAFT WEAPONS AND SCRAP AMMO \n"
                  "Version 008 is incompatible with AWKCR and will cause crashes while saving the game. \n"
                  "Advised Fix: Use Version 007 or remove AWKCR and switch to Equipment and Crafting Overhaul.",
                  #
                  "SOUTH OF THE SEA \n"
                  "Very unstable mod that consistently and frequently causes strange problems and crashes. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/59792?tab=files",
                  #
                  "START ME UP \n"
                  "Abandoned mod that can cause infinite loading and other problems. Use REDUX Version instead. \n"
                  "Upated REDUX Version: https://www.nexusmods.com/fallout4/mods/56984?tab=files",
                  #
                  "SUPER MUTANT REDUX \n"
                  "Causes crashes at specific locations or with certain Super Muntant enemies and items. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/51353?tab=files",
                  #
                  "TACTICAL RELOAD \n"
                  "Can cause weapon and combat related crashes. TR Expansion For ECO is highly recommended. \n"
                  "TR Expansion For ECO Link: https://www.nexusmods.com/fallout4/mods/62737",
                  #
                  "UNIQUE NPCs CREATURES AND MONSTERS \n"
                  "Causes crashes and breaks precombines at specific locations, some creature spawns are too frequent. \n"
                  "Patch Link: https://www.nexusmods.com/fallout4/mods/48637?tab=files",
                  #
                  "ZOMBIE WALKERS \n"
                  "Version 2.6.3 contains a resurrection script that will regularly crash the game. \n"
                  "Advised Fix: Make sure you're using the 3.0 Beta version of this mod or newer."]

    for line in all_lines:
        for elem in List_Mods2:
            if str("File:") not in line and str("[FE") not in line and elem in line:
                order_elem = List_Mods2.index(elem)
                print("[!] Found:", line[0:5].strip(), List_Warn2[order_elem])
                print("-----")
                Mod_Trap2 = 0
            elif str("File:") not in line and str("[FE") in line and elem in line:
                order_elem = List_Mods2.index(elem)
                print("[!] Found:", line[0:9].strip(), List_Warn2[order_elem])
                print("-----")
                Mod_Trap2 = 0
        #
        if no_repeat1 == 1 and str("File:") not in line and (str("Depravity.esp") in line or str("FusionCityRising.esp") in line or str("HotC.esp") in line or str("OutcastsAndRemnants.esp") in line or str("ProjectValkyrie.esp") in line):
            print("[!] Found:", line[0:9].strip(), "THUGGYSMURF QUEST MODS")
            print("If you have Depravity, Fusion City Rising, HOTC, Outcasts and Remnants and/or Project Valkyrie,")
            print("install this patch with facegen data, fully generated precomb/previs data and several tweaks.")
            print("Patch Link: https://www.nexusmods.com/fallout4/mods/56876?tab=files")
            print("-----")
            no_repeat1 = 0
            Mod_Trap2 = 0

    if counts["FallSouls"] >= 1:
        print("[!] Found: FALLSOULS UNPAUSED GAME MENUS")
        print("Occasionally breaks the Quests menu, can cause crashes while changing MCM settings.")
        print("Advised Fix: Toggle PipboyMenu in FallSouls MCM settings or completely reinstall the mod.")
        print("-----")
        Mod_Trap2 = 0
    # ===========================================================
    # DEFINE CHECKS IF NOTHING TRIGGERED TRAP 2 & NO PLUGINS

    print("[Due to inherent limitations, Auto-Scan will continue detecting certain mods,")
    print(" even if fixes or patches for them are already installed. You can ignore these.]")
    print("-----")
    print("FOR FULL LIST OF IMPORTANT PATCHES AND FIXES FOR THE BASE GAME AND MODS,")
    print("VISIT THIS ARTICLE: https://www.nexusmods.com/fallout4/articles/3769")
    print("-----")

    if Mod_TrapX == 0:
        print("BUFFOUT 4 COULDN'T LOAD THE PLUGIN LIST FOR THIS CRASH LOG!")
        print("Autoscan cannot continue. Try scanning a different crash log.")
        print("-----")
        Mod_Trap2 = 0
    elif Mod_Trap2 == 1:
        print("Autoscan found no problematic mods with solutions and community patches.")
        print("-----")

    # MOD TRAP 3 | ESL PLUGINS NEED 8 SPACES FOR [FE:XXX]
    print("====================================================")
    print("CHECKING FOR MODS PATCHED THROUGH OPC INSTALLER...")
    print("====================================================")
    Mod_Trap3 = 1

    # Needs 1 empty space as prefix to prevent duplicates.
    List_Mods3 = [" Beyond the Borders",
                  " Deadly Commonwealth Expansion",
                  " Dogmeat and Strong Armor",
                  " DoYourDamnJobCodsworth",
                  " ConcordEXPANDED",
                  " HagenEXPANDED",
                  " GlowingSeaEXPANDED",
                  " SalemEXPANDED",
                  " SwampsEXPANDED",
                  " _hod",
                  " ImmersiveBeantown",
                  " CovenantComplex",
                  " GunnersPlazaInterior",
                  " ImmersiveHubCity",
                  " Immersive_Lexington",
                  " Immersive Nahant",
                  " Immersive S Boston",
                  " MutilatedDeadBodies",
                  " Vault4",
                  " atlanticofficesf23",
                  " Minutemen Supply Caches",
                  " moreXplore",
                  " NEST_BUNKER_PROJECT",
                  " Raider Children.esp",
                  " sectorv",
                  " SettlementShelters",
                  " subwayrunnnerdynamiclighting",
                  " 3DNPC_FO4Settler.esp",
                  " 3DNPC_FO4.esp",
                  " The Hollow",
                  " nvvault1080",
                  " Vertibird Faction Paint Schemes",
                  " MojaveImports.esp",
                  " Firelance2.5",
                  " zxcMicroAdditions"]

    List_Warn3 = ["Beyond the Borders",
                  "Deadly Commonwealth Expansion",
                  "Dogmeat and Strong Armor",
                  "Do Your Damn Job Codsworth",
                  "Concord Expanded",
                  "Fort Hagen Expanded",
                  "Glowing Sea Expanded",
                  "Salem Expanded",
                  "Swamps Expanded",
                  "Hearts Of Darkness",
                  "Immersive Beantown Brewery",
                  "Immersive Covenant Compound",
                  "Immersive Gunners Plaza",
                  "Immersive Hub City",
                  "Immersive & Extended Lexington",
                  "Immersive & Extended Nahant",
                  "Immersive Military Checkpoint",
                  "Mutilated Dead Bodies",
                  "Fourville (Vault 4)",
                  "Lost Building of Atlantic",
                  "Minutemen Supply Caches",
                  "MoreXplore",
                  "NEST Survival Bunkers",
                  "Raider Children & Other Horrors",
                  "Sector Five - Rise and Fall",
                  "Settlement Shelters",
                  "Subway Runner (Dynamic Lights)",
                  "Settlers of the Commonwealth",
                  "Tales from the Commonwealth",
                  "The Hollow",
                  "Vault 1080 (Vault 80)",
                  "Vertibird Faction Paint Schemes",
                  "Wasteland Imports (Mojave Imports)",
                  "Xander's Aid",
                  "ZXC Micro Additions"]

    for line in all_lines:
        for elem in List_Mods3:
            if str("File:") not in line and str("[FE") not in line and elem in line:
                order_elem = List_Mods3.index(elem)
                print("- Found:", line[0:5].strip(), List_Warn3[order_elem])
                Mod_Trap3 = 0
            elif str("File:") not in line and str("[FE") in line and elem in line:
                order_elem = List_Mods3.index(elem)
                print("- Found:", line[0:9].strip(), List_Warn3[order_elem])
                Mod_Trap3 = 0

    # ===========================================================
    # DEFINE CHECKS IF NOTHING TRIGGERED TRAP 3 & NO PLUGINS
    if Mod_TrapX == 0:
        print("BUFFOUT 4 COULDN'T LOAD THE PLUGIN LIST FOR THIS CRASH LOG!")
        print("Autoscan cannot continue. Try scanning a different crash log.")
        print("-----")
    elif Mod_Trap3 == 0:
        print("-----")
        print("FOR PATCH REPOSITORY THAT PREVENTS CRASHES AND FIXES PROBLEMS IN THESE AND OTHER MODS,")
        print("VISIT OPTIMIZATION PATCHES COLLECTION: https://www.nexusmods.com/fallout4/mods/54872")
        print("-----")
    elif Mod_Trap3 == 1:
        print("Autoscan found no problematic mods that are already patched through OPC Installer.")
        print("-----")

    # MOD TRAP 4
    print("====================================================")
    print("SCANNING THE LOG FOR SPECIFIC (POSSIBLE) CUPLRITS...")
    print("====================================================")
    Mod_Trap4 = 1

    list_DETPLUGINS = []
    list_DETFORMIDS = []
    list_DETFILES = []
    list_ALLPLUGINS = []

    count_F4SE = crash_message.count("f4se_1_10_163.dll")
    count_Module = crash_message.count("steam_api64.dll")

    if count_F4SE == 0 and count_Module >= 1:
        print("AUTOSCAN CANNOT FIND FALLOUT 4 SCRIPT EXTENDER DLL!")
        print("MAKE SURE THAT F4SE IS CORRECTLY INSTALLED!")
        print("Link: https://f4se.silverlock.org/")
        print("-----")

    for line in all_lines:
        if len(line) >= 6 and "]" in line[4]:
            #line = line[6:]
            list_ALLPLUGINS.append(line.strip())
        if len(line) >= 7 and "]" in line[5]:
            #line = line[7:]
            list_ALLPLUGINS.append(line.strip())
        if len(line) >= 10 and "]" in line[8]:
            #line = line[10:]
            list_ALLPLUGINS.append(line.strip())
        if len(line) >= 11 and "]" in line[9]:
            #line = line[11:]
            list_ALLPLUGINS.append(line.strip())

    # =================== TEST - LIST OUTPUT ====================
    #print("TEST - ALL PLUGINS:")
    # print(list_ALLPLUGINS)
    # print("-----")

    print("LIST OF (POSSIBLE) PLUGIN CULRIPTS:")
    for line in all_lines:
        if "File:" in line:
            line = line.replace("File: ", "")
            line = line.replace('"', '')
            list_DETPLUGINS.append(line.strip())

    list_DETPLUGINS = list(dict.fromkeys(list_DETPLUGINS))
    list_remove = ["Fallout4.esm", "DLCCoast.esm", "DLCNukaWorld.esm", "DLCRobot.esm", "DLCworkshop01.esm", "DLCworkshop02.esm", "DLCworkshop03.esm", "", '']
    for elem in list_remove:
        if elem in list_DETPLUGINS:
            list_DETPLUGINS.remove(elem)

    # =================== TEST - LIST OUTPUT ===================
    #print("TEST - DETECTED PLUGINS:")
    # print(list_DETPLUGINS)
    # print("-----")

    # PYTHON MAGIC 1
    PL_strings = list_ALLPLUGINS
    PL_substrings = list_DETPLUGINS
    PL_result = []

    for string in PL_strings:
        PL_matches = []
        for substring in PL_substrings:
            if substring in string:
                PL_matches.append(string)
        if PL_matches:
            PL_result.append(PL_matches)
            print("- " + ' '.join(PL_matches))

    # ALTERNATIVE TO ABOVE
    # for s in PL_strings:
    #    for k in PL_substrings:
    #        if k in s:
    #            print("- " + s)

    if not PL_result:
        print("AUTOSCAN COULDN'T FIND ANY PLUGIN CULRIPTS")
        print("-----")
    else:
        print("-----")
        print("These Plugins were caught by Buffout 4 and some of them might be responsible for this crash.")
        print("You can try disabling these plugins and recheck your game, though this method can be unreliable.")
        print("-----")

    # ===========================================================

    print("LIST OF (POSSIBLE) FORM ID CULRIPTS:")
    for line in all_lines:
        if "Form ID:" in line:
            line = line.replace("0x", "")
            list_DETFORMIDS.append(line.strip())
            line = line.replace("Form ID: ", "")
            line = line[:5].strip()

    list_DETFORMIDS = list(dict.fromkeys(list_DETFORMIDS))
    for elem in list_DETFORMIDS:
        if elem[0:1] != "FF" and elem[0:1] != "ff":
            print(elem)

    if not list_DETFORMIDS:
        print("AUTOSCAN COULDN'T FIND ANY FORM ID CULRIPTS")
        print("-----")
    else:
        print("-----")
        print("These Form IDs were caught by Buffout 4 and some of them might be related to this crash.")
        print("You can try searching any listed Form IDs in FO4Edit and see if they lead to relevant records.")
        print("-----")

    # ===========================================================

    print("LIST OF (POSSIBLE) FILE CULPRITS:")

    List_Files = [".bgsm", ".bto", ".btr", ".dds", ".hkb", ".hkx", ".ini", ".nif", ".pex", ".swf", ".txt", ".uvd", ".wav", ".xwm"]

    for line in all_lines:
        for elem in List_Files:
            if elem in line.lower():
                line = line.replace("File Name: ", "")
                line = line.replace("Name: ", "")
                line = line.replace('"', '')
                list_DETFILES.append(line.strip())

    list_DETFILES = list(dict.fromkeys(list_DETFILES))
    for elem in list_DETFILES:
        print(elem)

    if not list_DETFILES:
        print("AUTOSCAN COULDN'T FIND ANY FILE CULRIPTS")
        print("-----")
    else:
        print("-----")
        print("These files were caught by Buffout 4 and some of them might be related to this crash.")
        print("Detected files in most cases appear as false positives, so no recommendation is given.")
        print("-----")

    print("FOR FULL LIST OF MODS THAT CAUSE PROBLEMS, THEIR ALTERNATIVES AND DETAILED SOLUTIONS,")
    print("VISIT THE BUFFOUT 4 CRASH ARTICLE: https://www.nexusmods.com/fallout4/articles/3115")
    print("===============================================================================")
    print("END OF AUTOSCAN | Author/Made By: Poet#9800 (DISCORD) | 060922")
    print("GUI VERSION: https://www.nexusmods.com/fallout4/mods/63346")
    crash_log.close()
    sys.stdout.close()
    # SUSSY MOVE (Move unsolved logs to special folder.)
    # if int(Buffout_Trap) == 1:
    #    unsolvedCRASH_path = "CL-UNSOLVED/" + crashlog
    #    shutil.move(crashlog, unsolvedCRASH_path)
    #    unsolvedSCAN_path = "CL-UNSOLVED/" + logname + "-AUTOSCAN.md"
    #    shutil.move(logname + "-AUTOSCAN.md", unsolvedSCAN_path)


# dict.fromkeys -> Command to create a dictionary, using items in a list as keys.
# This automatically removes duplicates as dictionaries cannot have duplicate keys.
# =========================== LOG END ===========================
sys.stdout = orig_stdout
print("SCAN COMPLETE! (IT MIGHT TAKE SEVERAL SECONDS FOR SCAN RESULTS TO APPEAR)")
print("SCAN RESULTS ARE AVAILABE IN FILES NAMED crash-date-and-time-AUTOSCAN.md")
print("===============================================================================")
print("FOR FULL LIST OF MODS THAT CAUSE PROBLEMS, THEIR ALTERNATIVES AND DETAILED SOLUTIONS,")
print("VISIT THE BUFFOUT 4 CRASH ARTICLE: https://www.nexusmods.com/fallout4/articles/3115")
print(random.choice(Sneaky_Tips))

# ============ CHECK FOR EMPTY (FAUTLY) AUTO-SCANS ============

list_SCANFAIL = []

autoscans = glob.glob("*-AUTOSCAN.md")

for file in autoscans:
    if file in autoscans:
        line_count = 0
        scanname = str(file)
        autoscan_log = open(file, errors="ignore")
        for line in autoscan_log:
            if line != "\n":
                line_count += 1
        if int(line_count) <= 10:
            list_SCANFAIL.append(scanname.removesuffix("-AUTOSCAN.md") + ".log")
            statL["failed"] += 1

if len(list_SCANFAIL) >= 1:
    print("NOTICE: AUTOSCANNER WAS UNABLE TO PROPERLY SCAN THE FOLLOWING LOG(S): ")
    for elem in list_SCANFAIL:
        print(elem)
    print("===============================================================================")
    print("To troubleshoot this, right click on Scan Crashlogs.py and select option 'Edit With IDLE'")
    print("Once it opens the code, press [F5] to run the script. Any error messages will appear in red.")
    print("-----")
    print('If any given error contains "codec cant decode byte", you can fix this in two ways:')
    print('1.) Move all crash logs and the scan script into a folder with short and simple path name, example: "C:\Crash Logs"')
    print("-----")
    print('2.) Open the original crash log with Notepad, select File > Save As... and make sure that Encoding is set to UTF-8,')
    print('then press Save and overwrite the original crash log file. Run the Scan Crashlogs script again after that.')
    print("-----")
    print('FOR ALL OTHER ERRORS PLEASE CONTACT ME DIRECTLY, CONTACT INFO BELOW!')

print("======================================================================")
print("END OF AUTOSCAN | Author/Made By: Poet | 060922 | All Rights Reserved.")
print("GUI VERSION | https://www.nexusmods.com/fallout4/mods/63346")
print("============================ CONTACT INFO ============================")
print("DISCORD | Poet#9800 (https://discord.gg/DfFYJtt8p4)")
print("NEXUS MODS | https://www.nexusmods.com/users/64682231")
print("SCAN SCRIPT PAGE | https://www.nexusmods.com/fallout4/mods/56255")
print("======================================================================")
print(" ")  # AUTOSCAN LOGGING RESULTS
print("Scanned all available logs in", (str(time.time() - start_time)[:7]), "seconds.")
print(f'Number of Scanned Logs (No Autoscan Errors): {statL["scanned"]}')
print(f'Number of Incomplete Logs (No Plugins List): {statL["incomplete"]}')
print(f'Number of Failed Logs (Autoscan Can\'t Scan): {statL["failed"]}')
print(f'Number of Very Old / Wrong Formatting Logs): {statL["veryold"]}')
print("-----")
print(f'Logs with Incorrect Achievement Settings:....{statB["Achieve"]}')
print("", )
print(f'Logs with Incorrect Memory Settings:.........{statB["Memory"]}')
print(f'Logs with Incorrect Looks Menu Settings:.....{statB["F4EE"]}')
print(f'Logs with No F4SE (Should Be Always 0):......{statB["F4SE"]}')
print("-----")
print(f'Logs with Stack Overflow Crash...........{statC["Overflow"]}')
print(f'Logs with Active Effects Crash...........{statC["ActiveEffect"]}')
print(f'Logs with Bad Math Crash.................{statC["BadMath"]}')
print(f'Logs with Null Crash.....................{statC["Null"]}')
print(f'Logs with DLL Crash......................{statC["DLL"]}')
print(f'Logs with LOD Crash......................{statC["LOD"]}')
print(f'Logs with MCM Crash......................{statC["MCM"]}')
print(f'Logs with Decal Crash....................{statC["Decal"]}')
print(f'Logs with Equip Crash....................{statC["Equip"]}')
print(f'Logs with Script Crash...................{statC["Papyrus"]}')
print(f'Logs with Generic Crash..................{statC["Generic"]}')
print(f'Logs with BA2 Limit Crash................{statC["BA2Limit"]}')
print(f'Logs with Rendering Crash................{statC["Rendering"]}')
print(f'Logs with Grid Scrap Crash...............{statC["GridScrap"]}')
print(f'Logs with Mesh (NIF) Crash...............{statC["NIF"]}')
print(f'Logs with Texture (DDS) Crash............{statC["Texture"]}')
print(f'Logs with Material (BGSM) Crash..........{statC["BGSM"]}')
print(f'Logs with BitDefender Crash..............{statC["BitDefender"]}')
print(f'Logs with NPC Pathing Crash..............{statC["NPCPathing"]}')
print(f'Logs with Audio Driver Crash.............{statC["Audio"]}')
print(f'Logs with Body Physics Crash.............{statC["BodyPhysics"]}')
print(f'Logs with Plugin Limit Crash.............{statC["PluginLimit"]}')
print(f'Logs with Plugin Order Crash.............{statC["LoadOrder"]}')
print(f'Logs with MO2 Extractor Crash............{statC["MO2Unp"]}')
print(f'Logs with Nvidia Debris Crash............{statC["NVDebris"]}')
print(f'Logs with Nvidia Driver Crash............{statC["NVDriver"]}')
print(f'Logs with Vulkan Memory Crash............{statC["VulkamMem"]}')
print(f'Logs with Vulkan Settings Crash..........{statC["VulkanSet"]}')
print(f'Logs with Console Command Crash..........{statC["ConsoleCommands"]}')
print(f'Logs with Particle Effects Crash.........{statC["Particles"]}')
print(f'Logs with Animation / Physics Crash......{statC["AnimationPhysics"]}')
print(f'Logs with Archive Invalidation Crash.....{statC["Invalidation"]}')
print("-----")
print(f'Crashes caused by Clas. Hols. Weapons....{statM_CHW}')
print("-----")
print(f'Logs with *[Item Crash]..................{statU["Item"]}')
print(f'Logs with *[Save Crash]..................{statU["Save"]}')
print(f'Logs with *[Input Crash].................{statU["Input"]}')
print(f'Logs with *[Bad INI Crash]...............{statU["INI"]}')
print(f'Logs with *[NPC Patrol Crash]............{statU["Patrol"]}')
print(f'Logs with *[Precombines Crash]...........{statU["Precomb"]}')
print(f'Logs with *[Ammo Counter Crash]..........{statU["HUDAmmo"]}')
print(f'Logs with *[NPC Projectile Crash]........{statU["Projectile"]}')
print(f'Logs with *[Player Character Crash]......{statU["Player"]}')
print("*Unsolved, see How To Read Crash Logs PDF")
print("===========================================")
sys.stdout.close()
os.system("pause")
