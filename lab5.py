import cv2
import numpy as np

def replace_background(input_image_path, background_image_path, output_image_path, target_color, tolerance):
    # Загрузите изображения
    input_image = cv2.imread(input_image_path)
    background_image = cv2.imread(background_image_path)

    # Определите цвет для удаления (здесь используется BGR)
    target_color = np.array(target_color)

    # Создайте маску
    mask = np.all(np.abs(input_image - target_color) < tolerance, axis=-1)

    # Измените размер фона, чтобы он соответствовал размеру входного изображения
    background_image_resized = cv2.resize(background_image, (input_image.shape[1], input_image.shape[0]))

    # Замените фон
    output_image = np.where(mask[:, :, None], background_image_resized, input_image)

    # Сохраните результат
    cv2.imwrite(output_image_path, output_image)

# Пример использования
replace_background('Images\BlueHills.bmp', 'Images\Dune.bmp', 'Outputs\output_image.bmp', [255, 255, 255], 150)
