import cv2
import numpy as np

def replace_background(input_image_path, background_image_path, output_image_path, target_color, tolerance):
    input_image = cv2.imread(input_image_path)
    background_image = cv2.imread(background_image_path)

    if input_image is None or background_image is None:
        print("Не удалось загрузить изображения.")
        return

    # Конвертация цветов изображений в формат HSV
    input_hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(np.uint8([[target_color]]), cv2.COLOR_BGR2HSV)[0][0]

    # Определение области с целевым цветом и замена фона
    lower_bound = np.array([target_hsv[0] - tolerance, 50, 50])
    upper_bound = np.array([target_hsv[0] + tolerance, 255, 255])
    mask = cv2.inRange(input_hsv, lower_bound, upper_bound)

    # Изменение размера фонового изображения
    background_resized = cv2.resize(background_image, (input_image.shape[1], input_image.shape[0]))

    # Выделение области фона
    background_region = background_resized.copy()
    background_region[mask > 0] = [0, 0, 0]  # Чтобы не влиять на область переднего плана

    # Сложение изображений переднего и заднего плана
    output_image = cv2.add(input_image, background_region)

    # Сохранение результата
    cv2.imwrite(output_image_path, output_image)

if __name__ == "__main__":
    input_image_path = 'Images\Ducky.bmp'
    background_image_path = 'Images\Dune.bmp'
    output_image_path = 'Outputs\output_image.jpg'

    target_color = [0, 255, 0]
    tolerance = 1

    replace_background(input_image_path, background_image_path, output_image_path, target_color, tolerance)
