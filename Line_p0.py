# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
mach = FindSource('Mach')

# set active source
SetActiveSource(mach)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')

# get 2D transfer function for 'Mach'
machTF2D = GetTransferFunction2D('Mach')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
machDisplay = GetDisplayProperties(mach, view=renderView1)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# rename source object
RenameSource('p0_L', plotOverLine1)

# find source
testfoam = FindSource('test.foam')

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [0.243872849280451, 0.023474100277417, 0.01475]
plotOverLine1.Point2 = [0.298619815445451, 0.028743796258061, 0.01475]
plotOverLine1.Resolution = 50


# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display.LookupTable = pLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'p'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'U'
plotOverLine1Display.ScaleFactor = 0.005474695563316346
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 0.00027373477816581724
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [151994.921875, 0.0, 0.5, 0.0, 152064.484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [151994.921875, 0.0, 0.5, 0.0, 152064.484375, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# find source
test = FindSource('test')

# update the view to ensure updated data information
lineChartView1.Update()

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1314, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1.3696828520482391, 0.35380738220263813, -0.9366087420053069]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.18624999653548002]
renderView1.CameraViewUp = [0.28736012409727085, 0.7556147178760424, 0.5886174965186731]
renderView1.CameraParallelScale = 0.18022409643410278
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
