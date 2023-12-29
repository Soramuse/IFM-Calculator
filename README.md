# IFM-Calculator
An Algorithm for Interfragmentary Motion Calculation in Finite Element Analysis or Biomechanical Test(Maybe)

## Introduction
This calculator was designed to address the lack of a standardized evaluation criterion for interfragmentary motion (IFM) in orthopedic biomechanics experiments. Initially tailored for finite element analysis in Ansys, it has now been enhanced to accommodate datasets from any source, including pre- and post-displacement coordinates. Data exported from Abaqus, Matlab, or other software can be processed with a simple conversion to our standardized format. Give it a try – it's free!

## Highlight
•
Precise and automated calculations of IFM parameters (e.g., distance, gap, sliding).

•
Versatile and applicable to various fracture types with robust methodologies.

•
Interfragmentary Angle (IFA) offering comprehensive parameter assessment.

•
A user-friendly GUI interface allows easy data I/O, result visualization for further analysis.

•
IFM-Cal provides valuable insights into biomechanics research and implant design

## Usage
### First thing
#### For Ansys users

For users of Ansys software, you can quickly export the required data using the 'Ansys_Export_ACT.py' and 'Ansys_file_merge.py' scripts located in the 'util' folder. However, please adhere to the following recommendations:

***Important!!!***

Please use the **English** version of Ansys Workbench as the standard compatibility of other language versions cannot be guaranteed. The language for Ansys Workbench can be changed in Tools-options-Regional and language options.

Please open ***'Include Node Numbers'*** and ***'Include Node Location'*** options in the Mechanical software, which can be found in File-Options-Export.

![export options](/figures/export_option.png)

*I have conducted tests in both Ansys 2022 R2 and Ansys 2023 R1, but due to limited resources, I cannot guarantee flawless operation in all scenarios. (The debugging functionality in Ansys is truly challenging to use.)*

Next:
1. Define a local coordinate system for the fracture ends. We recommend using the plane of the fracture proximal end as the reference plane, with its centroid serving as the origin of the coordinate system. The Z-axis should be perpendicular to the plane of the fracture proximal end.

2. Create named selections for all nodes on both sides of the fracture ends, and then name them M1 and M2, respectively. M1 serves as the reference surface, while M2 represents the moving surface. In other words, all relative motion is described with respect to M1 as the frame of reference, depicting the movement of M2 relative to M1.

3. Use the scripting feature in Mechanical to load *'Ansys_Export_ACT.py'* and execute the script. Please note that the naming format for data export is related to the project name and analysis name, so to prevent data confusion, ensure that each analysis is uniquely named.

4. After export, use Python to execute *'Ansys_file_merge.py'*, which will generate two sets of data files. The exported data can be found in the *user_files* directory.

![surface and LCS](/figures/surface_and_LCS.png)

#### For other users

You can also easily use this software with just a few simple conversions.

1. Ensure that your datasets are named *'data_series_1.csv'* and *'data_series_2.csv'*. *'data_series_1.csv'* corresponds to the reference surface, while *'data_series_2.csv'* represents the moving surface. All results of relative motion are obtained by comparing the moving surface to the reference surface, so please pay attention to the order of the data.

2. Each row in the data_series represents the coordinates of a point. The first row of the data_series should be named in the following order: ***'Node number', 'LOCX', 'LOCY', 'LOCZ', 'DEF_LOCX', 'DEF_LOCY', 'DEF_LOCZ'***. I understand this may seem rigid, but for the sake of data uniformity, I consider it necessary.

3. ***Important!!!*** It is strongly recommended to establish a local coordinate system on the fracture plane and use the coordinate data from the local coordinate system for calculations. Although the global coordinate system can adequately calculate IFM distance, many functions of this calculator rely on the local coordinate system. Errors may arise when calculating IFA using the global coordinate system, so using local coordinate system coordinates not only ensures accurate IFM calculation but also provides a more intuitive interpretation of the results. 

4. If anyone has developed conversion scripts tailored to their needs, sharing them can be beneficial and assist a wider users!

![data format](/figures/data_format.png)

### Next
#### Calculate page

1. In the file input section, select the file containing the datasets.

2. Enter your desired value in the Mesh accuracy section. Please note that in most cases, inputting your mesh size will yield accurate results. However, in certain exceptional circumstances, such as non-uniform grid sizing, using the mesh size may not yield the expected values, resulting in NaN values or peculiar data. In such cases, it is advisable to increase the Mesh accuracy appropriately. You will notice that as the Mesh accuracy increases, the computation results converge. However, excessively increasing the Mesh accuracy may lead to deviation in the computation results. Therefore, indiscriminately enlarging the Mesh accuracy is not advisable.

3. The text box below displays some data from the calculation process, allowing you to quickly preview and save it.

![calculate page](/figures/calculate_page.png)

#### Figure page

On the Figure page, you can observe and rotate the image and save it as a PNG-format image. Data is displayed on the movement surface, while the blue point cloud represents the reference surface.

(I understand this image may appear rudimentary with limited functionality, but this is the best result I've achieved using Matplotlib. In the future, I will consider employing alternative methods to enhance the visualization capabilities and introduce new customizable options.)

![figure page](/figures/figure_page.png)

#### Export page

You can name the results and export the data to any folder of your choice. The exported data includes individual data files containing information for each point, which can be utilized for further data analysis. Another file named Output Summary_ contains more intuitive statistical data. The data panel on the export page allows you to swiftly preview the necessary data without requiring a separate export, which is very convenient!

![export page](/figures/export_page.png)

## TO-DO

1. Enhance image functionality
2. Improve interface for enhanced usability
3. Expand data conversion scripts
4. ...

## One More Thing

If you find it useful, feel free to reference my article and I hope you can give it a star!

https://doi.org/10.1016/j.cmpb.2023.107996

If you encounter any usage issues or have feature suggestions, please don't hesitate to reach out to me!