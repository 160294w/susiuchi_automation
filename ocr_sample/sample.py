from PIL import Image
import pyocr




def processing(engine, lang='eng', image='test_text.png'):
    # read text from image.
    text = engine.image_to_string(Image.open(image), lang=lang)
    print(text)
    return

def preparation():
    # get ocr engine
    engines = pyocr.get_available_tools()
    engine = engines[0]
    return engine

if __name__ == '__main__':
    engine = preparation()
    processing(engine)
    processing(engine, 'jpn_vert', 'test_text2.png')
