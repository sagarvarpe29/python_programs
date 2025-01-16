import os

#os.mkdir('/Users/sagarvarpe/Desktop/CleanedUp/')

folder_original = '/Users/sagarvarpe/Desktop/'
folder_destination = '/Users/sagarvarpe/Desktop/CleanedUp/'
os.mkdir(folder_destination)

entries = os.scandir(folder_original)

for entry in entries:
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    if os.path.isdir(location_original):
        os.rename(location_original, location_destination)