import numpy as np 
import pickle

###############################################################################################################3
stupid_videos = [   49,    49,    49,   926,   926,   926,  1115,  1115,  1115,
        1129,  1129,  1129,  1297,  1297,  1297,  1998,  1998,  1998,
        5039,  5039,  5039,  5148,  5148,  5148,  5361,  5361,  5361,
        6025,  6025,  6025,  6241,  6241,  6241,  6512,  6512,  6512,
        6616,  6616,  6616,  6807,  6807,  6807,  7105,  7105,  7105,
        7511,  7511,  7511,  8069,  8069,  8069,  8421,  8421,  8421,
        8561,  8561,  8561,  9730,  9730,  9730,  9988,  9988,  9988,
       11058, 11058, 11058, 11207, 11207, 11207, 11825, 11825, 11825,
       11864, 11864, 11864, 12497, 12497, 12497, 13932, 13932, 13932,
       14268, 14268, 14268, 14585, 14585, 14585, 14938, 14938, 14938,
       15150, 15150, 15150, 15546, 15546, 15546, 15944, 15944, 15944,
       16209, 16209, 16209, 16640, 16640, 16640, 18362, 18362, 18362,
       18380, 18380, 18380, 19078, 19078, 19078, 19107, 19107, 19107,
       19191, 19191, 19191, 19300, 19300, 19300, 20215, 20215, 20215,
       20785, 20785, 20785, 22595, 22595, 22595, 22902, 22902, 22902,
       23774, 23774, 23774, 24660, 24660, 24660, 25205, 25205, 25205,
       25236, 25236, 25236, 25270, 25270, 25270, 25320, 25320, 25320,
       27642, 27642, 27642, 27737, 27737, 27737, 27947, 27947, 27947,
       28335, 28335, 28335, 29086, 29086, 29086, 29839, 29839, 29839,
       30260, 30260, 30260, 30290, 30290, 30290, 30421, 30421, 30421,
       30772, 30772, 30772, 31108, 31108, 31108, 31713, 31713, 31713,
       33532, 33532, 33532, 33608, 33608, 33608, 33661, 33661, 33661,
       34204, 34204, 34204, 34654, 34654, 34654, 35459, 35459, 35459,
       35812, 35812, 35812, 35865, 35865, 35865, 35881, 35881, 35881,
       36700, 36700, 36700, 37715, 37715, 37715, 38825, 38825, 38825,
       39403, 39403, 39403, 39667, 39667, 39667]#xsub

stupid_videos = stupid_videos[0:len(stupid_videos):3]

train_data = np.load(open('val_data.npy','rb'))
train_labes = pickle.load(open('val_label.pkl','rb'))
print(train_data.shape)
non_stupid = np.setdiff1d(range(len(train_labes[1])),stupid_videos)
print(len(non_stupid))
train_data = train_data[non_stupid,:,:,:,:]
print(train_data.shape)
print(len(train_labes[1]))
train_labes = np.asarray(train_labes[1])
print(train_labes.shape)
train_labes = train_labes[non_stupid]
train_data = train_data[np.asarray(train_labes)<49,:,:,:,0]
print(train_data.shape)

#train_labes = np.asarray(train_labes[1])

#train_labes = train_labes[non_stupid]

train_labes = train_labes[train_labes<49]

np.save('Final-Data/val_data.npy',train_data)
np.save('Final-Data/val_labels.npy',train_labes)

# indices = [0,13,22,23,37]
# mask = np.zeros(train_labes.shape[0])
# for i in range(train_labes.shape[0]):
#   if train_labes[i] in indices:
#     mask[i] = 1

# train_data = train_data[mask == 1]
# train_labes = train_labes[mask == 1]

# for i in range(train_labes.shape[0]):
#   if train_labes[i] == 13:
#     train_labes[i] = 1
#   if train_labes[i] == 22:
#     train_labes[i] = 2
#   if train_labes[i] == 23:
#     train_labes[i] = 3
#   if train_labes[i] == 37:
#     train_labes[i] = 4

# np.save('toyData/trainData.npy', train_data)
# np.save('toyData/trainLabels.npy', train_labes)
