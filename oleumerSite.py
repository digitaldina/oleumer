
from flask import Flask, render_template                 #imports              
 
#functions for calling, processing the model and prediction function
def load_image(img_path):

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    
    img_tensor = np.expand_dims(img_tensor, axis=0)         
    img_tensor /= 255.                                      

    return img_tensor

def get_model():
    global model
    model = load_model('model.h5')
    print("loaded!")

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


app = Flask(__name__)                                    
get_model()

#returning and calling web page
@app.route("/", methods=['GET', 'POST'])                 
def home():                                              

    return render_template('home.html')                  

#calling predications and print result
@app.route("/predict", methods = ['GET','POST'])
def predict():
    
    if request.method == 'POST':
        
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(r'C:/Users/nEW u/Flask/static/', filename)                       
        file.save(file_path)
        print(filename)
        product = prediction(file_path)
        print(product)

# you can use file_path instead of filename
    return render_template('predict.html', product = product, user_image = file_path)           

if __name__ == "__main__":
    app.run() 
