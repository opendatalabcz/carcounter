import pandas as pd

# readinag given csv file
# and creating dataframe
colnames = ['frame', 'object_class', 'x_center', 'y_center', 'width', 'heigth', '7', '8', '9', '10', ]
dataframe1 = pd.read_csv("det_yolo3.txt", names=colnames, header=None)
dataframe1 = dataframe1.drop(['7', '8', '9', '10'], axis=1)
dataframe1['object_class'] = 0
dataframe1['x_center'] = dataframe1['x_center'] + dataframe1['width'] / 2
dataframe1['y_center'] = dataframe1['y_center'] + dataframe1['heigth'] / 2
dataframe1['x_center'] = dataframe1['x_center'] / 1920
dataframe1['y_center'] = dataframe1['y_center'] / 1080
dataframe1['width'] = dataframe1['width'] / 1920
dataframe1['heigth'] = dataframe1['heigth'] / 1080
dataframe1['frame'] = dataframe1['frame'] - 1
dataframe1.frame = dataframe1.frame.astype(int)
dataframe1.object_class = dataframe1.object_class.astype(int)
dataframe1.x_center = dataframe1.x_center.round(4)
dataframe1.y_center = dataframe1.y_center.round(4)
dataframe1.width = dataframe1.width.round(4)
dataframe1.heigth = dataframe1.heigth.round(4)

dataframe1 = dataframe1.values.tolist()

frame = 0
count = 0
found = False

array_of_data = dict()

array_of_data[0] = list()

for row in range(len(dataframe1)):
    if dataframe1[row][0] != frame:
      frame+=1
      array_of_data[frame] = list()
    array_of_data[frame].append(dataframe1[row])






file_name = 0
frame = 0
for key in array_of_data:
    if key % 100 == 0:
        df = pd.DataFrame(array_of_data[key], columns=['a', 'b', 'c', 'd', 'e', 'f'])
        if df['a'][0] != frame:
            frame = frame + 100
            continue
        print(df['a'][0])
        frame = frame + 100
        df = df.drop(['a'], axis=1)
        df.to_csv("labels/" + str(file_name) + ".txt", header=False, sep=' ', index=False)
        print("Saved file number: " + str(file_name))
        file_name += 100

print(array_of_data[1])

dataframe1.to_csv('yolo_data.txt', sep=',', index=False)