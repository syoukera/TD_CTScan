import pydicom
import os
import numpy as np


root_dir = 'E:\Material\CT_Scan\20230215_born_h4\S0000000001'
dcms = []
for d, s, fl in os.walk(root_dir):
    for fn in fl:
        if ".dcm" in fn.lower():
            dcms.append(os.path.join(d, fn))
ref_dicom = pydicom.read_file(dcms[0])
d_array = np.zeros((ref_dicom.Rows, ref_dicom.Columns, len(dcms)), dtype=ref_dicom.pixel_array.dtype)
for dcm in dcms:
    d = pydicom.read_file(dcm)
    d_array[:, :, dcms.index(dcm)] = d.pixel_array