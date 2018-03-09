__author__ = "Ric Rodriguez"
__email__ = "therickyross2@gmail.com"
__project__ = "SEADSTestbed"

import logging
import tkinter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("latest.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MainGui(object):
    def __init__(self, master_frame):
        self.master_frame = master_frame
        pass


if __name__ == "__main__":
    logger.info("Started swagger")
    root = tkinter.Tk()
    root.attributes("-fullscreen", True)
    root.geometry("800x480")
    root.title("Swagger")
    root.mainloop()
