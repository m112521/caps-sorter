import numpy as np
import tflite_runtime.interpreter as tflite
import cv2

interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture(0)
img_w = 224
img_h = 224

labels = {0: 'blue', 1: 'green'}

while(True):
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # resize to [1xHxWx3]
    frame_resized = cv2.resize(frame_rgb, (img_w, img_h))
    input_data = np.expand_dims(frame_resized, axis=0)
    
    interpreter.set_tensor(input_details[0]['index'], input_data.astype(np.float32)/255) # /255
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    #print(output_data)
    max_idx = np.argmax(output_data)
    print(labels[max_idx])
    
    cv2.imshow('Color clf', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
