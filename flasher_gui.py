# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JLink Flasher", pos = wx.DefaultPosition, size = wx.Size( 550,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 550,500 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"&Exit"+ u"\t" + u"CTRL+X", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem_exit.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT,  ) )
		self.m_menu_file.AppendItem( self.m_menuItem_exit )
		
		self.m_menubar.Append( self.m_menu_file, u"&File" ) 
		
		self.m_menu_tools = wx.Menu()
		self.m_menuItem_settings = wx.MenuItem( self.m_menu_tools, wx.ID_ANY, u"&Settings"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem_settings.SetBitmap( wx.NullBitmap )
		self.m_menu_tools.AppendItem( self.m_menuItem_settings )
		
		self.m_menubar.Append( self.m_menu_tools, u"&Tools" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"&About.."+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem_about.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_FOLDER,  ) )
		self.m_menu_help.AppendItem( self.m_menuItem_about )
		
		self.m_menubar.Append( self.m_menu_help, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		fgSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		fgSizer31 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer31.AddGrowableCol( 0 )
		fgSizer31.AddGrowableRow( 2 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Target:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice_targetChoices = []
		self.m_choice_target = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_targetChoices, wx.CB_SORT )
		self.m_choice_target.SetSelection( 0 )
		self.m_choice_target.SetFont( wx.Font( 9, 74, 90, 90, False, "Sans" ) )
		self.m_choice_target.SetToolTipString( u"Select Target MCU" )
		
		bSizer6.Add( self.m_choice_target, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_button_add = wx.Button( self.m_panel2, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_add.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
		
		bSizer6.Add( self.m_button_add, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Image:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePicker_targetImage = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"BIN files (*.bin)|*.bin|HEX files (*.hex)|*.hex", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker_targetImage.SetFont( wx.Font( 9, 74, 90, 90, False, "Sans" ) )
		
		fgSizer3.Add( self.m_filePicker_targetImage, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText_offset = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Offset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_offset.Wrap( -1 )
		fgSizer3.Add( self.m_staticText_offset, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_offset = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"0x00000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl_offset.SetFont( wx.Font( 9, 74, 90, 90, False, "Sans" ) )
		self.m_textCtrl_offset.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_textCtrl_offset.Enable( False )
		self.m_textCtrl_offset.SetToolTipString( u"Set Image Offset" )
		self.m_textCtrl_offset.SetMinSize( wx.Size( 100,-1 ) )
		
		bSizer9.Add( self.m_textCtrl_offset, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Bus Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer9.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_dbg_interfaceChoices = []
		self.m_choice_dbg_interface = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_dbg_interfaceChoices, 0 )
		self.m_choice_dbg_interface.SetSelection( 0 )
		self.m_choice_dbg_interface.SetMinSize( wx.Size( 110,-1 ) )
		
		bSizer9.Add( self.m_choice_dbg_interface, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer9.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_speedChoices = []
		self.m_choice_speed = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_speedChoices, 0 )
		self.m_choice_speed.SetSelection( 0 )
		self.m_choice_speed.SetMinSize( wx.Size( 120,-1 ) )
		
		bSizer9.Add( self.m_choice_speed, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		fgSizer31.Add( fgSizer3, 1, wx.EXPAND|wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"<< Log >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetForegroundColour( wx.Colour( 80, 80, 80 ) )
		
		bSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer3.Add( self.m_staticline1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer3, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl_log = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.m_textCtrl_log.SetForegroundColour( wx.Colour( 15, 228, 100 ) )
		self.m_textCtrl_log.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		bSizer4.Add( self.m_textCtrl_log, 1, wx.EXPAND, 12 )
		
		
		fgSizer31.Add( bSizer4, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 12 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_unlock = wx.Button( self.m_panel2, wx.ID_ANY, u"Unlock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_unlock.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
		
		bSizer2.Add( self.m_button_unlock, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_reset = wx.Button( self.m_panel2, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_reset.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
		
		bSizer2.Add( self.m_button_reset, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_erase = wx.Button( self.m_panel2, wx.ID_ANY, u"Erase", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_erase.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
		
		bSizer2.Add( self.m_button_erase, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_flash = wx.Button( self.m_panel2, wx.ID_ANY, u"Flash", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_flash.SetFont( wx.Font( 9, 74, 90, 92, False, "Sans" ) )
		self.m_button_flash.Enable( False )
		
		bSizer2.Add( self.m_button_flash, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer2, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 6 )
		
		
		self.m_panel2.SetSizer( fgSizer31 )
		self.m_panel2.Layout()
		fgSizer31.Fit( self.m_panel2 )
		fgSizer.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnSettings, id = self.m_menuItem_settings.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem_about.GetId() )
		self.m_button_add.Bind( wx.EVT_BUTTON, self.OnTargetAdd )
		self.m_filePicker_targetImage.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnImageUpdated )
		self.m_button_unlock.Bind( wx.EVT_BUTTON, self.OnUnlockTarget )
		self.m_button_reset.Bind( wx.EVT_BUTTON, self.OnResetTarget )
		self.m_button_erase.Bind( wx.EVT_BUTTON, self.OnEraseTarget )
		self.m_button_flash.Bind( wx.EVT_BUTTON, self.OnFlashTarget )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnExit( self, event ):
		event.Skip()
	
	def OnSettings( self, event ):
		event.Skip()
	
	def OnAbout( self, event ):
		event.Skip()
	
	def OnTargetAdd( self, event ):
		event.Skip()
	
	def OnImageUpdated( self, event ):
		event.Skip()
	
	def OnUnlockTarget( self, event ):
		event.Skip()
	
	def OnResetTarget( self, event ):
		event.Skip()
	
	def OnEraseTarget( self, event ):
		event.Skip()
	
	def OnFlashTarget( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfigDialog
###########################################################################

class ConfigDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Flasher Settings", pos = wx.DefaultPosition, size = wx.Size( 480,160 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"JLink Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_jlink_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl_jlink_path.SetMinSize( wx.Size( -1,26 ) )
		
		bSizer10.Add( self.m_textCtrl_jlink_path, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bt_jlink_path = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bt_jlink_path, 0, wx.ALL, 5 )
		
		
		fgSizer5.Add( bSizer10, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MCU DB:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl_db_info = wx.TextCtrl( self, wx.ID_ANY, u"NA", wx.DefaultPosition, wx.Size( -1,25 ), wx.TE_CENTRE|wx.TE_READONLY )
		self.m_textCtrl_db_info.SetBackgroundColour( wx.Colour( 251, 210, 160 ) )
		self.m_textCtrl_db_info.Enable( False )
		
		bSizer5.Add( self.m_textCtrl_db_info, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_gauge_status = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,25 ), wx.GA_HORIZONTAL )
		self.m_gauge_status.SetValue( 0 ) 
		self.m_gauge_status.Enable( False )
		
		bSizer5.Add( self.m_gauge_status, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_db_update = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_db_update.Enable( False )
		
		bSizer5.Add( self.m_button_db_update, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer5.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( fgSizer5, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 10 )
		
		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();
		
		bSizer9.Add( m_sdbSizer2, 0, wx.ALIGN_RIGHT|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 10 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bt_jlink_path.Bind( wx.EVT_BUTTON, self.OnSelectDir )
		self.m_button_db_update.Bind( wx.EVT_BUTTON, self.OnUpdateDB )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSelectDir( self, event ):
		event.Skip()
	
	def OnUpdateDB( self, event ):
		event.Skip()
	

###########################################################################
## Class TargetDialog
###########################################################################

class TargetDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Supported Targets", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		
		bSizer_main = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.m_splitter.SetSashGravity( 1 )
		self.m_splitter.Bind( wx.EVT_IDLE, self.m_splitterOnIdle )
		self.m_splitter.SetMinimumPaneSize( 2 )
		
		self.m_panel_01 = wx.Panel( self.m_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText_vendor = wx.StaticText( self.m_panel_01, wx.ID_ANY, u"Manufacturer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_vendor.Wrap( -1 )
		bSizer13.Add( self.m_staticText_vendor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_vendorChoices = []
		self.m_choice_vendor = wx.Choice( self.m_panel_01, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_vendorChoices, 0 )
		self.m_choice_vendor.SetSelection( 0 )
		bSizer13.Add( self.m_choice_vendor, 1, wx.ALL, 5 )
		
		
		bSizer13.AddSpacer( ( 20, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_core = wx.StaticText( self.m_panel_01, wx.ID_ANY, u"MCU Core:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_core.Wrap( -1 )
		bSizer13.Add( self.m_staticText_core, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice_coreChoices = []
		self.m_choice_core = wx.Choice( self.m_panel_01, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_coreChoices, 0 )
		self.m_choice_core.SetSelection( 0 )
		bSizer13.Add( self.m_choice_core, 1, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer13, 1, wx.EXPAND|wx.TOP, 8 )
		
		self.m_listCtrl_mcu_db = wx.ListCtrl( self.m_panel_01, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_NO_SORT_HEADER|wx.LC_REPORT )
		fgSizer1.Add( self.m_listCtrl_mcu_db, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel_01.SetSizer( fgSizer1 )
		self.m_panel_01.Layout()
		fgSizer1.Fit( self.m_panel_01 )
		self.m_panel_02 = wx.Panel( self.m_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl_usr_db = wx.ListCtrl( self.m_panel_02, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_AUTOARRANGE|wx.LC_REPORT )
		fgSizer2.Add( self.m_listCtrl_usr_db, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel_02.SetSizer( fgSizer2 )
		self.m_panel_02.Layout()
		fgSizer2.Fit( self.m_panel_02 )
		self.m_splitter.SplitHorizontally( self.m_panel_01, self.m_panel_02, 280 )
		bSizer_main.Add( self.m_splitter, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_main.Add( self.m_staticline, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )
		
		m_sdbSizer = wx.StdDialogButtonSizer()
		self.m_sdbSizerOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer.AddButton( self.m_sdbSizerOK )
		self.m_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer.AddButton( self.m_sdbSizerCancel )
		m_sdbSizer.Realize();
		
		bSizer_main.Add( m_sdbSizer, 0, wx.EXPAND|wx.ALL, 10 )
		
		
		self.SetSizer( bSizer_main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choice_vendor.Bind( wx.EVT_CHOICE, self.OnVendorChoice )
		self.m_choice_core.Bind( wx.EVT_CHOICE, self.OnCoreChoice )
		self.m_listCtrl_mcu_db.Bind( wx.EVT_LEFT_DCLICK, self.OnAdd )
		self.m_listCtrl_usr_db.Bind( wx.EVT_LEFT_DCLICK, self.OnDelete )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnVendorChoice( self, event ):
		event.Skip()
	
	def OnCoreChoice( self, event ):
		event.Skip()
	
	def OnAdd( self, event ):
		event.Skip()
	
	def OnDelete( self, event ):
		event.Skip()
	
	def m_splitterOnIdle( self, event ):
		self.m_splitter.SetSashPosition( 280 )
		self.m_splitter.Unbind( wx.EVT_IDLE )
	

