import os
import glob
import tempfile
import validate_inputs
from apply_mask import apply_masks

class Struct: pass

def update_image(infile, url=None):
    f = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    outfile = f.name

    args = Struct()
    args.input = infile
    args.output = outfile
    args.mask = 'masks/'
    args.unique = False
    input_paths, masks, output_paths, apply_unique_masks, is_video = validate_inputs.run(args)
    apply_masks(input_paths, masks, output_paths, apply_unique_masks, is_video)
    return outfile

def test1():
    print update_image('test/face1.jpg')

if __name__ == '__main__':
    test1()
