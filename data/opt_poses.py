import os
import numpy as np

# 创建文件夹
for i in range(0, 11):
    folder_name = "data/poses/"+str(i).zfill(2)
    os.makedirs(folder_name, exist_ok=True)

# 处理txt文件并保存为npz格式
for i in range(0, 11):
    folder_name = "data/poses/"+str(i).zfill(2)
    txt_filename = folder_name + ".txt"
    npz_folder = folder_name

    with open(txt_filename, 'r') as file:
        lines = file.readlines()

        for idx, line in enumerate(lines):
            data = np.array([float(num) for num in line.split()])
            pose_matrix = np.zeros((4, 4))
            pose_matrix[:3, :4] = data.reshape((3, 4))  # 填充前3行数据
            pose_matrix[3, 3] = 1  # 填充最后一行
            npz_filename = os.path.join(npz_folder, '{:06d}.npz'.format(idx))
            np.savez(npz_filename, pose=pose_matrix)