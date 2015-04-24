#!/usr/bin/env python

from __future__ import print_function

import platform
import os, sys, wx, ConfigParser
import subprocess, threading
import flasher_gui

#wx.Log_EnableLogging()




class JLink(object):
    def __init__(self):
        """
        JLink control class

        """
        if platform.system() is "Windows":
            self.os_type = "win"
        else:
            self.os_type = "linux"
        self.pwd = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.mcu_db_file = os.path.join(self.pwd, "mcu.db")
        self.script_file = os.path.join(self.pwd, "script.jlink")
        self.config_file = os.path.join(self.pwd, "flasher.cfg")
        self.supported_speeds = ["100", "200", "400", "800", "1000"]
        self.supported_interfaces = ["JTAG", "SWD"]
        self.cmd = ""
        # Configurable var.
        self.app_file = ""
        self.supported_chips = []
        self.LoadConfig()
        print(platform.system())


    def __del__(self):
        pass

    def LoadConfig(self):
        print(self.config_file)
        config = ConfigParser.ConfigParser()
        if config.read(self.config_file):
            self.app_file = config.get('Settings', 'app_file')
            self.supported_chips = config.get('Settings', 'usr_chips').split(', ')
            return True
        else:
            self.app_file = "/opt/segger/jlink/JLinkExe"
            self.supported_chips = ["MKL25Z128xxx4", "MKL46Z256xxx4"]
            return False


    def SaveConfig(self):
        config = ConfigParser.ConfigParser()
        config.add_section("Settings")
        config.set('Settings', 'app_file', self.app_file)
        config.set('Settings', 'usr_chips', ', '.join(self.supported_chips))
        # Writing our configuration file to 'example.cfg'
        with open(self.config_file, 'wb') as configf:
            config.write(configf)
            configfile.close()


    def BuildScript(self, cmd_type, chip_type=None, interface=1, speed='100', image=None, offset='0x00000000'):
        with open(self.script_file, 'w') as jsc_file:
            jsc_file.write('si ' + str(interface) + '\n')
            jsc_file.write('speed ' + self.supported_speeds[speed] + '\n')
            jsc_file.write('device ' + self.supported_chips[chip_type] + '\n')

            if cmd_type == 'Erase':
                jsc_file.write('erase\n')
            elif cmd_type == 'Unlock':
                jsc_file.write('unlock kinetis\n')
            elif cmd_type == 'Program':
                jsc_file.write('loadbin ' + image + ', ' + offset + '\n')
            else:
                print("BuildScript: Unsuported CMD")

            jsc_file.write('r\n')
            jsc_file.write('exit\n')
            jsc_file.close()

            self.cmd = self.app_file + " -CommanderScript " + self.script_file
        return True


    def UpdateChipsColection(self):
        with open(self.script_file, 'w') as jsc_file:
            jsc_file.write('ExpDevList ' + self.mcu_db_file + '\n')
            jsc_file.write('exit\n')
            jsc_file.close()
            # Clear file if exist
            fd = open(self.mcu_db_file, 'w')
            fd.close()
            # Execute JLinkExe and generate supported MCU collection
            subprocess.call(self.app_file + " -CommanderScript " + self.script_file, shell=True)
        return True


    def LoadChipsColection(self):
        mcu_db = []
        if os.path.isfile(self.mcu_db_file) and os.access(self.mcu_db_file, os.R_OK):
            with open(self.mcu_db_file, 'r') as fd_r:
                lines = fd_r.readlines()
                fd_r.close()
                for line in lines[1:]:
                    line = line.strip('\r\n')
                    line = line.replace('"', '')
                    data = line.split(', ', 3)
                    mcu_db.append((data[0], data[1], data[2]))
        return mcu_db



class SettingsGUI(flasher_gui.ConfigDialog):
    def __init__(self, parent, jlink):
        flasher_gui.ConfigDialog.__init__(self, parent)
        self.jlink = jlink
        if self.jlink.app_file != "":
            self.m_textCtrl_jlink_path.SetValue(self.jlink.app_file)
            self.m_button_db_update.Enable(True)
            self.m_gauge_status.Enable(True)
            self.m_textCtrl_db_info.Enable(True)
            if os.path.isfile(self.jlink.mcu_db_file):
                self.m_textCtrl_db_info.Value = "OK"
                self.m_textCtrl_db_info.SetBackgroundColour(wx.Colour(200, 250, 160))

    def __del__(self):
        pass

    def OnSelectDir(self, event):
        if self.jlink.os_type is "win":
            file_filter = "JLink.exe |JLink.exe"
        else:
            file_filter = "JLinkExe |JLinkExe"
        path = wx.FileDialog(self, "Found JLink Install Dir",
                             os.path.dirname(self.m_textCtrl_jlink_path.Value),
                             "", file_filter, wx.FD_FILE_MUST_EXIST)
        if path.ShowModal() == wx.ID_OK:
            self.m_textCtrl_jlink_path.SetValue(path.Path)
            self.m_button_db_update.Enable(True)
            self.m_gauge_status.Enable(True)
            self.m_textCtrl_db_info.Enable(True)
        event.Skip()

    def OnUpdateDB(self, event):
        self.m_gauge_status.SetValue(40)
        self.m_gauge_status.Update()
        if self.jlink.UpdateChipsColection() is True:
            self.m_gauge_status.SetValue(100)
            self.m_gauge_status.Update()
            self.m_textCtrl_db_info.Value = "OK"
            self.m_textCtrl_db_info.SetBackgroundColour(wx.Colour(200, 250, 160))
        else:
            self.m_textCtrl_db_info.Value = "ERROR"
            self.m_textCtrl_db_info.SetBackgroundColour(wx.Colour(250, 200, 100))
        event.Skip()


class AddGUI(flasher_gui.TargetDialog):
    def __init__(self, parent, jlink):
        flasher_gui.TargetDialog.__init__(self, parent)
        self.jlink = jlink

        self.m_choice_vendor.AppendItems(["All",
                                          "Actel",
                                          "Analog",
                                          "Atmel",
                                          "Cypress",
                                          "Energy Micro",
                                          "Freescale",
                                          "Fujitsu",
                                          "Luminary",
                                          "Microchip",
                                          "Nordic Semi",
                                          "Nuvoton",
                                          "NXP",
                                          "Renesas",
                                          "Samsung",
                                          "Silicon Labs",
                                          "ST",
                                          "TI",
                                          "Toshiba"])
        self.m_choice_vendor.SetSelection(0)
        self.m_choice_core.AppendItems(["All",
                                        "Cortex-M0",
                                        "Cortex-M3",
                                        "Cortex-M4",
                                        "Cortex-R4",
                                        "ARM966E-S",
                                        "Cortex-A9"])
        self.m_choice_core.SetSelection(0)
        self.LoadSupportedChips("All", "All")
        self.LoadUsrChips()

    def __del__(self):
        pass

    def OnVendorChoice(self, event):
        self.LoadSupportedChips(self.m_choice_vendor.GetStringSelection(), self.m_choice_core.GetStringSelection())
        event.Skip()


    def OnCoreChoice(self, event):
        self.LoadSupportedChips(self.m_choice_vendor.GetStringSelection(), self.m_choice_core.GetStringSelection())
        event.Skip()

    def OnAdd( self, event ):
        index = self.m_listCtrl_mcu_db.GetFirstSelected()
        item = self.m_listCtrl_mcu_db.GetItem(index, 1).GetText()
        self.m_listCtrl_usr_db.InsertStringItem(self.m_listCtrl_usr_db.GetItemCount(), item)
        event.Skip()

    def OnDelete( self, event ):
        index = self.m_listCtrl_usr_db.GetFirstSelected()
        self.m_listCtrl_usr_db.DeleteItem(index)
        event.Skip()


    def LoadSupportedChips(self, vendor, core):
        self.m_listCtrl_mcu_db.ClearAll()
        self.m_listCtrl_mcu_db.InsertColumn(0, "Vendor", width=160)
        self.m_listCtrl_mcu_db.InsertColumn(1, "Device", width=250)
        self.m_listCtrl_mcu_db.InsertColumn(2, "Core", width=150)
        mcu_db = self.jlink.LoadChipsColection()
        if mcu_db != []:
            for item in mcu_db:
                if (vendor == "All" or item[0] == vendor) and (core == "All" or item[2] == core):
                    self.m_listCtrl_mcu_db.Append(item)

    def LoadUsrChips(self):
        self.m_listCtrl_usr_db.ClearAll()
        self.m_listCtrl_usr_db.InsertColumn(0, "Device", width=560)
        for item in self.jlink.supported_chips:
            self.m_listCtrl_usr_db.Append([item])


class FlasherGUI(flasher_gui.AppFrame):
    def __init__(self, parent):
        flasher_gui.AppFrame.__init__(self, parent)

        self.jlink = JLink()

        self.m_choice_target.AppendItems(self.jlink.supported_chips)
        self.m_choice_target.SetSelection(0)
        self.m_choice_dbg_interface.AppendItems(self.jlink.supported_interfaces)
        self.m_choice_dbg_interface.SetSelection(1)
        for n in self.jlink.supported_speeds:
            self.m_choice_speed.Append(n + ' kHz')
        self.m_choice_speed.SetSelection(0)
        #self.m_textCtrl_log.AppendText(self.jlink.pwd)

    def __del__(self):
        pass

    def OnOpen(self, event):
        event.Skip()

    def OnSave(self, event):
        event.Skip()

    def OnExit(self, event):
        exit()

    def OnSettings(self, event):
        m_setting_dialog = SettingsGUI(parent=None, jlink=self.jlink)
        if m_setting_dialog.ShowModal() != wx.ID_CANCEL:
            self.m_textCtrl_log.AppendText("OK\n")
            self.jlink.app_file = m_setting_dialog.m_textCtrl_jlink_path.Value
            self.jlink.SaveConfig()
        m_setting_dialog.Destroy()
        event.Skip()

    def OnAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "JLink Flasher"
        info.Version = "0.0.1 Beta"
        info.Copyright = "(C) 2014 Martin Olejar"
        info.WebSite = ("http://www.segger.com", "SEGGER Home Page")
        wx.AboutBox(info)
        event.Skip()

    def OnTargetAdd(self, event):
        m_add_dialog = AddGUI(parent=None, jlink=self.jlink)
        if m_add_dialog.ShowModal() == wx.ID_OK:
            self.m_choice_target.Clear()
            i = 0
            self.jlink.supported_chips = []
            while i < m_add_dialog.m_listCtrl_usr_db.GetItemCount():
                item = m_add_dialog.m_listCtrl_usr_db.GetItem(i, 0).GetText()
                self.m_choice_target.Append(item)
                self.jlink.supported_chips.append(item)
                i += 1
            self.m_choice_target.SetSelection(0)
            self.jlink.SaveConfig()
        m_add_dialog.Destroy()
        event.Skip()

    def OnImageUpdated(self, event):
        if self.m_filePicker_targetImage.CheckPath(self.m_filePicker_targetImage.Path):
            self.m_button_flash.Enable(True)
            self.m_textCtrl_offset.Enable(True)
        else:
            self.m_button_flash.Enable(False)
            self.m_textCtrl_offset.Enable(False)
        event.Skip()

    def OnLogEnable(self, event):
        if self.m_textCtrl_log.IsShown:
            self.m_textCtrl_log.Hide()
        else:
            self.m_textCtrl_log.Shown()
        event.Skip()

    def OnResetTarget(self, event):
        self.Execute('Reset')
        event.Skip()

    def OnUnlockTarget(self, event):
        self.Execute('Unlock')
        event.Skip()

    def OnEraseTarget(self, event):
        self.Execute('Erase')
        event.Skip()

    def OnFlashTarget(self, event):
        self.Execute('Program')
        event.Skip()

    def Execute(self, cmd):
        self.m_textCtrl_log.Clear()
        self.m_textCtrl_log.AppendText("\n<<<< " + cmd + " Target >>>> \n\n")
        status = self.jlink.BuildScript(cmd_type=cmd,
                                        chip_type=self.m_choice_target.GetSelection(),
                                        interface=self.m_choice_dbg_interface.GetSelection(),
                                        speed=self.m_choice_speed.GetSelection(),
                                        image=self.m_filePicker_targetImage.Path,
                                        offset=self.m_textCtrl_offset.Value)
        if status is True:
            try:
                thread = threading.Thread(target=self.run)
                thread.setDaemon(True)
                thread.start()
            except:
                self.m_textCtrl_log.AppendText("\n<<<< " + cmd + " Error >>>> \n")


    def run(self):
        if self.jlink.cmd != "":
            for line in subprocess.Popen(self.jlink.cmd, shell=True,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT).stdout:
                wx.CallAfter(self.m_textCtrl_log.AppendText, line)


class MyApp(wx.App):
    def OnInit(self):
        frame = FlasherGUI(None)
        frame.Show(True)
        return True


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
