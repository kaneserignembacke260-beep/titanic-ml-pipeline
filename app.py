import streamlit as st
import joblib
import pandas as pd

# Titre affiché en haut de la page
st.title("🚢 Prédiction de survie - Titanic")
st.write("Renseigne les informations d'un passager pour prédire s'il aurait survécu.")

# Charge le modèle entraîné (fichier sauvegardé avec joblib)
model = joblib.load("models/titanic_model.pkl")

# --- Formulaire pour entrer les caractéristiques du passager ---

# Menu déroulant pour la classe (1ère, 2ème, 3ème)
pclass = st.selectbox("Classe du passager", [1, 2, 3])

# Menu déroulant pour le sexe
sexe = st.selectbox("Sexe", ["Homme", "Femme"])
# on convertit en 0/1 comme dans l'entraînement (Sex : male=0, female=1)
sexe_encode = 0 if sexe == "Homme" else 1

# Curseur pour l'âge
age = st.slider("Âge", min_value=0, max_value=90, value=30)

# Curseur pour la taille de la famille (SibSp + Parch + 1)
family_size = st.slider("Taille de la famille à bord (lui/elle inclus)", min_value=1, max_value=10, value=1)

# --- Bouton pour lancer la prédiction ---
if st.button("Prédire la survie"):
    # on assemble les 4 features dans le même ordre que lors de l'entraînement
    X_nouveau = pd.DataFrame([[pclass, sexe_encode, age, family_size]],
                              columns=["Pclass", "Sex", "Age", "FamilySize"])

    # le modèle prédit 0 (n'a pas survécu) ou 1 (a survécu)
    prediction = model.predict(X_nouveau)[0]

    # on affiche le résultat de façon lisible
    if prediction == 1:
        st.success("✅ Ce passager aurait probablement survécu.")
    else:
        st.error("❌ Ce passager n'aurait probablement pas survécu.")
