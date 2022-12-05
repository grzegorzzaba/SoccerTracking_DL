import numpy as np
import matplotlib.pyplot as plt

w = 0.35
MOT = ["02", "04", "05", "09", "10", "11", "13", "AVERAGE"]
x = np.arange(0, len(MOT)) 
n = len(MOT)

y1Mota = [44.3, 75.1, 58.5, 64.2, 66.3, 69.2, 47.8, 64]
y2Mota = [77.6, 98.3, 82.9, 87.1, 85.5, 89.0, 88.8, 90.2]

plt.figure()
plt.subplot(211)
plt.title('MOTA', loc='left')
plt.xlabel('Dataset MOT17')
for i, value in enumerate([y1Mota, y2Mota]):
    position = x + i*w
    plt.bar(position, value, width=w)
plt.legend(['DeepSort tracking and YOLOv3 detecting', 'ByteTrack tracking and YOLOx detecting'], loc='lower right')
plt.xticks(x, MOT, rotation=45)
plt.show()

y1MOTP = [0.195, 0.170, 0.201, 0.148, 0.200, 0.146, 0.213, 0.179]
y2MOTP = [0.159,0.083,0.156, 0.142, 0.183, 0.119, 0.169, 0.121]

plt.figure()
plt.subplot(212)
plt.title('MOTP', loc='left')
plt.xlabel('Dataset MOT17')
for i, value in enumerate([y1MOTP, y2MOTP]):
    position = x + i*w
    plt.bar(position, value, width=w)
plt.legend(['DeepSort tracking and YOLOv3 detecting', 'ByteTrack tracking and YOLOx detecting'], loc='lower right')
plt.xticks(x, MOT, rotation=45)
plt.show()