import pandas as pd
import logging as log
log.basicConfig(level=log.DEBUG)

# df = pd.read_fwf('20200203')
# df.to_csv('log.csv')

def logic(index):
    if index < 2:
        return True
    elif (index - 15) % 17 == 0:
        return True
    elif (index - 16) % 17 == 0:
        return True
    elif (index - 17) % 17 == 0:
        return True
    elif (index - 18) % 17 == 0:
        return True
    return False

df = pd.read_csv('20200203', skiprows= lambda x: logic(x), sep="\s+", names=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"])
df.to_csv('test4.csv')#, index=False)#, sep=',')

num_of_snapshots = int((len(df.index) + 1) / 13)
snapshot_collection = {}

start_i = end_i = 0

# for snapshot in range(3):#range(num_of_snapshots):
#     end_i = start_i + 13
#     snapshot_collection[snapshot] = pd.iloc[start_i:end_i]
#     snapshot_collection[snapshot] = snapshot_collection[snapshot].reset_index(drop=True)
#     start_i = end_i
#     print('\n', snapshot_collection[snapshot])

for snapshot in range(3):#range(num_of_snapshots):
    end_i = start_i + 13
    snapshot_collection[snapshot] = df.iloc[start_i:end_i]
    snapshot_collection[snapshot] = snapshot_collection[snapshot].reset_index(drop=True)
    start_i = end_i
    print('\n', snapshot_collection[snapshot])
    #add metadata

# for key in dataframe_collection.keys():
#     print("\n" +"="*40)
#     print(key)
#     print("-"*40)
#     print(dataframe_collection[key])

#0 1, 15 16 17 18, 32 33 34 35, 49 50 51 52, 66 67 68 69,