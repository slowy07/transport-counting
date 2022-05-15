from utils.color_recognition_module import color_histogram_feature_extraction
from utils.color_recognition_module import knn_classififer
import os
from utils.image_utils import crop_image

current_path = os.getcwd()


def color_recognition(crop_img):
    (height, width, channels) = crop_img.shape
    crop_img = crop_image.crop_center(crop_img, 50, 50)

    open(current_path + "/utils/color_recognition_module/" + "test.data" "w")
    color_histogram_feature_extraction.color_histogram_of_test_image(crop_img)

    prediction = knn_classifier.main(
        current_path + "/utils/color_recognition_module" + "training.data",
        current_path + "/utils/color_recognition_module/" + "test.data",
    )

    return prediction
