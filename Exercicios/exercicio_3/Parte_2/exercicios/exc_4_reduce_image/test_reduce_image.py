import os
from reduce_image_size import reduce_image_size

def test_reduce_image_size():
    input_image_path = 'test_image.jpg'
    output_image_path = 'test_resized_output_image.jpg'
    scale_factor = 5
    
    expected_width = 1000 // scale_factor
    expected_height = 500 // scale_factor
    
    resized_dimensions = reduce_image_size(input_image_path, output_image_path, scale_factor)
    
    assert resized_dimensions == (expected_height, expected_width, 3), "The resized image dimensions are incorrect."
    
    if os.path.exists(output_image_path):
        os.remove(output_image_path)