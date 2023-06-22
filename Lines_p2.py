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

# get active source.
mach = GetActiveSource()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

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
plotOverLine1Display.ScaleFactor = 0.0053366094827651984
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 0.00026683047413825987
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

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
plotOverLine1Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

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

# rename source object
RenameSource('p2_L1-6.0', plotOverLine1)

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_1 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_1.Resolution = 50
plotOverLine1_1.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_1.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_1Display = Show(plotOverLine1_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_1Display.Representation = 'Surface'
plotOverLine1_1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_1Display.LookupTable = pLUT
plotOverLine1_1Display.SelectTCoordArray = 'None'
plotOverLine1_1Display.SelectNormalArray = 'None'
plotOverLine1_1Display.SelectTangentArray = 'None'
plotOverLine1_1Display.OSPRayScaleArray = 'p'
plotOverLine1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_1Display.SelectOrientationVectors = 'U'
plotOverLine1_1Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_1Display.SelectScaleArray = 'p'
plotOverLine1_1Display.GlyphType = 'Arrow'
plotOverLine1_1Display.GlyphTableIndexArray = 'p'
plotOverLine1_1Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_1Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_1Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_1Display_1 = Show(plotOverLine1_1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_1Display_1.UseIndexForXAxis = 0
plotOverLine1_1Display_1.XArrayName = 'arc_length'
plotOverLine1_1Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_1Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_1Display_1.SeriesLabelPrefix = ''
plotOverLine1_1Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_1Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_1Display_1
plotOverLine1_1Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_1Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_1Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_1Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_1Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_1Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_1Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L2-5.25', plotOverLine1_1)

# find source
p0_L2525 = FindSource('p0_L2-5.25')

# find source
testfoam = FindSource('test.foam')

# Properties modified on plotOverLine1_1
plotOverLine1_1.Resolution = 50
plotOverLine1_1.Point1 = [0.236925412291114, 0.06238067818392, 0.171]
plotOverLine1_1.Point2 = [0.290112749744221, 0.076384503898677, 0.171]

# find source
p0_L8075 = FindSource('p0_L8-0.75')

# find source
p0_L1760 = FindSource('p0_L17+6.0')

# find source
p0_L1330 = FindSource('p0_L13+3.0')

# find source
p0_L1545 = FindSource('p0_L15+4.5')

# find source
p0_L160 = FindSource('p0_L1-6.0')

# find source
p0_L12225 = FindSource('p0_L12+2.25')

# find source
p0_L14375 = FindSource('p0_L14+3.75')

# find source
p0_L715 = FindSource('p0_L7-1.5')

# find source
p0_L900 = FindSource('p0_L9+0.0')

# find source
p0_L4375 = FindSource('p0_L4-3.75')

# find source
p0_L345 = FindSource('p0_L3-4.5')

# find source
p0_L10075 = FindSource('p0_L10+0.75')

# find source
p0_L6225 = FindSource('p0_L6-2.25')

# find source
p0_L530 = FindSource('p0_L5-3.0')

# find source
p0_L1115 = FindSource('p0_L11+1.5')

# find source
p0_L16525 = FindSource('p0_L16+5.25')

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_2 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_2.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_2.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_2Display = Show(plotOverLine1_2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_2Display.Representation = 'Surface'
plotOverLine1_2Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_2Display.LookupTable = pLUT
plotOverLine1_2Display.SelectTCoordArray = 'None'
plotOverLine1_2Display.SelectNormalArray = 'None'
plotOverLine1_2Display.SelectTangentArray = 'None'
plotOverLine1_2Display.OSPRayScaleArray = 'p'
plotOverLine1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_2Display.SelectOrientationVectors = 'U'
plotOverLine1_2Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_2Display.SelectScaleArray = 'p'
plotOverLine1_2Display.GlyphType = 'Arrow'
plotOverLine1_2Display.GlyphTableIndexArray = 'p'
plotOverLine1_2Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_2Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_2Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_2Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_2Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_2Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_2Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_2Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_2Display_1 = Show(plotOverLine1_2, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_2Display_1.UseIndexForXAxis = 0
plotOverLine1_2Display_1.XArrayName = 'arc_length'
plotOverLine1_2Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_2Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_2Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_2Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_2Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_2Display_1.SeriesLabelPrefix = ''
plotOverLine1_2Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_2Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_2Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_2Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_2Display_1
plotOverLine1_2Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_2Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_2Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_2Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_2Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_2Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_2Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L3-4.5', plotOverLine1_2)

# Properties modified on plotOverLine1_2
plotOverLine1_2.Resolution = 50
plotOverLine1_2.Point1 = [0.23608857646737, 0.065476591707349, 0.171]
plotOverLine1_2.Point2 = [0.289088052817187, 0.080175418417162, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_3 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_3.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_3.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_3Display = Show(plotOverLine1_3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_3Display.Representation = 'Surface'
plotOverLine1_3Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_3Display.LookupTable = pLUT
plotOverLine1_3Display.SelectTCoordArray = 'None'
plotOverLine1_3Display.SelectNormalArray = 'None'
plotOverLine1_3Display.SelectTangentArray = 'None'
plotOverLine1_3Display.OSPRayScaleArray = 'p'
plotOverLine1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_3Display.SelectOrientationVectors = 'U'
plotOverLine1_3Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_3Display.SelectScaleArray = 'p'
plotOverLine1_3Display.GlyphType = 'Arrow'
plotOverLine1_3Display.GlyphTableIndexArray = 'p'
plotOverLine1_3Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_3Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_3Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_3Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_3Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_3Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_3Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_3Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_3Display_1 = Show(plotOverLine1_3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_3Display_1.UseIndexForXAxis = 0
plotOverLine1_3Display_1.XArrayName = 'arc_length'
plotOverLine1_3Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_3Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_3Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_3Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_3Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_3Display_1.SeriesLabelPrefix = ''
plotOverLine1_3Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_3Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_3Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_3Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_3Display_1
plotOverLine1_3Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_3Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_3Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_3Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_3Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_3Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_3Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L4-3.75', plotOverLine1_3)

# Properties modified on plotOverLine1_3
plotOverLine1_3.Resolution = 50
plotOverLine1_3.Point1 = [0.235211288081435, 0.068561286153864, 0.171]
plotOverLine1_3.Point2 = [0.288013822140533, 0.083952595290446, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_4 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_4.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_4.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_4Display = Show(plotOverLine1_4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_4Display.Representation = 'Surface'
plotOverLine1_4Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_4Display.LookupTable = pLUT
plotOverLine1_4Display.SelectTCoordArray = 'None'
plotOverLine1_4Display.SelectNormalArray = 'None'
plotOverLine1_4Display.SelectTangentArray = 'None'
plotOverLine1_4Display.OSPRayScaleArray = 'p'
plotOverLine1_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_4Display.SelectOrientationVectors = 'U'
plotOverLine1_4Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_4Display.SelectScaleArray = 'p'
plotOverLine1_4Display.GlyphType = 'Arrow'
plotOverLine1_4Display.GlyphTableIndexArray = 'p'
plotOverLine1_4Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_4Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_4Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_4Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_4Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_4Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_4Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_4Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_4Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_4Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_4Display_1 = Show(plotOverLine1_4, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_4Display_1.UseIndexForXAxis = 0
plotOverLine1_4Display_1.XArrayName = 'arc_length'
plotOverLine1_4Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_4Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_4Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_4Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_4Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_4Display_1.SeriesLabelPrefix = ''
plotOverLine1_4Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_4Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_4Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_4Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_4Display_1
plotOverLine1_4Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_4Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_4Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_4Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_4Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_4Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_4Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L5-3.0', plotOverLine1_4)

# Properties modified on plotOverLine1_4
plotOverLine1_4.Resolution = 50
plotOverLine1_4.Point1 = [0.234293697452159, 0.071634232976951, 0.171]
plotOverLine1_4.Point2 = [0.286890241778154, 0.087715387318716, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_5 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_5.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_5.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_5Display = Show(plotOverLine1_5, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_5Display.Representation = 'Surface'
plotOverLine1_5Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_5Display.LookupTable = pLUT
plotOverLine1_5Display.SelectTCoordArray = 'None'
plotOverLine1_5Display.SelectNormalArray = 'None'
plotOverLine1_5Display.SelectTangentArray = 'None'
plotOverLine1_5Display.OSPRayScaleArray = 'p'
plotOverLine1_5Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_5Display.SelectOrientationVectors = 'U'
plotOverLine1_5Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_5Display.SelectScaleArray = 'p'
plotOverLine1_5Display.GlyphType = 'Arrow'
plotOverLine1_5Display.GlyphTableIndexArray = 'p'
plotOverLine1_5Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_5Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_5Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_5Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_5Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_5Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_5Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_5Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_5Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_5Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_5Display_1 = Show(plotOverLine1_5, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_5Display_1.UseIndexForXAxis = 0
plotOverLine1_5Display_1.XArrayName = 'arc_length'
plotOverLine1_5Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_5Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_5Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_5Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_5Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_5Display_1.SeriesLabelPrefix = ''
plotOverLine1_5Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_5Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_5Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_5Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_5Display_1
plotOverLine1_5Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_5Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_5Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_5Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_5Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_5Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_5Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L5-2.25', plotOverLine1_5)

# rename source object
RenameSource('p2_L6-2.25', plotOverLine1_5)

# Properties modified on plotOverLine1_5
plotOverLine1_5.Resolution = 50
plotOverLine1_5.Point1 = [0.233335961803972, 0.074694905642992, 0.171]
plotOverLine1_5.Point2 = [0.285717504249761, 0.091463149766928, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_6 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_6.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_6.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_6Display = Show(plotOverLine1_6, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_6Display.Representation = 'Surface'
plotOverLine1_6Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_6Display.LookupTable = pLUT
plotOverLine1_6Display.SelectTCoordArray = 'None'
plotOverLine1_6Display.SelectNormalArray = 'None'
plotOverLine1_6Display.SelectTangentArray = 'None'
plotOverLine1_6Display.OSPRayScaleArray = 'p'
plotOverLine1_6Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_6Display.SelectOrientationVectors = 'U'
plotOverLine1_6Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_6Display.SelectScaleArray = 'p'
plotOverLine1_6Display.GlyphType = 'Arrow'
plotOverLine1_6Display.GlyphTableIndexArray = 'p'
plotOverLine1_6Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_6Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_6Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_6Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_6Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_6Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_6Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_6Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_6Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_6Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_6Display_1 = Show(plotOverLine1_6, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_6Display_1.UseIndexForXAxis = 0
plotOverLine1_6Display_1.XArrayName = 'arc_length'
plotOverLine1_6Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_6Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_6Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_6Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_6Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_6Display_1.SeriesLabelPrefix = ''
plotOverLine1_6Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_6Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_6Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_6Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_6Display_1
plotOverLine1_6Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_6Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_6Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_6Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_6Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_6Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_6Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L7-1.5', plotOverLine1_6)

# Properties modified on plotOverLine1_6
plotOverLine1_6.Resolution = 50
plotOverLine1_6.Point1 = [0.232338245239946, 0.077742779721481, 0.171]
plotOverLine1_6.Point2 = [0.284495810497893, 0.095195240475282, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_7 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_7.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_7.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_7Display = Show(plotOverLine1_7, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_7Display.Representation = 'Surface'
plotOverLine1_7Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_7Display.LookupTable = pLUT
plotOverLine1_7Display.SelectTCoordArray = 'None'
plotOverLine1_7Display.SelectNormalArray = 'None'
plotOverLine1_7Display.SelectTangentArray = 'None'
plotOverLine1_7Display.OSPRayScaleArray = 'p'
plotOverLine1_7Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_7Display.SelectOrientationVectors = 'U'
plotOverLine1_7Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_7Display.SelectScaleArray = 'p'
plotOverLine1_7Display.GlyphType = 'Arrow'
plotOverLine1_7Display.GlyphTableIndexArray = 'p'
plotOverLine1_7Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_7Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_7Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_7Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_7Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_7Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_7Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_7Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_7Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_7Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_7Display_1 = Show(plotOverLine1_7, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_7Display_1.UseIndexForXAxis = 0
plotOverLine1_7Display_1.XArrayName = 'arc_length'
plotOverLine1_7Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_7Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_7Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_7Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_7Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_7Display_1.SeriesLabelPrefix = ''
plotOverLine1_7Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_7Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_7Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_7Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_7Display_1
plotOverLine1_7Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_7Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_7Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_7Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_7Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_7Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_7Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L8-0.75', plotOverLine1_7)

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_8 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_8.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_8.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_8Display = Show(plotOverLine1_8, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_8Display.Representation = 'Surface'
plotOverLine1_8Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_8Display.LookupTable = pLUT
plotOverLine1_8Display.SelectTCoordArray = 'None'
plotOverLine1_8Display.SelectNormalArray = 'None'
plotOverLine1_8Display.SelectTangentArray = 'None'
plotOverLine1_8Display.OSPRayScaleArray = 'p'
plotOverLine1_8Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_8Display.SelectOrientationVectors = 'U'
plotOverLine1_8Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_8Display.SelectScaleArray = 'p'
plotOverLine1_8Display.GlyphType = 'Arrow'
plotOverLine1_8Display.GlyphTableIndexArray = 'p'
plotOverLine1_8Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_8Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_8Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_8Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_8Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_8Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_8Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_8Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_8Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_8Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_8Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_8Display_1 = Show(plotOverLine1_8, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_8Display_1.UseIndexForXAxis = 0
plotOverLine1_8Display_1.XArrayName = 'arc_length'
plotOverLine1_8Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_8Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_8Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_8Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_8Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_8Display_1.SeriesLabelPrefix = ''
plotOverLine1_8Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_8Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_8Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_8Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_8Display_1
plotOverLine1_8Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_8Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_8Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_8Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_8Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_8Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_8Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L9+0.0', plotOverLine1_8)

# Properties modified on plotOverLine1_8
plotOverLine1_8.Resolution = 50
plotOverLine1_8.Point1 = [0.23022356, 0.083798045448127, 0.171]
plotOverLine1_8.Point2 = [0.2819064, 0.102609851569135, 0.171]

# Properties modified on plotOverLine1_7
plotOverLine1_7.Resolution = 50
plotOverLine1_7.Point1 = [0.231300718713679, 0.080777332974885, 0.171]
plotOverLine1_7.Point2 = [0.283225369853485, 0.098911019969247, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_9 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_9.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_9.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_9Display = Show(plotOverLine1_9, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_9Display.Representation = 'Surface'
plotOverLine1_9Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_9Display.LookupTable = pLUT
plotOverLine1_9Display.SelectTCoordArray = 'None'
plotOverLine1_9Display.SelectNormalArray = 'None'
plotOverLine1_9Display.SelectTangentArray = 'None'
plotOverLine1_9Display.OSPRayScaleArray = 'p'
plotOverLine1_9Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_9Display.SelectOrientationVectors = 'U'
plotOverLine1_9Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_9Display.SelectScaleArray = 'p'
plotOverLine1_9Display.GlyphType = 'Arrow'
plotOverLine1_9Display.GlyphTableIndexArray = 'p'
plotOverLine1_9Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_9Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_9Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_9Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_9Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_9Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_9Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_9Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_9Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_9Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_9Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_9Display_1 = Show(plotOverLine1_9, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_9Display_1.UseIndexForXAxis = 0
plotOverLine1_9Display_1.XArrayName = 'arc_length'
plotOverLine1_9Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_9Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_9Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_9Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_9Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_9Display_1.SeriesLabelPrefix = ''
plotOverLine1_9Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_9Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_9Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_9Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_9Display_1
plotOverLine1_9Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_9Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_9Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_9Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_9Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_9Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_9Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L10+0.75', plotOverLine1_9)

# Properties modified on plotOverLine1_9
plotOverLine1_9.Resolution = 50
plotOverLine1_9.Point1 = [0.22910695366450973, 0.086804399557675, 0.171]
plotOverLine1_9.Point2 = [0.280539126936133, 0.106291101499194, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_10 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_10.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_10.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_10Display = Show(plotOverLine1_10, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_10Display.Representation = 'Surface'
plotOverLine1_10Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_10Display.LookupTable = pLUT
plotOverLine1_10Display.SelectTCoordArray = 'None'
plotOverLine1_10Display.SelectNormalArray = 'None'
plotOverLine1_10Display.SelectTangentArray = 'None'
plotOverLine1_10Display.OSPRayScaleArray = 'p'
plotOverLine1_10Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_10Display.SelectOrientationVectors = 'U'
plotOverLine1_10Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_10Display.SelectScaleArray = 'p'
plotOverLine1_10Display.GlyphType = 'Arrow'
plotOverLine1_10Display.GlyphTableIndexArray = 'p'
plotOverLine1_10Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_10Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_10Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_10Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_10Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_10Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_10Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_10Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_10Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_10Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_10Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_10Display_1 = Show(plotOverLine1_10, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_10Display_1.UseIndexForXAxis = 0
plotOverLine1_10Display_1.XArrayName = 'arc_length'
plotOverLine1_10Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_10Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_10Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_10Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_10Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_10Display_1.SeriesLabelPrefix = ''
plotOverLine1_10Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_10Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_10Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_10Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_10Display_1
plotOverLine1_10Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_10Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_10Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_10Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_10Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_10Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_10Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L11+1.5', plotOverLine1_10)

# Properties modified on plotOverLine1_10
plotOverLine1_10.Resolution = 50
plotOverLine1_10.Point1 = [0.227951091031953, 0.08979588018023, 0.171]
plotOverLine1_10.Point2 = [0.279123784937086, 0.109954138996199, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_11 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_11.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_11.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_11Display = Show(plotOverLine1_11, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_11Display.Representation = 'Surface'
plotOverLine1_11Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_11Display.LookupTable = pLUT
plotOverLine1_11Display.SelectTCoordArray = 'None'
plotOverLine1_11Display.SelectNormalArray = 'None'
plotOverLine1_11Display.SelectTangentArray = 'None'
plotOverLine1_11Display.OSPRayScaleArray = 'p'
plotOverLine1_11Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_11Display.SelectOrientationVectors = 'U'
plotOverLine1_11Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_11Display.SelectScaleArray = 'p'
plotOverLine1_11Display.GlyphType = 'Arrow'
plotOverLine1_11Display.GlyphTableIndexArray = 'p'
plotOverLine1_11Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_11Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_11Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_11Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_11Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_11Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_11Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_11Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_11Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_11Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_11Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_11Display_1 = Show(plotOverLine1_11, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_11Display_1.UseIndexForXAxis = 0
plotOverLine1_11Display_1.XArrayName = 'arc_length'
plotOverLine1_11Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_11Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_11Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_11Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_11Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_11Display_1.SeriesLabelPrefix = ''
plotOverLine1_11Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_11Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_11Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_11Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_11Display_1
plotOverLine1_11Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_11Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_11Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_11Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_11Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_11Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_11Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L13+2.25', plotOverLine1_11)

# rename source object
RenameSource('p2_L12+2.25', plotOverLine1_11)

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_12 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_12.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_12.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_12Display = Show(plotOverLine1_12, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_12Display.Representation = 'Surface'
plotOverLine1_12Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_12Display.LookupTable = pLUT
plotOverLine1_12Display.SelectTCoordArray = 'None'
plotOverLine1_12Display.SelectNormalArray = 'None'
plotOverLine1_12Display.SelectTangentArray = 'None'
plotOverLine1_12Display.OSPRayScaleArray = 'p'
plotOverLine1_12Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_12Display.SelectOrientationVectors = 'U'
plotOverLine1_12Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_12Display.SelectScaleArray = 'p'
plotOverLine1_12Display.GlyphType = 'Arrow'
plotOverLine1_12Display.GlyphTableIndexArray = 'p'
plotOverLine1_12Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_12Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_12Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_12Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_12Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_12Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_12Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_12Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_12Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_12Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_12Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_12Display_1 = Show(plotOverLine1_12, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_12Display_1.UseIndexForXAxis = 0
plotOverLine1_12Display_1.XArrayName = 'arc_length'
plotOverLine1_12Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_12Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_12Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_12Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_12Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_12Display_1.SeriesLabelPrefix = ''
plotOverLine1_12Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_12Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_12Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_12Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_12Display_1
plotOverLine1_12Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_12Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_12Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_12Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_12Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_12Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_12Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L13+3.0', plotOverLine1_12)

# Properties modified on plotOverLine1_12
plotOverLine1_12.Resolution = 50
plotOverLine1_12.Point1 = [0.225522395772524, 0.095732173301461, 0.171]
plotOverLine1_12.Point2 = [0.27614987237452, 0.117223069348727, 0.171]

# Properties modified on plotOverLine1_11
plotOverLine1_11.Resolution = 50
plotOverLine1_11.Point1 = [0.226756170153445, 0.092771974740985, 0.171]
plotOverLine1_11.Point2 = [0.277660616514422, 0.113598336417533, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_13 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_13.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_13.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_13Display = Show(plotOverLine1_13, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_13Display.Representation = 'Surface'
plotOverLine1_13Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_13Display.LookupTable = pLUT
plotOverLine1_13Display.SelectTCoordArray = 'None'
plotOverLine1_13Display.SelectNormalArray = 'None'
plotOverLine1_13Display.SelectTangentArray = 'None'
plotOverLine1_13Display.OSPRayScaleArray = 'p'
plotOverLine1_13Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_13Display.SelectOrientationVectors = 'U'
plotOverLine1_13Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_13Display.SelectScaleArray = 'p'
plotOverLine1_13Display.GlyphType = 'Arrow'
plotOverLine1_13Display.GlyphTableIndexArray = 'p'
plotOverLine1_13Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_13Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_13Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_13Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_13Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_13Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_13Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_13Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_13Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_13Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_13Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_13Display_1 = Show(plotOverLine1_13, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_13Display_1.UseIndexForXAxis = 0
plotOverLine1_13Display_1.XArrayName = 'arc_length'
plotOverLine1_13Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_13Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_13Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_13Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_13Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_13Display_1.SeriesLabelPrefix = ''
plotOverLine1_13Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_13Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_13Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_13Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_13Display_1
plotOverLine1_13Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_13Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_13Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_13Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_13Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_13Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_13Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L14+3.75', plotOverLine1_13)

# Properties modified on plotOverLine1_13
plotOverLine1_13.Resolution = 50
plotOverLine1_13.Point1 = [0.224249979290081, 0.098675968646871, 0.171]
plotOverLine1_13.Point2 = [0.274591811375609, 0.120827716710455, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_14 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_14.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_14.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_14Display = Show(plotOverLine1_14, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_14Display.Representation = 'Surface'
plotOverLine1_14Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_14Display.LookupTable = pLUT
plotOverLine1_14Display.SelectTCoordArray = 'None'
plotOverLine1_14Display.SelectNormalArray = 'None'
plotOverLine1_14Display.SelectTangentArray = 'None'
plotOverLine1_14Display.OSPRayScaleArray = 'p'
plotOverLine1_14Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_14Display.SelectOrientationVectors = 'U'
plotOverLine1_14Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_14Display.SelectScaleArray = 'p'
plotOverLine1_14Display.GlyphType = 'Arrow'
plotOverLine1_14Display.GlyphTableIndexArray = 'p'
plotOverLine1_14Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_14Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_14Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_14Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_14Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_14Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_14Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_14Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_14Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_14Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_14Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_14Display_1 = Show(plotOverLine1_14, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_14Display_1.UseIndexForXAxis = 0
plotOverLine1_14Display_1.XArrayName = 'arc_length'
plotOverLine1_14Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_14Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_14Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_14Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_14Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_14Display_1.SeriesLabelPrefix = ''
plotOverLine1_14Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_14Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_14Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_14Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_14Display_1
plotOverLine1_14Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_14Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_14Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_14Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_14Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_14Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_14Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L15+4.5', plotOverLine1_14)

# Properties modified on plotOverLine1_14
plotOverLine1_14.Resolution = 50
plotOverLine1_14.Point1 = [0.222939138728128, 0.10160285637304, 0.171]
plotOverLine1_14.Point2 = [0.272986700483422, 0.124411660864947, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_15 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_15.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_15.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_15Display = Show(plotOverLine1_15, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_15Display.Representation = 'Surface'
plotOverLine1_15Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_15Display.LookupTable = pLUT
plotOverLine1_15Display.SelectTCoordArray = 'None'
plotOverLine1_15Display.SelectNormalArray = 'None'
plotOverLine1_15Display.SelectTangentArray = 'None'
plotOverLine1_15Display.OSPRayScaleArray = 'p'
plotOverLine1_15Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_15Display.SelectOrientationVectors = 'U'
plotOverLine1_15Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_15Display.SelectScaleArray = 'p'
plotOverLine1_15Display.GlyphType = 'Arrow'
plotOverLine1_15Display.GlyphTableIndexArray = 'p'
plotOverLine1_15Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_15Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_15Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_15Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_15Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_15Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_15Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_15Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_15Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_15Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_15Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_15Display_1 = Show(plotOverLine1_15, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_15Display_1.UseIndexForXAxis = 0
plotOverLine1_15Display_1.XArrayName = 'arc_length'
plotOverLine1_15Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_15Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_15Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_15Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_15Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_15Display_1.SeriesLabelPrefix = ''
plotOverLine1_15Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_15Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_15Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_15Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_15Display_1
plotOverLine1_15Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_15Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_15Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_15Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_15Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_15Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_15Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L16+5.25', plotOverLine1_15)

# Properties modified on plotOverLine1_15
plotOverLine1_15.Resolution = 50
plotOverLine1_15.Point1 = [0.221590098692448, 0.104512334972821, 0.171]
plotOverLine1_15.Point2 = [0.271334814725446, 0.127974287721822, 0.171]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(mach)

# create a new 'Plot Over Line'
plotOverLine1_16 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1_16.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1_16.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# show data in view
plotOverLine1_16Display = Show(plotOverLine1_16, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1_16Display.Representation = 'Surface'
plotOverLine1_16Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1_16Display.LookupTable = pLUT
plotOverLine1_16Display.SelectTCoordArray = 'None'
plotOverLine1_16Display.SelectNormalArray = 'None'
plotOverLine1_16Display.SelectTangentArray = 'None'
plotOverLine1_16Display.OSPRayScaleArray = 'p'
plotOverLine1_16Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1_16Display.SelectOrientationVectors = 'U'
plotOverLine1_16Display.ScaleFactor = 0.0053366094827651984
plotOverLine1_16Display.SelectScaleArray = 'p'
plotOverLine1_16Display.GlyphType = 'Arrow'
plotOverLine1_16Display.GlyphTableIndexArray = 'p'
plotOverLine1_16Display.GaussianRadius = 0.00026683047413825987
plotOverLine1_16Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1_16Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1_16Display.OpacityArray = ['POINTS', 'p']
plotOverLine1_16Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1_16Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1_16Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1_16Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1_16Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1_16Display.ScaleTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1_16Display.OpacityTransferFunction.Points = [129221.921875, 0.0, 0.5, 0.0, 135317.421875, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1_16Display_1 = Show(plotOverLine1_16, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1_16Display_1.UseIndexForXAxis = 0
plotOverLine1_16Display_1.XArrayName = 'arc_length'
plotOverLine1_16Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_16Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1_16Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'T', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_X', '0', '0', '0', 'U_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotOverLine1_16Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'T', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1_16Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_16Display_1.SeriesLabelPrefix = ''
plotOverLine1_16Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_16Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1_16Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1_16Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1_16Display_1
plotOverLine1_16Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'T', 'U_Magnitude']
plotOverLine1_16Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1_16Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_16Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1_16Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1_16Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1_16Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# rename source object
RenameSource('p2_L17+6.0', plotOverLine1_16)

# Properties modified on plotOverLine1_16
plotOverLine1_16.Resolution = 50
plotOverLine1_16.Point1 = [0.220203090334106, 0.107403905922037, 0.171]
plotOverLine1_16.Point2 = [0.269636437143803, 0.13151498684331, 0.171]

# update the view to ensure updated data information
renderView1.Update()

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
