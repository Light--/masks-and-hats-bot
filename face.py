import tempfile
import validate_inputs
from apply_mask import apply_masks

class Struct: pass

def update_image(infile, url=None):
    """
    make temporary outfile for masked version of infile
    """
    f = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    outfile = f.name

    args = Struct()
    args.input = infile
    args.output = outfile
    args.mask = 'masks/'
    args.unique = False
    input_paths, masks, output_paths, apply_unique_masks, is_video = validate_inputs.run(args)
    success = apply_masks(input_paths, masks, output_paths, apply_unique_masks, is_video)
    if not success:
        outfile = None
    return outfile

if __name__ == '__main__':
    """
    test by providing a path to an image of a face
    """
    import os
    import sys
    if len(sys.argv) > 1:
        infile = sys.argv[1] # user passed filepath of image
    else:
        infile = 'test/face1.jpg'
    infile = sys.argv[1] if len(sys.argv) > 1 else 'test/face1.jpg'
    outfile = update_image(infile)
    os.system('open ' + outfile)
