import os, cv2, threading, time
import face_recognition as fr
import numpy as np
from datetime import datetime

from PyQt5 import QtWidgets, QtGui, QtCore

from View.WebCam import Ui_WebCam
from Content.Layout import Layout


class ReconhecimentoFacialController(QtCore.QObject):
    sinal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.banco_imagens = './Content/bancoimagens'
        self.face_detector = cv2.CascadeClassifier(self.banco_imagens+"/algoritmoreconhecimento/haarcascade_frontalface_default.xml")
        self.modal_cam = QtWidgets.QDialog()
        self.ui = Ui_WebCam()
        self.ui.setupUi(self.modal_cam)
        self.modal_cam.setModal(True)
        self.sinal.connect(self.modal_cam.show)

    def run_thread_reconhecimento(self, interface):
        threading.Thread(target=self.reconhecer_rosto, args=(interface,), name="THREAD_RECONHECIMENTO").start()
        
    def run_thread_cadastro(self, nome, interface):
        threading.Thread(target=self.cadastrar_rosto, args=(nome, interface), name="THREAD_CADASTRO").start()

    def cadastrar_rosto(self, nome, interface):
        video_capture = cv2.VideoCapture(0)
        
        cap = 0
        while cap<= 10:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            # image_gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2RGB)
            image_face = self.face_detector.detectMultiScale(frame,minSize=(200,200))
            if len(image_face) != 0:
                # print("detectado")
                cap += 1
                name = f'{self.banco_imagens}/{nome}.png'
                cv2.imwrite(name,frame)
                for (x, y, w, h) in image_face:
                    # print(w, h)
                    pass
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            else:
                pass # Não detectou nada
            
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        interface.set_success.emit()
        
        video_capture.release()
        cv2.destroyAllWindows()
        
    def reconhecer_rosto(self, interface):
        Layout.show_modal_box(self)
        fgbg = cv2.createBackgroundSubtractorKNN(history=1, detectShadows=False)
        w, h = 640, 460
        x1, x2 = 100, w - 110
        y1, y2 = 100, h - 65
        xAnterior = 0
        yAnterior = 0
        data = None
        imagem = None
        controle = 0
        self.kill = False
        try:
            known_names = []
            known_name_encodings = []

            images = tuple(imagem for imagem in os.listdir(self.banco_imagens) if '.png' in imagem)
            
            if not images:
                interface.set_message.emit("Nenhum cadastro encontrado")
                return

            for image in images:
                image_path = f'{self.banco_imagens}/{image}'
                image = fr.load_image_file(image_path)
                
                try:
                    encoding = fr.face_encodings(image)[0]
                    known_name_encodings.append(encoding)

                    known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())
                except Exception as ex:
                    pass # Não foi encontrado rosto
                    # print(f'Não foi encontrado rosto na imagem {image}, {ex}')
            
                
            video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) ### REMOVER cv2.CAP_DSHOW AO EXECUTAR NO LINUX
            
            while not self.kill:
                # Captura frame-by-frame
                ret, frame = video_capture.read()
                
                self.sinal.emit() # Emite o sinal para mostrar imagem da camera
                
                if ret:
                    imagem = frame.copy()
                    black = np.zeros_like(frame)
                    ROI = black.copy()
                    ROI[y1:y2, x1:x2] = frame[y1:y2, x1:x2]
                    gray = cv2.cvtColor(ROI, cv2.COLOR_RGB2GRAY)
                    gray = cv2.equalizeHist(gray)
                    # cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 255, 255), 1, cv2.LINE_AA)
                    fgmask = fgbg.apply(gray)
                    mask_blur = cv2.blur(fgmask, (3, 3))
                    contours, hierarchy = cv2.findContours(mask_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    
                    image_face = self.face_detector.detectMultiScale(frame, minSize=(200, 200))
                    for (x, y, w, h) in image_face:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (77, 46, 25), 2, cv2.LINE_AA)

                    if len(contours) > 0:
                        contour = max(contours, key=cv2.contourArea)
                        (x, y, w, h) = cv2.boundingRect(contour)
                        contour_valid = (w >= 200) and (h >= 150)
                        # contour_valid = True
                        # contour_valid = (w >= 150) and (h >= 75)

                        if contour_valid and controle > 10:
                            cv2.drawContours(black, contour, 0, (255, 255, 255), 5)
                            (x, y, w, h) = cv2.boundingRect(contour)

                            if xAnterior != x or yAnterior != y:
                                data = datetime.now()
                                
                            xAnterior, yAnterior = x, y

                        if data and controle > 10:
                            # dif = (datetime.now() - data).total_seconds()
                            # if abs(dif) >= 3:
                            self.kill = True
                    
                    rgbImage = cv2.cvtColor(frame if not self.kill else imagem, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                    img = convertToQtFormat.scaled(w, h, QtCore.Qt.KeepAspectRatio)
                    controle += 1
                    
                    self.ui.divWebCam.setPixmap(QtGui.QPixmap.fromImage(img))
                else:
                    break
                
                if cv2.waitKey(1) & 0xFF == ord('q'): ### COMENTAR AO COMPILAR NO LINUX ###
                    break
            
            name = self.banco_imagens + "/compara.png"
            cv2.imwrite(name,frame)
            image = cv2.imread(name)
            
            rostos_detectados = list()
            face_locations = fr.face_locations(image)
            face_encodings = fr.face_encodings(image, face_locations)
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = fr.compare_faces(known_name_encodings, face_encoding)
                name = None
                
                # Busca todas as faces
                c = 0
                for match in matches:
                    if match == True:
                        rostos_detectados.append(known_names[c])
                    c += 1
                    
                # Busca apenas uma face com o melhor match
                face_distances = fr.face_distance(known_name_encodings, face_encoding)
                best_match = np.argmin(face_distances)
                
                # AQUI VAI SER O RESULTADO DA BUSCA
                if matches[best_match]:
                    name = known_names[best_match]

            os.remove(self.banco_imagens + "/compara.png")
                
            if name:
                interface.set_message.emit(f"Rosto de {name} reconhecido")
            else:
                interface.set_message.emit("Não reconhecido")
        
            self.modal_box.close()
                
        except Exception as e:
            print(e)
        