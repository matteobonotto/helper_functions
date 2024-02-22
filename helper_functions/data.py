import os
import sys
import h5py
import numpy as np


def write_h5(
        data : dict,
        filename: str,
        dtype : str = 'float64',
        compression : str = 'lzf',
        compression_opts : int = 1,
        chunk_1st_dim = None
        ):
    
    kwargs = {
        'dtype' : dtype,
        'compression' : compression, 
        }
    if compression == 'gzip':
            kwargs.update({'compression_opts' : compression_opts})

    with h5py.File(filename + '.h5', 'w') as hf:
        for key,item in data.items():
            if chunk_1st_dim is not None:
                 if chunk_1st_dim == True:
                      chunks = True
                 else:
                    chunks = [chunk_1st_dim]
                    chunks.extend(item.shape[1:])
                    chunks = tuple(chunks)
            # print(chunks)

            hf.create_dataset(
                key,
                data = item,
                shape = item.shape,
                chunks=chunks,
                **kwargs)
    hf.close()



def read_h5_numpy(
        filename : str, 
        ):
    data = {}
    with h5py.File(filename, 'r') as hf:
        for key,item in hf.items():
            data.update({
                    key : item[()]
            })
    return data
                 