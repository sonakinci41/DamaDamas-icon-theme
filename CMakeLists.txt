project(DamaDamas-icons NONE)

cmake_minimum_required(VERSION 2.8)
# include specific modules
set (CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

if (WIN32)
   set(ICON_INSTALL_DIR         "share/icons"             ) # The icon install dir (default ${SHARE_INSTALL_PREFIX}/share/)
else (WIN32)
   set(SHARE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}/share" )
   set(ICON_INSTALL_DIR     "${SHARE_INSTALL_PREFIX}/icons" )
endif(WIN32)

########### install files ###############

set( damadamas_icon_dirs  actions apps categories devices emblems extras mimetypes places status)



set(DAMADAMAS_INSTALL_DIR ${ICON_INSTALL_DIR}/damadamas)
install( DIRECTORY ${damadamas_icon_dirs} DESTINATION ${DAMADAMAS_INSTALL_DIR} PATTERN "*.sh" EXCLUDE )
install( FILES index.theme DESTINATION ${DAMADAMAS_INSTALL_DIR})
install(FILES colors metadata.desktop DESTINATION ${PLASMA_DATA_INSTALL_DIR}/usr/share/plasma/desktoptheme/damadamas/)

FILE(GLOB widgets widgets/*.svgz)
install( FILES ${widgets} DESTINATION ${PLASMA_DATA_INSTALL_DIR}/usr/share/plasma/desktoptheme/damadamas/widgets/ )

FILE(GLOB dialogs dialogs/*.svgz)
install( FILES ${dialogs} DESTINATION ${PLASMA_DATA_INSTALL_DIR}/usr/share/plasma/desktoptheme/damadamas/dialogs/ )

FILE(GLOB icons icons/*.svgz)
install( FILES ${icons} DESTINATION ${PLASMA_DATA_INSTALL_DIR}/usr/share/plasma/desktoptheme/damadamas/icons/ )