# Chronical-Kidney-Disease-Using-ML

## instruction

1) project models.ipynb contains all models with EDA 
2) dataset = kidney_disease.csv
3) finalized_model.pkl contain final model 

### To run the model, Run app.py in any text editor 

# Details of ML project 

Because of the increasing number of patients, the high risk of progression to end-stage renal disease, and the poor prognosis of morbidity and mortality, chronic kidney disease (CKD) places a significant burden on the healthcare system. The goal of this research is to create a machine-learning model that can predict the early-stage chronical kidney desies. A total of 400 people were chosen. The Random Forest model performed best with a 0.989 accuracy. The model proposed in this study may be useful for policymakers in predicting CKD trends in the population. The models can enable close monitoring of people at risk, early detection of CKD, better resource allocation, and patient-centred management.

## Goal:

Our kidneys are responsible for filtering blood and removing waste in the form of urine. It also known as chronic kidney failure, Dangerous quantities of fluid, and wastes can build up in the body at advanced stages. Patients must then undergo dialysis or consider a transplant if this occurs.
Our goal in this experiment is to investigate if we can use 24 variables to predict whether a patient will develop chronic kidney disease or not. We may be able to recognize and help patients at risk of kidney failure if we can identify characteristics that have a strong influence on kidney failure.
These ML-based models, in the opinion of policymakers, could be efficiently used in resource management and initiating public health initiatives such as closely monitoring and early detection of CKD. Clearly, for such models to be used in clinical practise with individual patients, the feature set would need to be expanded to include laboratory measurements and possibly lifestyle information, which will be addressed in future research.

## ➢ Dataset's Attribute Information:

We use 24 + class = 25 (11 numeric ,14 nominal)

Age(numerical) = age in years

Blood Pressure(numerical) = bp in mm/Hg

Specific Gravity(nominal) = sg - (1.005,1.010,1.015,1.020,1.025)

Albumin(nominal) = al - (0,1,2,3,4,5)

Sugar(nominal) = su - (0,1,2,3,4,5)

Red Blood Cells(nominal) = rbc - (normal, abnormal)

Pus Cell (nominal) = pc - (normal, abnormal)

Pus Cell clumps(nominal) = pcc - (present, notpresent)

Bacteria(nominal) = ba - (present, notpresent)

Blood Glucose Random(numerical) = bgr in mgs/dl

Blood Urea(numerical) = bu in mgs/dl

Serum Creatinine(numerical) = sc in mgs/dl

Sodium(numerical) = sod in mEq/L

Potassium(numerical) = pot in mEq/L

Haemoglobin(numerical) = hemo in gms

Packed Cell Volume(numerical)

White Blood Cell Count(numerical) = wc in cells/cumm

Red Blood Cell Count(numerical) = rc in millions/cmm

Hypertension(nominal) = htn - (yes, no)

Diabetes Mellitus(nominal) = dm - (yes, no)

Coronary Artery Disease(nominal) = cad - (yes, no)

Appetite(nominal) = appet - (good, poor)

Pedal Edema(nominal) = pe - (yes, no)

Anaemia(nominal) = ane - (yes, no)

➢ Targeted Feature

Class (nominal) = class - (ckd, notckd)

![image](https://user-images.githubusercontent.com/73816107/157976073-81d25efa-79f4-41a5-9511-989b08c9fa50.png)

Chronic Kidney Disease effect by Age and Blood Pressure

## ➢ Model Development

We used various modeling algorithms from packages like Scikit-learn (decision tree, random forest), K-Nearest Neighbors Algorithm, Support Vector Machine, Multilayer perceptron.
## ➢ Result

Among the methods listed above, we used random forest

![image](https://user-images.githubusercontent.com/73816107/157976179-2ebec3cf-119c-4d96-ac71-1562c4265eca.png)

## ➢ Other Machine Learning Models:

![image](https://user-images.githubusercontent.com/73816107/157976223-a8711ea4-c9a8-41aa-acbe-18614d31ebdd.png)

other Machine Learning Models with Accuracy

## ➢ Testing the Model for Real World
![image](https://user-images.githubusercontent.com/73816107/157976266-24d08039-da99-4e43-90b8-85d35088b9fd.png)

## ➢ Front-End
![image](https://user-images.githubusercontent.com/73816107/157976297-efa039a9-de54-4edb-824b-b2f85e9da7bb.png)
