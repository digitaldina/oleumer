from flask import Flask, render_template                 #import

app = Flask(__name__)                                    #calling

@app.route("/", methods=['GET', 'POST'])                 #initialising
def home():                                              #function call

    return render_template('home.html')                  #return and calling HTML page (designed template)

if __name__ == "__main__":
    app.run() 
    
#functions for calling, processing the model and prediction function
def load_image(img_path):

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

def get_model():
    global model
    model = load_model('model.h5')
    print("Model loaded!")

def prediction(img_path):
    new_image = load_image(img_path)
    
    pred = model.predict(new_image)
    
    print(pred)
    
    labels=np.array(pred)
    labels[labels>=0.6]=1
    labels[labels<0.6]=0
    
    print(labels)
    final=np.array(labels)
    
    if final[0][0]==1:
        return "Bad"
    else:
        return "Good"