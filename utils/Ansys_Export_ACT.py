import os
import shutil
import wbjn

cmd = 'returnValue(GetUserFilesDirectory())'
PROJECT_NAME = DataModel.Project.Name
GEOM = Model.Geometry
ANALYSES_COUNT = Model.Analyses.Count
COORDINATE_OUTPUT_DIR = wbjn.ExecuteCommand(ExtAPI,cmd)
print('Current output directory: ' + COORDINATE_OUTPUT_DIR)

for i in range(len(GEOM.Children)):
    GEOM.Children[i].Visible = True

def create_coordinate_results(analysis):
    named_selections = Model.NamedSelections
    solution = analysis.Solution
    coordinate_systems = Model.CoordinateSystems
    tot_child_NS_GRP = named_selections.Children.Count
    
    # Make directory
    folder_path = os.path.join(COORDINATE_OUTPUT_DIR, PROJECT_NAME, 'Analysis_' + analysis.Name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)
    
    # Setting LCS
    for i in range(tot_child_NS_GRP):
        ns = named_selections.Children[i].Name
        if ns == 'M1':
            M1 = named_selections.Children[i]
        if ns == 'M2':
            M2 = named_selections.Children[i]
            
    M1O = DataModel.GetObjectById(M1.ObjectId)
    M2O = DataModel.GetObjectById(M2.ObjectId)
    
    # Name your local Coordinates as LCS
    CS_COUNT = coordinate_systems.Children.Count
    for ii in range(CS_COUNT):
        CS_NAME = coordinate_systems.Children[ii].Name
        if CS_NAME == 'LCS':
            LCS = coordinate_systems.Children[ii]
    
    # Define results
    results = [
        ('X1', 'LOCX'),
        ('Y1', 'LOCY'),
        ('Z1', 'LOCZ'),
        ('DX1', 'LOC_DEFX'),
        ('DY1', 'LOC_DEFY'),
        ('DZ1', 'LOC_DEFZ'),
        ('X2', 'LOCX'),
        ('Y2', 'LOCY'),
        ('Z2', 'LOCZ'),
        ('DX2', 'LOC_DEFX'),
        ('DY2', 'LOC_DEFY'),
        ('DZ2', 'LOC_DEFZ')
    ]

    # Add results to solution
    variables = {}
    for name, expression in results:
        result = solution.AddUserDefinedResult()
        result.Name = name
        result.ScopingMethod = GeometryDefineByType.Component
        result.CoordinateSystem = LCS
        if name.endswith('1'):
            result.Expression = expression
            result.Location = M1O
        else:
            result.Expression = expression
            result.Location = M2O
        # Add result to variables dictionary
        variables[name] = result

    # Add group
    group = Tree.Group([variables[name] for name, _ in results])
    group.Name = 'Coordinate Group'

    # Solve and export results
    analysis.Solve(True)
    for name, _ in results:
        result = variables[name]
        result.ExportToTextFile(os.path.join(folder_path, name + '.txt'))
        

for x in range(ANALYSES_COUNT):
    analysis = Model.Analyses[x]
    create_coordinate_results(analysis)

