import cv2

def reduce_image_size(input_image_path, output_image_path, scale_factor):
    img = cv2.imread(input_image_path)
    print("Original Dimensions : ", img.shape)
    
    width = int(img.shape[1] / scale_factor)
    height = int(img.shape[0] / scale_factor)
    
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    print("Resized Dimensions : ", resized_img.shape)
    
    cv2.imwrite(output_image_path, resized_img)
    return resized_img.shape

if __name__ == "__main__":
    input_path = 'image.jpg'
    output_path = 'resized_output_image.jpg'
    k = 5
    reduce_image_size(input_path, output_path, k)