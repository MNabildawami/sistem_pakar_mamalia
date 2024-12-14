import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Memuat data
data_mamalia = pd.read_csv('mamalia.csv')

# Menyiapkan data
X = data_mamalia[['Habitat', 'Jenis_Makanan', 'Tingkah_Laku', 'Ciri_Bentuk_Tubuh', 'Warna_Tubuh', 'Tempat_Tinggal']]
y = data_mamalia['Nama_Mamalia']

# Label Encoding untuk target (Nama_Mamalia)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# One-Hot Encoding untuk fitur (X)
X_encoded = pd.get_dummies(X)

# Membagi data menjadi data training dan testing
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Latih model menggunakan Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluasi model
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Simpan model yang telah dilatih
joblib.dump(model, 'model_mamalia.pkl')

# Simpan encoder untuk mendekode hasil prediksi nantinya
joblib.dump(encoder, 'encoder_mamalia.pkl')
