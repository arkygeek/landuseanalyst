; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "Landuse Analyst"
!define PRODUCT_VERSION "0.0.1"
!define PRODUCT_PUBLISHER "http://code.google.com/p/landuseanalyst/"
!define PRODUCT_WEB_SITE "http://code.google.com/p/landuseanalyst/"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\landuseanalyst.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

SetCompressor zlib
; Added by Tim for setting env vars (see this file on disk)
!include WriteEnvStr.nsh

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "..\src\gui\la64x64.ico"
!define MUI_UNICON "..\src\gui\la64x64.ico"
; Added by Tim for side image
!define MUI_WELCOMEFINISHPAGE_BITMAP "la_logo.bmp"
; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!define MUI_LICENSEPAGE_RADIOBUTTONS
!insertmacro MUI_PAGE_LICENSE "..\LICENSE.txt"
; Components page
!insertmacro MUI_PAGE_COMPONENTS
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Start menu page
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "Landuse Analyst"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\landuseanalyst.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; Language files
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "PortugueseBR" 
;!insertmacro MUI_LANGUAGE "French" 
;!insertmacro MUI_LANGUAGE "German" 
;!insertmacro MUI_LANGUAGE "SimpChinese" 
;!insertmacro MUI_LANGUAGE "Japanese" 
;!insertmacro MUI_LANGUAGE "Italian" 
;!insertmacro MUI_LANGUAGE "Swedish" 
;!insertmacro MUI_LANGUAGE "Russian" 
;!insertmacro MUI_LANGUAGE "Portuguese" 
;!insertmacro MUI_LANGUAGE "Polish" 
;!insertmacro MUI_LANGUAGE "Czech" 
;!insertmacro MUI_LANGUAGE "Slovak" 
;!insertmacro MUI_LANGUAGE "Latvian" 
;!insertmacro MUI_LANGUAGE "Indonesian" 

; Initialize language
Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd


; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "LanduseAnalystSetup${PRODUCT_VERSION}.exe"
InstallDir "$PROGRAMFILES\Landuse Analyst"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show


Section "Application" SEC01
  ;this section is mandatory
  SectionIn RO
  ;Added by Tim to install for all users not just the logged in user..
  ;make sure this is at the top of the section
  SetShellVarContext all
  
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File "c:\Program Files\landuseanalyst\landuseanalyst.exe"
  SetOverwrite try
;------- Qt 
  File "c:\Program Files\landuseanalyst\QtCore4.dll"
  File "c:\Program Files\landuseanalyst\QtGui4.dll"
  ;File "c:\Program Files\landuseanalyst\QtNetwork4.dll"
  File "c:\Program Files\landuseanalyst\QtXml4.dll"
  File "c:\Program Files\landuseanalyst\mingwm10.dll"
; Shortcuts
; Next line is important - added by Tim
; if its not there the application working dir will be the last used
;outpath and libom wont be able to find its alg
  SetOutPath "$INSTDIR"
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Landuse Analyst.lnk" "$INSTDIR\landuseanalyst.exe"
  CreateShortCut "$DESKTOP\Landuse Analyst.lnk" "$INSTDIR\landuseanalyst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END

SectionEnd


Section -AdditionalIcons
  SetOutPath $INSTDIR
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  ; its more consistant to let user remove the app from add/remove progs in control panel
  ;CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\landuseanalyst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\landuseanalyst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

; Section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} "Main application files - you really need this!"
!insertmacro MUI_FUNCTION_DESCRIPTION_END


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  ;Added by Tim to install for all users not just the logged in user..
  ;make sure this is at the top of the section
  SetShellVarContext all
  # remove the variable
  Push PROJ_LIB
  Call un.DeleteEnvStr

  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
;---------- Qt Requirements
  ;Delete "$INSTDIR\QtNetwork4.dll"
  Delete "$INSTDIR\QtGui4.dll"
  Delete "$INSTDIR\QtCore4.dll"
  Delete "$INSTDIR\QtXml4.dll"
  Delete "$INSTDIR\mingwm10.dll"
  ;Delete "$INSTDIR\*.qm"
;---------------- app related
  Delete "$INSTDIR\landuseanalyst.exe"

;----------------- icons and shortcuts
  ;Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\Landuse Analyst.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Landuse Analyst.lnk"
  RMDir "$SMPROGRAMS\$ICONS_GROUP"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd
