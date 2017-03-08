#! /usr/bin/env python
import sys
# This script is used to generate mod setup file for DST(don't  starve togerther).including
# 'dedicated_server_mods_setup.lua' ,which  in the Cluster folder,
# and
# 'modoverrides.lua' ,which in the Master folder
#
##For reference  https://steamcommunity.com/sharedfiles/filedetails/?id=591543858&searchtext=mod

if(__name__=="__main__"):
    if(len(sys.argv) != 2):
        print("No filename passed in.")
        exit()
    mod_list = sys.argv[1]
    mod_setup = "dedicated_server_mods_setup.lua"
    mod_enable_lua = "modoverrides.lua"

    with open(mod_list, mode='r') as m_list:
        with open(mod_setup,mode='w') as m_setup:
            with open(mod_enable_lua, mode='w') as m_lua:
                m_lua.write("return {\n")
                for i in m_list.readlines():
                    # print("ServerModSetup('%s')" % i.replace('\n',''))
                    m_setup.write('ServerModSetup("%s")\n' % i.replace('\n',''))
                    m_lua.write('["workshop-%s"] = { enable = true },\n' % i.replace("\n",''))
                m_lua.write("}")


