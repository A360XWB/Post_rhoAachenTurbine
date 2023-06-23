# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
p3_L160 = FindSource('p3_L1-6.0')

# set active source
SetActiveSource(p3_L160)

# get active view
spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')

# show data in view
p3_L160Display = Show(p3_L160, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
p3_L160Display.Assembly = ''

# show data in view
p3_L160Display = Show(p3_L160, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude', 'U']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude', 'U', 'vtkValidPointMask']

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L1.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L2525 = FindSource('p3_L2-5.25')

# set active source
SetActiveSource(p3_L2525)

# show data in view
p3_L2525Display = Show(p3_L2525, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L2525Display
p3_L2525Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L2.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L345 = FindSource('p3_L3-4.5')

# set active source
SetActiveSource(p3_L345)

# show data in view
p3_L345Display = Show(p3_L345, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L345Display
p3_L345Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L3.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L4375 = FindSource('p3_L4-3.75')

# set active source
SetActiveSource(p3_L4375)

# show data in view
p3_L4375Display = Show(p3_L4375, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L4375Display
p3_L4375Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L4.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L530 = FindSource('p3_L5-3.0')

# set active source
SetActiveSource(p3_L530)

# show data in view
p3_L530Display = Show(p3_L530, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L530Display
p3_L530Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L5.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L6225 = FindSource('p3_L6-2.25')

# set active source
SetActiveSource(p3_L6225)

# show data in view
p3_L6225Display = Show(p3_L6225, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L6225Display
p3_L6225Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L6.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L715 = FindSource('p3_L7-1.5')

# set active source
SetActiveSource(p3_L715)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L715)

# show data in view
p3_L715Display = Show(p3_L715, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L715Display
p3_L715Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L7.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L8075 = FindSource('p3_L8-0.75')

# set active source
SetActiveSource(p3_L8075)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L715)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L8075)

# show data in view
p3_L8075Display = Show(p3_L8075, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L8075Display
p3_L8075Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L8.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L960 = FindSource('p3_L9+0.0')

# set active source
SetActiveSource(p3_L960)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L8075)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L960)

# show data in view
p3_L960Display = Show(p3_L960, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L960Display
p3_L960Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L9.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L10075 = FindSource('p3_L10+0.75')

# set active source
SetActiveSource(p3_L10075)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L960)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L10075)

# show data in view
p3_L10075Display = Show(p3_L10075, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L10075Display
p3_L10075Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L10.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L1115 = FindSource('p3_L11+1.5')

# set active source
SetActiveSource(p3_L1115)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L10075)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L1115)

# show data in view
p3_L1115Display = Show(p3_L1115, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L1115Display
p3_L1115Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L11.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L12225 = FindSource('p3_L12+2.25')

# set active source
SetActiveSource(p3_L12225)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L1115)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L12225)

# show data in view
p3_L12225Display = Show(p3_L12225, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L12225Display
p3_L12225Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L12.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# set active source
SetActiveSource(p3_L12225)

# find source
p3_L1330 = FindSource('p3_L13+3.0')

# set active source
SetActiveSource(p3_L1330)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L12225)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L1330)

# show data in view
p3_L1330Display = Show(p3_L1330, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L1330Display
p3_L1330Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L13.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L14375 = FindSource('p3_L14+3.75')

# set active source
SetActiveSource(p3_L14375)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L1330)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L14375)

# show data in view
p3_L14375Display = Show(p3_L14375, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L14375Display
p3_L14375Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L14.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L1545 = FindSource('p3_L15+4.5')

# set active source
SetActiveSource(p3_L1545)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L14375)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L1545)

# show data in view
p3_L1545Display = Show(p3_L1545, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L1545Display
p3_L1545Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L15.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# set active source
SetActiveSource(p3_L1545)

# find source
p3_L16525 = FindSource('p3_L16+5.25')

# set active source
SetActiveSource(p3_L16525)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L1545)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L16525)

# show data in view
p3_L16525Display = Show(p3_L16525, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L16525Display
p3_L16525Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L16.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p3_L1760 = FindSource('p3_L17+6.0')

# set active source
SetActiveSource(p3_L1760)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p3_L16525)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p3_L1760)

# show data in view
p3_L1760Display = Show(p3_L1760, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p3_L1760Display
p3_L1760Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_rho_AachenTurbine_1p5/p3/p3_960_L17.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout2 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout2.SetSize(400, 400)

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
