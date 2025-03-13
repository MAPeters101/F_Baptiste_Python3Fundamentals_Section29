'''
Question 1
The accompanying file data.csv contains information for the value x of
something observed at time t.

Given this data, we want to calculate the rate of change of this value over
time - we'll do this by taking two consecutive observations, say
 and
 and approximate the rate of change using this formula:



For example, if the data looks like this:

t     x
0.1   10
0.2   12
0.4   14
0.5   15
Then the first row of data would be considered
, the second row
, etc

And we can start approximating the rate of change starting at
 which would be calculated as:



Similarly,
 would be calculated as:



Use NumPy arrays to create an array that holds the calculated rates of change
and determine the minimum, maximum, average and standard deviation of the rate
of change.

Solution
import numpy as np
import csv
We'll start by importing the data first:

with open('data.csv') as f:
    reader = csv.reader(f)
    next(f)  # skip header row
    raw_data = list(reader)

raw_data
[['0.092', '14.765674972872079'],
 ['0.2', '20.259226923447223'],
 ['0.296', '25.246364712175524'],
 ['0.39', '28.59196014284041'],
 ['0.494', '35.5838751542487'],
 ['0.605', '39.92405609554009'],
 ['0.699', '44.900143003396344'],
 ['0.806', '50.111998705949176'],
 ['0.89', '55.33744839374389'],
 ['1.003', '61.13682148020512'],
 ['1.109', '64.5004524657241'],
 ['1.195', '69.43382286277865'],
 ['1.304', '75.21429131416473'],
 ['1.394', '80.68024464266546'],
 ['1.51', '85.69045993029255'],
 ['1.596', '90.67365382390035'],
 ['1.699', '94.26145999596629'],
 ['1.801', '100.1501806890637'],
 ['1.893', '104.02236089943838'],
 ['2.006', '110.57471384341925'],
 ['2.098', '114.10017544334872'],
 ['2.193', '120.51135990363724'],
 ['2.302', '125.75356699020317'],
 ['2.402', '129.9848906541477'],
 ['2.508', '135.67840981521636'],
 ['2.599', '139.99229760200282'],
 ['2.691', '145.23099677011123'],
 ['2.799', '149.00349744583'],
 ['2.893', '155.49635992161282'],
 ['2.992', '158.88764234748376'],
 ['3.11', '164.85985880020678'],
 ['3.196', '168.9285892684912'],
 ['3.297', '175.05784410369083'],
 ['3.403', '180.14110291795092'],
 ['3.508', '185.67137343088842'],
 ['3.606', '189.5103768410742'],
 ['3.695', '195.08825597002667'],
 ['3.807', '200.3912029495062'],
 ['3.909', '205.5994160367691'],
 ['4.008', '210.03909338865586'],
 ['4.092', '214.89340700145732'],
 ['4.195', '219.0194782671354'],
 ['4.308', '225.7078797621994'],
 ['4.394', '230.00267066063859'],
 ['4.495', '234.45077449519394'],
 ['4.599', '240.0494003382387'],
 ['4.705', '244.7759953488627'],
 ['4.792', '249.47567519784653'],
 ['4.9', '255.69959529115064'],
 ['4.999', '259.9121756203331'],
 ['5.104', '264.4652490087814'],
 ['5.203', '271.06968884443165'],
 ['5.301', '274.2438815044272'],
 ['5.409', '280.51583467727727'],
 ['5.5', '285.1980402823528'],
 ['5.6', '290.06115615654596'],
 ['5.706', '295.39807651038325'],
 ['5.804', '299.75145571440345'],
 ['5.892', '303.81171123098665'],
 ['6.0', '310.4230380735074'],
 ['6.102', '314.87986213573475'],
 ['6.207', '319.76477201300037'],
 ['6.298', '325.33122102463204'],
 ['6.409', '330.33498759967193'],
 ['6.505', '336.15301070754094'],
 ['6.608', '339.6475615987411'],
 ['6.702', '345.21891028655386'],
 ['6.796', '349.54352032536843'],
 ['6.901', '356.04704049488873'],
 ['7.0', '360.6234150837835'],
 ['7.107', '365.54797004355794'],
 ['7.198', '369.5383579034627'],
 ['7.291', '374.65474628201645'],
 ['7.392', '379.451597982914'],
 ['7.507', '384.7116364547615'],
 ['7.61', '389.62234341709893'],
 ['7.708', '394.7206816321832'],
 ['7.808', '399.5664665006217'],
 ['7.895', '404.1149352068449'],
 ['8.006', '410.8428090736998'],
 ['8.093', '414.65970465943377'],
 ['8.205', '419.4318816190822'],
 ['8.291', '425.0751073848335'],
 ['8.394', '429.0974132851946'],
 ['8.492', '435.4423333270774'],
 ['8.598', '439.1818683482232'],
 ['8.705', '445.18364086896224'],
 ['8.803', '450.6665278007753'],
 ['8.905', '455.3163546862087'],
 ['9.002', '460.1406320266459'],
 ['9.096', '465.5588987264332'],
 ['9.193', '469.3194056327499'],
 ['9.307', '476.15064544937627'],
 ['9.393', '478.6814017283073'],
 ['9.5', '484.098909523116'],
 ['9.607', '490.9238724774915'],
 ['9.702', '495.84696538915017'],
 ['9.796', '500.0896641383723'],
 ['9.9', '504.17430338283964'],
 ['9.992', '508.75450801856044']]
We have to convert our data to floats, so we could do it this way:

data = [[float(t), float(x)] for t, x in raw_data]
data
[[0.092, 14.765674972872079],
 [0.2, 20.259226923447223],
 [0.296, 25.246364712175524],
 [0.39, 28.59196014284041],
 [0.494, 35.5838751542487],
 [0.605, 39.92405609554009],
 [0.699, 44.900143003396344],
 [0.806, 50.111998705949176],
 [0.89, 55.33744839374389],
 [1.003, 61.13682148020512],
 [1.109, 64.5004524657241],
 [1.195, 69.43382286277865],
 [1.304, 75.21429131416473],
 [1.394, 80.68024464266546],
 [1.51, 85.69045993029255],
 [1.596, 90.67365382390035],
 [1.699, 94.26145999596629],
 [1.801, 100.1501806890637],
 [1.893, 104.02236089943838],
 [2.006, 110.57471384341925],
 [2.098, 114.10017544334872],
 [2.193, 120.51135990363724],
 [2.302, 125.75356699020317],
 [2.402, 129.9848906541477],
 [2.508, 135.67840981521636],
 [2.599, 139.99229760200282],
 [2.691, 145.23099677011123],
 [2.799, 149.00349744583],
 [2.893, 155.49635992161282],
 [2.992, 158.88764234748376],
 [3.11, 164.85985880020678],
 [3.196, 168.9285892684912],
 [3.297, 175.05784410369083],
 [3.403, 180.14110291795092],
 [3.508, 185.67137343088842],
 [3.606, 189.5103768410742],
 [3.695, 195.08825597002667],
 [3.807, 200.3912029495062],
 [3.909, 205.5994160367691],
 [4.008, 210.03909338865586],
 [4.092, 214.89340700145732],
 [4.195, 219.0194782671354],
 [4.308, 225.7078797621994],
 [4.394, 230.00267066063859],
 [4.495, 234.45077449519394],
 [4.599, 240.0494003382387],
 [4.705, 244.7759953488627],
 [4.792, 249.47567519784653],
 [4.9, 255.69959529115064],
 [4.999, 259.9121756203331],
 [5.104, 264.4652490087814],
 [5.203, 271.06968884443165],
 [5.301, 274.2438815044272],
 [5.409, 280.51583467727727],
 [5.5, 285.1980402823528],
 [5.6, 290.06115615654596],
 [5.706, 295.39807651038325],
 [5.804, 299.75145571440345],
 [5.892, 303.81171123098665],
 [6.0, 310.4230380735074],
 [6.102, 314.87986213573475],
 [6.207, 319.76477201300037],
 [6.298, 325.33122102463204],
 [6.409, 330.33498759967193],
 [6.505, 336.15301070754094],
 [6.608, 339.6475615987411],
 [6.702, 345.21891028655386],
 [6.796, 349.54352032536843],
 [6.901, 356.04704049488873],
 [7.0, 360.6234150837835],
 [7.107, 365.54797004355794],
 [7.198, 369.5383579034627],
 [7.291, 374.65474628201645],
 [7.392, 379.451597982914],
 [7.507, 384.7116364547615],
 [7.61, 389.62234341709893],
 [7.708, 394.7206816321832],
 [7.808, 399.5664665006217],
 [7.895, 404.1149352068449],
 [8.006, 410.8428090736998],
 [8.093, 414.65970465943377],
 [8.205, 419.4318816190822],
 [8.291, 425.0751073848335],
 [8.394, 429.0974132851946],
 [8.492, 435.4423333270774],
 [8.598, 439.1818683482232],
 [8.705, 445.18364086896224],
 [8.803, 450.6665278007753],
 [8.905, 455.3163546862087],
 [9.002, 460.1406320266459],
 [9.096, 465.5588987264332],
 [9.193, 469.3194056327499],
 [9.307, 476.15064544937627],
 [9.393, 478.6814017283073],
 [9.5, 484.098909523116],
 [9.607, 490.9238724774915],
 [9.702, 495.84696538915017],
 [9.796, 500.0896641383723],
 [9.9, 504.17430338283964],
 [9.992, 508.75450801856044]]
And then we can load this data up into a NumPy array:

data = np.array(data)
data
array([[9.20000000e-02, 1.47656750e+01],
       [2.00000000e-01, 2.02592269e+01],
       [2.96000000e-01, 2.52463647e+01],
       [3.90000000e-01, 2.85919601e+01],
       [4.94000000e-01, 3.55838752e+01],
       [6.05000000e-01, 3.99240561e+01],
       [6.99000000e-01, 4.49001430e+01],
       [8.06000000e-01, 5.01119987e+01],
       [8.90000000e-01, 5.53374484e+01],
       [1.00300000e+00, 6.11368215e+01],
       [1.10900000e+00, 6.45004525e+01],
       [1.19500000e+00, 6.94338229e+01],
       [1.30400000e+00, 7.52142913e+01],
       [1.39400000e+00, 8.06802446e+01],
       [1.51000000e+00, 8.56904599e+01],
       [1.59600000e+00, 9.06736538e+01],
       [1.69900000e+00, 9.42614600e+01],
       [1.80100000e+00, 1.00150181e+02],
       [1.89300000e+00, 1.04022361e+02],
       [2.00600000e+00, 1.10574714e+02],
       [2.09800000e+00, 1.14100175e+02],
       [2.19300000e+00, 1.20511360e+02],
       [2.30200000e+00, 1.25753567e+02],
       [2.40200000e+00, 1.29984891e+02],
       [2.50800000e+00, 1.35678410e+02],
       [2.59900000e+00, 1.39992298e+02],
       [2.69100000e+00, 1.45230997e+02],
       [2.79900000e+00, 1.49003497e+02],
       [2.89300000e+00, 1.55496360e+02],
       [2.99200000e+00, 1.58887642e+02],
       [3.11000000e+00, 1.64859859e+02],
       [3.19600000e+00, 1.68928589e+02],
       [3.29700000e+00, 1.75057844e+02],
       [3.40300000e+00, 1.80141103e+02],
       [3.50800000e+00, 1.85671373e+02],
       [3.60600000e+00, 1.89510377e+02],
       [3.69500000e+00, 1.95088256e+02],
       [3.80700000e+00, 2.00391203e+02],
       [3.90900000e+00, 2.05599416e+02],
       [4.00800000e+00, 2.10039093e+02],
       [4.09200000e+00, 2.14893407e+02],
       [4.19500000e+00, 2.19019478e+02],
       [4.30800000e+00, 2.25707880e+02],
       [4.39400000e+00, 2.30002671e+02],
       [4.49500000e+00, 2.34450774e+02],
       [4.59900000e+00, 2.40049400e+02],
       [4.70500000e+00, 2.44775995e+02],
       [4.79200000e+00, 2.49475675e+02],
       [4.90000000e+00, 2.55699595e+02],
       [4.99900000e+00, 2.59912176e+02],
       [5.10400000e+00, 2.64465249e+02],
       [5.20300000e+00, 2.71069689e+02],
       [5.30100000e+00, 2.74243882e+02],
       [5.40900000e+00, 2.80515835e+02],
       [5.50000000e+00, 2.85198040e+02],
       [5.60000000e+00, 2.90061156e+02],
       [5.70600000e+00, 2.95398077e+02],
       [5.80400000e+00, 2.99751456e+02],
       [5.89200000e+00, 3.03811711e+02],
       [6.00000000e+00, 3.10423038e+02],
       [6.10200000e+00, 3.14879862e+02],
       [6.20700000e+00, 3.19764772e+02],
       [6.29800000e+00, 3.25331221e+02],
       [6.40900000e+00, 3.30334988e+02],
       [6.50500000e+00, 3.36153011e+02],
       [6.60800000e+00, 3.39647562e+02],
       [6.70200000e+00, 3.45218910e+02],
       [6.79600000e+00, 3.49543520e+02],
       [6.90100000e+00, 3.56047040e+02],
       [7.00000000e+00, 3.60623415e+02],
       [7.10700000e+00, 3.65547970e+02],
       [7.19800000e+00, 3.69538358e+02],
       [7.29100000e+00, 3.74654746e+02],
       [7.39200000e+00, 3.79451598e+02],
       [7.50700000e+00, 3.84711636e+02],
       [7.61000000e+00, 3.89622343e+02],
       [7.70800000e+00, 3.94720682e+02],
       [7.80800000e+00, 3.99566467e+02],
       [7.89500000e+00, 4.04114935e+02],
       [8.00600000e+00, 4.10842809e+02],
       [8.09300000e+00, 4.14659705e+02],
       [8.20500000e+00, 4.19431882e+02],
       [8.29100000e+00, 4.25075107e+02],
       [8.39400000e+00, 4.29097413e+02],
       [8.49200000e+00, 4.35442333e+02],
       [8.59800000e+00, 4.39181868e+02],
       [8.70500000e+00, 4.45183641e+02],
       [8.80300000e+00, 4.50666528e+02],
       [8.90500000e+00, 4.55316355e+02],
       [9.00200000e+00, 4.60140632e+02],
       [9.09600000e+00, 4.65558899e+02],
       [9.19300000e+00, 4.69319406e+02],
       [9.30700000e+00, 4.76150645e+02],
       [9.39300000e+00, 4.78681402e+02],
       [9.50000000e+00, 4.84098910e+02],
       [9.60700000e+00, 4.90923872e+02],
       [9.70200000e+00, 4.95846965e+02],
       [9.79600000e+00, 5.00089664e+02],
       [9.90000000e+00, 5.04174303e+02],
       [9.99200000e+00, 5.08754508e+02]])
Now that we have our data in a NumPy array, we can calculate the differences
in the t values and the x values this way:

delta_t = data[1:, 0] - data[:-1, 0]
delta_t
array([0.108, 0.096, 0.094, 0.104, 0.111, 0.094, 0.107, 0.084, 0.113,
       0.106, 0.086, 0.109, 0.09 , 0.116, 0.086, 0.103, 0.102, 0.092,
       0.113, 0.092, 0.095, 0.109, 0.1  , 0.106, 0.091, 0.092, 0.108,
       0.094, 0.099, 0.118, 0.086, 0.101, 0.106, 0.105, 0.098, 0.089,
       0.112, 0.102, 0.099, 0.084, 0.103, 0.113, 0.086, 0.101, 0.104,
       0.106, 0.087, 0.108, 0.099, 0.105, 0.099, 0.098, 0.108, 0.091,
       0.1  , 0.106, 0.098, 0.088, 0.108, 0.102, 0.105, 0.091, 0.111,
       0.096, 0.103, 0.094, 0.094, 0.105, 0.099, 0.107, 0.091, 0.093,
       0.101, 0.115, 0.103, 0.098, 0.1  , 0.087, 0.111, 0.087, 0.112,
       0.086, 0.103, 0.098, 0.106, 0.107, 0.098, 0.102, 0.097, 0.094,
       0.097, 0.114, 0.086, 0.107, 0.107, 0.095, 0.094, 0.104, 0.092])
delta_x = data[1:, 1] - data[:-1, 1]
delta_x
array([5.49355195, 4.98713779, 3.34559543, 6.99191501, 4.34018094,
       4.97608691, 5.2118557 , 5.22544969, 5.79937309, 3.36363099,
       4.9333704 , 5.78046845, 5.46595333, 5.01021529, 4.98319389,
       3.58780617, 5.88872069, 3.87218021, 6.55235294, 3.5254616 ,
       6.41118446, 5.24220709, 4.23132366, 5.69351916, 4.31388779,
       5.23869917, 3.77250068, 6.49286248, 3.39128243, 5.97221645,
       4.06873047, 6.12925484, 5.08325881, 5.53027051, 3.83900341,
       5.57787913, 5.30294698, 5.20821309, 4.43967735, 4.85431361,
       4.12607127, 6.6884015 , 4.2947909 , 4.44810383, 5.59862584,
       4.72659501, 4.69967985, 6.22392009, 4.21258033, 4.55307339,
       6.60443984, 3.17419266, 6.27195317, 4.68220561, 4.86311587,
       5.33692035, 4.3533792 , 4.06025552, 6.61132684, 4.45682406,
       4.88490988, 5.56644901, 5.00376658, 5.81802311, 3.49455089,
       5.57134869, 4.32461004, 6.50352017, 4.57637459, 4.92455496,
       3.99038786, 5.11638838, 4.7968517 , 5.26003847, 4.91070696,
       5.09833822, 4.84578487, 4.54846871, 6.72787387, 3.81689559,
       4.77217696, 5.64322577, 4.0223059 , 6.34492004, 3.73953502,
       6.00177252, 5.48288693, 4.64982689, 4.82427734, 5.4182667 ,
       3.76050691, 6.83123982, 2.53075628, 5.41750779, 6.82496295,
       4.92309291, 4.24269875, 4.08463924, 4.58020464])
And we can then calculate the rates of change this way:

rates = delta_x / delta_t
rates
array([50.86622176, 51.94935197, 35.59144075, 67.22995203, 39.1007292 ,
       52.93709476, 48.7089318 , 62.20773438, 51.32188572, 31.73236779,
       57.36477206, 53.03182065, 60.73281476, 43.1915111 , 57.94411504,
       34.83306963, 57.73255581, 42.08891533, 57.98542428, 38.32023478,
       67.48615221, 48.093643  , 42.31323664, 53.71244492, 47.40536029,
       56.94238226, 34.93056181, 69.07300506, 34.25537804, 50.61200384,
       47.3108194 , 60.68569144, 47.95527183, 52.66924298, 39.17350419,
       62.6727992 , 47.34774089, 51.06091262, 44.84522578, 57.78944777,
       40.05894433, 59.18939376, 49.93942905, 44.04063203, 53.8329408 ,
       44.59051897, 54.01930861, 57.62888975, 42.55131646, 43.3626037 ,
       66.71151349, 32.38972102, 58.07364049, 51.45280885, 48.63115874,
       50.34830522, 44.42223678, 46.13926723, 61.21598928, 43.69435355,
       46.52295121, 61.16976936, 45.07897815, 60.60440737, 33.92767856,
       59.26966689, 46.00648977, 61.93828733, 46.22600595, 46.02387813,
       43.85041604, 55.0149288 , 47.4935812 , 45.73946497, 47.67676662,
       52.02385934, 48.45784868, 52.2812495 , 60.61147628, 43.87236305,
       42.60872285, 65.61890425, 39.0515136 , 64.74408206, 35.27863227,
       56.09133197, 55.94782583, 45.58653809, 49.73481794, 57.6411351 ,
       38.76811244, 59.92315629, 29.42739859, 50.63091397, 63.78470051,
       51.82203065, 45.13509308, 39.27537735, 49.784833  ])
Of course, we could just do all this in one step as well since we want to
perform the same difference calculations on each column:

delta = data[1:] - data[:-1]
delta
array([[0.108     , 5.49355195],
       [0.096     , 4.98713779],
       [0.094     , 3.34559543],
       [0.104     , 6.99191501],
       [0.111     , 4.34018094],
       [0.094     , 4.97608691],
       [0.107     , 5.2118557 ],
       [0.084     , 5.22544969],
       [0.113     , 5.79937309],
       [0.106     , 3.36363099],
       [0.086     , 4.9333704 ],
       [0.109     , 5.78046845],
       [0.09      , 5.46595333],
       [0.116     , 5.01021529],
       [0.086     , 4.98319389],
       [0.103     , 3.58780617],
       [0.102     , 5.88872069],
       [0.092     , 3.87218021],
       [0.113     , 6.55235294],
       [0.092     , 3.5254616 ],
       [0.095     , 6.41118446],
       [0.109     , 5.24220709],
       [0.1       , 4.23132366],
       [0.106     , 5.69351916],
       [0.091     , 4.31388779],
       [0.092     , 5.23869917],
       [0.108     , 3.77250068],
       [0.094     , 6.49286248],
       [0.099     , 3.39128243],
       [0.118     , 5.97221645],
       [0.086     , 4.06873047],
       [0.101     , 6.12925484],
       [0.106     , 5.08325881],
       [0.105     , 5.53027051],
       [0.098     , 3.83900341],
       [0.089     , 5.57787913],
       [0.112     , 5.30294698],
       [0.102     , 5.20821309],
       [0.099     , 4.43967735],
       [0.084     , 4.85431361],
       [0.103     , 4.12607127],
       [0.113     , 6.6884015 ],
       [0.086     , 4.2947909 ],
       [0.101     , 4.44810383],
       [0.104     , 5.59862584],
       [0.106     , 4.72659501],
       [0.087     , 4.69967985],
       [0.108     , 6.22392009],
       [0.099     , 4.21258033],
       [0.105     , 4.55307339],
       [0.099     , 6.60443984],
       [0.098     , 3.17419266],
       [0.108     , 6.27195317],
       [0.091     , 4.68220561],
       [0.1       , 4.86311587],
       [0.106     , 5.33692035],
       [0.098     , 4.3533792 ],
       [0.088     , 4.06025552],
       [0.108     , 6.61132684],
       [0.102     , 4.45682406],
       [0.105     , 4.88490988],
       [0.091     , 5.56644901],
       [0.111     , 5.00376658],
       [0.096     , 5.81802311],
       [0.103     , 3.49455089],
       [0.094     , 5.57134869],
       [0.094     , 4.32461004],
       [0.105     , 6.50352017],
       [0.099     , 4.57637459],
       [0.107     , 4.92455496],
       [0.091     , 3.99038786],
       [0.093     , 5.11638838],
       [0.101     , 4.7968517 ],
       [0.115     , 5.26003847],
       [0.103     , 4.91070696],
       [0.098     , 5.09833822],
       [0.1       , 4.84578487],
       [0.087     , 4.54846871],
       [0.111     , 6.72787387],
       [0.087     , 3.81689559],
       [0.112     , 4.77217696],
       [0.086     , 5.64322577],
       [0.103     , 4.0223059 ],
       [0.098     , 6.34492004],
       [0.106     , 3.73953502],
       [0.107     , 6.00177252],
       [0.098     , 5.48288693],
       [0.102     , 4.64982689],
       [0.097     , 4.82427734],
       [0.094     , 5.4182667 ],
       [0.097     , 3.76050691],
       [0.114     , 6.83123982],
       [0.086     , 2.53075628],
       [0.107     , 5.41750779],
       [0.107     , 6.82496295],
       [0.095     , 4.92309291],
       [0.094     , 4.24269875],
       [0.104     , 4.08463924],
       [0.092     , 4.58020464]])
And then the rates are simply:

rates = delta[:, 1] / delta[:, 0]
rates
array([50.86622176, 51.94935197, 35.59144075, 67.22995203, 39.1007292 ,
       52.93709476, 48.7089318 , 62.20773438, 51.32188572, 31.73236779,
       57.36477206, 53.03182065, 60.73281476, 43.1915111 , 57.94411504,
       34.83306963, 57.73255581, 42.08891533, 57.98542428, 38.32023478,
       67.48615221, 48.093643  , 42.31323664, 53.71244492, 47.40536029,
       56.94238226, 34.93056181, 69.07300506, 34.25537804, 50.61200384,
       47.3108194 , 60.68569144, 47.95527183, 52.66924298, 39.17350419,
       62.6727992 , 47.34774089, 51.06091262, 44.84522578, 57.78944777,
       40.05894433, 59.18939376, 49.93942905, 44.04063203, 53.8329408 ,
       44.59051897, 54.01930861, 57.62888975, 42.55131646, 43.3626037 ,
       66.71151349, 32.38972102, 58.07364049, 51.45280885, 48.63115874,
       50.34830522, 44.42223678, 46.13926723, 61.21598928, 43.69435355,
       46.52295121, 61.16976936, 45.07897815, 60.60440737, 33.92767856,
       59.26966689, 46.00648977, 61.93828733, 46.22600595, 46.02387813,
       43.85041604, 55.0149288 , 47.4935812 , 45.73946497, 47.67676662,
       52.02385934, 48.45784868, 52.2812495 , 60.61147628, 43.87236305,
       42.60872285, 65.61890425, 39.0515136 , 64.74408206, 35.27863227,
       56.09133197, 55.94782583, 45.58653809, 49.73481794, 57.6411351 ,
       38.76811244, 59.92315629, 29.42739859, 50.63091397, 63.78470051,
       51.82203065, 45.13509308, 39.27537735, 49.784833  ])
We can then calculate the min, max and average rates of change:

np.amin(rates)
29.42739859222142
np.amax(rates)
69.07300506151955
np.mean(rates)
49.98125178748103
np.std(rates)
9.043463532187504
Question 2
In linear regression we try to find the coefficients m (slope) and c
(y-intercept) of a straight line


that provides the "best" fit given some x and y data. This formula then allows
to predict y values for given x values.

Given an array of n (x, y) data pairs, these coefficients can be calculated
very simply.

A bit of terminology first:

Let X mean the column of X values.
Let Y mean the column of Y values.
Let XX mean a column calculated by multiplying each x in the X column by itself
Let XY mean a column calculated by multiplying the x and y values from the X and Y columns
Then, given some column (say X), this symbol:
 means the sum of all the elements in the column.

Similarly, the symbol
 means the sum of the values obtained by multiplying (pairwise) the values in
 X and Y.

Given those definitions, the formulas for calculating the "best" values of m
and c are given by:





(where n is the number of (x,y) pairs in our data set.)

Using the same data we saw in Question 1, calculate the values for m and c for
that data set given the formulas above.

You can think of the t column in the data as the X column, and the x values in
the data as the Y column - we are trying to predict the value of x given a
value of t.

This will result in a straight line that "best" fits through the data.

Compare the slope of this regression line to the average rate of change you
calculated in Question 1.

Solution
We already saw how to load the data in Question 1.

I'll do the import, conversion to floats, and loading up into a NumPy array in
the same step to simplify our earlier code a bit.

import numpy as np
import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    next(f)  # skip header row
    data = np.array([[float(t), float(x)] for t, x in reader])

data

array([[9.20000000e-02, 1.47656750e+01],
       [2.00000000e-01, 2.02592269e+01],
       [2.96000000e-01, 2.52463647e+01],
       [3.90000000e-01, 2.85919601e+01],
       [4.94000000e-01, 3.55838752e+01],
       [6.05000000e-01, 3.99240561e+01],
       [6.99000000e-01, 4.49001430e+01],
       [8.06000000e-01, 5.01119987e+01],
       [8.90000000e-01, 5.53374484e+01],
       [1.00300000e+00, 6.11368215e+01],
       [1.10900000e+00, 6.45004525e+01],
       [1.19500000e+00, 6.94338229e+01],
       [1.30400000e+00, 7.52142913e+01],
       [1.39400000e+00, 8.06802446e+01],
       [1.51000000e+00, 8.56904599e+01],
       [1.59600000e+00, 9.06736538e+01],
       [1.69900000e+00, 9.42614600e+01],
       [1.80100000e+00, 1.00150181e+02],
       [1.89300000e+00, 1.04022361e+02],
       [2.00600000e+00, 1.10574714e+02],
       [2.09800000e+00, 1.14100175e+02],
       [2.19300000e+00, 1.20511360e+02],
       [2.30200000e+00, 1.25753567e+02],
       [2.40200000e+00, 1.29984891e+02],
       [2.50800000e+00, 1.35678410e+02],
       [2.59900000e+00, 1.39992298e+02],
       [2.69100000e+00, 1.45230997e+02],
       [2.79900000e+00, 1.49003497e+02],
       [2.89300000e+00, 1.55496360e+02],
       [2.99200000e+00, 1.58887642e+02],
       [3.11000000e+00, 1.64859859e+02],
       [3.19600000e+00, 1.68928589e+02],
       [3.29700000e+00, 1.75057844e+02],
       [3.40300000e+00, 1.80141103e+02],
       [3.50800000e+00, 1.85671373e+02],
       [3.60600000e+00, 1.89510377e+02],
       [3.69500000e+00, 1.95088256e+02],
       [3.80700000e+00, 2.00391203e+02],
       [3.90900000e+00, 2.05599416e+02],
       [4.00800000e+00, 2.10039093e+02],
       [4.09200000e+00, 2.14893407e+02],
       [4.19500000e+00, 2.19019478e+02],
       [4.30800000e+00, 2.25707880e+02],
       [4.39400000e+00, 2.30002671e+02],
       [4.49500000e+00, 2.34450774e+02],
       [4.59900000e+00, 2.40049400e+02],
       [4.70500000e+00, 2.44775995e+02],
       [4.79200000e+00, 2.49475675e+02],
       [4.90000000e+00, 2.55699595e+02],
       [4.99900000e+00, 2.59912176e+02],
       [5.10400000e+00, 2.64465249e+02],
       [5.20300000e+00, 2.71069689e+02],
       [5.30100000e+00, 2.74243882e+02],
       [5.40900000e+00, 2.80515835e+02],
       [5.50000000e+00, 2.85198040e+02],
       [5.60000000e+00, 2.90061156e+02],
       [5.70600000e+00, 2.95398077e+02],
       [5.80400000e+00, 2.99751456e+02],
       [5.89200000e+00, 3.03811711e+02],
       [6.00000000e+00, 3.10423038e+02],
       [6.10200000e+00, 3.14879862e+02],
       [6.20700000e+00, 3.19764772e+02],
       [6.29800000e+00, 3.25331221e+02],
       [6.40900000e+00, 3.30334988e+02],
       [6.50500000e+00, 3.36153011e+02],
       [6.60800000e+00, 3.39647562e+02],
       [6.70200000e+00, 3.45218910e+02],
       [6.79600000e+00, 3.49543520e+02],
       [6.90100000e+00, 3.56047040e+02],
       [7.00000000e+00, 3.60623415e+02],
       [7.10700000e+00, 3.65547970e+02],
       [7.19800000e+00, 3.69538358e+02],
       [7.29100000e+00, 3.74654746e+02],
       [7.39200000e+00, 3.79451598e+02],
       [7.50700000e+00, 3.84711636e+02],
       [7.61000000e+00, 3.89622343e+02],
       [7.70800000e+00, 3.94720682e+02],
       [7.80800000e+00, 3.99566467e+02],
       [7.89500000e+00, 4.04114935e+02],
       [8.00600000e+00, 4.10842809e+02],
       [8.09300000e+00, 4.14659705e+02],
       [8.20500000e+00, 4.19431882e+02],
       [8.29100000e+00, 4.25075107e+02],
       [8.39400000e+00, 4.29097413e+02],
       [8.49200000e+00, 4.35442333e+02],
       [8.59800000e+00, 4.39181868e+02],
       [8.70500000e+00, 4.45183641e+02],
       [8.80300000e+00, 4.50666528e+02],
       [8.90500000e+00, 4.55316355e+02],
       [9.00200000e+00, 4.60140632e+02],
       [9.09600000e+00, 4.65558899e+02],
       [9.19300000e+00, 4.69319406e+02],
       [9.30700000e+00, 4.76150645e+02],
       [9.39300000e+00, 4.78681402e+02],
       [9.50000000e+00, 4.84098910e+02],
       [9.60700000e+00, 4.90923872e+02],
       [9.70200000e+00, 4.95846965e+02],
       [9.79600000e+00, 5.00089664e+02],
       [9.90000000e+00, 5.04174303e+02],
       [9.99200000e+00, 5.08754508e+02]])
So here, the X column is the first column (the time column), and the Y column
is the second column (the observed value column).

We can certainly assign those individual columns to variable names:

X = data[:, 0]
Y = data[:, 1]
We also need the value for n:

n = len(X)
Then we can simply use NumPy's universal operators for our formulas:



m = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X * X) - (np.sum(X)) ** 2)
m
49.978008206387344


c = (np.sum(Y) * np.sum(X * X) - np.sum(X) * np.sum(X * Y)) / (n * np.sum(X * X) - (np.sum(X)) ** 2)
c
10.081268844890284
So the "best" straight line through our data is given by:


If we compare our value for m here: 49.978, we'll see that it is very close to
the average rate of change we calculated in Question 1: 49.981.

(I won't get into the math here, but if
, then the rate of change of
 (w.r.t.
) is given by the derivative of the function (i.e.

). And for a linear equation, that derivative is the slope m.)
'''